#!/usr/bin/env python3
"""
Module for task 9: Insert a document in Python using PyMongo
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    Returns the new _id of the inserted document
    """
    new_document = mongo_collection.insert_one(kwargs)
    return new_document.inserted_id
