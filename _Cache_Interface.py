class Cache(object):
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

    def get(self, key: int) -> int:
        pass

    def put(self, key: int, val: int) -> None:
        pass
