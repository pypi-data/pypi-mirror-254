/**
 * idb script
 */
var idb=function(e){"use strict";let t,n;const r=new WeakMap,o=new WeakMap,s=new WeakMap,a=new WeakMap,i=new WeakMap;let c={get(e,t,n){if(e instanceof IDBTransaction){if("done"===t)return o.get(e);if("objectStoreNames"===t)return e.objectStoreNames||s.get(e);if("store"===t)return n.objectStoreNames[1]?void 0:n.objectStore(n.objectStoreNames[0])}return p(e[t])},set:(e,t,n)=>(e[t]=n,!0),has:(e,t)=>e instanceof IDBTransaction&&("done"===t||"store"===t)||t in e};function u(e){return e!==IDBDatabase.prototype.transaction||"objectStoreNames"in IDBTransaction.prototype?(n||(n=[IDBCursor.prototype.advance,IDBCursor.prototype.continue,IDBCursor.prototype.continuePrimaryKey])).includes(e)?function(...t){return e.apply(f(this),t),p(r.get(this))}:function(...t){return p(e.apply(f(this),t))}:function(t,...n){const r=e.call(f(this),t,...n);return s.set(r,t.sort?t.sort():[t]),p(r)}}function d(e){return"function"==typeof e?u(e):(e instanceof IDBTransaction&&function(e){if(o.has(e))return;const t=new Promise(((t,n)=>{const r=()=>{e.removeEventListener("complete",o),e.removeEventListener("error",s),e.removeEventListener("abort",s)},o=()=>{t(),r()},s=()=>{n(e.error||new DOMException("AbortError","AbortError")),r()};e.addEventListener("complete",o),e.addEventListener("error",s),e.addEventListener("abort",s)}));o.set(e,t)}(e),n=e,(t||(t=[IDBDatabase,IDBObjectStore,IDBIndex,IDBCursor,IDBTransaction])).some((e=>n instanceof e))?new Proxy(e,c):e);var n}function p(e){if(e instanceof IDBRequest)return function(e){const t=new Promise(((t,n)=>{const r=()=>{e.removeEventListener("success",o),e.removeEventListener("error",s)},o=()=>{t(p(e.result)),r()},s=()=>{n(e.error),r()};e.addEventListener("success",o),e.addEventListener("error",s)}));return t.then((t=>{t instanceof IDBCursor&&r.set(t,e)})).catch((()=>{})),i.set(t,e),t}(e);if(a.has(e))return a.get(e);const t=d(e);return t!==e&&(a.set(e,t),i.set(t,e)),t}const f=e=>i.get(e);const l=["get","getKey","getAll","getAllKeys","count"],D=["put","add","delete","clear"],v=new Map;function b(e,t){if(!(e instanceof IDBDatabase)||t in e||"string"!=typeof t)return;if(v.get(t))return v.get(t);const n=t.replace(/FromIndex$/,""),r=t!==n,o=D.includes(n);if(!(n in(r?IDBIndex:IDBObjectStore).prototype)||!o&&!l.includes(n))return;const s=async function(e,...t){const s=this.transaction(e,o?"readwrite":"readonly");let a=s.store;return r&&(a=a.index(t.shift())),(await Promise.all([a[n](...t),o&&s.done]))[0]};return v.set(t,s),s}return c=(e=>({...e,get:(t,n,r)=>b(t,n)||e.get(t,n,r),has:(t,n)=>!!b(t,n)||e.has(t,n)}))(c),e.deleteDB=function(e,{blocked:t}={}){const n=indexedDB.deleteDatabase(e);return t&&n.addEventListener("blocked",(()=>t())),p(n).then((()=>{}))},e.openDB=function(e,t,{blocked:n,upgrade:r,blocking:o,terminated:s}={}){const a=indexedDB.open(e,t),i=p(a);return r&&a.addEventListener("upgradeneeded",(e=>{r(p(a.result),e.oldVersion,e.newVersion,p(a.transaction))})),n&&a.addEventListener("blocked",(()=>n())),i.then((e=>{s&&e.addEventListener("close",(()=>s())),o&&e.addEventListener("versionchange",(()=>o()))})).catch((()=>{})),i},e.unwrap=f,e.wrap=p,e}({});

const ChatSW = self;


/**
 * Fibonacci sequence generator
 */
const checkInterval = () => {

    function* getSequence() {
        let start = 1,
            next = 1;
        while (true) {
            yield start;
            if (next < 3600) {
                [next, start] = [next + start, next];
            }
        }
    }
    return getSequence();

};


/**
 * Check if provided response is valid, based on expiration date
 *
 * @param response: initial response
 */
