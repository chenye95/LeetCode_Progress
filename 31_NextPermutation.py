"""
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.
"""
from typing import List


def next_permutation(nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    if i < 0:
        nums.reverse()
    else:
        j = len(nums) - 1
        while j >= 0 and nums[j] <= nums[i]:
            j -= 1
        nums[i], nums[j] = nums[j], nums[i]
        nums[i + 1:] = nums[i + 1:][::-1]


from copy import deepcopy


test_cases = [[[1, 2, 3],
               [1, 3, 2],
               [2, 1, 3],
               [2, 3, 1],
               [3, 1, 2],
               [3, 2, 1]],
              [[1, 1, 5],
               [1, 5, 1],
               [5, 1, 1]]]

for case_i in test_cases:
    for j in range(len(case_i)):
        test_nums = deepcopy(case_i[j])
        # print(test_nums)
        next_permutation(test_nums)
        if j < len(case_i) - 1:
            assert test_nums == case_i[j + 1]
        else:
            assert test_nums == case_i[0]
    # print()
