#!/usr/bin/env python3
"""
Writing strings to Redis
"""

from uuid import uuid4
from typing import Union
import redis


def call_history(method):
    """call_history decorator"""
    def wrapper(*args, **kwargs):
        return method(*args, **kwargs)
    return wrapper


def count_calls(method):
    """count_calls decorator"""
    def wrapper(*args, **kwargs):
        return method(*args, **kwargs)
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
