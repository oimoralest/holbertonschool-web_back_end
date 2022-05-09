#!/usr/bin/env python3
""" some stats of nginx logs
"""
from pymongo import MongoClient


def logs_stats_ip(mongo_collection):
    """ Improving logs stats print ips
    Args:
        mongo_collection ([type]): [description]
    Returns:
        [type]: [description]
    """
    return collection.aggregate([
        {
            "$group": {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {
            "$sort": {"count": -1, "_id": -1}
        },
        {
            "$limit": 10
        }
    ])


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    documents = collection.count_documents({})
    print(f"{documents} logs")
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status_check} status check')

    # add top 10 of the most present IPs in the collection
    print("IPs:")
    ips = logs_stats_ip(collection)
    for ip in ips:
        print("\t{_id} {count}".format(**ip))
