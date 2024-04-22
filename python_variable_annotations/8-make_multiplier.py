#!/usr/bin/python3
"""
Type-annotated function make_multiplier that
takes a float multiplier and returns
a function that multiplies a float by multiplier.
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Multiplies a float by another."""

    def mult(n: float) -> float:
        """Returns a float."""

        return n * multiplier

    return mult
