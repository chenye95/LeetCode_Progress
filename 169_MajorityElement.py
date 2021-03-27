"""
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋
times.

You may assume that the array is non-empty and the majority element always exist in the array.
"""
from typing import List

NOT_FOUND = -100


def majority_element(nums: List[int]) -> int:
    """
    :return: find majority element in nums that appears more than ⌊ n/2 ⌋ times, or NOT_FOUND if no such element exists
    """
    candidate, count = 0, 0
    for n in nums:
        if n == candidate:
            count += 1
        elif count == 0:
            candidate, count = n, 1
        else:
            count -= 1
    return candidate if nums.count(candidate) > len(nums) // 2 else NOT_FOUND


test_cases = [([3, 2, 3], 3),
              ([3, 3, 3], 3),
              ([2, 2, 1, 1, 1, 2, 2], 2),
              ([6, 5, 5], 5),
              ([1, 1, 2, 2], NOT_FOUND),
              ([1, 1, 1, 2, 3, 4], NOT_FOUND), ]
for test_nums, expected_output in test_cases:
    assert majority_element(nums=test_nums) == expected_output
