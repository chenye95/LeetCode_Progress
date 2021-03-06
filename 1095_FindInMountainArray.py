"""
You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.
If such an index doesn't exist, return -1.
"""
from typing import List


class MountainArray:
    def __init__(self, array: List[int]):
        self.array = array
        self.call_time = 0
        self.max_call = 100

    def get(self, index: int) -> int:
        self.call_time += 1
        assert self.call_time <= self.max_call, 'Exceed max %d queries of get method' % self.max_call
        return self.array[index]

    def length(self) -> int:
        return len(self.array)


def find_in_mountain_array(target: int, mountain_arr: MountainArray) -> int:
    """
    :param target: target to be found in Mountain Array
    :param mountain_arr: Mountain Array object
    :return: index of target in Mountain Array if it exists, -1 otherwise
    """
    # Find the index of peak in Mountain Array
    left, right = 0, mountain_arr.length() - 1
    while left < right:
        probe = (left + right) // 2
        if mountain_arr.get(probe) > mountain_arr.get(probe + 1):
            right = probe
        else:
            left = probe + 1
    peak_index = left

    # Find in Uphill leg
    left, right = 0, peak_index
    while left <= right:
        probe = (left + right) // 2
        probe_val = mountain_arr.get(probe)
        if probe_val == target:
            return probe
        elif probe_val < target:
            left = probe + 1
        else:
            right = probe - 1

    # Find in Downhill Leg
    left, right = peak_index, mountain_arr.length() - 1
    while left <= right:
        probe = (left + right) // 2
        probe_val = mountain_arr.get(probe)
        if probe_val == target:
            return probe
        elif probe_val > target:
            left = probe + 1
        else:
            right = probe - 1

    return -1


assert find_in_mountain_array(mountain_arr=MountainArray([1, 2, 3, 4, 5, 3, 1]), target=3) == 2
assert find_in_mountain_array(mountain_arr=MountainArray(array=[0, 1, 2, 4, 2, 1]), target=3) == -1
assert find_in_mountain_array(mountain_arr=MountainArray(array=[1, 2, 3, 5, 3]), target=0) == -1
