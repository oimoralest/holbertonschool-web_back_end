#!/usr/bin/env python3
""" find all data that contains a particular value
"""


def schools_by_topic(mongo_collection, topic):
    """ find all data that contains a particular value
    """
    return mongo_collection.find(
        {
            "topics": {
                "$in": [topic]
            }
        }
    )
