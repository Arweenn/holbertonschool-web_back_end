#!/usr/bin/python3
"""
Annotates the parameters of the
function below.
"""

from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> Listist[Tuple[Sequence, int]]:
    """Annotates the parameters of a given function"""

    return [(i, len(i)) for i in lst]
