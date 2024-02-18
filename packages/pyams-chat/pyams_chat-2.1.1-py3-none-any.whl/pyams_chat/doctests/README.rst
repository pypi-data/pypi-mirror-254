==================
PyAMS chat package
==================


Introduction
------------

This package is composed of a set of utility functions, usable into any Pyramid application.

It allows to send notifications through websockets to connected users, using a Redis server and
a *pubsub* subscriber as defined by PyAMS_chat_WS package.

    >>> import pprint
    >>> from pyramid.testing import setUp, tearDown, DummyRequest
    >>> config = setUp(hook_zca=True)
    >>> config.registry.settings['zodbconn.uri'] = 'memory://'
    >>> config.registry.settings['pyams_chat.channel_name'] = 'chat:main'

    >>> from beaker.cache import CacheManager, cache_regions
    >>> cache = CacheManager(**{'cache.type': 'memory'})
    >>> cache_regions.update({'short': {'type': 'memory', 'expire': 0}})
    >>> cache_regions.update({'long': {'type': 'memory', 'expire': 0}})

    >>> from pyramid_zodbconn import includeme as include_zodbconn
    >>> include_zodbconn(config)
    >>> from cornice import includeme as include_cornice
    >>> include_cornice(config)
    >>> from cornice_swagger import includeme as include_swagger
    >>> include_swagger(config)
    >>> from pyams_utils import includeme as include_utils
    >>> include_utils(config)
    >>> from pyams_security import includeme as include_security
    >>> include_security(config)
    >>> from pyams_auth_http import includeme as include_auth_http
    >>> include_auth_http(config)
    >>> from pyams_chat import includeme as include_chat
    >>> include_chat(config)

    >>> import transaction

We will ne a security policy:

    >>> from pyams_security.policy import PyAMSSecurityPolicy
    >>> policy = PyAMSSecurityPolicy(secret='my secret',
    ...                              http_only=True,
    ...                              secure=False)
    >>> config.set_security_policy(policy)

    >>> from pyams_security.principal import PrincipalInfo
    >>> from pyams_security.tests import new_test_request

    >>> request = new_test_request('{system}.admin', 'admin', registry=config.registry)
    >>> request.principal = PrincipalInfo(id='system:admin')

    >>> from pyramid.threadlocal import manager
    >>> manager.push({'request': request, 'registry': config.registry})

    >>> from pyams_site.generations import upgrade_site
    >>> app = upgrade_site(request)
    Upgrading PyAMS security to generation 2...

    >>> from zope.traversing.interfaces import BeforeTraverseEvent
    >>> from pyams_utils.registry import handle_site_before_traverse
    >>> handle_site_before_traverse(BeforeTraverseEvent(app, request))


Chat messages
-------------

The base of this package usage is to create and send messages:

    >>> from pyams_chat.include import client_from_config
    >>> from pyams_chat.message import ChatMessage

    >>> request.redis_client = client_from_config(config.registry.settings)

    >>> message = ChatMessage(request=request,
    ...                       action='notify',
    ...                       category='pyams.test',
    ...                       source=request.principal.id,
    ...                       title="Test message",
    ...                       message="Test message content")
    >>> message.send()

    >>> transaction.commit()


Chat messaging API
------------------

A REST API is available to get chat context; this context is used to filter chat messages:

    >>> from pyams_chat.api import get_chat_context
    >>> pprint.pprint(get_chat_context(request))
    {'context': {'*': ['user.login']},
     'principal': {'id': 'system:admin',
                   'principals': [...'system:admin'...],
                   'title': '__unknown__'},
     'status': 'success'}

We can also get chat messages:

    >>> from pyams_chat.api import get_notifications
    >>> pprint.pprint(get_notifications(request))
    {'notifications': [], 'timestamp': '...T...'}

The notifications list is actually empty because the Redis list is filled by the websocket
server only when notifications are actually dispatched.

    >>> with request.redis_client as redis:
    ...     redis.lrange(f'chat:notifications::{request.host_url}', 0, -1)
    []

We can simulate this:

    >>> import json
    >>> from pyams_chat.message import ChatMessageEncoder

    >>> with request.redis_client as redis:
    ...     redis.lpush(f'chat:notifications::{request.host_url}',
    ...                 json.dumps(message, cls=ChatMessageEncoder))
    1

    >>> pprint.pprint(get_notifications(request))
    {'notifications': [], 'timestamp': ...}

We still get an empty notifications list because a message sender doesn't receive it's
own notifications:

    >>> pprint.pprint(get_notifications(request))
    {'notifications': [], 'timestamp': ...}

