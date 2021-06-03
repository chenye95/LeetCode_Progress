"""
Given a rectangular cake with height h and width w, and two arrays of integers horizontalCuts and verticalCuts where
 horizontalCuts[i] is the distance from the top of the rectangular cake to the ith horizontal cut and similarly,
 verticalCuts[j] is the distance from the left of the rectangular cake to the jth vertical cut.

Return the maximum area of a piece of cake after you cut at each horizontal and vertical position provided in the arrays
 horizontalCuts and verticalCuts. Since the answer can be a huge number, return this modulo 10^9 + 7.
"""
from typing import List


def max_area(h: int, w: int, horizontal_cuts: List[int], vertical_cuts: List[int]) -> int:
    """
    :param h: 2 <= h <= 1e9
    :param w: 2 <= w <= 1e9
    :param horizontal_cuts: 1 <= len(horizontal_cuts) <= min(h, 1e5). Guaranteed to be distinct values in [1, h]
    :param vertical_cuts: 1 <= len(horizontal_cuts) <= min(w, 1e5). Guaranteed to be distinct values in [1, w]
    :return: max area of the pieces mod 1e9 + 7
    """
    _mod_value = 10 ** 9 + 7

    horizontal_cuts.sort()
    dh = previous_h = 0
    for next_h in horizontal_cuts + [h]:
        if (next_h - previous_h) > dh:
            dh = next_h - previous_h
        previous_h = next_h

    vertical_cuts.sort()
    dw = previous_w = 0
    for next_w in vertical_cuts + [w]:
        if (next_w - previous_w) > dw:
            dw = next_w - previous_w
        previous_w = next_w

    return dh * dw % _mod_value


test_cases = [(5, 4, [1, 2, 4], [1, 3], 4),
              (5, 4, [3, 1], [1], 6),
              (5, 4, [3], [3], 9),
              (50, 15,
               [33, 2, 37, 10, 30, 22, 35, 45, 28, 11, 32, 24, 19, 25, 41, 46, 12, 17, 5, 31, 29, 15, 48, 39, 3, 43, 38,
                16, 4, 6, 23, 18, 20, 36, 8, 13, 7, 34, 40, 42, 14, 49, 21, 27, 44, 26],
               [12, 10, 1], 18),
              (12, 44,
               [2, 1, 9, 6, 7],
               [35, 5, 21, 12, 4, 7, 18, 32, 36, 40, 10, 30, 24, 17, 8, 20, 9, 3, 34, 41, 26, 42, 28, 31, 38, 2, 14, 19,
                37, 33, 23, 43, 29, 15, 16, 11], 8), ]
for test_h, test_w, test_horizontal_cuts, test_vertical_cuts, expected_value in test_cases:
    assert max_area(test_h, test_w, test_horizontal_cuts, test_vertical_cuts) == expected_value
