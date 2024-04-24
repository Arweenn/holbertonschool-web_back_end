#!/usr/bin/env python3
"""
Coroutine called async_generator that loop 10 times
and wait 1 second between each loop, then yield a
random number from 0 to 10.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """A coroutine that loops 10 times."""

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
