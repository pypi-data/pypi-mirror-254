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

"""PyAMS_chat.zmi.worker module

This module is used to declare specific endpoints which are required to
use chat service worker.
"""

import os

from pyramid.response import FileResponse, Response
from pyramid.view import view_config

from pyams_chat.interfaces import CHAT_PING_ROUTE, CHAT_WORKER_ROUTE


__docformat__ = 'restructuredtext'


@view_config(route_name=CHAT_PING_ROUTE)
def chat_ping(request):
    """Chat ping endpoint"""
    return Response(body='PONG',
                    content_type='text/plain')


@view_config(route_name=CHAT_WORKER_ROUTE)
def chat_worker_script(request):
    """Chat ServiceWorker route"""
    here = os.path.dirname(__file__)
    script = os.path.join(here, 'resources', 'js', 'chat-sw.js')
    return FileResponse(script, request=request)
