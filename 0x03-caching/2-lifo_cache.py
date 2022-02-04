#!/usr/bin/python3
"""
class LIFOCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """
    class LIFOCache that inherits from BaseCaching and is a caching system
    """
    def put(self, key, item):
        """ Add an item in the cache
        """
        if not key or not item:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            removed = self.cache_data.popitem()
            print("DISCARD: {}".format(removed[0]))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if (not key or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
