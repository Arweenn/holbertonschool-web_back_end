#!/usr/bin/python3
"""
Type-annotated function to_kv that
takes a string and an int/float v as
arguments and returns a tuple.
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple."""

    return (k, v * v)
