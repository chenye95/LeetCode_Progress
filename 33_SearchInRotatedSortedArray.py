"""
There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such
 that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For
 example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or
 -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    if nums:
        first_num = nums[0]

        if target == first_num:
            return 0

        left_pointer = 0
        right_pointer = len(nums) - 1
        less_than_first_num = first_num < target

        while left_pointer <= right_pointer:
            mid_pointer = (left_pointer + right_pointer) // 2
            if target > nums[mid_pointer]:
                if less_than_first_num and nums[mid_pointer] < first_num:
                    # nums[mid_pointer] < first_num < target
                    right_pointer = mid_pointer - 1
                else:
                    # nums[mid_pointer] < target < first_num or first_num < nums[mid_pointer] < target
                    left_pointer = mid_pointer + 1
            elif target < nums[mid_pointer]:
                if not less_than_first_num and nums[mid_pointer] >= first_num:
                    # target < first_num <= nums[mid_pointer]
                    left_pointer = mid_pointer + 1
                else:
                    # first_num < target < nums[mid_pointer] or target < nums[mid_pointer] < first_num
                    right_pointer = mid_pointer - 1
            else:
                return mid_pointer

    return -1


test_cases = [
    ([4, 5, 6, 7, 0, 1, 2], 0, 4),
    ([4, 5, 6, 7, 0, 1, 2], 3, -1),
    ([1], 0, -1),
    ([], 0, -1),
    ([284, 287, 289, 293, 295, 298, 0, 3, 8, 9, 10, 11, 12, 15, 17, 19, 20, 22, 26, 29, 30, 31, 35, 36, 37, 38, 42, 43,
      45, 50, 51, 54, 56, 58, 59, 60, 62, 63, 68, 70, 73, 74, 81, 83, 84, 87, 92, 95, 99, 101, 102, 105, 108, 109, 112,
      114, 115, 116, 122, 125, 126, 127, 129, 132, 134, 136, 137, 138, 139, 147, 149, 152, 153, 154, 155, 159, 160, 161,
      163, 164, 165, 166, 168, 169, 171, 172, 174, 176, 177, 180, 187, 188, 190, 191, 192, 198, 200, 203, 204, 206, 207,
      209, 210, 212, 214, 216, 221, 224, 227, 228, 229, 230, 233, 235, 237, 241, 242, 243, 244, 246, 248, 252, 253, 255,
      257, 259, 260, 261, 262, 265, 266, 268, 269, 270, 271, 272, 273, 277, 279, 281], 235, 113),
    ([1, 3], 3, 1),
    ([4, 5, 6, 7, 0, 1, 2], 2, 6),
]
for test_nums, test_target, expected_value in test_cases:
    assert search(test_nums, test_target) == expected_value
