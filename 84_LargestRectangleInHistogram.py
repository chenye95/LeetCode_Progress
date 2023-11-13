"""
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the
 area of the largest rectangle in the histogram.
"""
from typing import List


def largest_rectangle_area(heights: List[int]) -> int:
    """
    :param heights: 1 <= len(heights) <= 1e5, and 0 <= heights[i] <= 1e4
    :return: the largest rectangle in the histogram
    """
    heights.append(0)
    i_asc_order = [-1]
    max_rectangle = 0
    for i, height_i in enumerate(heights):
        while height_i < heights[i_asc_order[-1]]:
            h = heights[i_asc_order.pop()]
            w = i - i_asc_order[-1] - 1
            if max_rectangle < w * h:
                max_rectangle = w * h
        i_asc_order.append(i)
    heights.pop()
    return max_rectangle


test_cases = [([2, 1, 5, 6, 2, 3], 10),
              ([2, 4], 4),
              ([3, 5, 5, 2, 5, 5, 6, 6, 4, 4, 1, 1, 2, 5, 5, 6, 6, 4, 1, 3], 24),
              ([1] * 30000, 30000),
              ([5, 5, 1, 7, 1, 1, 5, 2, 7, 6], 12),
              ([999, 999, 999, 999], 3996),
              ([999, 999, 999, 998], 3992),
              ]
for test_heights, expected_value in test_cases:
    assert largest_rectangle_area(test_heights) == expected_value
