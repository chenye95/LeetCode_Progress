"""
Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
"""
from typing import List


def subset(nums: List[int]) -> List[List[int]]:
    output_list = [[]]

    for num in nums:
        output_list += [out + [num] for out in output_list]

    return output_list


assert subset(nums=[1, 2, 3]) == [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]
assert subset(nums=[0]) == [[], [0]]
