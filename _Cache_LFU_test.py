from _Cache_LFU import LFUCache

cache = LFUCache(2)
cache.put(1, 1)
cache.put(2, 2)
assert cache.get(1) == 1       # returns 1
cache.put(3, 3)                # evicts key 2
assert cache.get(2) == LFUCache.NOT_FOUND       # returns NOT_FOUND
assert cache.get(3) == 3       # returns 3.
cache.put(4, 4)                # evicts key 1.
assert cache.get(1) == LFUCache.NOT_FOUND       # returns NOT_FOUND
assert cache.get(3) == 3       # returns 3
assert cache.get(4) == 4       # returns 4
cache.put(5, 5)
assert cache.get(3) == 3       # return 3
assert cache.get(4) == LFUCache.NOT_FOUND      # returns NOT_FOUND
assert cache.get(5) == 5       # return 5
