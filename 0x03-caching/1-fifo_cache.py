#!/usr/bin/python3
"""
class FIFOCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    class FIFOCache that inherits from BaseCaching and is a caching system
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (not key or not item):
            return
        if (len(self.cache_data) >= BaseCaching.MAX_ITEMS):
            print("DISCARD: {}".format(next(iter(self.cache_data))))
            self.cache_data.pop(next(iter(self.cache_data)))
        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if (not key or key not in self.cache_data.keys()):
            return None
        return self.cache_data[key]
