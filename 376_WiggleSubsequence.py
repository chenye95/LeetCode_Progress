"""
Given an integer array nums, return the length of the longest wiggle sequence.

A wiggle sequence is a sequence where the differences between successive numbers strictly alternate between positive and
 negative. The first difference (if one exists) may be either positive or negative. A sequence with fewer than two
 elements is trivially a wiggle sequence.
    * For example, [1, 7, 4, 9, 2, 5] is a wiggle sequence because the differences (6, -3, 5, -7, 3) are alternately
    positive and negative.
    * In contrast, [1, 4, 7, 2, 5] and [1, 7, 4, 5, 5] are not wiggle sequences, the first because its first two
    differences are positive and the second because its last difference is zero.

A subsequence is obtained by deleting some elements (eventually, also zero) from the original sequence, leaving the
remaining elements in their original order.
"""
from typing import List


def wiggle_max_length_dp(nums: List[int]) -> int:
    """
    Dynamic Programming approach

    :return: max length of wiggle subsequences in nums
    """
    if len(nums) < 2:
        return len(nums)

    up_len = 1  # length of wiggle if the subsequence ends wiggling up
    down_len = 1  # length of wiggle if the subsequence ends wiggling down
    for i in range(1, len(nums)):
        if nums[i] > nums[i - 1]:
            up_len = down_len + 1
            # down_len = down_len
        elif nums[i] < nums[i - 1]:
            down_len = up_len + 1
            # up_len = up_len
        # else:
        # up_len = up_len
        # down_len = down_len

    return max(up_len, down_len)


def wiggle_max_length_greedy(nums: List[int]) -> int:
    """
    equivalent to finding number of local max and local min in the array
    - if we choose any other intermediate number to be a part of the current wiggle subsequence, the maximum length of
    that wiggle subsequence will always be less than or equal to the one obtained by choosing only the consecutive max
    and min elements.

    :return: number of local max and local min in the array + 1
    """
    if len(nums) < 2:
        return len(nums)

    prev_trend = nums[1] - nums[0]
    peak_count = 2 if prev_trend != 0 else 1

    for i in range(2, len(nums)):
        current_trend = nums[i] - nums[i - 1]
        # only looking for local max and local min
        if prev_trend <= 0 < current_trend or current_trend < 0 <= prev_trend:
            peak_count += 1
            prev_trend = current_trend

    return peak_count


