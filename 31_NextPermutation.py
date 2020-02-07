from typing import List
from copy import deepcopy

def nextPermutation(nums: List[int]) -> None:
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
        tmp = nums[i]
        nums[i] = nums[j]
        nums[j] = tmp
        nums[i+1:] = nums[i+1:][::-1]


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
        nums = deepcopy(case_i[j])
        print(nums)
        nextPermutation(nums)
        if j < len(case_i) - 1:
            assert nums == case_i[j + 1]
        else:
            assert nums == case_i[0]
    print()
