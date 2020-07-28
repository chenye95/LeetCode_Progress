"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

You may assume no duplicate exists in the array.
"""
from random import randint
from typing import List


def find_min(nums: List[int]) -> int:
    """
    Modified version of binary search to find inflection, pivot point
    :param nums: an array sorted in ascending order is rotated at some pivot; no duplicates allowed
    :return: min element in nums
    """

    if len(nums) == 1 or nums[-1] > nums[0]:
        # if last element is greater than first element, there is no rotation
        return nums[0]

    # Rotated at pivot nums[k], since pre rotation nums is sorted
    # nums[k] < nums[k+1] < nums[k+2] < ... < nums[-1] < nums[0] < nums[1] < ... < nums[k-1]
    # i.e. nums[0] < nums[1] < ... < nums[k-1] > nums[k] < nums[k+1] < .... < nums[-1]
    left, right = 0, len(nums) - 1
    while left <= right:
        # mid element of sub array left, ..., right
        mid = (left + right) // 2
        # evaluate if mid or mid + 1 is the pivot point
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        if nums[left] < nums[mid]:
            # left ... mid is sorted
            left = mid + 1
        else:
            # mid ... right is sorted
            right = mid - 1


assert 1 == find_min([3, 4, 5, 1, 2])
assert 0 == find_min([4, 5, 6, 7, 0, 1, 2])

N = randint(500, 1000)
range_list = list(range(N))
for _ in range(10):
    i = randint(0, N - 1)
    print(N, i)
    assert 0 == find_min(range_list[i:] + range_list[:i])
