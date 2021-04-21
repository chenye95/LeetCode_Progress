"""
You are given two positive integer arrays nums1 and nums2, both of length n.

The absolute sum difference of arrays nums1 and nums2 is defined as the sum of |nums1[i] - nums2[i]| for each
 0 <= i < n (0-indexed).

You can replace at most one element of nums1 with any other element in nums1 to minimize the absolute sum difference.

Return the minimum absolute sum difference after replacing at most one element in the array nums1. Since the answer may
 be large, return it modulo 10**9 + 7.
"""
from bisect import bisect_left
from typing import List


def min_absolute_diff(nums1: List[int], nums2: List[int]) -> int:
    """
    :param nums1: list of integers, one item can be replaced by any other item in num1
    :param nums2: list of same length as num1
    :return: min absolute sum difference after at most one replacement in num1
    """
    old_abs_diff = [abs(num1_i - num2_i) for num1_i, num2_i in zip(nums1, nums2)]

    sorted_nums1 = sorted(nums1)
    reduction_replacement = 0

    for num2_i, old_diff_i in zip(nums2, old_abs_diff):
        idx = bisect_left(sorted_nums1, num2_i)
        if idx > 0 and - old_diff_i + abs(num2_i - sorted_nums1[idx - 1]) < reduction_replacement:
            # replace num1_i with sorted_nums1[idx - 1]
            reduction_replacement = - old_diff_i + abs(num2_i - sorted_nums1[idx - 1])
        if idx < len(nums1) and - old_diff_i + abs(num2_i - sorted_nums1[idx]) < reduction_replacement:
            # replace num1_i with sorted_nums1[idx]
            reduction_replacement = - old_diff_i + abs(num2_i - sorted_nums1[idx])

    return (sum(old_abs_diff) + reduction_replacement) % (10 ** 9 + 7)


test_cases = [([1, 2, 3, 4, 5], [1, 4, 3, 9, 1000], 1000),
              ([1, 7, 5], [2, 3, 5], 3),
              ([2, 4, 6, 8, 10], [2, 4, 6, 8, 10], 0),
              ([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4], 20),
              ([57, 42, 21, 28, 30, 25, 22, 12, 55, 3, 47, 18, 43, 29, 20, 44, 59, 9, 43, 7, 8, 5, 42, 53, 99, 34, 37,
                88, 87, 62, 38, 68, 31, 3, 11, 61, 93, 34, 63, 27, 20, 48, 38, 5, 71, 100, 88, 54, 52, 15, 98, 59, 74,
                26, 81, 38, 11, 44, 25, 69, 79, 81, 51, 85, 59, 84, 83, 99, 31, 47, 31, 23, 83, 70, 82, 79, 86, 31, 50,
                17, 11, 100, 55, 15, 98, 11, 90, 16, 46, 89, 34, 33, 57, 53, 82, 34, 25, 70, 5, 1],
               [76, 3, 5, 29, 18, 53, 55, 79, 30, 33, 87, 3, 56, 93, 40, 80, 9, 91, 71, 38, 35, 78, 32, 58, 77, 41, 63,
                5, 21, 67, 21, 84, 52, 80, 65, 38, 62, 99, 80, 13, 59, 94, 21, 61, 43, 82, 29, 97, 31, 24, 95, 52, 90,
                92, 37, 26, 65, 89, 90, 32, 27, 3, 42, 47, 93, 25, 14, 5, 39, 85, 89, 7, 74, 38, 12, 46, 40, 25, 51, 2,
                19, 8, 21, 62, 58, 29, 32, 77, 62, 9, 74, 98, 10, 55, 25, 62, 48, 48, 24, 21], 3441)]
for test_num1, test_num2, expected_output in test_cases:
    assert min_absolute_diff(test_num1, test_num2) == expected_output
