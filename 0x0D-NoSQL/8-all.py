#!/usr/bin/env python3
"""List all documents inside collection
"""


def list_all(mongo_collection):
    """ mongo_collection will be the pymongo collection object
    Returns:
        collections otherwise empty list
    """
    collections = mongo_collection.find()
    if collections.count() > 0:
        return collections
    else:
        return []
