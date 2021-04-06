"""
Given an array w of positive integers, where w[i] describes the weight of index i, write a function pick_index which
randomly picks an index in proportion to its weight.

Note:
(a) 1 <= w.length <= 10000
(b) 1 <= w[i] <= 10^5
(c) pick_index will be called at most 10000 times.
"""
from bisect import bisect_left
from collections import Counter
from itertools import accumulate
from random import randint
from typing import List


class RandomPickWithWeight:
    def __init__(self, w: List[int]):
        """
        :param w: w[i] describes the weight of index i
        """
        self.processed_w = list(accumulate(w))

    def pick_index(self) -> int:
        """
        :return: randomly picks an index in [0, ..., len(w) - 1] with weights w
        """
        return bisect_left(self.processed_w, randint(1, self.processed_w[-1]))


test_cases = [[1], [1, 2, 3, 4], [1, 3], ]
n_cycles = 100_000
acceptable_delta = 0.005
for weights in test_cases:
    expected_distribution = [c / float(sum(weights)) for c in weights]
    random_picker = RandomPickWithWeight(w=weights)
    num_list = []
    for _ in range(n_cycles):
        c = random_picker.pick_index()
        assert c < len(weights)
        num_list.append(c)
    draw_distribution = Counter(num_list)
    for key in draw_distribution:
        draw_distribution[key] /= n_cycles
    assert all(abs(draw_distribution[c] - expected_distribution[c]) < acceptable_delta for c in draw_distribution), \
        weights
