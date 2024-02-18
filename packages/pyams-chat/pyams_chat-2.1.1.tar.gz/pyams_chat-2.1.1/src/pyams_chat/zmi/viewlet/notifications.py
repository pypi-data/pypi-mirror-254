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

"""PyAMS_chat.zmi.viewlet.notifications module

This module defines a viewlet which can be used to display user notifications.
"""
from pyams_chat.interfaces import CHAT_JWT_REFRESH_PATH, CHAT_JWT_REFRESH_ROUTE, CHAT_JWT_VERIFY_PATH, \
    CHAT_JWT_VERIFY_ROUTE, CHAT_WS_ENDPOINT_SETTING
from pyams_chat.zmi.viewlet.interfaces import IUserNotificationsViewletManager
from pyams_security.interfaces.names import UNKNOWN_PRINCIPAL_ID
from pyams_template.template import template_config
from pyams_viewlet.manager import TemplateBasedViewletManager, WeightOrderedViewletManager, \
    viewletmanager_config
from pyams_zmi.interfaces import IAdminLayer
from pyams_zmi.interfaces.viewlet import IUserLinksViewletManager


__docformat__ = 'restructuredtext'


@viewletmanager_config(name='pyams.user-notifications',
                       layer=IAdminLayer,
                       manager=IUserLinksViewletManager, weight=850,
                       provides=IUserNotificationsViewletManager)
@template_config(template='templates/notifications.pt')
class UserNotificationsViewlet(TemplateBasedViewletManager, WeightOrderedViewletManager):
    """User notifications viewlet manager"""

    def __new__(cls, context, request, view, manager):  # pylint: disable=unused-argument
        principal = request.principal
        if principal.id == UNKNOWN_PRINCIPAL_ID:
            return None
        return WeightOrderedViewletManager.__new__(cls)

    render_empty = True

    @property
    def jwt_refresh_route(self):
        """JWT authentication endpoint"""
        return self.request.registry.settings.get(f'{CHAT_JWT_REFRESH_ROUTE}_route.path',
                                                  CHAT_JWT_REFRESH_PATH)

    @property
    def jwt_verify_route(self):
        """JWT token verification route"""
        return self.request.registry.settings.get(f'{CHAT_JWT_VERIFY_ROUTE}_route.path',
                                                  CHAT_JWT_VERIFY_PATH)

    @property
    def ws_endpoint(self):
        """Websocket endpoint"""
        return self.request.registry.settings.get(CHAT_WS_ENDPOINT_SETTING)
