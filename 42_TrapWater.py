"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it
can trap after raining.
"""
from typing import List


def trap_dynamic_programming(height: List[int]) -> int:
    """
    Water trapped on location i = min(tallest_left_to_i, tallest_right_to_i) - height[i]
    """
    if not height:
        return 0

    n = len(height)
    # tallest elevation to the left of i, inclusive
    left_max = [height[0]] * n
    # tallest elevation to the right of i, inclusive
    right_max = [height[-1]] * n

    for i in range(1, n):
        left_max[i] = max(left_max[i - 1], height[i])
        right_max[n - i - 1] = max(right_max[n - i], height[n - i - 1])

    return sum([min(left_max[i], right_max[i]) - height[i] for i in range(n)])


def trap_2_pointer(height: List[int]) -> int:
    """
    Optimization on Dynamic Programming approach
    estimate bound on left_max and right_max
    """
    left, right = 0, len(height) - 1
    left_max = right_max = 0
    total_volume = 0

    while left < right:
        if height[left] < height[right]:
            # right to height[left] exits taller height >= height[right]
            if height[left] > left_max:
                left_max = height[left]
            else:
                # left_max < height[left] < height[right]
                total_volume += (left_max - height[left])
            left += 1
        else:
            # left to height[right] exits taller height >= height[left]
            if height[right] > right_max:
                right_max = height[right]
            else:
                # right_max < height[right] < height[left]
                total_volume += (right_max - height[right])
            right -= 1

    return total_volume


def trap_stack(height: List[int]) -> int:
    """
    Use stack to keep track of taller heights to the left
    """
    total_volume = 0
    height_stack = []

    for i in range(len(height)):
        while height_stack and height[i] > height[height_stack[-1]]:
            shorter_to_left = height_stack.pop()
            if not height_stack:
                break
            # shorter_to_left is bounded by height_stack[-1] to the left and i to the right
            distance = (i - height_stack[-1] - 1)
            bounded_height = min(height[i], height[height_stack[-1]]) - height[shorter_to_left]
            total_volume += distance * bounded_height
        height_stack.append(i)

    return total_volume


test_cases = [([], 0),
              ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
              ([4, 2, 0, 3, 2, 5], 9)]
for trap_fn in [trap_2_pointer, trap_stack, trap_dynamic_programming, ]:
    for test_input, expected_out in test_cases:
        assert trap_fn(test_input) == expected_out