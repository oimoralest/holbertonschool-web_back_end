#!/usr/bin/python3
"""
class LRUCache that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """
    class LRUCache that inherits from BaseCaching
    """

    QUEUE = []

    def update_queue(self, key_to_remove, key_to_append):
        """ update queue
        """
        self.__class__.QUEUE.remove(key_to_remove)
        self.__class__.QUEUE.append(key_to_append)

    def put(self, key, item):
        """ Add an item in the cache
        """
        if (not key or not item):
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            if key in self.cache_data.keys():
                self.cache_data[key] = item
                self.update_queue(key, key)
            else:
                print("DISCARD: {}".format(self.__class__.QUEUE[0]))
                key_to_delete = self.__class__.QUEUE[0]
                del self.cache_data[key_to_delete]
                self.cache_data[key] = item
                self.update_queue(key_to_delete, key)

        else:

            self.cache_data[key] = item
            self.__class__.QUEUE.append(key)

    def get(self, key):
        """ key item to retrieve
        """
        if (not key or key not in self.cache_data.keys()):
            return None
        self.update_queue(key, key)
        return self.cache_data[key]
