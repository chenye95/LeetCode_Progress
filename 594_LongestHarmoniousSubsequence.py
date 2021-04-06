"""
We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly
 1.

Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences

A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing
 the order of the remaining elements.
"""
from collections import Counter
from typing import List


def find_LHS(nums: List[int]) -> int:
    """
    Harmonious array is an array where the difference between its maximum value and its minimum value is exactly 1

    :param nums: array of integers
    :return: length of its longest harmonious subsequences
    """
    num_counter = Counter(nums)
    len_lhs = 0
    for n in num_counter:
        if n + 1 in num_counter:
            len_lhs = max(len_lhs, num_counter[n] + num_counter[n + 1])
    return len_lhs


test_cases = [([1, 3, 2, 2, 5, 2, 3, 7], 5),
              ([1, 2, 3, 4], 2),
              ([1, 1, 1, 1], 0),
              ([1, 2, 2, 1], 4), ]
for test_nums, expected_output in test_cases:
    assert find_LHS(nums=test_nums) == expected_output
