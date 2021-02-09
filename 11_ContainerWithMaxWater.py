"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the
x-axis forms a container, such that the container contains the most water.
"""
from typing import List


def max_area(height: List[int]) -> int:
    max_area_tracker = 0
    l, r = 0, len(height) - 1
    while l < r:
        if height[l] < height[r]:
            max_area_tracker = max(max_area_tracker, (r - l) * height[l])
            l += 1
        else:
            max_area_tracker = max(max_area_tracker, (r - l) * height[r])
            r -= 1

    return max_area_tracker


assert max_area(height=[1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
assert max_area(height=[1, 1]) == 1
assert max_area(height=[4, 3, 2, 1, 4]) == 16
assert max_area(height=[1, 2, 1]) == 2
