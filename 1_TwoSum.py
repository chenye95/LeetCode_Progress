"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
"""
from typing import List


def two_sum(nums: List[int], target: int) -> List[int]:
    complement_lookup = {}
    for i, n in enumerate(nums):
        if target - n in complement_lookup:
            return [i, complement_lookup[target - n]]
        else:
            complement_lookup[n] = i


assert set(two_sum(nums=[2, 7, 11, 15], target=9)) == {0, 1}
assert set(two_sum(nums=[3, 2, 4], target=6)) == {1, 2}
assert set(two_sum(nums=[3, 3], target=6)) == {0, 1}
