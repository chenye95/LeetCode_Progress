from random import randint
from typing import Any


class RandomizedSet:
    def __init__(self):
        """
        Supports unweighted randomly chooses one elements from the collection
        """
        self.obj_in_collections = []
        self.pos_to_obj_lookup = {}

    def insert(self, val: Any) -> bool:
        """
        :param val: inserts a value to the set
        :return: if the set did not already contain the specified element.
        """
        if val in self.pos_to_obj_lookup:
            return False

        self.obj_in_collections.append(val)
        self.pos_to_obj_lookup[val] = len(self.obj_in_collections) - 1
        return True

    def remove(self, val: Any) -> bool:
        """
        :param val: removes a value from the set
        :return if the set contained the specified element.
        """
        if val not in self.pos_to_obj_lookup:
            return False

        idx, lst = self.pos_to_obj_lookup[val], self.obj_in_collections[-1]
        self.obj_in_collections[idx], self.pos_to_obj_lookup[lst] = lst, idx
        self.obj_in_collections.pop()
        del self.pos_to_obj_lookup[val]
        return True

    def get_random(self) -> Any:
        """
        Get a unweighted random element from the set
        :return an object if the collection is not empty or None otherwise
        """
        if not self.obj_in_collections:
            return None
        else:
            return self.obj_in_collections[randint(0, len(self.obj_in_collections) - 1)]