const isValidResponse = (response) => {
    const expires = response.headers.get('Expires');
    if (expires) {
        const expirationDate = new Date(expires);
        return expirationDate > new Date();
    }
    return true;
};


/**
 * Notifications permission checker
 */
const checkNotificationPermission = () => {

    const checkNotificationPromise = () => {
        try {
            Notification.requestPermission().then();
        } catch (e) {
            return false;
        }
        return true;
    };

    return new Promise((resolve, reject) => {
        if (Notification.permission !== 'denied') {
            if (Notification.permission === 'default') {
                if (checkNotificationPromise()) {
                    Notification.requestPermission().then((permission) => {
                        resolve(permission === 'granted');
                    });
                } else {
                    Notification.requestPermission((permission) => {
                        resolve(permission === 'granted');
                    });
                }
            } else {
                resolve(true);
            }
        } else {
            resolve(false);
        }
    });
};


/**
 * Main chat service worker
 */
const ChatService = {

    DB_NAME: 'chat-db',
    CACHE_NAME: 'chat-service',
    CACHED_URLS: [
        '/chat-ping'
    ],

    wsEndpoint: null,
    wsClient: null,
    wsChecker: null,

    init: async () => {
        console.debug('[chat-sw] init...');
        await ChatService.checkConnection();
    },

    getDB: async () => {
        return idb.openDB(ChatService.DB_NAME, 1, {
            upgrade(db) {
                db.createObjectStore('config');
            }
        });
    },

    setConfig: async (config) => {
        console.debug('[chat-sw] storing config', config)
        const db = await ChatService.getDB();
        // store config to indexedDB
        for (const [key, value] of Object.entries(config)) {
            await db.put('config', value, key);
        }
        // add verifyRoute to cached URLs
        const verifyRoute = config?.jwtVerifyRoute;
        console.debug(`[chat-sw] setting verifyRoute to ${verifyRoute}...`);
        if (verifyRoute && (ChatService.CACHED_URLS.indexOf(verifyRoute) < 0)) {
            ChatService.CACHED_URLS.push(verifyRoute);
            console.debug(`[chat-sw] adding ${verifyRoute} to cached URLs...`);
        }
    },

    checkConnection: async () => {

        let interval = checkInterval();

        const getInterval = () => {
            let int = interval.next();
            if (int.hasOwnProperty('value')) {
                int = int.value;
            }
            return int;
        };

        const doCheck = async () => {
            if (ChatService.wsChecker !== null) {
                clearTimeout(ChatService.wsChecker);
            }
            if ((ChatService.wsClient === null) || (ChatService.wsClient.readyState === WebSocket.CLOSED)) {
                await ChatService.openConnection();
            }
            if ((ChatService.wsClient === null) || (ChatService.wsClient.readyState === WebSocket.CLOSED)) {
                ChatService.wsChecker = setTimeout(doCheck, getInterval());
            }
        };

        await doCheck();
    },

    openConnection: async () => {
        const
            db = await ChatService.getDB(),
            endpoint = await db.get('config', 'wsEndpoint'),
            token = await db.get('config', 'accessToken');

        if (endpoint && token) {
            console.debug('[chat-sw] opening websocket connection...');
            ChatService.wsClient = new WebSocket(endpoint,
                ['accessToken', token]);
            ChatService.wsClient.onopen = ChatService.onOpened;
            ChatService.wsClient.onmessage = ChatService.onMessage;
            ChatService.wsClient.onclose = ChatService.onClosed;
        }
    },

    closeConnection: () => {
        if (ChatService.wsClient !== null) {
            ChatService.wsClient.close();
            ChatService.wsClient = null;
        }
    },

    onOpened: (event) => {
        console.debug('[chat-sw] opened websocket', event);
    },

    onMessage: async (event) => {
        console.debug('[chat-sw] received websocket message', event);
        let message = event.data;
        if (typeof message === 'string') {
            try {
                message = JSON.parse(message);
            }
            catch (e) {
                console.debug('[chat-sw] JSON parsing error', message);
                return;
            }
        }
        await ChatService.handleMessage(message);
    },

    onClosed: async (event) => {
        ChatService.wsClient = null;
        console.debug('[chat-sw] closed websocket', event);
        await ChatService.checkConnection();
    },

    handleMessage: async (message) => {
        const service = ChatService.messageServices[message.action];
        if (service === undefined) {
            console.debug('[chat-sw] no message handler defined for message', message);
            return;
        }
        console.debug('[chat-sw] handle message', message);
        await service(message);
    },

    /**
     * List of service messages handlers
     */
    messageServices: {

        /**
         * Configuration setter
         *
         * @param message: initial message
         * @returns {Promise<void>}
         */
        setConfig: async (message) => {
            await ChatService.setConfig(message.config);
            await ChatService.checkConnection();
        },

        /**
         * Create notification for given message
         *
         * @param message: initial message
         * @returns {Promise<void>}
         */
        notify: async (message) => {
            checkNotificationPermission().then((status) => {
                if (!status) {
                    return;
                }
                const
                    options = {
                        body: message.message,
                        data: {
                            url: message.url
                        },
                        timestamp: message.timestamp
                    },
                    avatar = message.source?.avatar,
                    image = message.image;
                if (avatar) {
                    options.icon = avatar;
                }
                if (image) {
                    options.image = image;
                }
                ChatSW.registration.showNotification(message.title, options);
            });
            await ChatService.postMessage(message);
        },

        logout: async (message) => {
            if (message.status === 'FORBIDDEN') {
                console.debug('[chat-sw] forbidden access!');
                console.debug('[chat-sw] closing connection...');
                ChatService.closeConnection();
                console.debug('[chat-sw] refreshing JWT token...');
                const
                    db = await ChatService.getDB(),
                    jwtRoute = await db.get('config', 'jwtRefreshRoute'),
                    token = await db.get('config', 'refreshToken'),
                    response = await fetch(jwtRoute, {
                        method: 'PATCH',
                        headers: {
                            'Content-type': 'application/json',
                            'Accept': 'application/json',
                            'Authorization': `Bearer ${token}`
                        }
                    }),
                    json = await response.json();
                console.debug('[chat-sw] got JSON response:', json);
                if (json.status === 'success') {
                    await db.put('config', json.accessToken, 'accessToken');
                    await ChatService.checkConnection();
                }
            }
        }
    },

    postMessage: async (message) => {
        const clients = await ChatSW.clients.matchAll({
            includeUncontrolled: true,
            type: 'window'
        });
        if (clients && clients.length) {
            clients.forEach((client) => {
                client.postMessage(message);
            });
        }
    }
};


