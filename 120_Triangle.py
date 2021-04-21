"""
Given a triangle array, return the minimum path sum from top to bottom.

For each step, you may move to an adjacent number of the row below. More formally, if you are on index i on the current
 row, you may move to either index i or index i + 1 on the next row.
"""
from copy import deepcopy
from typing import List


def minimum_total_top_down(triangle: List[List[int]]) -> int:
    """
    Start from top of the triangle and traverse downwards

    :param triangle: list of list of length 1 <= len(triangle) <= 100, and len(triangle[i]) == i + 1
    :return: minimum path sum from top to bottom such that you can move to index i or i + 1 on the next row from index i
        on the current row
    """
    n_levels = len(triangle)
    previous_level_sum = [triangle[0][0], ]
    for i in range(1, n_levels):
        current_level_val = triangle[i]
        previous_level_sum = [current_level_val[0] + previous_level_sum[0]] + \
                             [current_level_val[j] + min(previous_level_sum[j], previous_level_sum[j - 1])
                              for j in range(1, i)] + \
                             [current_level_val[i] + previous_level_sum[i - 1]]
    return min(previous_level_sum)


def minimum_total_bottom_up(triangle: List[List[int]]) -> int:
    """
    Start from bottom of the triangle and traverse upwards

    :param triangle: list of list of length 1 <= len(triangle) <= 100, and len(triangle[i]) == i + 1
    :return: minimum path sum from top to bottom such that you can move to index i or i + 1 on the next row from index i
        on the current row
    """
    next_level_min = deepcopy(triangle[-1])
    for i in range(len(triangle) - 2, -1, -1):
        current_level_val = triangle[i]
        for j in range(i + 1):
            # override next_level_min[j] represents current_level_min[j]
            next_level_min[j] = min(next_level_min[j], next_level_min[j + 1]) + current_level_val[j]
            # next_level_min = current_level_min
    return next_level_min[0]


test_cases = [([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]], 11),
              ([[-10]], -10),
              ([[-7], [-2, 1], [-5, -5, 9], [-4, -5, 4, 4], [-6, -6, 2, -1, -5], [3, 7, 8, -3, 7, -9],
                [-9, -1, -9, 6, 9, 0, 7], [-7, 0, -6, -8, 7, 1, -4, 9], [-3, 2, -6, -9, -7, -6, -9, 4, 0],
                [-8, -6, -3, -9, -2, -6, 7, -5, 0, 7], [-9, -1, -2, 4, -2, 4, 4, -1, 2, -5, 5],
                [1, 1, -6, 1, -2, -4, 4, -2, 6, -6, 0, 6], [-3, -3, -6, -2, -6, -2, 7, -9, -5, -7, -5, 5, 1]], -63), ]
for minimum_total in [minimum_total_top_down, minimum_total_bottom_up]:
    for test_triangle, expected_output in test_cases:
        assert minimum_total(test_triangle) == expected_output
