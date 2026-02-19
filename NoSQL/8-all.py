#!/usr/bin/env python3
"""8-all"""


def list_all(mongo_collection):
    """Lists all documents in a collection"""
    documents = list(mongo_collection.find())
    if documents == 0:
        return []
    else:
        return documents
    
