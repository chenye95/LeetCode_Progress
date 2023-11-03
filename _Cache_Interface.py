from typing import Any


class CacheNode:
    def __init__(self, key: int, val: Any, is_lfu: bool = False):
        self.key = key
        self.val = val
        self.prev = self.next = None
        if is_lfu:
            self.freq = 1


class Cache:
    """
    Interface Definition for all Cache implementation
    All implementation supports put() and get(), as well as constant NOT_FOUND
    """
    NOT_FOUND = -1
    MIN_CAPACITY_THRESHOLD = 0

    def __init__(self, capacity: int):
        """
        Initialize a cache object of capacity

        :param capacity: capacity should be larger than Cache.MIN_CAPACITY_THRESHOLD
        """
        assert capacity > self.MIN_CAPACITY_THRESHOLD, \
            "Cache system should hold more than %d items" % self.MIN_CAPACITY_THRESHOLD
        self.capacity = capacity

    def get(self, key: int) -> Any:
        """
        :param key: query value associated with key
        :return: value associated with key, return Cache.NOT_FOUND if key doesn't exist or have been evicted
        """
        pass

    def put(self, key: int, val: Any) -> None:
        """
        :param key: put key-val pair into cache object
        :param val: put key-val pair into cache object
        """
        pass
