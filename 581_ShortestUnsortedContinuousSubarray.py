"""
Given an integer array nums, you need to find one continuous sub array that if you only sort this sub array in ascending
order, then the whole array will be sorted in ascending order.

Return the shortest such sub array and output its length.
"""
from typing import List


def find_unsorted_sub_array_stack(nums: List[int]) -> int:
    """
    Scanning with stack approach

    :param nums: an integer array
    :return: length of shorted continuous sub array that if you only sort this sub array in ascending order, the whole
        array will be sorted in ascending order
    """
    ascending_stack = []  # i such that nums[i] is in ascending order
    left_bound = len(nums)
    for i, num_i in enumerate(nums):
        while ascending_stack and nums[ascending_stack[-1]] > num_i:
            left_bound = min(left_bound, ascending_stack.pop())
        ascending_stack.append(i)

    right_bound = 0
    descending_stack = []  # i such that nums[i] in descending order
    for i in range(len(nums) - 1, -1, -1):
        while descending_stack and nums[descending_stack[-1]] < nums[i]:
            right_bound = max(right_bound, descending_stack.pop())
        descending_stack.append(i)

    return right_bound - left_bound + 1 if right_bound > left_bound else 0


def find_unsorted_sub_array_sorted(nums: List[int]) -> int:
    """
    Sort the array to find the first and last mismatch approach

    :param nums: an integer array
    :return: length of shorted continuous sub array that if you only sort this sub array in ascending order, the whole
        array will be sorted in ascending order
    """
    is_same = [a == b for a, b in zip(nums, sorted(nums))]
    return 0 if all(is_same) else len(nums) - is_same.index(False) - is_same[::-1].index(False)


test_cases = [([2, 6, 4, 8, 10, 9, 15], 5),
              ([1, 2, 3, 4], 0),
              ([1], 0), ]
for find_unsorted_sub in [find_unsorted_sub_array_sorted, find_unsorted_sub_array_stack]:
    for test_input, expected_output in test_cases:
        assert find_unsorted_sub(test_input) == expected_output
