#!/usr/bin/end python3
"""Creates a cache class which connects with Redis"""
from typing import Union
import redis
from uuid import uuid4


class Cache(object):
    """Defines a Cache class to track(query) data stored in Redis"""
    def __init__(self) -> None:
        """Constructor: creates a connection with redis"""
        self._redis: redis.Redis = redis.Redis()

        self._redis.flushdb(asynchronous=True)

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data inside Redis

        Arguments:
            - data [Any]: data to be stored in Redis

        Return:
            - key [str]: Key for the data stored in Redis
        """
        key: str = str(uuid4())
        self._redis.set(name=key, value=data)

        return key
