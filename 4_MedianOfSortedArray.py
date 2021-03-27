"""
Given two sorted arrays short_list and long_list of size m and n respectively, return the median of the two sorted arrays.
"""
from typing import List


def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    """
    Two sorted arrays concatenated has length m + n, and median is greater than (m + n) // 2 elements in concatenated
    list

    Assume short_list[0], ..., short_list[i] and long_list[0], ..., long_list[j] are smaller than the median, then
    j = (m + n + 1) // 2 - i and short_list[i - 1] <= long_list[j] and long_list[j - 1] <= short_list[i]

    Binary search on i

    :param nums1: sorted list of length m
    :param nums2: sorted list of length n
    :return: median of the combined list of num1 and num2
    """
    m, n = len(nums1), len(nums2)
    if m <= n:
        short_list, long_list = nums1, nums2
    else:
        # ensure m <= n and len(short_list) <= len(long_list)
        short_list, long_list, m, n = nums2, nums1, n, m

    i_lower, i_upper, half_len = 0, m, (m + n + 1) // 2
    while i_lower <= i_upper:
        i = (i_lower + i_upper) // 2
        j = half_len - i
        if i < m and long_list[j - 1] > short_list[i]:
            # i < m, then j = (m + n + 1) // 2 - i > 0
            # need to find bigger short_list[i] by raising i
            i_lower = i + 1
        elif i > 0 and short_list[i - 1] > long_list[j]:
            # need to find smaller short_list[i] by decreasing i
            i_upper = i - 1
        else:
            # i is perfect
            if i == 0:
                # no value taken from short_list
                max_of_left = long_list[j - 1]
            elif j == 0:
                # no value taken from long_list
                max_of_left = short_list[i - 1]
            else:
                max_of_left = max(short_list[i - 1], long_list[j - 1])

            if (m + n) % 2:
                return max_of_left

            if i == m:
                # no value taken from short_list
                min_of_right = long_list[j]
            elif j == n:
                # no value taken from long_list
                min_of_right = short_list[i]
            else:
                min_of_right = min(short_list[i], long_list[j])

            return (max_of_left + min_of_right) / 2.0


test_cases = [([1, 3], [2], 2.0),
              ([1, 2], [3, 4], 2.5),
              ([0, 0], [0, 0], 0),
              ([], [1], 1),
              ([2], [], 2), ]
for test_num_1, test_num_2, expected_output in test_cases:
    assert find_median_sorted_arrays(nums1=test_num_1, nums2=test_num_2) == expected_output
