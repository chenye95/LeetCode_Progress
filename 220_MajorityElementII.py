"""
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.

Note: The algorithm should run in linear time and in O(1) space.
"""
from typing import List


def majorityElement(nums: List[int]) -> List[int]:
    if not nums:
        return []
    candidate_1, count_1 = 0, 0
    candidate_2, count_2 = 1, 0
    for n in nums:
        if n == candidate_1:
            count_1 += 1
        elif n == candidate_2:
            count_2 += 1
        elif count_1 == 0:
            candidate_1, count_1 = n, 1
        elif count_2 == 0:
            candidate_2, count_2 = n, 1
        else:
            count_1, count_2 = count_1 - 1, count_2 - 1
    return [n for n in (candidate_1, candidate_2) if nums.count(n) > len(nums) // 3]


assert {3} == set(majorityElement([3, 2, 3]))
assert {1, 2} == set(majorityElement([1, 1, 1, 3, 3, 2, 2, 2]))
