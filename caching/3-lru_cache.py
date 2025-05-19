#!/usr/bin/python3
""" LRU Caching """

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ LRU caching """

    def __init__(self):
        """ Constructor """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ Puts item in cache """
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed = self.queue.pop(0)
            del self.cache_data[removed]
            print("DISCARD: {}".format(removed))

        if key in self.queue:
            self.queue.remove(key)
        self.queue.append(key)

    def get(self, key):
        """ Gets item from cache """
        if key in self.queue:
            self.queue.remove(key)
            self.queue.append(key)
        return self.cache_data.get(key, None)
