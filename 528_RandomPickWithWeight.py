"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pickIndex which
randomly picks an index in proportion to its weight.

Note:
(a) 1 <= w.length <= 10000
(b) 1 <= w[i] <= 10^5
(c) pickIndex will be called at most 10000 times.
"""
from bisect import bisect_left
from itertools import accumulate
from random import randint
from typing import List


class RandomPickWithWeight:
    def __init__(self, w: List[int]):
        self.processed_w = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.processed_w, randint(1, self.processed_w[-1]))


from collections import Counter

test_cases = [[1, 2, 3, 4]]
n_cycles = 100000
for case in test_cases:
    weights = case
    random_picker = RandomPickWithWeight(weights)
    num_list = []
    for _ in range(n_cycles):
        c = random_picker.pickIndex()
        assert c < len(weights)
        num_list.append(c)
    draw_distribution = Counter(num_list)
    for key in draw_distribution:
        draw_distribution[key] /= n_cycles
    print(draw_distribution)
