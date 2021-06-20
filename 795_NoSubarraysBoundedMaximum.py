"""
Given an integer array nums and two integers left and right, return the number of contiguous non-empty sub arrays such
 that the value of the maximum array element in that sub array is in the range [left, right].

The test cases are generated so that the answer will fit in a 32-bit integer.
"""
from typing import List


def num_sub_array_bounded_max_one(nums: List[int], left: int, right: int) -> int:
    """
    :param nums: 1 <= len(nums) <= 1e5 and 0 <= nums[i] <= 1e9
    :param left: 0 <= left <= right <= 1e9
    :param right: 0 <= left <= right <= 1e9
    :return: count of sub array whose max value is left <= max(sub_array) <= right
    """
    sub_array_count = 0
    i = -1
    i_to_last_in_range_count = 0
    for j, a_j in enumerate(nums):
        if left <= a_j <= right:
            i_to_last_in_range_count = j - i
            sub_array_count += i_to_last_in_range_count
        elif a_j > right:
            # restart counting from j + 1
            i_to_last_in_range_count = 0
            i = j
        elif j > 0:
            # a_j < left
            # a[i: j + 1] to a[i + i_to_last_in_range_count - 1: j + 1] satisfy the conditions
            sub_array_count += i_to_last_in_range_count

    return sub_array_count


def num_sub_array_bounded_max_two(nums: List[int], left: int, right: int) -> int:
    """
    :param nums: 1 <= len(nums) <= 1e5 and 0 <= nums[i] <= 1e9
    :param left: 0 <= left <= right <= 1e9
    :param right: 0 <= left <= right <= 1e9
    :return: count of sub array whose max value is left <= max(sub_array) <= right
    """
    sub_array_count = great_left_count = less_right_count = 0
    # less_right_count: distance from last num_i > right
    # great_left_count: distance from last num_i >= left
    for num_i in nums:
        if num_i > right:
            less_right_count = 0
        else:
            less_right_count += 1
            sub_array_count += less_right_count

        if num_i < left:
            great_left_count += 1
            sub_array_count -= great_left_count
        else:
            great_left_count = 0

    return sub_array_count


test_cases = [([2, 1, 4, 3], 2, 3, 3),
              ([2, 9, 2, 5, 6], 2, 8, 7),
              ([73, 55, 36, 5, 55, 14, 9, 7, 72, 52], 32, 69, 22),
              ([453, 995, 939, 975, 918, 464, 421, 166, 414, 713, 921, 682, 184, 244, 793, 371, 344, 11, 927, 841, 53,
                341, 382, 990, 744, 84, 558, 434, 674, 946, 484, 592, 934, 512, 555, 489, 496, 696, 812, 175, 865, 472,
                933, 406, 203, 643, 451, 839, 464, 165, 497, 814, 340, 442, 1, 192, 834, 503, 950, 614, 624, 14, 43,
                975, 349, 345, 888, 412, 163, 870, 492, 299, 310, 170, 57, 142, 139, 594, 529, 650, 391, 946, 895, 99,
                291, 832, 390, 64, 219, 988, 980, 509, 75, 846, 346, 542, 331, 827, 396, 608],
               50, 633, 146),
              ([876, 880, 482, 260, 132, 421, 732, 703, 795, 420, 871, 445, 400, 291, 358, 589, 617, 202, 755, 810, 227,
                813, 549, 791, 418, 528, 835, 401, 526, 584, 873, 662, 13, 314, 988, 101, 299, 816, 833, 224, 160, 852,
                179, 769, 646, 558, 661, 808, 651, 982, 878, 918, 406, 551, 467, 87, 139, 387, 16, 531, 307, 389, 939,
                551, 613, 36, 528, 460, 404, 314, 66, 111, 458, 531, 944, 461, 951, 419, 82, 896, 467, 353, 704, 905,
                705, 760, 61, 422, 395, 298, 127, 516, 153, 299, 801, 341, 668, 598, 98, 241], 658, 719, 19),
              ]
for num_count_bounded_max in [num_sub_array_bounded_max_one, num_sub_array_bounded_max_two, ]:
    for test_nums, test_left, test_right, expected_value in test_cases:
        assert num_count_bounded_max(test_nums, test_left, test_right) == expected_value, num_count_bounded_max.__name__
