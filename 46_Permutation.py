"""
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
"""
from typing import List


def permute(nums: List[int]) -> List[List[int]]:
    return [[n] + p
            for i, n in enumerate(nums)
            for p in permute(nums[:i] + nums[i + 1:])] or [[]]


assert permute(nums=[1, 2, 3]) == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]
assert permute(nums=[0, 1]) == [[0, 1], [1, 0]]
assert permute(nums=[1]) == [[1]]
