#!/usr/bin/env python3
"""
Async routine called wait_n that takes 2 int arguments
and return the list of all delays as floats.
"""

from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all delays."""

    del_list = []
    for w in range(1, n + 1):
        del_list.append(await wait_random(max_delay))

    for x in range(1, n):
        y = del_list[x]
        z = x - 1

        while z >= 0 and del_list[z] > y:
            del_list[z + 1] = del_list[z]
            z -= 1

        del_list[z + 1] = y

    return del_list
