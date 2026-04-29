#!/usr/bin/env python3
"""
Module that contains the function insert_school
"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs
    """
    # Usamos insert_one, que es el estándar actual
    result = mongo_collection.insert_one(kwargs)
    
    # Debes retornar el atributo .inserted_id del objeto resultante
    return result.inserted_id
