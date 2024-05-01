#!/usr/bin/env python3
"""
Function that takes two arguments ('page' and 'page_size') and return
a tuple of size two.
"""


def index_range(page, page_size):
    """
    Return a tuple of size twocontaining a start index and
    an end index corresponding to the range of indexes.
    """

    start = (page - 1) * page_size
    end = page * page_size
    range = start, end

    return range