self.addEventListener('install', (event) => {
    console.debug('[chat-sw] install', event);
    event.waitUntil(
        caches.open(ChatService.CACHE_NAME)
            .then((cache) => {
                return cache.addAll(ChatService.CACHED_URLS);
            }));
});


self.addEventListener('activate', async (event) => {
    console.debug('[chat-sw] activate', event);
    event.waitUntil(self.clients.claim());
    await ChatService.init();
});


self.addEventListener('fetch', (event) => {
    console.debug('[chat-sw] fetch event', event.request.url, event);
    event.respondWith(
        caches.match(event.request, { ignoreSearch: true })
            .then((response) => {
                if (response) {
                    if (isValidResponse(response)) {
                        return response;
                    }
                    caches.open(ChatService.CACHE_NAME)
                        .then((cache) => {
                            cache.delete(event.request, { ignoreSearch: true }).then();
                        });
                    }
                return fetch(event.request).then((response) => {
                    const
                        request = event.request,
                        queryIndex = request.url.indexOf('?');
                    let url = request.url;
                    if (queryIndex > 0) {
                        url = request.url.substring(0, queryIndex);
                    }
                    if (!((ChatService.CACHED_URLS.indexOf(url) < 0) ||
                          !response ||
                          response.status !== 200 ||
                          response.type !== 'basic')) {
                        const cachedResponse = response.clone();
                        caches.open(ChatService.CACHE_NAME)
                            .then((cache) => {
                                console.debug(`[chat-sw] caching fetched URL ${event.request.url}...`);
                                cache.put(event.request, cachedResponse).then();
                            });
                    }
                    return response;
                });
            })
    );
});


self.addEventListener('message', async (event) => {
    console.debug('[chat-sw] message', event);
    let message = event.data;
    if (typeof message === 'string') {
        try {
            message = JSON.parse(message);
        }
        catch (e) {}
    }
    await ChatService.handleMessage(message);
});


self.addEventListener('push', async (event) => {
    console.debug('[chat-sw] push', event);
    let message = event.data.text();
    if (typeof message === 'string') {
        try {
            message = JSON.parse(message);
        }
        catch (e) {}
    }
    await ChatService.handleMessage(message);
});


self.addEventListener('notificationclick', (event) => {
    event.notification.close();
    event.waitUntil(self.clients.matchAll({
        type: 'window'
    }).then(clients => {
        for (const client of clients) {
            if ('openWindow' in client) {
                return client.openWindow(event.notification.data.url);
            }
        }
    }));
});
