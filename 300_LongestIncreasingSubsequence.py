"""
Given an unsorted array of integers, find the length of longest increasing subsequence.
"""
from bisect import bisect_left
from typing import List


def length_of_LIS(nums: List[int]) -> int:
    """
    :return: the length of longest increasing subsequence in an unsorted array of integers
    """
    if not nums:
        return 0

    visited, max_len = [nums[0]], 1
    for x in nums[1:]:
        if x > visited[-1]:
            max_len += 1
            visited.append(x)
        else:
            visited[bisect_left(visited, x)] = x
    return max_len


test_cases = [([10, 9, 2, 5, 3, 7, 101, 18], 4),
              ([0], 1), ]
for nums, expected_value in test_cases:
    assert length_of_LIS(nums) == expected_value
