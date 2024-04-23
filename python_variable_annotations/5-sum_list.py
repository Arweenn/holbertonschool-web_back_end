#!/usr/bin/python3
"""
Type-annotated function sum_list
that takes a list of floats and returns
their sum as a float.
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of a list of floats."""

    return (sum(input_list))
