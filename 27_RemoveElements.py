"""
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra
memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.
"""
from collections import Counter
from copy import deepcopy
from typing import List


def remove_elements_1(nums: List[int], val: int) -> int:
    i = 0
    for j in range(len(nums)):
        if nums[j] != val:
            nums[i] = nums[j]
            i += 1
    return i


def remove_elements_2(nums: List[int], val: int) -> int:
    i = 0
    n = len(nums)
    while i < n:
        if nums[i] == val:
            nums[i] = nums[n - 1]
            n -= 1
        else:
            i += 1
    return n


test_cases_original = [([3, 2, 2, 3], 3, [2, 2]),
                       ([0, 1, 2, 2, 3, 0, 4, 2], 2, [0, 1, 4, 0, 3])]
for remove_elements in [remove_elements_1, remove_elements_2]:
    test_cases = deepcopy(test_cases_original)
    for test_input, remove_val, expected_output in test_cases:
        assert remove_elements(nums=test_input, val=remove_val) == len(expected_output)
        assert Counter(test_input[:len(expected_output)]) == Counter(expected_output)
