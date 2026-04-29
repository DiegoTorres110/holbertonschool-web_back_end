#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def log_stats():
    """Display stats about Nginx logs stored in MongoDB"""
    client = MongoClient('mongodb://localhost:27017')
    collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    total = collection.count_documents({})
    print("{} logs".format(total))

    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, count))

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))


if __name__ == '__main__':
    log_stats()
    
