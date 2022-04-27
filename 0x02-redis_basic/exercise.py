#!/usr/bin/env python3

"""
Module exercise
"""
import redis
from typing import Union
import uuid


class Cache:
    """
    A redis Cache class
    """
    def __init__(self):
        """
        Stores an instnace of redis client
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Takes a data argument and
        returns a string
        """
        key: uuid.UUID = str(uuid.uuid1())

        self._redis.set(key, data)

        return key