Why is it still empty? That's because we have to define a *target* for a message, which is
a set of principals which should receive the message. These targets are defined by using a
named adapter, whose name must be the *category* of the message:

    >>> from pyams_utils.testing import call_decorator
    >>> from pyams_utils.adapter import adapter_config
    >>> from pyams_utils.adapter import ContextAdapter
    >>> from pyams_chat.interfaces import IChatMessage, IChatMessageHandler

    >>> class TestMessageHandler(ContextAdapter):
    ...
    ...     def get_target(self):
    ...         return {
    ...             'principals': ['system:admin']
    ...     }

    >>> call_decorator(config, adapter_config, TestMessageHandler, name='pyams.test',
    ...                required=(IChatMessage, ), provides=IChatMessageHandler)

    >>> message.send()
    >>> with request.redis_client as redis:
    ...     redis.lpush(f'chat:notifications::{request.host_url}',
    ...                 json.dumps(message, cls=ChatMessageEncoder))
    2
    >>> pprint.pprint(get_notifications(request))
    {'notifications': [],
     'timestamp': ...}

A default message handler is available on user login:

    >>> from pyams_security.interfaces.plugin import AuthenticatedPrincipalEvent

    >>> request.principal = PrincipalInfo(id='system:admin')
    >>> event = AuthenticatedPrincipalEvent('admin', 'test:user')

    >>> from pyams_chat.handler.login import handle_authenticated_principal
    >>> handle_authenticated_principal(event)

    >>> message = ChatMessage(request=request,
    ...                       action='notify',
    ...                       category='user.login',
    ...                       source='test:user',
    ...                       title="User login",
    ...                       message="{} logged in...".format(request.principal.title))
    >>> message.send()
    >>> with request.redis_client as redis:
    ...     redis.lpush(f'chat:notifications::{request.host_url}',
    ...                 json.dumps(message, cls=ChatMessageEncoder))
    3
    >>> pprint.pprint(get_notifications(request))
    {'notifications': [{'action': 'notify',
                        'category': 'user.login',
                        'channel': 'chat:main',
                        'host': 'http://example.com',
                        'image': None,
                        'message': '__unknown__ logged in...',
                        'modal': False,
                        'source': {'id': 'test:user',
                                   'title': 'MissingPrincipal: test:user'},
                        'status': 'info',
                        'timestamp': '...T...',
                        'title': 'User login',
                        'url': None}],
     'timestamp': ...}


Chat notifications viewlet
--------------------------

A small viewlet is available to integrate notifications into management interface:

    >>> from pyams_chat.zmi.viewlet.notifications import UserNotificationsViewlet

    >>> viewlet = UserNotificationsViewlet(app, request, None, None)
    >>> viewlet.update()
    >>> print(viewlet.render())
    <div id="user-notifications" class="ml-1"
         data-ams-modules='{
             "events": "events",
             "callbacks": "callbacks",
             "notifications": "notifications",
             "chat": {
                 "src": "/--static--/pyams_chat/:version:...T.../js/pyams_chat.js"
             }
         }'
         data-ams-callback="MyAMS.chat.initChat"
         data-ams-events-handlers='{"show.bs.dropdown": "MyAMS.notifications.getNotifications"}'
         data-ams-events-options='{"localTimestamp": "true"}'
         data-ams-jwt-refresh-route="http://example.com/api/auth/jwt/token"
         data-ams-jwt-verify-route="http://example.com/api/auth/jwt/verify"
         data-ams-notifications-target="#notifications-pane"
         data-ams-notifications-source="http://example.com/api/chat/notifications">
        <a href="#" class="btn btn-light pt-2"
           data-toggle="dropdown" data-offset="36,7">
            <i class="fa fa-bell hint"
               title="Notifications"
               data-placement="bottom" data-offset="0,10"></i>
            <b id="notifications-count" data-content="10"
               class="badge bg-danger text-white"></b>
        </a>
        <div class="dropdown-menu dropdown-menu-right p-1"
             data-ams-click-dismiss="false">
            <div class="position-relative d-flex flex-column h-100">
                <ul class="nav nav-tabs nav-fill">
                    <li class="nav-item">
                        <a href="#notifications-pane" class="nav-link active"
                           data-toggle="tab"
                           data-ams-events-handlers='{"show.bs.tab": "MyAMS.notifications.getNotifications"}'
                           data-ams-events-options='{"localTimestamp": "true"}'>Notifications</a>
                    </li>
                </ul>
                <div class="tab-content flex-grow-1 overflow-hidden p-1 pt-2 border">
                    <div class="tab-pane d-flex flex-column overflow-hidden h-100 fade show active"
                         id="notifications-pane">
                        <!-- dynamic content -->
                    </div>
                </div>
            </div>
        </div>
    </div>


Chat service worker views
-------------------------

Two custom views are used by chat service worker: one is just a ping service, while the other
one is used to load worker script in a global scope:

    >>> from pyams_chat.zmi.worker import chat_ping, chat_worker_script

    >>> resp = chat_ping(request)
    >>> resp
    <Response at 0x... 200 OK>
    >>> resp.text
    'PONG'

    >>> resp = chat_worker_script(request)
    >>> resp
    <FileResponse at 0x... 200 OK>
    >>> resp.content_type
    'text/javascript'


Tests cleanup:

    >>> tearDown()
