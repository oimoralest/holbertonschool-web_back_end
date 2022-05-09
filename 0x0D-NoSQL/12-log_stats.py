#!/usr/bin/env python3
""" some stats of nginx logs
"""
from pymongo import MongoClient


# def log_stats(collection):
#     return collection.find()


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
