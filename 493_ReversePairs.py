"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2 * nums[j].

You need to return the number of important reverse pairs in the given array.
"""
from bisect import bisect_left
from copy import deepcopy
from typing import List


def reverse_pairs_bit(nums: List[int]) -> int:
    """
    Based on Binary Search Tree implementation

    :param nums: array of integers
    :return: count of important reverse pairs in nums: i < j such that nums[i] > 2 * nums[j]
    """

    def bit_query(bit_tree: List[int], tree_idx: int) -> int:
        """
        :return: return sum for range [tree_idx:]
        """
        bit_sum = 0
        while 0 < tree_idx < len(bit_tree):
            bit_sum += bit_tree[tree_idx]
            tree_idx += (tree_idx & -tree_idx)  # next node that is not an ancestor of tree_idx
        return bit_sum

    def bit_update(bit_tree: List[int], tree_idx: int, val: int):
        """
        Update tree_idx to assume value val in array underlying Binary Search Tree
        """
        while tree_idx > 0:
            bit_tree[tree_idx] += val
            tree_idx -= tree_idx & (-tree_idx)

    nums_sorted = sorted(deepcopy(nums))
    count = 0
    bit_array = [0] * (len(nums) + 1)  # partial representation of count of numbers greater than nums_sorted[i]
    for i in range(len(nums)):
        count += bit_query(bit_array, bisect_left(nums_sorted, nums[i] * 2 + 1) + 1)
        bit_update(bit_array, bisect_left(nums_sorted, nums[i]) + 1, 1)
    return count


def reverse_pairs_merge_sort(nums: List[int]) -> int:
    """
    Based on Merge Sort implementation

    :param nums: array of integers
    :return: count of important reverse pairs in nums: i < j such that nums[i] > 2 * nums[j]
    """

    def merge_sort_merge(nums: List[int], start_inclusive: int, mid_inclusive_in_left: int, end_inclusive: int) -> None:
        l_tmp = deepcopy(nums[start_inclusive:mid_inclusive_in_left + 1])
        r_tmp = deepcopy(nums[mid_inclusive_in_left + 1:end_inclusive + 1])
        i = j = 0
        k = start_inclusive
        while i < len(l_tmp) and j < len(r_tmp):
            if l_tmp[i] <= r_tmp[j]:
                nums[k] = l_tmp[i]
                i += 1
            else:
                nums[k] = r_tmp[j]
                j += 1
            k += 1

        if i < len(l_tmp):
            nums[k:end_inclusive + 1] = l_tmp[i:]
        elif j < len(r_tmp):
            nums[k:end_inclusive + 1] = r_tmp[j:]

    def merge_sort_count(nums: List[int], start_inclusive: int, end_inclusive: int) -> int:
        if start_inclusive < end_inclusive:
            mid_inclusive_in_left = (start_inclusive + end_inclusive) // 2
            count = merge_sort_count(nums, start_inclusive, mid_inclusive_in_left) \
                    + merge_sort_count(nums, mid_inclusive_in_left + 1, end_inclusive)
            j = mid_inclusive_in_left + 1
            for i in range(start_inclusive, mid_inclusive_in_left + 1):
                while j <= end_inclusive and nums[i] > nums[j] * 2:
                    j += 1
                count += j - (mid_inclusive_in_left + 1)
            merge_sort_merge(nums, start_inclusive, mid_inclusive_in_left, end_inclusive)
            return count
        else:
            return 0

    return merge_sort_count(nums, 0, len(nums) - 1)


test_cases = [([3, 2, 1], 1),
              ([8, 7, 6, 5, 4, 3, 2, 1], 3 * 2 + 2 * 2 + 1 * 2),
              ([1, 3, 2, 3, 1], 2),
              ([2, 4, 3, 5, 1], 3), ]
for reverse_pairs in [reverse_pairs_bit, reverse_pairs_merge_sort]:
    for test_list, test_count in test_cases:
        return_res = reverse_pairs(test_list)
        assert return_res == test_count, "%s: Expected %d Got %d" % \
                                         (reverse_pairs.__name__, test_count, return_res)
