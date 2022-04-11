#!/usr/bin/end python3
"""Creates a cache class which connects with Redis"""
from typing import Callable, Optional, Union
import redis
from uuid import uuid4


class Cache(object):
    """Defines a Cache class to track(query) data stored in Redis"""
    def __init__(self) -> None:
        """Constructor: creates a connection with redis"""
        self._redis: redis.Redis = redis.Redis()
        self._redis.flushdb()

    def get(
        self,
        key: str,
        fn: Optional[Callable] = None
    ) -> Union[str, bytes, int, float]:
        """Gets the value if a given key an applies on it a passed function if
        this last is available

        Arguments:
            - Key: Key to look for
            - fn: Callable to apply on the returned data

        Return:
            - data: data stored in Redis
        """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_int(self, key: str) -> int:
        """Look for a key and return the data converted into int if it is
        possible

        Arguments:
            - key: Key to look for

        Return:
            - data: data stored in Redis
        """
        data = self._redis.get(key)
        try:
            data = int(data.decode("utf-8"))
        except Exception:
            data = 0
        return data

    def get_str(self, key: str) -> str:
        """Look for a key and return the data converted into str

        Arguments:
            - key: Key to look for

        Return:
            - data: data stored in Redis
        """
        data = self._redis.get(key)
        return data.decode()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores data inside Redis

        Arguments:
            - data: data to be stored in Redis

        Return:
            - key: Key for the data stored in Redis
        """
        key: str = str(uuid4())
        self._redis.set(name=key, value=data)

        return key
