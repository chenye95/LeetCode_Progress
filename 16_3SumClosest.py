"""
Given an array nums of n integers and an integer target, find three integers in nums such that the sum is closest to
target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
"""
from typing import List


def three_sum_closest(nums: List[int], target: int) -> int:
    """
    Assume each input has exactly one solution

    :return: sum of 3 integers in nums such that sum is closest to target (in terms of absolute value)
    """
    if not nums or len(nums) < 3:
        return 0

    nums.sort()
    less_than_target_max, more_than_target_min = sum(nums[:3]), sum(nums[-3:])

    if less_than_target_max > target:
        return less_than_target_max
    if more_than_target_min < target:
        return more_than_target_min

    for i in range(len(nums)):
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        left_pointer, right_pointer = i + 1, len(nums) - 1
        while left_pointer < right_pointer:
            current_sum = nums[i] + nums[left_pointer] + nums[right_pointer]
            if current_sum < target:
                less_than_target_max = max(less_than_target_max, current_sum)
                left_pointer += 1
            elif current_sum > target:
                more_than_target_min = min(more_than_target_min, current_sum)
                right_pointer -= 1
            else:
                return target
    return more_than_target_min if more_than_target_min - target < target - less_than_target_max \
        else less_than_target_max


test_cases = [([-1, 2, 1, -4], 1, 2),
              ([0, 2, 1, -3], 1, 0),
              ([-1, 2, 1, -4], 1, 2),
              ([-4, -7, -2, 2, 5, -2, 1, 9, 3, 9, 4, 9, -9, -3, 7, 4, 1, 0, 8, 5, -7, -7], 29, 27),
              ([-10, 0, -2, 3, -8, 1, -10, 8, -8, 6, -7, 0, -7, 2, 2, -5, -8, 1, -4, 6], 18, 17),
              ([13, 2, 0, -14, -20, 19, 8, -5, -13, -3, 20, 15, 20, 5, 13, 14, -17, -7, 12, -6, 0, 20, -19, -1, -15, -2,
                8, -2, -9, 13, 0, -3, -18, -9, -9, -19, 17, -14, -19, -4, -16, 2, 0, 9, 5, -7, -4, 20, 18, 9, 0, 12, -1,
                10, -17, -11, 16, -13, -14, -3, 0, 2, -18, 2, 8, 20, -15, 3, -13, -12, -2, -19, 11, 11, -10, 1, 1, -10,
                -2, 12, 0, 17, -19, -7, 8, -19, -17, 5, -5, -10, 8, 0, -12, 4, 19, 2, 0, 12, 14, -9, 15, 7, 0, -16, -5,
                16, -12, 0, 2, -16, 14, 18, 12, 13, 5, 0, 5, 6], -59, -58), ]
for input_list, test_target, expected_output in test_cases:
    assert three_sum_closest(input_list, test_target) == expected_output
