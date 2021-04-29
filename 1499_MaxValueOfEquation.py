"""
Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] =
[xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length. It is
guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.
"""
from collections import deque
from typing import List, Tuple


def find_max_value_of_equation(points: List[Tuple[int, int]], k: int) -> int:
    """
    Since x_i < x_j, y_i + y_j + |x_i - x_j| = (y_i - x_i) + (y_j + x_j)

    :param points: list of (x_i, y_i)
    :param k: max difference between |xi - xj| <= k
    :return: max value of y_i + y_j + |x_i - x_j|
    """
    return_val = -2 * (10 ** 8)
    current_stack = deque()  # (x_i, y_i - x_i)
    for x_i, y_i in points:
        while current_stack and x_i > current_stack[0][0] + k:  # ensure x_i <= x_j + k
            current_stack.popleft()
        if current_stack:
            return_val = max(return_val, current_stack[0][1] + x_i + y_i)
        while current_stack and current_stack[-1][1] <= y_i - x_i:  # max value of (y_i - x_i)
            current_stack.pop()
        current_stack.append((x_i, y_i - x_i))
    return return_val


test_cases = [([(1, 3), (2, 0), (5, 10), (6, -10)], 1, 4),
              ([(0, 0), (3, 0), (9, 2)], 3, 3),
              ([(-19, 9), (-15, -19), (-5, -8)], 10, -6),
              ([(-19, -12), (-13, -18), (-12, 18), (-11, -8), (-8, 2), (-7, 12), (-5, 16), (-3, 9), (1, -7), (5, -4),
                (6, -20), (10, 4), (16, 4), (19, -9), (20, 19)], 6, 35), ]
for test_points, test_k, expected_output in test_cases:
    assert find_max_value_of_equation(test_points, test_k) == expected_output
