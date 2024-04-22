#!/usr/bin/env python3
"""
Type-annotated function sum_mixed_list that
takes a list mxd_lst of int and floats and
returns their sum as a float.
"""

from typing import Union


def sum_mixed_list(mxd_list: list[Union[int, float]]) -> float:
    """Returns sum of ints and floats as a float."""

    sum = 0.0
    for input in mxd_list:
        sum += input
    return sum
