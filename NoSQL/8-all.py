#!/usr/bin/env python3
"""
Python function that lists all documents in a collection.
"""


def list_all(mongo_collection):
    """Returns all documents in a collection."""

    return mongo_collection.find()
