#!/usr/bin/env python3
"""
Coroutine called async_comprehension that collects
10 random numbers and return them.
"""

from typing import List


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """A coroutine called async_comprehension."""

    return [x async for x in async_generator()]
