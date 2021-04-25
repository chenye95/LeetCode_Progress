"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines
are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). Find two lines, which, together with the
x-axis forms a container, such that the container contains the most water.
"""
from typing import List


def max_area(height: List[int]) -> int:
    """
    :param height: n non-negative integers, each represents a vertical line at point i with height[i]
    :return: most water contained by any two vertical lines which together with x-axis form a container
    """
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


test_cases = [([76, 155, 15, 188, 180, 154, 84, 34, 187, 142, 22, 5, 27, 183, 111, 128, 50, 58, 2, 112, 179, 2, 100,
                111, 115, 76, 134, 120, 118, 103, 31, 146, 58, 198, 134, 38, 104, 170, 25, 92, 112, 199, 49, 140, 135,
                160, 20, 185, 171, 23, 98, 150, 177, 198, 61, 92, 26, 147, 164, 144, 51, 196, 42, 109, 194, 177, 100,
                99, 99, 125, 143, 12, 76, 192, 152, 11, 152, 124, 197, 123, 147, 95, 73, 124, 45, 86, 168, 24, 34, 133,
                120, 85, 81, 163, 146, 75, 92, 198, 126, 191], 18048),
              ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
              ([1, 1], 1),
              ([4, 3, 2, 1, 4], 16),
              ([1, 2, 1], 2), ]
for test_height, expected_output in test_cases:
    assert max_area(height=test_height) == expected_output
