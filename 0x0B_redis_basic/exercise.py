#!/usr/bin/env python3
"""
Writing strings to Redis
"""

from uuid import uuid4
from typing import Union, Optional, Callable
import redis
from functools import wraps


def call_history(method):
    """call_history decorator"""
    def wrapper(*args, **kwargs):
        return method(*args, **kwargs)
    return wrapper


def count_calls(method: Callable) -> Callable:
    """ Decorator for counting how many times a function
    has been called """

    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper for decorator functionality """
        self._redis.incr(key)
        return method(self, *args, **kwargs)

    return wrapper


class Cache:
    """ Class Cache """

    def __init__(self):
        """ Constructor Method """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store the input data in Redis using a
        random key and return the key.
        """
        random_key = str(uuid4())
        self._redis.set(random_key, data)

        return random_key

    def get(self, key: str,
            fn: Optional[Callable] = None) -> Union[str, bytes, int, float]:
        """
        store input data in dedis using a random key
        and return a key
        """
        value = self._redis.get(key)
        if fn:
            value = fn(value)

        return value

    def get_str(self, key: str) -> str:
        """
        param a value from redis to str
        """
        value = self._redis.get(key)
        return value.decode('utf-8')

    def get_int(self, key: int) -> int:
        """
        param a value from redis to int
        """
        value = self._redis.get(key)
        try:
            value = int(value.decode('utf-8'))
        except Exception:
            value = 0
        return value
