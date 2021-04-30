"""
Given three integers x, y, and bound, return a list of all the powerful integers that have a value less than or equal
 to bound.

An integer is powerful if it can be represented as x**i + y**j for some integers i >= 0 and j >= 0.

You may return the answer in any order. In your answer, each value should occur at most once.
"""
from math import log
from typing import List


def powerful_integers(x: int, y: int, bound: int) -> List[int]:
    """
    :param x: 1 <= x <= 100
    :param y: 1 <= y <= 100
    :param bound: 0 <= bound <= 10**6
    :return: number of integers in range [1, bound] that can be expresses as x**i + y**j for some non-negative integers
        i and j
    """
    i_bound = 1 if x == 1 else int(log(bound, x))
    j_bound = 1 if y == 1 else int(log(bound, y))

    return_values = set()

    for i in range(i_bound + 1):
        for j in range(j_bound + 1):
            powerful_int = x ** i + y ** j
            if powerful_int <= bound:
                return_values.add(powerful_int)
            else:
                break

    return list(return_values)


test_cases = [(2, 3, 10, {2, 3, 4, 5, 7, 9, 10}),
              (3, 5, 15, {2, 4, 6, 8, 10, 14}),
              (2, 1, 10, {2, 3, 5, 9}),
              (2, 91, 996, {2, 3, 5, 9, 17, 33, 65, 92, 93, 95, 99, 107, 123, 129, 155, 219, 257, 347, 513, 603}),
              (81, 21, 900000, {2, 22, 82, 102, 442, 522, 6562, 6582, 7002, 9262, 9342, 15822, 194482, 194562, 201042,
                                531442, 531462, 531882, 540702, 725922}), ]
for test_x, test_y, test_bound, expected_output in test_cases:
    assert set(powerful_integers(test_x, test_y, test_bound)) == expected_output
