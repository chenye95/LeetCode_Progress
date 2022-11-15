"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing
 the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To
 accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
 and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""
from typing import List


def merge(nums1: List[int], m: int, nums2: List[int], n: int) -> None:
    scan_1, scan_2 = m - 1, n - 1
    sort_pointer = m + n - 1

    while scan_1 >= 0 and scan_2 >= 0:
        if nums1[scan_1] > nums2[scan_2]:
            nums1[sort_pointer] = nums1[scan_1]
            scan_1 -= 1
        else:
            nums1[sort_pointer] = nums2[scan_2]
            scan_2 -= 1
        sort_pointer -= 1

    if scan_2 >= 0:
        nums1[: scan_2 + 1] = nums2[: scan_2 + 1]


test_cases = [
    ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3),
    ([1], 1, [], 0),
    ([0], 0, [1], 1),
    ([-1, 0, 0, 3, 3, 3, 0, 0, 0], 6, [1, 2, 3], 3),
    ([-10, -10, -9, -9, -9, -8, -8, -7, -7, -7, -6, -6, -6, -6, -6, -6, -6, -5, -5, -5, -4, -4, -4, -3, -3, -2, -2, -1,
      -1, 0, 1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 5, 5, 6, 6, 6, 6, 7, 7, 7, 7, 8, 9, 9, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
      0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], 55,
     [-10, -10, -9, -9, -9, -9, -8, -8, -8, -8, -8, -7, -7, -7, -7, -7, -7, -7, -7, -6, -6, -6, -6, -5, -5, -5, -5, -5,
      -4, -4, -4, -4, -4, -3, -3, -3, -2, -2, -2, -2, -2, -2, -2, -1, -1, -1, 0, 0, 0, 0, 0, 1, 1, 1, 2, 2, 2, 2, 2, 2,
      2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 8, 8, 8, 8, 9, 9, 9,
      9], 99),
]
for test_nums_1, test_m, test_nums_2, test_n in test_cases:
    expected_values = sorted(test_nums_1[:test_m] + test_nums_2)
    merge(test_nums_1, test_m, test_nums_2, test_n)
    assert test_nums_1 == expected_values
