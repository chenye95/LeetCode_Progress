from collections import Counter

from _Randomized_Collection import RandomizedCollection
from _Randomized_Set import RandomizedSet

# Your RandomizedCollection object will be instantiated and called as such:
obj = RandomizedCollection()
assert obj.get_random() is None
assert obj.insert(1) is True
assert obj.insert(1) is False
assert obj.insert(2) is True
rand_counter = Counter()
for _ in range(1000):
    rand_counter[obj.get_random()] += 1
assert rand_counter[1] + rand_counter[2] == 1000
assert 666 - 40 <= rand_counter[1] <= 666 + 40
assert 334 - 40 <= rand_counter[2] <= 334 + 40
assert obj.remove(1) is True
assert obj.get_random() in {1, 2}
assert obj.remove(1) is True
assert obj.get_random() == 2
assert obj.remove(1) is False
assert obj.get_random() == 2
assert obj.insert(1) is True
assert obj.remove(2) is True
assert obj.get_random() == 1
# param_3 = obj_in_collections.get_random()

# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet()
assert obj.get_random() is None
assert obj.insert(1) is True
assert obj.get_random() == 1
assert obj.insert(1) is False
assert obj.get_random() == 1
assert obj.insert(2) is True
assert obj.get_random() in {1, 2}
random_counter_2 = Counter()
for _ in range(1000):
    random_counter_2[obj.get_random()] += 1
assert random_counter_2[1] + random_counter_2[2] == 1000
assert 500 - 50 <= random_counter_2[1] <= 500 + 50
assert 500 - 50 <= random_counter_2[2] <= 500 + 50
assert obj.insert(2) is False
assert obj.get_random() in {1, 2}
assert obj.remove(1) is True
assert obj.remove(1) is False
assert obj.get_random() == 2
