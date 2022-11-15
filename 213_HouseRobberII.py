"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed.
 All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one.
 Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two
 adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
 rob tonight without alerting the police.
"""
from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    return max(rob_helper(nums, 0, len(nums) - 1), rob_helper(nums, 1, len(nums)))


def rob_helper(nums: List[int], start_house: int, end_house):
    rob_house = not_rob_house = 0
    for house_i in nums[start_house: end_house]:
        rob_house, not_rob_house = not_rob_house + house_i, max(not_rob_house, rob_house)
    return max(rob_house, not_rob_house)


test_cases = [
    ([1], 1),
    ([2, 3, 2], 3),
    ([1, 2, 3, 1], 4),
    ([1, 2, 3], 3),
    ([155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146, 73, 55,
      6, 122, 196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203, 238, 239, 217, 212, 241,
      242, 157, 79, 133, 66, 36, 165], 4388),
    ([226, 174, 214, 16, 218, 48, 153, 131, 128, 17, 157, 142, 88, 43, 37, 157, 43, 221, 191, 68, 206, 23, 225, 82, 54,
      118, 111, 46, 80, 49, 245, 63, 25, 194, 72, 80, 143, 55, 209, 18, 55, 122, 65, 66, 177, 101, 63, 201, 172, 130,
      103, 225, 142, 46, 86, 185, 62, 138, 212, 192, 125, 77, 223, 188, 99, 228, 90, 25, 193, 211, 84, 239, 119, 234,
      85, 83, 123, 120, 131, 203, 219, 10, 82, 35, 120, 180, 249, 106, 37, 169, 225, 54, 103, 55, 166, 124], 7102),
    ([94, 40, 49, 65, 21, 21, 106, 80, 92, 81, 679, 4, 61, 6, 237, 12, 72, 74, 29, 95, 265, 35, 47, 1, 61, 397, 52, 72,
      37, 51, 1, 81, 45, 435, 7, 36, 57, 86, 81, 72], 2926)
]
for test_nums, expected_value in test_cases:
    assert rob(test_nums) == expected_value
