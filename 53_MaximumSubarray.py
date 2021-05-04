"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
 return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
 which is more subtle.
"""
from typing import List


def max_sub_array(nums: List[int]) -> int:
    """
    Greedy algorithm

    :return: maximum sum of any non-empty sub array of nums
    """
    max_tracker = nums[0]
    accumulation_tracker = 0
    for n_i in nums:
        accumulation_tracker += n_i
        if accumulation_tracker > max_tracker:
            max_tracker = accumulation_tracker
        # keep adding int until the accumulator is negative
        if accumulation_tracker < 0:
            accumulation_tracker = 0
    return max_tracker


test_cases = [([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
              ([1], 1),
              ([0], 0),
              ([-1], -1),
              ([-2147483647], -2147483647),
              ([-84, -87, -78, -16, -94, -36, -87, -93, -50, -22, -63, -28, -91, -60, -64, -27, -41, -27, -73, -37, -12,
                -69, -68, -30, -83, -31, -63, -24, -68, -36, -30, -3, -23, -59, -70, -68, -94, -57, -12, -43, -30, -74,
                -22, -20, -85, -38, -99, -25, -16, -71, -14, -27, -92, -81, -57, -74, -63, -71, -97, -82, -6, -26, -85,
                -28, -37, -6, -47, -30, -14, -58, -25, -96, -83, -46, -15, -68, -35, -65, -44, -51, -88, -9, -77, -79,
                -89, -85, -4, -52, -55, -100, -33, -61, -77, -69, -40, -13, -27, -87, -95, -40], -3),
              ([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4], 6), ]
for test_nums, expected_output in test_cases:
    assert max_sub_array(nums=test_nums) == expected_output
