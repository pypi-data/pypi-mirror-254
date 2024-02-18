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

"""PyAMS_chat.client module

This module defines a Redis transaction manager
"""

import json
import logging
import sys

import transaction

try:
    from fakeredis import FakeRedis
except ImportError:
    FakeRedis = None

from redis import Redis

from pyams_utils.transaction import TransactionClient, transactional


__docformat__ = 'restructuredtext'


LOGGER = logging.getLogger('PyAMS (chat)')

TEST_MODE = sys.argv[-1].endswith('/test')


class RedisClient(TransactionClient):
    """Redis client class"""

    def __init__(self,
                 server_url=None,
                 use_transaction=True,
                 transaction_manager=transaction.manager):
        super().__init__(use_transaction, transaction_manager)
        assert server_url is not None, "You must provide a Redis connection URL!"
        factory = FakeRedis if TEST_MODE else Redis
        self.redis = factory.from_url(server_url)

    def close(self):
        """Close redis connection"""
        self.redis.close()

    def __enter__(self):
        return self.redis

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.redis.close()

    @transactional
    def publish(self, channel, message):
        """Public data to given channel"""
        if not isinstance(message, str):
            message = json.dumps(message)
        LOGGER.debug(f'Publishing message to {channel} channel...')  # pylint: disable=logging-fstring-interpolation
        self.redis.publish(channel, message)
