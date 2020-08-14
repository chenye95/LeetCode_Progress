"""
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are
adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.
"""
from typing import List


def sort_color(nums: List[int]) -> None:
    """
    Dutch partitioning problem: sort list of 3 colors
    :param nums: list of integer representing colors, 0: red, 1: white, 2: blue
    :return: does not return anything. Inplace sorting
    """
    white_start = white_end_plus_one = 0
    blue_start_minus_one = len(nums) - 1

    while white_end_plus_one <= blue_start_minus_one:
        if nums[white_end_plus_one] == 0:
            # current number is red, swap with white_end_plus_one
            # guaranteed white_start points to white, and follows the red color block
            nums[white_start], nums[white_end_plus_one] = nums[white_end_plus_one], nums[white_start]
            white_end_plus_one += 1
            white_start += 1
        elif nums[white_end_plus_one] == 1:
            # current number is white
            white_end_plus_one += 1
        else:
            # current number is blue
            # swap into blue blocks
            nums[white_end_plus_one], nums[blue_start_minus_one] = nums[blue_start_minus_one], nums[white_end_plus_one]
            blue_start_minus_one -= 1


from random import randint

for i in range(100):
    if i % 10 == 0:
        print('Testing case %d' % i)
    test_case_input = [randint(0, 2) for _ in range(10000)]
    test_case_output = sorted(test_case_input)
    sort_color(test_case_input)
    assert test_case_input == test_case_output, test_case_input
