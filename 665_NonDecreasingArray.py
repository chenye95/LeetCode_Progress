"""
Given an array nums with n integers, your task is to check if it could become non-decreasing by modifying at most one
 element.

We define an array is non-decreasing if nums[i] <= nums[i + 1] holds for every i (0-based) such that (0 <= i <= n - 2).
"""
from typing import List


def check_possibility(nums: List[int]) -> bool:
    """
    :param nums: array of integers where 1 <= len(nums) <= 10000
    :return: whether we can convert nums into a non-decreasing array by modifying at most one elements
    """
    n = len(nums)
    # violation position p where nums[p] > nums[p + 1]
    # to be able to convert, there exists at most one such violation in nums
    p = -1

    for i in range(n - 1):
        if nums[i] > nums[i + 1]:
            if p != -1:
                # such violation already exists
                return False
            p = i

    # violation is fixable if p are at the ends
    # or nums[p - 1] <= nums[p + 1] (fix nums[p])
    # or nums[p] <= nums[p + 2] (fix nums[p + 1])
    return p in (-1, 0, n - 2) or nums[p - 1] <= nums[p + 1] or nums[p] <= nums[p + 2]


test_cases = [([4, 2, 3], True),
              ([4, 2, 1], False),
              (list(range(27)), True),
              ([1, 2, 3, 4, 5, 65, 45, 23, 23, 23, 44, 100, 101, 102, 103, 342, 512, 312, 423, 454, 623, 231, 111, 235,
                1001, 1002, 1003, 1004], False),
              ([3, 3, 5, 2, 2], False),
              ([3, 3, 5, 2], True),
              ([3, 3, 2], True),
              ([5, 3, 4, 5, 6], True), ]
for test_nums, expected_output in test_cases:
    assert check_possibility(test_nums) is expected_output
