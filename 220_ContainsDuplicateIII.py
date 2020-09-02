"""
Given an array of integers, find out whether there are two distinct indices i and j in the array such that the absolute
difference between nums[i] and nums[j] is at most t and the absolute difference between i and j is at most k.
"""
from typing import List


def contains_nearby_almost_duplicate(nums: List[int], k: int, t: int) -> bool:
    """
    :return: exists (i, j) pair such that i < j <= i + k and |nums[i] - nums[j]| <= t
    """
    if t < 0 or k < 0:
        return False
    # divide nums into bucket of (t + 1)
    buckets = {}
    t_plus_1 = t + 1
    for i, num_i in enumerate(nums):
        num_i_bucket = num_i // t_plus_1
        if (num_i_bucket in buckets) or \
                (num_i_bucket - 1 in buckets and abs(num_i - buckets[num_i_bucket - 1]) < t_plus_1) or \
                (num_i_bucket + 1 in buckets and abs(num_i - buckets[num_i_bucket + 1]) < t_plus_1):
            # some previous nums satisfies nums[j] // t_plus_1 == num_i_bucket
            # or look to previous and next bucket for potential match
            return True
        buckets[num_i_bucket] = num_i
        if i >= k:
            # sliding window of length k
            del buckets[nums[i - k] // t_plus_1]
    return False


assert contains_nearby_almost_duplicate(nums=[1, 2, 3, 1], k=3, t=0) is True
assert contains_nearby_almost_duplicate(nums=[1, 0, 1, 1], k=1, t=2) is True
assert contains_nearby_almost_duplicate(nums=[1, 5, 9, 1, 5, 9], k=2, t=3) is False
