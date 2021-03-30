"""
You are given an array x of n positive numbers. You start at point (0,0) and moves x[0] metres to the north, then
x[1] metres to the west, x[2] metres to the south, x[3] metres to the east and so on. In other words, after each move
your direction changes counter-clockwise.

Write a one-pass algorithm with O(1) extra space to determine, if your path crosses itself, or not.
"""
from typing import List


def is_self_crossing(x: List[int]) -> bool:
    """
    :param x: array of positive integers, representing moves. Starting at (0, 0) and facing north, droid moves x[i]
    steps and turn 90 degrees counter clock wise
    :return: whether the path is self crossing
    """
    # let a, b, c, d, e, f be 6 consecutive moves
    b = c = d = e = f = 0
    for a in x:
        if d >= b > 0 and (a >= c or a >= c - e >= 0 and f >= d - b):
            # The directions of the line doesn't matter, so long as there is a 90 degree counter-clockwise turn between
            # 2 lines
            # - Cross a from the left: d >= b and a >= c
            # - Cross a from the right: d >= b and b + f >= d and c >= e and a + e >= c
            return True
        b, c, d, e, f = a, b, c, d, e
    return False


test_cases = [([2, 1, 1, 2], True),
              ([3, 3, 3, 2, 1, 1], False),
              ([1, 2, 2, 3, 4], False),
              ([1, 1, 2, 1, 1], True),
              ([1, 2, 2, 3, 4], False), ]
for test_x, expected_outcome in test_cases:
    assert is_self_crossing(test_x) is expected_outcome
