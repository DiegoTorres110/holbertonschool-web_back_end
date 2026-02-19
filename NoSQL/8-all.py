#!/usr/bin/env python3
def list_all(mongo_collection):
    documents = list(mongo_collection.find())
    if documents == 0:
        return []
    else:
        return documents
    
