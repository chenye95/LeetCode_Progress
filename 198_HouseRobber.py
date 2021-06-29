"""
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed,
 the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and
 it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can
 rob tonight without alerting the police.
"""
from typing import List


def rob(nums: List[int]) -> int:
    rob_house = not_rob_house = 0
    for house_i in nums:
        rob_house, not_rob_house = not_rob_house + house_i, max(not_rob_house, rob_house)
    return max(rob_house, not_rob_house)


test_cases = [([1, 2, 3, 1], 4),
              ([2, 7, 9, 3, 1], 12),
              ([155, 44, 52, 58, 250, 225, 109, 118, 211, 73, 137, 96, 137, 89, 174, 66, 134, 26, 25, 205, 239, 85, 146,
                73, 55, 6, 122, 196, 128, 50, 61, 230, 94, 208, 46, 243, 105, 81, 157, 89, 205, 78, 249, 203, 238, 239,
                217, 212, 241, 242, 157, 79, 133, 66, 36, 165], 4517),
              ([82, 217, 170, 215, 153, 55, 185, 55, 185, 232, 69, 131, 130, 102], 1082),
              ([226, 174, 214, 16, 218, 48, 153, 131, 128, 17, 157, 142, 88, 43, 37, 157, 43, 221, 191, 68, 206, 23,
                225, 82, 54, 118, 111, 46, 80, 49, 245, 63, 25, 194, 72, 80, 143, 55, 209, 18, 55, 122, 65, 66, 177,
                101, 63, 201, 172, 130, 103, 225, 142, 46, 86, 185, 62, 138, 212, 192, 125, 77, 223, 188, 99, 228, 90,
                25, 193, 211, 84, 239, 119, 234, 85, 83, 123, 120, 131, 203, 219, 10, 82, 35, 120, 180, 249, 106, 37,
                169, 225, 54, 103, 55, 166, 124], 7102),
              ]
for test_nums, expected_value in test_cases:
    assert rob(test_nums) == expected_value
