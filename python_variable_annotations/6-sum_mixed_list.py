#!/usr/bin/python3
"""
Type-annotated function sum_mixed_list that
takes a list mxd_lst of int and floats and
returns their sum as a float.
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List[Union[int, float]]) -> float:
    """Returns sum of ints and floats as a float."""

    return (sum(mxd_list))
