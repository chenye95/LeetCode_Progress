"""
Given a blacklist B containing unique integers from [0, N), write a function to return a uniform random integer from
[0, N) which is NOT in B.
"""
from collections import Counter
from random import randint
from typing import List


class RandomPickBlackList:
    def __init__(self, N: int, blacklist: List[int]):
        black_set = set(blacklist)
        self.white_N = N - len(black_set)
        key = [x for x in black_set if x < self.white_N]
        val = [x for x in range(self.white_N, N) if x not in black_set]
        self.mapping = dict(zip(key, val))

    def pick(self) -> int:
        i = randint(0, self.white_N - 1)
        return self.mapping.get(i, i)


test_cases = [(10, [3, 4, 6, 5, 3])]
n_cycles = 100000
for case in test_cases:
    N, blacklist = case
    random_picker = RandomPickBlackList(N, blacklist)
    num_list = []
    for _ in range(n_cycles):
        c = random_picker.pick()
        assert c not in blacklist and 0 <= c < N
        num_list.append(c)
    print(Counter(num_list))

