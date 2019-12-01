from collections import defaultdict
from _Cache_Interface import Cache

class LFUCache_Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class LFUCache_LinkedList(object):
    def __init__(self):
        self.head = LFUCache_Node(None, None)
        self.tail = LFUCache_Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def __len__(self) -> int:
        return self.size


    def insert(self, node: LFUCache_Node):
        """
        Insert to the front of Double Linked List
        """
        node.next = self.head.next
        node.prev = self.head
        node.next.prev = node
        self.head.next = node
        self.size += 1


    def pop(self, node: LFUCache_Node = None) -> LFUCache_Node:
        """
        Server tie between Node and its predecessors and successors, and decrease the list size by 1
        If Node is None, pop the last node in the linked list
        """
        if self.size == 0:
            return None

        if node is None:
            node = self.tail.prev

        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

        return node

class LFUCache(Cache):
    """
    Data structure for Least Frequently Used (LFU) cache.
    Per interface requirements, it support operations get() and put() as well as constant NOT_FOUND
    When at capacity, invalidate the least frequently used item before inserting a new item.
    When there is a tie (i.e., two or more keys that have the same frequency), the least recently used key would be evicted.
    """
    def __init__(self, capacity: int):
        super().__init__(capacity = capacity)
        self.lookup_table = {}
        self.freq_table = defaultdict(LFUCache_LinkedList)
        self.min_freq = 0

    def _update_freq(self, node: LFUCache_Node) -> None:
        """
        * Increment frequency of node by 1
        * Move node from freq list to freq + 1 list and insert to the front
        * Update min_freq when needed
        """
        freq = node.freq
        self.freq_table[freq].pop(node)

        if self.min_freq == freq and not self.freq_table[freq]:
            self.min_freq += 1

        node.freq += 1
        self.freq_table[freq + 1].insert(node)

    def get(self, key: int) -> int:
        if key in self.lookup_table:
            node = self.lookup_table[key]
            self._update_freq(node)
            return node.val
        else:
            return self.NOT_FOUND

    def put(self, key: int, val: int) -> None:
        if key in self.lookup_table:
            node = self.lookup_table[key]
            self._update_freq(node)
            node.val = val
        else:
            if len(self.lookup_table) == self.capacity:
                node = self.freq_table[self.min_freq].pop()
                del self.lookup_table[node.key]
                del node

            node = LFUCache_Node(key, val)
            self.lookup_table[key] = node
            self.freq_table[1].insert(node)
            self.min_freq = 1

