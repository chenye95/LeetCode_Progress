from typing import Any


class CacheNode:
    def __init__(self, key: int, val: Any, is_LFU: bool = False):
        self.key = key
        self.val = val
        self.prev = self.next = None
        if is_LFU:
            self.freq = 1


class Cache:
    """
    Interface Definition for all Cache implementation
    All implementation supports put() and get(), as well as constant NOT_FOUND
    """
    NOT_FOUND = -1
    MIN_CAPACITY_THRESHOLD = 0

    def __init__(self, capacity: int):
        assert capacity > self.MIN_CAPACITY_THRESHOLD, \
            "Cache system should hold more than %d items" % self.MIN_CAPACITY_THRESHOLD
        self.capacity = capacity

    def get(self, key: int) -> Any:
        pass

    def put(self, key: int, val: Any) -> None:
        pass
