"""
Given an array nums, we call (i, j) an important reverse pair if i < j and nums[i] > 2*nums[j].

You need to return the number of important reverse pairs in the given array.
"""
from bisect import bisect_left
from copy import deepcopy
from typing import List


class BITSolution:
    def query(self, bit: List[int], tree_idx: int) -> int:
        sum = 0
        while 0 < tree_idx < len(bit):
            sum += bit[tree_idx]
            tree_idx += (tree_idx & -tree_idx)      # next node that is not an ancestor of tree_idx
        return sum

    def update(self, bit: List[int], tree_idx: int, val: int):
        while tree_idx > 0:
            bit[tree_idx] += val
            tree_idx -= tree_idx & (-tree_idx)

    def reversePairs(self, nums: List[int]) -> int:
        nums_sorted = deepcopy(nums)
        nums_sorted.sort()
        count = 0
        BIT_array = [0] * (len(nums) + 1)   # partial representation of count of numbers greater than nums_sorted[i]
        for i in range(len(nums)):
            count += self.query(BIT_array, bisect_left(nums_sorted, nums[i] * 2 + 1) + 1)
            self.update(BIT_array, bisect_left(nums_sorted, nums[i]) + 1, 1)
        return count


class MergeSortSolution():
    def merge(self, nums: List[int], start_inclusive: int, mid_inclusive_in_left: int, end_inclusive: int) -> None:
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

    def merge_sort_count(self, nums: List[int], start_inclusive: int, end_inclusive: int) -> int:
        if start_inclusive < end_inclusive:
            mid_inclusive_in_left = (start_inclusive + end_inclusive) // 2
            count = self.merge_sort_count(nums, start_inclusive, mid_inclusive_in_left) \
                    + self.merge_sort_count(nums, mid_inclusive_in_left + 1, end_inclusive)
            j = mid_inclusive_in_left + 1
            for i in range(start_inclusive, mid_inclusive_in_left + 1):
                while j <= end_inclusive and nums[i] > nums[j] * 2:
                    j += 1
                count += j - (mid_inclusive_in_left + 1)
            self.merge(nums, start_inclusive, mid_inclusive_in_left, end_inclusive)
            return count
        else:
            return 0

    def reversePairs(self, nums: List[int]) -> int:
        return self.merge_sort_count(nums, 0, len(nums) - 1)


solution_class = BITSolution()
test_cases = [([3, 2, 1], 1),
              ([8, 7, 6, 5, 4, 3, 2, 1], 3 * 2 + 2 * 2 + 1 * 2),
              ([1, 3, 2, 3, 1], 2),
              ([2, 4, 3, 5, 1], 3)]
for test_list, test_count in test_cases:
    return_res = solution_class.reversePairs(test_list)
    assert return_res == test_count, "BIT Method Expected %d Got %d" % (test_count, return_res)

solution_class = MergeSortSolution()
for test_list, test_count in test_cases:
    return_res = solution_class.reversePairs(test_list)
    assert return_res == test_count, "Merge Sort Method Expected %d Got %d" % (test_count, return_res)
