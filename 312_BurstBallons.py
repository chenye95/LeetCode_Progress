"""
Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are
asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here
left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:
- You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
- 0 ≤ n ≤ 500, 0 ≤ nums[i] ≤ 100
"""
from typing import List


def burst_balloons(nums: List[int]) -> int:
    # Drop all 0s in nums as this will not change final results
    # Extend both ends by 1
    nums = [1] + list(filter(lambda x: x > 0, nums)) + [1]
    n = len(nums)
    # Record the biggest number from nums[i], ..., nums[j] when all balloons inside the range are dropped off,
    # and nums[i] and nums[j] stay
    # dp_memory[0][-1] stores the final result, as nums[0] and nums[-1] are filler 1 and don't need to be dropped
    dp_memory = [[0] * n for _ in range(n)]

    # Scan (i, j) pair by window size j - i
    for window_size in range(2, n):
        for window_start in range(n - window_size):
            window_end = window_start + window_size
            window_multiplier = nums[window_start] * nums[window_end]
            # burst in way such that the last three remaining items in the group are nums[window_start],
            # nums[window_end] and nums[window_mid], and then burst nums[window_mid]
            dp_memory[window_start][window_end] = max(dp_memory[window_start][window_mid] +
                                                      dp_memory[window_mid][window_end] +
                                                      window_multiplier * nums[window_mid]
                                                      for window_mid in range(window_start + 1, window_end))
    return dp_memory[0][-1]


assert burst_balloons(nums=[3, 1, 5, 8]) == 167
assert burst_balloons(nums=[1, 5]) == 10
