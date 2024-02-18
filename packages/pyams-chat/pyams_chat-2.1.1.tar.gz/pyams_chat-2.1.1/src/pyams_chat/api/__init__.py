#
# Copyright (c) 2015-2021 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_chat.api module

This module provides REST API for chat services.
"""

import json
from datetime import datetime

from colander import MappingSchema, SchemaNode, SequenceSchema, String, drop
from cornice import Service
from pyramid.httpexceptions import HTTPOk

from pyams_chat.interfaces import IChatMessageHandler, REST_CONTEXT_ROUTE, \
    REST_NOTIFICATIONS_ROUTE
from pyams_chat.message import ChatMessage
from pyams_security.rest import check_cors_origin, set_cors_headers
from pyams_utils.rest import BaseStatusSchema, STATUS, StringListSchema, rest_responses
from pyams_utils.timezone import tztime

__docformat__ = 'restructuredtext'


class PrincipalInfo(MappingSchema):
    """Base principal info"""
    id = SchemaNode(String(),
                    description="Principal ID")
    title = SchemaNode(String(),
                       description="Principal title")


class Principal(PrincipalInfo):
    """Principal schema"""
    principals = StringListSchema(description="List of inner sub-principals supported "
                                              "by this principal (including roles)")


class ChatContext(BaseStatusSchema):
    """User chat context schema"""
    principal = Principal(description="Context principal")
    context = MappingSchema(description="Chat events categories subscribed by the principal")


class NotificationSource(PrincipalInfo):
    """Notification source"""
    avatar = SchemaNode(String(),
                        description="URL of principal avatar",
                        missing=drop)


class Notification(MappingSchema):
    """Notification schema"""
    host = SchemaNode(String(),
                      description="Message host name")
    channel = SchemaNode(String(),
                         description="Message channel")
    action = SchemaNode(String(),
                        description="Message action")
    category = SchemaNode(String(),
                          description="Message category")
    status = SchemaNode(String(),
                        description="Message status")
    title = SchemaNode(String(),
                       description="Message title")
    message = SchemaNode(String(),
                         description="Message content")
    image = SchemaNode(String(),
                       description="Message image URL",
                       missing=drop)
    source = NotificationSource(description="Message source")
    timestamp = SchemaNode(String(),
                           description="Message timestamp, in ISO-8601 format")


class NotificationsList(SequenceSchema):
    """Notifications list schema"""
    notification = Notification()


class NotificationsResults(MappingSchema):
    """Notifications results schema"""
    timestamp = SchemaNode(String(),
                           description="Notifications timestamp, in ISO-8601 format")
    notifications = NotificationsList(description="Notifications list")


#
# Chat service
#

chat_service = Service(name=REST_CONTEXT_ROUTE,
                       pyramid_route=REST_CONTEXT_ROUTE,
                       description="PyAMS chat context API")


@chat_service.options(validators=(check_cors_origin, set_cors_headers))
def chat_options(request):  # pylint: disable=unused-argument
    """Chat service OPTIONS handler"""
    return ''


class ChatServiceGetResponse(MappingSchema):
    """Chat service getter response"""
    body = ChatContext()


chat_service_get_responses = rest_responses.copy()
chat_service_get_responses[HTTPOk.code] = ChatServiceGetResponse(
    description="Description of chat service context")


@chat_service.get(validators=(check_cors_origin, set_cors_headers),
                  response_schemas=chat_service_get_responses)
def get_chat_context(request):
    """Description of chat service context"""
    principal = request.principal
    message = ChatMessage.create_empty_message(request)
    identity = request.identity
    principals = identity.get('principals', ()) if identity is not None else ()
    adapters = [
        name
        for name, adapter in request.registry.getAdapters((message, ),
                                                          IChatMessageHandler)
    ]
    return {
        'status': STATUS.SUCCESS.value,
        'principal': {
            'id': principal.id,
            'title': principal.title,
            'principals': list(principals)
        },
        'context': {
            '*': adapters
        }
    }


#
# Notifications service
#

notifications_service = Service(name=REST_NOTIFICATIONS_ROUTE,
                                pyramid_route=REST_NOTIFICATIONS_ROUTE,
                                description='PyAMS chat notifications API')


@notifications_service.options(validators=(check_cors_origin, set_cors_headers))
def notifications_options(request):  # pylint: disable=unused-argument
    """Notifications service OPTIONS handler"""
    return ''


class NotificationsServiceGetResponse(MappingSchema):
    """Notifications service getter response"""
    body = NotificationsResults()


notifications_service_get_responses = rest_responses.copy()
notifications_service_get_responses[HTTPOk.code] = NotificationsServiceGetResponse(
    description="List of current notifications")


@notifications_service.get(validators=(check_cors_origin, set_cors_headers),
                           response_schemas=notifications_service_get_responses)
def get_notifications(request):
    """REST notifications service"""

    def filter_messages(messages):
        """Filter user notifications"""
        identity = request.identity
        principals = identity.get('principals', ()) if identity is not None else ()
        for message in messages:
            if isinstance(message, (str, bytes)):
                message = json.loads(message)
            # don't get messages from other hosts
            if message.get('host') != request.host_url:
                continue
            # don't get messages from current user
            if message.get('source', {}).get('id') == request.principal.id:
                continue
            # filter message targets
            target = message.pop('target', {})
            if set(principals) & set(target.get('principals', ())):
                yield message

    timestamp = tztime(datetime.utcnow()).isoformat()
    client = request.redis_client
    if client is None:
        return {
            "timestamp": timestamp,
            "notifications": []
        }
    settings = request.registry.settings
    notifications_key = settings.get('pyams_chat.notifications_key', 'chat:notifications')
    notifications = client.redis.lrange(f'{notifications_key}::{request.host_url}', 0, -1)
    return {
        "timestamp": timestamp,
        "notifications": list(filter_messages(notifications or ()))
    }
