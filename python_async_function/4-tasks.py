#!/usr/bin/env python3
"""
Alter the previous code to a new function 'task_wait_n'
where 'task_wait_random' is called.
"""

from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all delays."""

    del_list = []
    for _ in range(1, n + 1):
        del_list.append(await task_wait_random(max_delay))

    for i in range(1, n):
        cle = del_list[i]
        j = i - 1

        while j >= 0 and del_list[j] > cle:
            del_list[j + 1] = del_list[j]
            j -= 1

        del_list[j + 1] = cle

    return del_list
