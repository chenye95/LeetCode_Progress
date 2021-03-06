"""
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.
"""
from typing import List


def jump(nums: List[int]) -> int:
    """
    :param nums: array of non-negative integers, representing maximum jump length from that position
    :return: minimum number of jumps to reach last index
    """
    n = len(nums)
    steps = [n] * n
    steps[0] = 0
    reach = 1

    for idx in range(n):
        # update assuming traverse through idx
        # any index before start is within in reach from previous indexes;
        # doesn't make sense to travel through current idx
        start = reach
        reach = max(nums[idx], reach - 1)
        for r in range(start, min(reach + 1, n - idx)):
            steps[idx + r] = min(steps[idx + r], steps[idx] + 1)

    return steps[-1]


test_cases = [([2, 3, 1, 1, 4], 2),
              ([2, 3, 0, 1, 4], 2), ]
for test_nums, expected_jump in test_cases:
    assert jump(nums=test_nums) == expected_jump, expected_jump
