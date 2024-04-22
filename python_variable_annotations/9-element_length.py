#!/usr/bin/env python3
"""
Annotates the parameters of the
function below.
"""

from typing import Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> list[Tuple[Sequence, int]]:
    """Annotates the parameters of a given function"""
    return [(i, len(i)) for i in lst]
