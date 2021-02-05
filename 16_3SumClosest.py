"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
"""
from typing import List


def threeSumClosest(nums: List[int], target: int) -> int:
    if not nums or len(nums) < 3:
        return 0

    nums.sort()
    less_than_target_max, more_than_target_min = sum(nums[:3]), sum(nums[-3:])

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        l, r = i + 1, len(nums) - 1
        while l < r:
            current_sum = nums[i] + nums[l] + nums[r]
            if current_sum < target:
                less_than_target_max = max(less_than_target_max, current_sum)
                l += 1
            elif current_sum > target:
                more_than_target_min = min(more_than_target_min, current_sum)
                r -= 1
            else:
                return target
    return more_than_target_min if more_than_target_min - target < target - less_than_target_max \
        else less_than_target_max


test_cases = [([-1, 2, 1, -4], 1, 2),
              ([0, 2, 1, -3], 1, 0),
              ([-1, 2, 1, -4], 1, 2), ]
for input_list, test_target, expected_output in test_cases:
    assert threeSumClosest(input_list, test_target) == expected_output
