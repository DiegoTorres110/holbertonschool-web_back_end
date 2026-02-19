//Act8
#!/usr/bin/env python3
def list_all(mongo_collection):
    x = mongo_collection.find()
    return list(x)
