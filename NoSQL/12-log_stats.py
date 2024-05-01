#!/usr/bin/env python3
"""
Python script that provides some stats
about Nginx logs stored in MongoDB.
"""

from pymongo import MongoClient


if __name__ == "__main__":
    """
    Provide some stats about logs stored in MongoDB.
    Database: logs
    Collection: nginx
    """

    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client["logs"]
    collection = db["nginx"]

    num_logs = collection.count_documents({})
    print(f'{num_logs} logs')

    method = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    print('Methods:')
    for meth in method:
        num = collection.count_documents({"method": meth})
        print(f'\tmethod {meth}: {num}')

    status = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status} status check')
