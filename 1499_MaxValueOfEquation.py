"""
Given an array points containing the coordinates of points on a 2D plane, sorted by the x-values, where points[i] =
[xi, yi] such that xi < xj for all 1 <= i < j <= points.length. You are also given an integer k.

Find the maximum value of the equation yi + yj + |xi - xj| where |xi - xj| <= k and 1 <= i < j <= points.length. It is
guaranteed that there exists at least one pair of points that satisfy the constraint |xi - xj| <= k.
"""
from collections import deque
from typing import List


def findMaxValueOfEquation(points: List[List[int]], k: int) -> int:
    """
    Since x_i < x_j, y_i + y_j + |x_i - x_j| = (y_i - x_i) + (y_j + x_j)
    :param points: list of (x_i, y_i)
    :param k: max difference between |xi - xj| <= k
    """
    return_val = -float("inf")
    current_stack = deque()  # (x_i, y_i - x_i)
    for x_i, y_i in points:
        while current_stack and x_i > current_stack[0][0] + k:  # ensure x_i >= x_j - k
            current_stack.popleft()
        if current_stack:
            return_val = max(return_val, current_stack[0][1] + x_i + y_i)
        while current_stack and current_stack[-1][1] <= y_i - x_i:  # max value of (y_i - x_i)
            current_stack.pop()
        current_stack.append((x_i, y_i - x_i))
    return return_val


assert findMaxValueOfEquation(points=[[1, 3], [2, 0], [5, 10], [6, -10]], k=1) == 4
assert findMaxValueOfEquation(points=[[0, 0], [3, 0], [9, 2]], k=3) == 3