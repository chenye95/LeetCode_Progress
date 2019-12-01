from random import randint


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.obj = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.pos:
            return False

        self.obj.append(val)
        self.pos[val] = len(self.obj) - 1
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.pos:
            return False

        idx, lst = self.pos[val], self.obj[-1]
        self.obj[idx], self.pos[lst] = lst, idx
        self.obj.pop()
        del self.pos[val]
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        if not self.obj:
            return None
        else:
            return self.obj[randint(0, len(self.obj) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
assert obj.insert(1)
assert obj.insert(2)
assert obj.getRandom() in set([1, 2])
assert not obj.insert(2)
assert obj.remove(1)
assert not obj.remove(1)
assert obj.getRandom() == 2