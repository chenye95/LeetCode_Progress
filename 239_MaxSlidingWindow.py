"""
Given an array nums, there is a sliding window of size k which is moving from the very left of the array to the very
right. You can only see the k numbers in the window. Each time the sliding window moves right by one position. Return
the max sliding window.
"""
from collections import deque
from typing import List


def max_sliding_window(nums: List[int], k: int) -> List[int]:
    """
    :param nums: array of integers
    :param k: sliding window of size k
    :return: list of max values in sliding window as window slides across nums from very left to very right
    """
    current_candidates = deque()
    return_list = []
    for i, n_i in enumerate(nums):
        while current_candidates and nums[current_candidates[-1]] < n_i:
            current_candidates.pop()
        current_candidates.append(i)
        if current_candidates[0] == i - k:
            current_candidates.popleft()
        if i >= k - 1:
            return_list.append(nums[current_candidates[0]])
    return return_list


assert max_sliding_window(nums=[1, 3, -1, -3, 5, 3, 6, 7], k=3) == [3, 3, 5, 5, 6, 7]

from random import randint
from datetime import datetime

for i in range(10):
    N = 10000
    k = randint(2, 20)
    nums = [randint(-100, 100) for _ in range(N)]
    out = [max(nums[i:i + k]) for i in range(N - k + 1)]
    start_time = datetime.now()
    calculated_output = max_sliding_window(nums, k)
    end_time = datetime.now()
    assert calculated_output == out
    print("Cycle %d" % i, end_time - start_time)