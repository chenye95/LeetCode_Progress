"""
Given an array, rotate the array to the right by k steps, where k is non-negative.
"""
from copy import deepcopy
from typing import List


def rotate_extra_space(nums: List[int], k: int) -> None:
    """
    :param nums: list of integers with 1 <= nums.length <= 10 ** 5, rotate in place
    :param k: 0 <= k <= 10 ** 5
    """
    k %= len(nums)
    if k == 0:
        return
    nums[:] = nums[-k:] + nums[:-k]


def rotate_cyclic_replacement(nums: List[int], k: int) -> None:
    """
    :param nums: list of integers with 1 <= nums.length <= 10 ** 5, rotate in place
    :param k: 0 <= k <= 10 ** 5
    """
    n = len(nums)
    k %= n

    if k == 0:
        return

    start_idx = replaced_count = 0
    while replaced_count < n:
        current_idx, previous_val = start_idx, nums[start_idx]
        while True:
            next_idx = (current_idx + k) % n
            nums[next_idx], previous_val = previous_val, nums[next_idx]
            current_idx = next_idx
            replaced_count += 1

            if start_idx == current_idx:
                break

        start_idx += 1


def rotate_reverse(nums: List[int], k: int) -> None:
    """
    :param nums: list of integers with 1 <= nums.length <= 10 ** 5, rotate in place
    :param k: 0 <= k <= 10 ** 5
    """

    def reverse_section(start_idx: int, end_idx: int) -> None:
        """
        Reverse in place section nums[start_idx : end_idx + 1]
        :param start_idx: 0 <= start_idx <= end_idx < len(nums)
        :param end_idx: 0 <= start_idx <= end_idx < len(nums)
        """
        while start_idx < end_idx:
            nums[start_idx], nums[end_idx] = nums[end_idx], nums[start_idx]
            start_idx += 1
            end_idx -= 1

    n = len(nums)
    k %= n

    if k == 0:
        return

    nums.reverse()
    reverse_section(0, k - 1)
    reverse_section(k, n - 1)


test_cases = [([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
              ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
              ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28,
                29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54,
                55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80,
                81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97], 192,
               [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
                31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
                57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82,
                83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 1, 2]), ]
for rotate_array in [rotate_extra_space, rotate_cyclic_replacement]:
    for test_input, test_k, expected_output in test_cases:
        test_nums = deepcopy(test_input)
        rotate_extra_space(test_nums, test_k)
        assert test_nums == expected_output
