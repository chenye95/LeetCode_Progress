"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    """
    :param nums: list of distinct integers
    :return: all possible permutations in any order
    """
    return [[n] + p
            for i, n in enumerate(nums)
            for p in permute(nums[:i] + nums[i + 1:])] or [[]]


test_cases = [([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
              ([0, 1], [[0, 1], [1, 0]]),
              ([1], [[1]]), ]
for test_nums, expected_output in test_cases:
    assert sorted(permute(nums=test_nums)) == sorted(expected_output)
