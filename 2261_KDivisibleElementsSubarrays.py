"""
Given an integer array nums and two integers k and p, return the number of distinct sub arrays, which have at most k
 elements that are divisible by p.

Two arrays nums1 and nums2 are said to be distinct if:
    - They are of different lengths, or
    - There exists at least one index i where nums1[i] != nums2[i].

A subarray is defined as a non-empty contiguous sequence of elements in an array.
"""
from typing import List, Callable


def hash_function(old_hash: int, new_num: int, sub_array_len: int) -> int:
    return (old_hash * 397 + new_num + sub_array_len) % 100000000069


def count_distinct(nums: List[int], k: int, p: int, use_hash_function: Callable[[int, int, int], int]) -> int:
    is_divisible = [num_i % p == 0 for num_i in nums]
    ans_set = set()
    for i in range(len(nums)):
        cnt_divisible = 0
        current_sub_array_hash = 0
        for j in range(i, len(nums)):
            current_sub_array_hash = use_hash_function(current_sub_array_hash, nums[j], j - i + 1)
            if is_divisible[j]:
                cnt_divisible += 1
            if cnt_divisible <= k:
                ans_set.add(current_sub_array_hash)
            else:
                break

    return len(ans_set)


test_cases = [
    ([2, 3, 3, 2, 2], 2, 2, 11),
    ([1, 2, 3, 4], 4, 1, 10),
]
for test_nums, test_k, test_p, expected_value in test_cases:
    assert count_distinct(test_nums, test_k, test_p, hash_function) == expected_value
