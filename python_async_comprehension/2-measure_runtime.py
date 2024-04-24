#!/usr/bin/env python3
"""
Coroutine that will execute async_comprehension
four times using asyncio.gather.
"""

import asyncio
import time


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measure the runtime and return it."""

    task = []
    start = time.time()

    for x in range(4):
        task.append(asyncio.create_task(async_comprehension()))

    await asyncio.gather(*task)
    end = time.time()

    return end - start
