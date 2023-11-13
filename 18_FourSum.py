"""
Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]]
 such that:
    - 0 <= a, b, c, d < n
    - a, b, c, and d are distinct.
    - nums[a] + nums[b] + nums[c] + nums[d] == target

You may return the answer in any order.
"""
from typing import List


def four_sum(nums: List[int], target: int) -> List[List[int]]:
    def find_n_sum(left_pointer: int, right_pointer: int, sub_target: int, n: int, partial_result: List[int]) -> None:
        if (right_pointer - left_pointer + 1 < n or n < 2 or
                sub_target < nums[left_pointer] * n or sub_target > nums[right_pointer] * n):
            return

        if n == 2:
            # solve 2 sum problem
            while left_pointer < right_pointer:
                s = nums[left_pointer] + nums[right_pointer]
                if s == sub_target:
                    results.append(partial_result + [nums[left_pointer], nums[right_pointer]])
                    left_pointer += 1

                    # Skip duplicates
                    while left_pointer < right_pointer and nums[left_pointer] == nums[left_pointer - 1]:
                        left_pointer += 1
                elif s < sub_target:
                    left_pointer += 1
                else:
                    right_pointer -= 1

        else:
            for i in range(left_pointer, right_pointer - n + 2):
                # try to fix one number at a time
                if i == left_pointer or nums[i] > nums[i - 1]:
                    find_n_sum(i + 1, right_pointer, sub_target - nums[i], n - 1, partial_result + [nums[i]])

    nums.sort()
    results: List[List[int]] = []
    find_n_sum(0, len(nums) - 1, target, 4, [])
    return results


test_cases = [
    ([1, 0, -1, 0, -2, 2], 0, [[-2, -1, 1, 2], [-2, 0, 0, 2], [-1, 0, 0, 1]]),
    ([2, 2, 2, 2, 2], 8, [[2, 2, 2, 2]]),
    ([[0, 0, 0, 0], 0, [[0, 0, 0, 0]]]),
    ([-493, -470, -464, -453, -451, -446, -445, -407, -406, -393, -328, -312, -307, -303, -259, -253, -252, -243, -221,
      -193, -126, -126, -122, -117, -106, -105, -101, -71, -20, -12, 3, 4, 20, 20, 54, 84, 98, 111, 148, 149, 152, 171,
      175, 176, 211, 218, 227, 331, 352, 389, 410, 420, 448, 485], 1057,
     [[-221, 410, 420, 448], [-12, 211, 410, 448], [3, 149, 420, 485], [4, 148, 420, 485], [54, 98, 420, 485],
      [84, 211, 352, 410], [98, 218, 331, 410], [98, 218, 352, 389], [171, 211, 227, 448]]),
]
for test_nums, test_target, expected_values in test_cases:
    expected_set_list = {tuple(sorted(idx_list)) for idx_list in expected_values}
    get_lists = four_sum(test_nums, test_target)
    get_set_list = {tuple(sorted(idx_list)) for idx_list in get_lists}
    assert expected_set_list == get_set_list
