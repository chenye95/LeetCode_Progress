"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:
- put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the
value.
- get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
- remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
"""
from typing import List, Optional, Callable


class MyHashNode:
    def __init__(self, key: int, val: int):
        self.key = key
        self.val = val
        self.next = None


class MyHashMap:
    not_in_map = -1

    def __init__(self):
        """
        Hash with chaining implementation
        """
        self.bucket_count = 1000
        self.get_bucket_id: Callable[[int], int] = lambda key: key % self.bucket_count
        self.buckets: List[Optional[MyHashNode]] = [None] * self.bucket_count

    def put(self, key: int, value: int) -> None:
        bucket_id = self.get_bucket_id(key)
        if self.buckets[bucket_id] is None:
            self.buckets[bucket_id] = MyHashNode(key, value)
            return

        current_node = self.buckets[bucket_id]
        while True:
            if current_node.key == key:
                # update node if node already exists in the HashMap
                current_node.val = value
                return
            if current_node.next is None:
                break
            current_node = current_node.next

        # Insert new key into HashMap
        current_node.next = MyHashNode(key, value)

    def get(self, key: int) -> int:
        """
        :return: the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        bucket_id = self.get_bucket_id(key)

        current_node = self.buckets[bucket_id]
        while current_node:
            if current_node.key == key:
                return current_node.val
            current_node = current_node.next

        return self.not_in_map

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        bucket_id = self.get_bucket_id(key)
        if self.buckets[bucket_id] is None:
            return

        prev_node, current_node = None, self.buckets[bucket_id]
        if current_node.key == key:
            self.buckets[bucket_id] = current_node.next
            return

        while current_node:
            if current_node.key == key:
                prev_node.next = current_node.next
                break
            else:
                prev_node, current_node = current_node, current_node.next


test_map = MyHashMap()
test_map.put(1, 1)
test_map.put(2, 2)
assert test_map.get(1) == 1
assert test_map.get(3) == test_map.not_in_map
test_map.put(2, 1)
assert test_map.get(2) == 1
test_map.remove(2)
assert test_map.get(2) == test_map.not_in_map