test_cases = [([1, 7, 4, 9, 2, 5], 6),
              ([1, 17, 5, 10, 13, 15, 10, 5, 16, 8], 7),
              ([1, 2, 3, 4, 5, 6, 7, 8, 9], 2),
              ([56, 148, 74, 69, 95, 84, 172, 49, 182, 164, 20, 171, 20, 5, 102, 176, 125, 103, 95, 60, 52, 186, 181,
                191, 193, 87, 134, 129, 162, 8, 90, 76, 119, 92, 61, 148, 144, 112, 119, 197, 25, 149, 32, 80, 15, 148,
                25, 30, 172, 29, 91, 38, 98, 9, 0, 103, 0, 12, 36, 197, 127, 158, 139, 27, 157, 95, 61, 39, 45, 51, 30,
                105, 163, 5, 27, 196, 148, 137, 114, 198, 94, 161, 44, 185, 11, 131, 96, 117, 44, 102, 5, 61, 1, 149,
                52, 70, 131, 4, 173, 189, 124, 96, 8, 191, 161, 75, 59, 104, 111, 72, 100, 78, 156, 184, 55, 146, 130,
                63, 118, 113, 175, 128, 138, 188, 88, 173, 174, 115, 177, 78, 50, 111, 131, 138, 107, 173, 152, 198,
                195, 9, 23, 65, 57, 24, 102, 35, 91, 141, 90, 186, 104, 97, 134, 139, 99, 175, 93, 159, 101, 128, 48,
                144, 194, 176, 60, 25, 103, 177, 52, 6, 22, 183, 76, 129, 3, 6, 81, 162, 108, 111, 49, 96, 190, 195, 28,
                74, 160, 48, 91, 36, 160, 174, 190, 192, 155, 96, 151, 123, 128, 17], 141),
              (
              [372, 492, 288, 399, 81, 2, 320, 94, 416, 469, 427, 117, 265, 357, 399, 456, 496, 337, 355, 219, 475, 295,
               457, 350, 490, 470, 281, 127, 131, 36, 430, 412, 442, 174, 128, 253, 1, 56, 306, 295, 340, 73, 253, 130,
               259, 223, 14, 79, 409, 384, 209, 151, 317, 441, 156, 275, 140, 224, 128, 250, 290, 191, 161, 472, 477,
               125, 470, 230, 321, 5, 311, 23, 27, 248, 138, 284, 215, 356, 320, 194, 434, 136, 221, 273, 450, 440, 28,
               179, 36, 386, 482, 203, 24, 8, 391, 21, 500, 484, 135, 348, 292, 396, 145, 443, 406, 61, 212, 480, 455,
               78, 309, 318, 84, 474, 209, 225, 177, 356, 227, 263, 181, 476, 478, 151, 494, 395, 23, 114, 395, 429,
               450, 247, 245, 150, 354, 230, 100, 172, 454, 155, 189, 33, 290, 187, 443, 123, 59, 358, 241, 141, 39,
               196, 491, 381, 157, 157, 134, 431, 295, 20, 123, 118, 207, 199, 317, 188, 267, 335, 315, 308, 115, 321,
               56, 52, 253, 492, 97, 374, 398, 272, 74, 206, 109, 172, 471, 55, 452, 452, 329, 367, 372, 252, 99, 62,
               122, 287, 320, 325, 307, 481, 316, 378, 87, 97, 457, 21, 312, 249, 354, 286, 196, 43, 170, 500, 265, 253,
               19, 480, 438, 113, 473, 247, 257, 33, 395, 456, 246, 310, 469, 408, 112, 385, 53, 449, 117, 122, 210,
               286, 149, 20, 364, 372, 71, 26, 155, 292, 16, 72, 384, 160, 79, 241, 346, 230, 15, 427, 96, 95, 59, 151,
               325, 490, 223, 131, 81, 294, 18, 70, 171, 339, 14, 40, 463, 421, 355, 123, 408, 357, 202, 235, 390, 344,
               198, 98, 361, 434, 174, 216, 197, 274, 231, 85, 494, 57, 136, 258, 134, 441, 477, 456, 318, 155, 138,
               461, 65, 426, 162, 90, 342, 284, 374, 204, 464, 9, 280, 391, 491, 231, 298, 284, 82, 417, 355, 356, 207,
               367, 262, 244, 283, 489, 477, 143, 495, 472, 372, 447, 322, 399, 239, 450, 168, 202, 89, 333, 276, 199,
               416, 490, 494, 488, 137, 327, 113, 189, 430, 320, 197, 120, 71, 262, 31, 295, 218, 74, 238, 169, 489,
               308, 300, 260, 397, 308, 328, 267, 419, 84, 357, 486, 289, 312, 230, 64, 468, 227, 268, 28, 243, 267,
               254, 153, 407, 399, 346, 385, 77, 297, 273, 484, 366, 482, 491, 368, 221, 423, 107, 272, 98, 309, 426,
               181, 320, 77, 185, 382, 478, 398, 476, 22, 328, 450, 299, 211, 285, 62, 344, 484, 395, 466, 291, 487,
               301, 407, 28, 295, 36, 429, 99, 462, 240, 124, 261, 387, 30, 362, 161, 156, 184, 188, 99, 377, 392, 442,
               300, 98, 285, 312, 312, 365, 415, 367, 105, 81, 378, 413, 43, 326, 490, 320, 266, 390, 53, 327, 75, 332,
               454, 29, 370, 392, 360, 1, 335, 355, 344, 120, 417, 455, 93, 60, 256, 451, 188, 161, 388, 338, 238, 26,
               275, 340, 109, 185], 334),
              ]
for wiggle_max_length in [wiggle_max_length_dp, wiggle_max_length_greedy]:
    for test_input, expected_output in test_cases:
        assert wiggle_max_length(test_input) == expected_output, wiggle_max_length.__name__
