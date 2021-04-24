"""
You are given an array nums of non-negative integers. nums is considered special if there exists a number x such that
 there are exactly x numbers in nums that are greater than or equal to x.

Notice that x does not have to be an element in nums.

Return x if the array is special, otherwise, return -1. It can be proven that if nums is special, the value for x is
 unique.
"""
from typing import List


def x_special_array(nums: List[int]) -> int:
    """
    :param nums: array of non negative integers where 1 <= len(nums) <= 100 and 0 <= nums[i] <= 1000
    :return: X such that exactly X elements of nums are greater or equal to X; -1 otherwise
    """
    nums.sort()
    previous_num = -1
    remainder_len = len(nums)
    for num_i in nums:
        if previous_num < remainder_len <= num_i:
            return remainder_len
        previous_num = num_i
        remainder_len -= 1

    return -1


test_cases = [([1, 1], -1),
              ([3, 5], 2),
              ([0, 0], -1),
              ([0, 4, 3, 0, 4], 3),
              ([3, 6, 7, 7, 0], -1),
              ([17, 11, 11, 4, 15, 5, 15, 13, 2, 0, 8, 12, 11], -1),
              ([30, 0, 6, 1, 14, 9, 28, 3, 9, 22, 13, 20, 10, 24, 16, 27, 27, 3, 20, 10, 21, 8, 23, 20, 15], 14), ]
for test_nums, expected_output in test_cases:
    assert x_special_array(test_nums) == expected_output
