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

"""PyAMS_chat.handler.login module

This module defines a custom *login* handler, which is used to send notifications
on any user login to site managers.
"""

from pyramid.events import subscriber

from pyams_chat.interfaces import IChatMessage, IChatMessageHandler
from pyams_chat.message import ChatMessage
from pyams_security.interfaces import IProtectedObject
from pyams_security.interfaces.names import ADMIN_USER_ID, SYSTEM_ADMIN_ROLE
from pyams_security.interfaces.plugin import IAuthenticatedPrincipalEvent
from pyams_security.utility import get_principal
from pyams_utils.adapter import ContextAdapter, adapter_config
from pyams_utils.request import query_request


__docformat__ = 'restructuredtext'

from pyams_chat import _  # pylint: disable=ungrouped-imports


@subscriber(IAuthenticatedPrincipalEvent)
def handle_authenticated_principal(event):
    """Handle authenticated principal"""
    request = query_request()
    if request is None:
        return
    principal = get_principal(request, principal_id=event.principal_id)
    translate = request.localizer.translate
    message = ChatMessage(request=request,
                          action='notify',
                          category='user.login',
                          source=principal.id,
                          title=translate(_("User login")),
                          message=translate(_("{} logged in...")).format(principal.title))
    message.send()


@adapter_config(name='user.login',
                required=IChatMessage,
                provides=IChatMessageHandler)
class UserLoginMessageTarget(ContextAdapter):
    """User login message target adapter"""

    def get_target(self):
        """Get message targets"""
        principals = {ADMIN_USER_ID}
        root = self.context.request.root
        protection = IProtectedObject(root, None)
        if protection is not None:
            principals |= protection.get_principals(SYSTEM_ADMIN_ROLE)
        return {
            'principals': tuple(principals)
        }
