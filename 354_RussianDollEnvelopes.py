"""
You have a number of envelopes with widths and heights given as a pair of integers (w, h). One envelope can fit into
another if and only if both the width and height of one envelope is greater than the width and height of the other
envelope. What is the maximum number of envelopes can you Russian doll? (put one inside other)

Note: Rotation is not allowed.
"""
from bisect import bisect_left
from typing import List, Tuple


def max_envelopes(envelopes: List[Tuple[int, int]]) -> int:
    """
    Longest increasing sub sequence algorithm (LISS) similar to 300 Dynamic Programming with Binary Search approach

    :param envelopes: list of tuples (width, height) of each envelope
    :return: max number of envelopes that can Russian doll (fit one in another)
    """
    if not envelopes:
        return 0
    # sort envelopes by width first in ascending order, i.e. next envelops can encompass all previous ones in width
    # to break tie, descending order in height to avoid <3, 4> followed by <3, 5>
    # (width has to be strictly greater for insertion
    increasing_heights = []
    for width, height in sorted(envelopes, key=lambda x: (x[0], -x[-1])):
        if not increasing_heights or height > increasing_heights[-1]:
            increasing_heights.append(height)
        else:
            increasing_heights[bisect_left(increasing_heights, height)] = height
    return len(increasing_heights)


test_cases = [([(4, 1), (4, 6), (6, 7), (2, 3), (1, 1), (4, 2)], 4),
              ([(4, 6), (6, 7), (2, 3), (1, 1), (4, 2)], 4),
              ([(5, 4), (6, 4), (6, 7), (2, 3)], 3),
              ([(2, 3), (4, 6), (3, 7), (4, 8)], 3),
              ([(2, 3), (4, 6), (3, 7), (4, 2)], 2),
              ([(5, 4), (6, 3), (6, 7), (2, 3)], 3),
              ]
for test_envelopes, expected_value in test_cases:
    assert max_envelopes(test_envelopes) == expected_value
