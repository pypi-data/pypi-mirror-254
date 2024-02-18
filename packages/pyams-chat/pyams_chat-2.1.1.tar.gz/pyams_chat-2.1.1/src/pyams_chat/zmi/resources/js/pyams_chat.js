/* global MyAMS */

'use strict';


if (window.$ === undefined) {
    window.$ = MyAMS.$;
}


/**
 * PyAMS chat module
 */
const chat = {

    unloadHandler: null,
    wsClient: null,
    accessToken: null,
    refreshToken: null,
    checkInterval: null,

    /**
     * Module initialization
     */
    initChat: () => {
        chat.initService();
    },

    /**
     * Initialize service worker
     */
    initService: () => {
        if ('serviceWorker' in navigator) {

            navigator.serviceWorker
                .register('/chat-sw.js')
                .then((reg) => {
                    console.debug(">>> Chat ServiceWorker registered with scope: ", reg.scope);
                })
                .catch((err) => {
                    console.debug(">>> Chat ServiceWorker registration failed: ", err);
                });

            navigator.serviceWorker
                .addEventListener('message', chat.onServiceMessage);

            navigator.serviceWorker.ready
                .then((reg) => {
                    console.debug('>>> Service worker ready', reg);
                    const
                        notifications = $('#user-notifications'),
                        wsEndpoint = notifications.data('ams-notifications-endpoint'),
                        refreshRoute = notifications.data('ams-jwt-refresh-route'),
                        verifyRoute = `${notifications.data('ams-jwt-verify-route')}`;
                    setTimeout(() => {
                        console.debug(`  > fetching URL ${verifyRoute}...`);
                        MyAMS.require('ajax', 'notifications')
                            .then(() => {
                                MyAMS.ajax.get(verifyRoute)
                                    .then((result) => {
                                        console.debug('  > got JWT token!', result);
                                        reg.active.postMessage(JSON.stringify({
                                            action: 'setConfig',
                                            config: {
                                                accessToken: result.accessToken,
                                                refreshToken: result.refreshToken,
                                                wsEndpoint: wsEndpoint,
                                                jwtRefreshRoute: refreshRoute,
                                                jwtVerifyRoute: verifyRoute
                                            }
                                        }));
                                    });
                            });
                    }, 100);
                });

            /**
             * Fetch resource to keep service-worker alive!
             */
            setInterval(async () => {
                await fetch('/chat-ping')
            }, 15000);
        }
    },

    onServiceMessage: (event) => {
        console.debug(">>> received service message", event);
        const
            message = event.data,
            service = chat.services[message.action];
        if (typeof service === 'function') {
            service(message);
        }
    },

    services: {

        notify: (message) => {
            MyAMS.notifications.addNotification(message, false);
        }
    }
};


if (window.MyAMS) {
    MyAMS.config.modules.push('chat');
    MyAMS.chat = chat;
    console.debug("MyAMS: chat module loaded...");
}
