"""
Given an array of distinct integers nums and a target integer target, return the number of possible combinations that
 add up to target.

The answer is guaranteed to fit in a 32-bit integer.
"""
from typing import List


def combination_sum_iv(nums: List[int], target: int) -> int:
    """
    Dynamic Programming Approach

    :param nums: array of distinct integers, may be negative
    :param target: find combinations of nums (repeatable) that add up to target
    :return: number of possible combinations that add up to target
    """
    nums.sort()
    combination_count_dp = [1] + [0] * target
    for add_up_to in range(target + 1):
        for num_i in nums:
            if num_i > add_up_to:
                break
            else:
                combination_count_dp[add_up_to] += combination_count_dp[add_up_to - num_i]
    return combination_count_dp[-1]


test_cases = [([1, 2, 3], 4, 7),
              ([9], 3, 0),
              ([5, 1, 8], 24, 982),
              ([3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25], 10, 9), ]
for test_nums, test_target, expected_count in test_cases:
    assert combination_sum_iv(test_nums, test_target) == expected_count
