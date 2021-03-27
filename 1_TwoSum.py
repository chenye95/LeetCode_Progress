"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    """
    :param nums: an array of integers
    :param target: an integer target
    :return: indices i, j such that they add up to target: nums[i] + nums[j] == target. Return in any order
    """
    complement_lookup = {}
    for i, n in enumerate(nums):
        if target - n in complement_lookup:
            return [i, complement_lookup[target - n]]
        else:
            complement_lookup[n] = i


test_cases = [([2, 7, 11, 15], 9, {0, 1}),
              ([3, 2, 4], 6, {1, 2}),
              ([3, 3], 6, {0, 1}), ]
for test_nums, test_target, expected_output in test_cases:
    assert set(two_sum(nums=test_nums, target=test_target)) == expected_output
