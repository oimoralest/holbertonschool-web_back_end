#!/usr/bin/python3
"""
BasicCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    class BasicCache that inherits from BaseCaching and is a caching system
    """

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (not key or not item):
            return
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if (not key or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
