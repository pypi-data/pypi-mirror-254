#
# Copyright (c) 2015-2019 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS chat.include module

This module is used for Pyramid integration
"""

import re

from pyramid.settings import asbool

from pyams_chat.client import RedisClient
from pyams_chat.interfaces import CHAT_PING_PATH, CHAT_PING_ROUTE, CHAT_WORKER_PATH, CHAT_WORKER_ROUTE, IRedisClient, \
    REST_CONTEXT_PATH, REST_CONTEXT_ROUTE, REST_NOTIFICATIONS_PATH, REST_NOTIFICATIONS_ROUTE


__docformat__ = 'restructuredtext'


def client_from_config(settings, prefix='pyams_chat.'):
    """
    Instantiate and configure a Redis client from settings.

    In a typical Pyramid application, just include ``pyams_chat`` and use
    :py:func:`get_client` function to get access to the shared :py:class:`.client.RedisClient`
    instance (which is also available using *request.redis_client* notation).
    """
    return RedisClient(
        server_url=settings.get(f'{prefix}redis_server', 'redis://localhost:6379/0'),
        use_transaction=settings.get(f'{prefix}use_transaction', True)
    )


def get_client(request):
    """
    Get registered Redis client
    """
    registry = request.registry
    return registry.queryUtility(IRedisClient)


def include_package(config):
    """Pyramid package include"""

    registry = config.registry
    settings = registry.settings

    # add translations
    config.add_translation_dirs('pyams_chat:locales')

    # add request methods
    config.add_request_method(get_client, 'redis_client', reify=True)

    # register ServiceWorker script route
    config.add_route(CHAT_PING_ROUTE,
                     settings.get(f'{CHAT_PING_ROUTE}_route.path',
                                  CHAT_PING_PATH))

    config.add_route(CHAT_WORKER_ROUTE,
                     settings.get(f'{CHAT_WORKER_ROUTE}_route.path',
                                  CHAT_WORKER_PATH))

    # register new REST API routes
    config.add_route(REST_CONTEXT_ROUTE,
                     settings.get(f'{REST_CONTEXT_ROUTE}_route.path',
                                  REST_CONTEXT_PATH))

    config.add_route(REST_NOTIFICATIONS_ROUTE,
                     settings.get(f'{REST_NOTIFICATIONS_ROUTE}_route.path',
                                  REST_NOTIFICATIONS_PATH))

    # initialize Redis client
    if asbool(settings.get('pyams_chat.start_client', True)):
        client = client_from_config(settings)
        registry.registerUtility(client, IRedisClient)

    # package scan
    try:
        import pyams_zmi  # pylint: disable=import-outside-toplevel,unused-import
    except ImportError:
        config.scan(ignore=[re.compile(r'pyams_chat\..*\.zmi\.?.*').search])
    else:
        config.scan()
