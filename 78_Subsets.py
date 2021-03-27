"""
Given an integer array nums, return all possible subsets (the power set).

The solution set must not contain duplicate subsets.
"""
from typing import List


def subset(nums: List[int]) -> List[List[int]]:
    """
    Power set of array nums

    :return: all possible subsets of nums; does not contain duplicates
    """
    output_list = [[]]

    for num in nums:
        output_list += [out + [num] for out in output_list]

    return output_list


test_cases = [([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
              ([0], [[], [0]]), ]
for test_nums, expected_output in test_cases:
    assert sorted(subset(nums=test_nums)) == sorted(expected_output)
