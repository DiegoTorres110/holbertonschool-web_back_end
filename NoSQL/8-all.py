#!/usr/bin/env python3
#Act8
def list_all(mongo_collection):
    x = mongo_collection.find()
    if x.count() == 0:
      return[]
    else:
      return x
