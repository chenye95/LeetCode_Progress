from collections import Counter

from _Randomized_Collection import RandomizedCollection
from _Randomized_Set import RandomizedSet

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
assert obj.insert(1)
assert not obj.insert(1)
assert obj.insert(2)
rand_counter = Counter()
for _ in range(1000):
    rand_counter[obj.getRandom()] += 1
print(rand_counter)
# param_3 = obj_in_collections.getRandom()

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
assert obj.insert(1)
assert obj.insert(2)
assert obj.getRandom() in {1, 2}
assert not obj.insert(2)
assert obj.remove(1)
assert not obj.remove(1)
assert obj.getRandom() == 2
