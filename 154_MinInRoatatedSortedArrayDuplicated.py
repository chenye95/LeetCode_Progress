"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.
"""
from typing import List


def find_min(nums: List[int]) -> int:
    """
    Modified version of binary search to find inflection, pivot point
    :param nums: an array sorted in ascending order is rotated at some pivot; may contain duplicates
    :return: min element in nums
    """

    # Rotated at pivot nums[k], since pre rotation nums is sorted
    # nums[k] <= nums[k+1] <= nums[k+2] <= ... <= nums[-1] <= nums[0] <= nums[1] <= ... <= nums[k-1]
    # i.e. nums[0] <= nums[1] <= ... <= nums[k-1] >= nums[k] <= nums[k+1] <= .... <= nums[-1]
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] < nums[right]:
            # left, ..., right is sorted, min is nums[left]
            return nums[left]

        mid = (left + right) // 2
        # evaluate if mid or mid + 1 is the pivot point
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if nums[mid - 1] > nums[mid]:
            return nums[mid]

        # nums[left] >= nums[right]
        if nums[left] == nums[mid] == nums[right]:
            # unclear, e.g. 3, 3, 1, 3
            left += 1
            right -= 1
        elif nums[left] <= nums[mid]:
            # nums[left] <= nums[mid] and nums[mid] >= nums[right]
            # left, ..., mid is sorted, pivot in mid+1, ..., right
            left = mid + 1
        else:
            # nums[left] > nums[mid] and nums[mid] <= nums[right]
            # left, ..., mid contains the pivot
            right = mid - 1

    return nums[left]


assert 1 == find_min([3, 3, 3, 3, 3, 3, 3, 3, 1, 3])
assert 1 == find_min([3, 3, 3, 1])
assert 1 == find_min([1, 1])
assert 1 == find_min([3, 1, 3])
assert 1 == find_min([3, 4, 5, 1, 2])
assert 0 == find_min([4, 5, 6, 7, 0, 1, 2])
assert 0 == find_min([2, 2, 2, 0, 1])
