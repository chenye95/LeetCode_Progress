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
    NOT_IN_HASH_MAP = -1

    def __init__(self, bucket_count: int = 500):
        """
        Hash with chaining implementation
        """
        self.bucket_count = bucket_count
        self.get_bucket_id: Callable[[int], int] = lambda key: key % self.bucket_count
        self.buckets: List[Optional[MyHashNode]] = [None] * bucket_count

    def put(self, key: int, value: int) -> None:
        """
        :param key: put an association {key: value} into HashMap, 0 <= key, value <= 10**6
        :param value: put an association {key: value} into HashMap, 0 <= key, value <= 10**6
        """
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
        :param key: query key: retrieve value associated with key, 0 <= key <= 10**6
        :return: the value to which the specified key is mapped, or NOT_IN_HASH_MAP if this map contains no mapping for
            the key
        """
        bucket_id = self.get_bucket_id(key)

        current_node = self.buckets[bucket_id]
        while current_node:
            if current_node.key == key:
                return current_node.val
            current_node = current_node.next

        return self.NOT_IN_HASH_MAP

    def remove(self, key: int) -> None:
        """
        :param key: removes the mapping of the specified value key if this map contains a mapping for the key
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


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[int]]) -> None:
    test_object = MyHashMap()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "put":
            test_object.put(next_parameter[0], next_parameter[1])
        elif next_instruction == "remove":
            test_object.remove(next_parameter[0])
        else:
            assert test_object.get(next_parameter[0]) == expected_value


test_cases = [(["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"],
               [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]],
               [None, None, None, 1, -1, None, 1, None, -1]),
              (["MyHashMap", "remove", "put", "remove", "remove", "get", "remove", "put", "get", "remove", "put", "put",
                "put", "put", "put", "put", "put", "put", "put", "put", "put", "remove", "put", "put", "get", "put",
                "get", "put", "put", "get", "put", "remove", "remove", "put", "put", "get", "remove", "put", "put",
                "put", "get", "put", "put", "remove", "put", "remove", "remove", "remove", "put", "remove", "get",
                "put", "put", "put", "put", "remove", "put", "get", "put", "put", "get", "put", "remove", "get", "get",
                "remove", "put", "put", "put", "put", "put", "put", "get", "get", "remove", "put", "put", "put", "put",
                "get", "remove", "put", "put", "put", "put", "put", "put", "put", "put", "put", "put", "remove",
                "remove", "get", "remove", "put", "put", "remove", "get", "put", "put"],
               [[], [27], [65, 65], [19], [0], [18], [3], [42, 0], [19], [42], [17, 90], [31, 76], [48, 71], [5, 50],
                [7, 68], [73, 74], [85, 18], [74, 95], [84, 82], [59, 29], [71, 71], [42], [51, 40], [33, 76], [17],
                [89, 95], [95], [30, 31], [37, 99], [51], [95, 35], [65], [81], [61, 46], [50, 33], [59], [5], [75, 89],
                [80, 17], [35, 94], [80], [19, 68], [13, 17], [70], [28, 35], [99], [37], [13], [90, 83], [41], [50],
                [29, 98], [54, 72], [6, 8], [51, 88], [13], [8, 22], [85], [31, 22], [60, 9], [96], [6, 35], [54], [15],
                [28], [51], [80, 69], [58, 92], [13, 12], [91, 56], [83, 52], [8, 48], [62], [54], [25], [36, 4],
                [67, 68], [83, 36], [47, 58], [82], [36], [30, 85], [33, 87], [42, 18], [68, 83], [50, 53], [32, 78],
                [48, 90], [97, 95], [13, 8], [15, 7], [5], [42], [20], [65], [57, 9], [2, 41], [6], [33], [16, 44],
                [95, 30]],
               [None, None, None, None, None, -1, None, None, -1, None, None, None, None, None, None, None, None, None,
                None, None, None, None, None, None, 90, None, -1, None, None, 40, None, None, None, None, None, 29,
                None, None, None, None, 17, None, None, None, None, None, None, None, None, None, 33, None, None, None,
                None, None, None, 18, None, None, -1, None, None, -1, 35, None, None, None, None, None, None, None, -1,
                -1, None, None, None, None, None, -1, None, None, None, None, None, None, None, None, None, None, None,
                None, None, -1, None, None, None, None, 87, None, None]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
