"""
Design and implement a data structure for a Least Frequently Used (LFU) cache.

Implement the LFUCache class:
- LFUCache(int capacity) Initializes the object with the capacity of the data structure.
- int get(int key) Gets the value of the key if the key exists in the cache. Otherwise, returns -1.
- void put(int key, int value) Update the value of the key if present, or inserts the key if not already present. When
 the cache reaches its capacity, it should invalidate and remove the least frequently used key before inserting a new
 item. For this problem, when there is a tie (i.e., two or more keys with the same frequency), the least recently used
 key would be invalidated.

To determine the least frequently used key, a use counter is maintained for each key in the cache. The key with the
 smallest use counter is the least frequently used key.

When a key is first inserted into the cache, its use counter is set to 1 (due to the put operation). The use counter for
 a key in the cache is incremented either a get or put operation is called on it.
"""
from typing import List, Optional

from _Cache_LFU import LFUCache


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[int]]) -> None:
    test_object = LFUCache(parameters[0][0])
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "put":
            test_object.put(next_parameter[0], next_parameter[1])
        else:
            assert test_object.get(next_parameter[0]) == expected_value


# Place holders to run test cases
test_cases = [(["LFUCache", "put", "put", "get", "put", "get", "get", "put", "get", "get", "get"],
               [[2], [1, 1], [2, 2], [1], [3, 3], [2], [3], [4, 4], [1], [3], [4]],
               [None, None, None, 1, None, -1, 3, None, -1, 3, 4]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
