#!/usr/bin/python3
"""
Type-annotated function sum_list
that takes a list of floats and returns
their sum as a float.
"""


def sum_list(input_list: list[float]) -> float:
    """Returns the sum of a list of floats."""

    sum_input = 0.0
    for input in input_list:
        sum_input += input
    return sum_input
