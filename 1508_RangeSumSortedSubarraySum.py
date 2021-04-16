"""
Given the array nums consisting of n positive integers. You computed the sum of all non-empty continuous sub-arrays from
the array and then sort them in non-decreasing order, creating a new array of n * (n + 1) / 2 numbers.

Return the sum of the numbers from index left to index right (indexed from 1), inclusive, in the new array. Since the
answer can be a huge number return it modulo 10^9 + 7.
"""
import heapq
from typing import List


def range_sum_sorted_sum(nums: List[int], n: int, left: int, right: int) -> int:
    """
    :param nums: list of positive integer to compute sub array sum on
    :param n: total number of integer in nums
    :param left: sort sub array sum and return range sum between left and right
    :param right: sort sub array sum and return range sum between left and right
    """
    min_heap_sub_array_sum = [(n_i, i) for i, n_i in enumerate(nums)]
    heapq.heapify(min_heap_sub_array_sum)

    range_sum = 0
    for k in range(1, right + 1):
        sub_array_sum, i = heapq.heappop(min_heap_sub_array_sum)
        if k >= left:
            range_sum += sub_array_sum
        if i < n - 1:
            heapq.heappush(min_heap_sub_array_sum, (sub_array_sum + nums[i + 1], i + 1))

    return range_sum % 1_000_000_007


test_cases = [([1, 2, 3, 4], 4, 1, 5, 13),
              ([1, 2, 3, 4], 4, 3, 4, 6),
              ([1, 2, 3, 4], 4, 1, 10, 50), ]
for test_nums, test_n, test_left, test_right, expected_output in test_cases:
    assert range_sum_sorted_sum(test_nums, test_n, test_left, test_right) == expected_output
