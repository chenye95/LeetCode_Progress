"""
AllOne() Initializes the object of the data structure.
- increment(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert
    it with count 1.
- decrement(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement,
    remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
- get_max_key() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
- getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
"""
from typing import Dict, Set, List, Optional


class KeysByCount:
    def __init__(self, count: int = 0):
        self.count: int = count
        self.keys: Set[str] = set()
        self.before: Optional[KeysByCount] = None
        self.after: Optional[KeysByCount] = None

    def remove_self(self):
        self.before.after = self.after
        self.after.before = self.before
        self.after = self.before = None

    def insert_after(self, new_block: "KeysByCount"):
        """
        :param new_block: insert new count block after current block
        """
        old_after = self.after
        self.after = new_block
        new_block.before = self
        new_block.after = old_after
        old_after.before = new_block


class AllOne:
    def __init__(self):
        """
        Use double linked list to store key sets by count: each block contain the set of keys that has the same count
        """
        self.dummy_start = KeysByCount()
        self.dummy_end = KeysByCount()
        self.dummy_start.after = self.dummy_end
        self.dummy_end.before = self.dummy_start
        self.key_to_block: Dict[str, KeysByCount] = {}

    def increment(self, key: str) -> None:
        """
        :param key: Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        """
        if key in self.key_to_block:
            current_block = self.key_to_block[key]
            current_block.keys.remove(key)
        else:
            current_block = self.dummy_start

        if current_block.count + 1 != current_block.after.count:
            # insert new block
            key_new_block = KeysByCount(count=current_block.count + 1)
            current_block.insert_after(key_new_block)
        else:
            key_new_block = current_block.after

        # update block associated with key
        key_new_block.keys.add(key)
        self.key_to_block[key] = key_new_block

        # delete current block if no longer holds any key
        if current_block.count and not current_block.keys:
            current_block.remove_self()

    def decrement(self, key: str) -> None:
        """
        :param key: Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        """
        if key not in self.key_to_block:
            return

        current_block = self.key_to_block[key]
        current_block.keys.remove(key)
        del self.key_to_block[key]

        if current_block.count > 1:
            if current_block.count - 1 != current_block.before.count:
                # need to insert a new block
                key_new_block = KeysByCount(count=current_block.count - 1)
                current_block.before.insert_after(key_new_block)
            else:
                key_new_block = current_block.before

            # update block associated with key
            key_new_block.keys.add(key)
            self.key_to_block[key] = key_new_block

        # delete current block if no longer holds any key
        if current_block.count and not current_block.keys:
            current_block.remove_self()

    def get_max_key(self) -> str:
        """
        :return: one of the keys with maximal value. or “” if data structure is empty
        """
        if self.dummy_end.before.count == 0:
            return ""
        else:
            return_val = self.dummy_end.before.keys.pop()
            self.dummy_end.before.keys.add(return_val)
            return return_val

    def get_min_key(self) -> str:
        """
        :return: one of the keys with Minimal value. or “” if data structure is empty
        """
        if self.dummy_start.after.count == 0:
            return ""
        else:
            return_val = self.dummy_start.after.keys.pop()
            self.dummy_start.after.keys.add(return_val)
            return return_val


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[str]]) -> None:
    test_object = AllOne()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value_set = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "inc":
            test_object.increment(next_parameter[0])
        elif next_instruction == "dec":
            test_object.decrement(next_parameter[0])
        elif next_instruction == "getMaxKey":
            assert test_object.get_max_key() in expected_value_set
        else:
            assert test_object.get_min_key() in expected_value_set


test_cases = [(["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"],
               [[], ["hello"], ["hello"], [], [], ["leet"], [], []],
               [None, None, None, {"hello"}, {"hello"}, None, {"hello"}, {"leet"}]),
              (["AllOne", "inc", "inc", "inc", "inc", "inc", "dec", "getMaxKey", "getMinKey", "inc", "inc", "inc",
                "getMaxKey", "getMinKey", "inc", "inc", "getMinKey"],
               [[], ["hello"], ["hello"], ["world"], ["world"], ["hello"], ["world"], [], [], ["world"], ["world"],
                ["leet"], [], [], ["leet"], ["leet"], []],
               [None, None, None, None, None, None, None, {"hello"}, {"world"}, None, None, None, {"world", "hello"},
                {"leet"}, None, None, {"world", "hello", "leet"}]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
