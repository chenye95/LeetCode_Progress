"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the
x-axis forms a container, such that the container contains the most water.
"""
from typing import List


def max_area(height: List[int]) -> int:
    max_area_tracker = 0
    left_pointer, right_pointer = 0, len(height) - 1
    while left_pointer < right_pointer:
        if height[left_pointer] < height[right_pointer]:
            max_area_tracker = max(max_area_tracker, (right_pointer - left_pointer) * height[left_pointer])
            left_pointer += 1
        else:
            max_area_tracker = max(max_area_tracker, (right_pointer - left_pointer) * height[right_pointer])
            right_pointer -= 1

    return max_area_tracker


test_cases = [([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
              ([1, 1], 1),
              ([4, 3, 2, 1, 4], 16),
              ([1, 2, 1], 2), ]
for test_height, expected_output in test_cases:
    assert max_area(height=test_height) == expected_output
