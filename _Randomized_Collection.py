from random import randint
from collections import Counter

class RandomizedCollection:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.val_pos = {}
        self.pos_val = {}
        self.n = 0

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag_new_obj = val not in self.val_pos
        if flag_new_obj:
            self.val_pos[val] = set()
        self.val_pos[val].add(self.n)
        self.pos_val[self.n] = val
        self.n += 1
        return flag_new_obj


    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.val_pos:
            return False
        val_idx = self.val_pos[val].pop()
        if not self.val_pos[val]: # No more val in the collections
            del self.val_pos[val]

        last_val = self.pos_val[self.n-1]
        if val_idx != self.n-1:
            self.val_pos[last_val].remove(self.n-1)
            self.val_pos[last_val].add(val_idx)
            self.pos_val[val_idx] = last_val
        else:
            del self.pos_val[self.n-1]
        self.n -= 1
        return True

    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.pos_val[randint(0, self.n-1)]

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
assert obj.insert(1)
assert not obj.insert(1)
assert obj.insert(2)
rand_counter = Counter()
for _ in range(1000):
    rand_counter[obj.getRandom()] += 1
print(rand_counter)
# param_3 = obj.getRandom()