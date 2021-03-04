"""
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is
missing from the array.

Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
"""
from typing import List


def missing_number_sort(nums: List[int]) -> int:
    nums.sort()
    if nums[-1] != len(nums):
        # ensure that n is the last index
        return len(nums)

    for i in range(0, len(nums)):
        if nums[i] != i:
            return i


def missing_number_hash_set(nums: List[int]) -> int:
    num_set = set(nums)
    for n_i in range(len(nums) + 1):
        if n_i not in num_set:
            return n_i


def missing_number_xor(nums: List[int]) -> int:
    missing_num = len(nums)
    for i, n_i in enumerate(nums):
        missing_num ^= (i ^ n_i)
    return missing_num


def missing_number_sum(nums: List[int]) -> int:
    return len(nums) * (len(nums) + 1) // 2 - sum(nums)


test_cases = [([3, 0, 1], 2),
              ([0, 1], 2),
              ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
              ([0], 1),
              ]
for missing_number in [missing_number_sort, missing_number_hash_set, missing_number_xor, missing_number_sum]:
    for test_input, expected_output in test_cases:
        assert missing_number(test_input) == expected_output
