#!/usr/bin/env python3
""" Insert a register into a DB NoSQL
"""


def insert_school(mongo_collection, **kwargs):
    """ Insert a register into a DB NoSQL
    Args:
        mongo_collection ([type]): all arguments
    Returns:
        [type]: id
    """
    insert_data = mongo_collection.insert_one(dict(**kwargs))
    return insert_data.inserted_id
