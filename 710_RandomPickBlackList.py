"""
Given a black_list B containing unique integers from [0, n), write a function to return a uniform random integer from
[0, n) which is NOT in B.
"""
from collections import Counter
from random import randint
from typing import List


class RandomPickBlackList:
    def __init__(self, n: int, black_list: List[int]):
        """
        :param n: integers from [0, n)
        :param black_list: a subset of [0, n) to avoid by random generator
        """
        black_set = set(black_list)
        self.white_N = n - len(black_set)
        key = [x for x in black_set if x < self.white_N]
        val = [x for x in range(self.white_N, n) if x not in black_set]
        self.mapping = dict(zip(key, val))

    def pick(self) -> int:
        """
        :return: uniformly select an integer from [0, n) that is not on the black list
        """
        i = randint(0, self.white_N - 1)
        return self.mapping.get(i, i)


test_cases = [(10, [3, 4, 6, 5, 3])]
n_cycles = 100_000
expected_delta = 500
for case in test_cases:
    N, blacklist = case
    random_picker = RandomPickBlackList(N, blacklist)
    num_list = []
    for _ in range(n_cycles):
        c = random_picker.pick()
        assert c not in blacklist and 0 <= c < N
        num_list.append(c)
    output_counter = Counter(num_list)
    expected_mean = n_cycles // len(output_counter)
    for i in output_counter:
        assert expected_mean - expected_delta <= output_counter[i] <= expected_mean + expected_delta, \
            "%d: %d" % (i, output_counter[i])
