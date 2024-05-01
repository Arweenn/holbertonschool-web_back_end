#!/usr/bin/env python3
"""
Python function that inserts a new document in a collection.
"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""

    new_id = mongo_collection.insert_one(kwargs).inserted_id
    return new_id
