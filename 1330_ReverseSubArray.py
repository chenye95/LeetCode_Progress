"""
You are given an integer array nums. The value of this array is defined as the sum of |nums[i]-nums[i+1]| for all 0 <=
i < nums.length-1.

You are allowed to select any subarray of the given array and reverse it. You can perform this operation only once.

Find maximum possible value of the final array.
"""

from typing import List


def maxValueAfterReverse(nums: List[int]) -> int:
    """
    ...a,b,...,c,d,...
    switching b, ..., c will only changes |a-b| + |c-d| to |a-c| + |b-d|
    only make sense to switch when
    (1) a,b < c,d increases return value by 2 * (min(c,d) - max(a,b))
    (2) a,b > c,d increases return value by 2 * (min(a,b) - max(c,d))
    """
    maxi, mini = -float('inf'), float('inf')
    for a, b in zip(nums, nums[1:]):  # consecutive pairs
        maxi = max(min(a, b), maxi)  # maximize(min(c,d))
        mini = min(max(a, b), mini)  # minimize(max(a,b))
    delta = max(0, (maxi - mini) * 2)

    # Special Case: c,.....a,b,.... and .....a,b,.....,c
    # solving the boundary situation
    for a, b in zip(nums, nums[1:]):
        flip_from_bgn = - abs(a - b) + abs(nums[0] - b)
        flip_from_end = - abs(a - b) + abs(nums[-1] - a)
        delta = max([flip_from_bgn, flip_from_end, delta])

    return sum(abs(a - b) for a, b in zip(nums, nums[1:])) + delta


assert maxValueAfterReverse(nums=[2, 3, 1, 5, 4]) == 10
assert maxValueAfterReverse(nums=[2, 4, 9, 24, 2, 1, 10]) == 68
