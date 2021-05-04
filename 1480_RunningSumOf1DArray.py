"""
Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0], …, nums[i]).

Return the running sum of nums.
"""
from typing import List


def running_sum(nums: List[int]) -> List[int]:
    """
    :param nums: list of numbers; 1 <= len(nums) <= 1000 and -10**6 <= nums[i] <= 10**6
    :return: running sum of nums
    """
    return_list = [0] * len(nums)
    accumulator = 0
    for i, num_i in enumerate(nums):
        accumulator += num_i
        return_list[i] = accumulator
    return return_list


test_cases = [([1, 2, 3, 4], [1, 3, 6, 10]),
              ([1, 1, 1, 1, 1], [1, 2, 3, 4, 5]),
              ([3, 1, 2, 10, 1], [3, 4, 6, 16, 17]),
              ([34, -13, 12, -59, 27, -63, 1, 94, 84, 54, 9, 57, 53, 11, 85, -17, -78, -85, -84, 5, 43, -44, -48, -38],
               [34, 21, 33, -26, 1, -62, -61, 33, 117, 171, 180, 237, 290, 301, 386, 369, 291, 206, 122, 127, 170, 126,
                78, 40]), ]
for test_nums, expected_output in test_cases:
    assert running_sum(test_nums) == expected_output
