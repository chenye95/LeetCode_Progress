from random import randint
from typing import Hashable, Optional, List, Dict


class RandomizedSet:
    def __init__(self):
        """
        Supports unweighted randomly chooses one elements from the collection
        """
        self.obj_in_collections: List[Hashable] = []
        self.obj_to_pos_lookup: Dict[Hashable, int] = {}

    def insert(self, val: Hashable) -> bool:
        """
        :param val: inserts a value to the set
        :return: if the set did not already contain the specified element.
        """
        if val in self.obj_to_pos_lookup:
            return False

        self.obj_to_pos_lookup[val] = len(self.obj_in_collections)
        self.obj_in_collections.append(val)
        return True

    def remove(self, val: Hashable) -> bool:
        """
        :param val: removes a value from the set
        :return: if the set contained the specified element.
        """
        if val not in self.obj_to_pos_lookup:
            return False

        val_index = self.obj_to_pos_lookup[val]
        if val_index != len(self.obj_in_collections) - 1:
            # move last object in the list to fill the gap of val
            last_object = self.obj_in_collections[-1]
            self.obj_in_collections[val_index] = last_object
            self.obj_to_pos_lookup[last_object] = val_index

        self.obj_in_collections.pop()
        del self.obj_to_pos_lookup[val]
        return True

    def get_random(self) -> Optional[Hashable]:
        """
        Get a unweighted random element from the set

        :return: an object if the collection is not empty or None otherwise
        """
        if self.obj_in_collections:
            return self.obj_in_collections[randint(0, len(self.obj_in_collections) - 1)]
        else:
            return None
