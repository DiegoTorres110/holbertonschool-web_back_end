#!/usr/bin/env python3
""" Write a Python function that inserts a new document in a
    collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
    """ mongo_collection will be the pymongo collection object
        Returns the new _id
    """
    # Use insert_one for a single document
    result = mongo_collection.insert_one(kwargs)
    
    # Return specifically the inserted_id attribute
    return result.inserted_id
