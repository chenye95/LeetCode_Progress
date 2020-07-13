from _Cache_LRU import LRUCache

cache = LRUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(2) == 2       # returns 1
assert cache.get(1) == 1       # returns 1
cache.put(3, 3)                # evicts key 2
assert cache.get(2) == LRUCache.NOT_FOUND       # returns NOT_FOUND
cache.put(4, 4)                # evicts key 1.
assert cache.get(1) == LRUCache.NOT_FOUND       # returns NOT_FOUND
assert cache.get(3) == 3       # returns 3
assert cache.get(4) == 4       # returns 4
