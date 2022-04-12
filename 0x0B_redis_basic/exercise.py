#!/usr/bin/end python3
"""Creates a cache class which connects with Redis"""
from functools import wraps
from typing import Any, Callable, Optional, Union
import redis
from uuid import uuid4


def call_history(method: Callable) -> Callable:

    inputs: str = method.__qualname__ + ":inputs"
    outputs: str = method.__qualname__ + ":outputs"

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        self._redis.rpush(inputs, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(outputs, str(output))

        return output

    return wrapper


def count_calls(method: Callable) -> Callable:
    """Creates a decorator that count how many time a method has been called

    Arguments:
        - method: Callable method of a class

    Return:
        - wrapper: Function applicable as decorator
    """
    key: str = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """ Wrapper for method """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


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

    @call_history
    @count_calls
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
