from random import randint
from typing import Any


class RandomizedCollection:
    def __init__(self):
        """
        Supports weighted randomly chooses one elements from the collection
        """
        self.values_in_collections = {}
        self.position_to_value_lookup = dict()
        self.total_counter = 0

    def insert(self, val: Any) -> bool:
        """
        Inserts a value to the collection or increment its weight by 1

        :parameter val: needs to be hashable
        :return: whether the collection did not already contain the specified element.
        """
        flag_new_obj = val not in self.values_in_collections
        if flag_new_obj:
            self.values_in_collections[val] = set()
        self.values_in_collections[val].add(self.total_counter)
        self.position_to_value_lookup[self.total_counter] = val
        self.total_counter += 1
        return flag_new_obj

    def remove(self, val: Any) -> bool:
        """
        Decrease weight of val by 1 if it exists

        :parameter val: needs to be hashable
        :return: if the collection contained the specified element.
        """
        if val not in self.values_in_collections:
            return False
        val_idx = self.values_in_collections[val].pop()
        if not self.values_in_collections[val]:  # No more val in the collections
            del self.values_in_collections[val]

        last_val = self.position_to_value_lookup[self.total_counter - 1]
        if val_idx != self.total_counter - 1:
            self.values_in_collections[last_val].remove(self.total_counter - 1)
            self.values_in_collections[last_val].add(val_idx)
            self.position_to_value_lookup[val_idx] = last_val
        else:
            del self.position_to_value_lookup[self.total_counter - 1]
        self.total_counter -= 1
        return True

    def get_random(self) -> Any:
        """
        Get a random element from the collection according to its weigh
        """
        return self.position_to_value_lookup[randint(0, self.total_counter - 1)]
