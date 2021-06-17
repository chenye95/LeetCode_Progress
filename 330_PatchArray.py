"""
Given a sorted integer array nums and an integer n, add/patch elements to the array such that any number in the range
 [1, n] inclusive can be formed by the sum of some elements in the array.

Return the minimum number of patches required.
"""
from typing import List


def min_patches(nums: List[int], n: int) -> int:
    """
    :param nums: list of numbers in ascending order, 1 <= len(nums) <= 10000, 1 <= nums[i] <= 10000
    :param n: 1 <= n <= 2 ** 31 - 1
    :return: number of patches needed in the list
    """
    # Greedy algorithm
    patch_count = satisfied_until = k = 0
    while satisfied_until < n:
        if k < len(nums) and nums[k] <= satisfied_until + 1:
            # All numbers from [1, satisfied_until] can be expressed as sum of some numbers in the list
            # therefore so will [nums[k] + 1, nums[k] + satisfied_until]
            satisfied_until += nums[k]
            k += 1
        else:
            # satisfied_until + 1 cannot be represented as sum of numbers, yet
            # add satisfied_until + 1 as a patch to the list
            patch_count += 1
            satisfied_until += (satisfied_until + 1)
    return patch_count


test_cases = [([1, 3], 6, 1),
              ([1, 5, 10], 20, 2),
              ([1, 2, 2], 5, 0),
              ([2, 4, 14, 22, 28, 29, 38, 48, 50, 58, 58, 67, 72, 72, 79, 79, 82, 90, 90, 94], 10, 2),
              ([1, 3, 5, 7, 9, 9, 10, 10, 12, 12, 12, 13, 16, 19, 20, 22, 24, 24, 25, 27, 28, 30, 35, 35, 47, 47, 48,
                49, 50, 60, 60, 60, 61, 64, 64, 65, 65, 67, 69, 69, 70, 73, 79, 81, 81, 82, 82, 87, 96, 99], 54, 1),
              ([2, 3, 3, 4, 6, 8, 8, 10, 10, 10, 12, 13, 13, 14, 15, 15, 16, 17, 19, 20, 20, 21, 21, 21, 23, 23, 24, 25,
                26, 27, 27, 28, 28, 29, 29, 30, 30, 31, 31, 32, 32, 32, 36, 36, 38, 41, 41, 41, 43, 44, 46, 46, 46, 48,
                48, 49, 50, 51, 51, 52, 52, 53, 54, 55, 56, 56, 58, 58, 58, 59, 60, 60, 60, 61, 63, 63, 66, 66, 70, 70,
                73, 74, 74, 75, 78, 80, 81, 83, 85, 87, 87, 89, 89, 89, 90, 90, 92, 92, 96, 98], 60844, 5),
              ]
for test_nums, test_n, expected_value in test_cases:
    assert min_patches(test_nums, test_n) == expected_value
