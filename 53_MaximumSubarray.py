"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and
 return its sum.

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach,
 which is more subtle.
"""
from typing import List


def max_sub_array(nums: List[int]) -> int:
    max_tracker = nums[0]
    accumulation_tracker = 0
    for n_i in nums:
        accumulation_tracker += n_i
        if accumulation_tracker > max_tracker:
            max_tracker = accumulation_tracker
        if accumulation_tracker < 0:
            accumulation_tracker = 0
    return max_tracker


assert 6 == max_sub_array(nums=[-2, 1, -3, 4, -1, 2, 1, -5, 4])
assert 1 == max_sub_array(nums=[1])
assert 0 == max_sub_array(nums=[0])
assert -1 == max_sub_array(nums=[-1])
assert -2147483647 == max_sub_array(nums=[-2147483647])
