from typing import Any

from _Cache_Interface import Cache, CacheNode


class LRUCache(Cache):
    """
    Data structure for Least Recently Used (LRU) cache.
    Per interface requirements, it support operations get() and put() as well as constant NOT_FOUND
    When at capacity, invalidate the least recently used item before inserting a new item.
    """

    def __init__(self, capacity: int):
        super().__init__(capacity=capacity)
        self.lookup_table = {}
        self.delete_end = CacheNode(-1, None)
        self.insert_end = CacheNode(-1, None)
        self.delete_end.next = self.insert_end
        self.insert_end.prev = self.delete_end

    def get(self, key: int) -> int:
        if key in self.lookup_table:
            node = self.lookup_table[key]
            if self.insert_end.prev != node:
                node.prev.next = node.next
                node.next.prev = node.prev
                self._insert_node(node)
            return node.val
        else:
            return self.NOT_FOUND

    def put(self, key: int, value: Any) -> None:
        if key in self.lookup_table:
            node = self.lookup_table[key]
            node.val = value
            if self.insert_end.prev != node:
                node.prev.next = node.next
                node.next.prev = node.prev
                self._insert_node(node)
        else:
            if len(self.lookup_table) >= self.capacity:
                node_evict = self.delete_end.next
                self.delete_end.next = node_evict.next
                node_evict.next.prev = self.delete_end
                del self.lookup_table[node_evict.key]
                del node_evict
            node = CacheNode(key, value)
            self.lookup_table[key] = node
            self._insert_node(node)

    def _insert_node(self, node: CacheNode) -> None:
        """
        :param node:iInsert to the end of the list, before the INSERT_END
        """
        self.insert_end.prev.next = node
        node.prev = self.insert_end.prev
        node.next = self.insert_end
        self.insert_end.prev = node
