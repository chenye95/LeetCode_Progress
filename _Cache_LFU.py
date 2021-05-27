from collections import defaultdict
from typing import Optional, Any

from _Cache_Interface import Cache, CacheNode


class _LFUCacheLinkedList:
    def __init__(self):
        self.dummy_head = CacheNode(-1, None, True)
        self.dummy_tail = CacheNode(-1, None, True)
        self.dummy_head.next = self.dummy_tail
        self.dummy_tail.prev = self.dummy_head
        self.size = 0

    def __len__(self) -> int:
        return self.size

    def insert(self, node: CacheNode):
        """
        :param node: insert node to the front of the Double Linked List
        """
        node.next = self.dummy_head.next
        node.prev = self.dummy_head
        node.next.prev = node
        self.dummy_head.next = node
        self.size += 1

    def pop(self, node: Optional[CacheNode] = None) -> Optional[CacheNode]:
        """
        Server tie between Node and its predecessors and successors, and decrease the list size by 1
        If Node is None, pop the last node in the linked list

        :param node: node to be removed from the double linked list, i.e. server tie between node and its prev and next.
            If node is None, short hand for removing the last node of the linked list
        :return: CacheNode that is removed from the linked list. None if the list is empty
        """
        if self.size == 0:
            return None

        if node is None:
            node = self.dummy_tail.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

        return node


class LFUCache(Cache):
    """
    Data structure for Least Frequently Used (LFU) cache.
    Per interface requirements, it support operations get() and put() as well as constant NOT_FOUND
    When at capacity, invalidate the least frequently used item before inserting a new item.
    When there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be
     evicted.
    """

    def __init__(self, capacity: int):
        super().__init__(capacity=capacity)
        self.lookup_table = {}
        self.freq_table = defaultdict(_LFUCacheLinkedList)
        self.min_freq = 0

    def _update_freq(self, node: CacheNode) -> None:
        """
        * Increment frequency of node by 1
        * Move node from freq list to freq + 1 list and insert to the front
        * Update min_freq when needed

        :param node: increment frequency of node by 1
        """
        freq = node.freq
        self.freq_table[freq].pop(node)

        if self.min_freq == freq and not self.freq_table[freq]:
            self.min_freq += 1

        node.freq += 1
        self.freq_table[freq + 1].insert(node)

    def get(self, key: int) -> Any:
        if key in self.lookup_table:
            node = self.lookup_table[key]
            self._update_freq(node)
            return node.val
        else:
            return self.NOT_FOUND

    def put(self, key: int, val: Any) -> None:
        if key in self.lookup_table:
            node = self.lookup_table[key]
            self._update_freq(node)
            node.val = val
        else:
            if len(self.lookup_table) == self.capacity:
                node = self.freq_table[self.min_freq].pop()
                del self.lookup_table[node.key]
                del node

            node = CacheNode(key, val, True)
            self.lookup_table[key] = node
            self.freq_table[1].insert(node)
            self.min_freq = 1
