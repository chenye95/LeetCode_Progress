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
              ([-2147483647], -2147483647), ]
for test_nums, expected_output in test_cases:
    assert max_sub_array(nums=test_nums) == expected_output
