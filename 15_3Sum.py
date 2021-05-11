"""
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets
in the array which gives the sum of zero.
"""
from collections import Counter
from functools import reduce
from typing import List, Tuple


def three_sum(nums: List[int]) -> List[Tuple[int, int, int]]:
    """
    :param nums: array of integers, may contain duplicates
    :return: all unique triplets in nums that add up to 0, triplet in sorted order
    """
    if not nums:
        return []

    return_set = set()
    less_than_zero = Counter(filter(lambda x: x < 0, nums))
    more_than_zero = Counter(filter(lambda x: x > 0, nums))
    zero_count = reduce(lambda count, num: count + (num == 0), nums, 0)

    for num_i in set(nums):
        if num_i < 0:
            for num_j in more_than_zero:
                num_k = -num_i - num_j
                if num_k == 0 and zero_count > 0:
                    return_set.add(tuple(sorted((num_i, num_j, 0))))
                elif num_k in more_than_zero and (num_k != num_j or more_than_zero[num_j] >= 2):
                    return_set.add(tuple(sorted((num_i, num_j, num_k))))
                # elif num_k in less_than_zero and (num_k != num_i or less_than_zero[num_i] >= 2):
                #    return_set.add(tuple(sorted((num_i, num_j, num_k))))
                #    Covered when num_i > 0
        elif num_i > 0:
            for num_j in less_than_zero:
                num_k = -num_i - num_j
                if num_k == 0 and zero_count > 0:
                    return_set.add(tuple(sorted((num_i, num_j, 0))))
                elif num_k in less_than_zero and (num_k != num_j or less_than_zero[num_j] >= 2):
                    return_set.add(tuple(sorted((num_i, num_j, num_k))))
                # elif num_k in more_than_zero and (num_k != num_i or more_than_zero[num_i] >= 2):
                #     return_set.add(tuple(sorted((num_i, num_j, num_k))))
                #     Covered when num_i < 0
        elif zero_count >= 3:
            return_set.add((0, 0, 0))

    return list(return_set)


test_cases = [
    ([-4, -2, 1, -5, -4, -4, 4, -2, 0, 4, 0, -2, 3, 1, -5, 0],
     [(-5, 1, 4), (-4, 0, 4), (-4, 1, 3), (-2, -2, 4), (-2, 1, 1), (0, 0, 0)]),
    ([-4, -2, -2, -2, 0, 1, 2, 2, 2, 3, 3, 4, 4, 6, 6],
     [(-4, -2, 6), (-4, 0, 4), (-4, 1, 3), (-4, 2, 2), (-2, -2, 4), (-2, 0, 2)]),
    ([0, 0, 0], [(0, 0, 0)]),
    ([0, 0], []),
    ([-1, 0, 1], [(-1, 0, 1)]),
    ([34, 55, 79, 28, 46, 33, 2, 48, 31, -3, 84, 71, 52, -3, 93, 15, 21, -43, 57, -6, 86, 56, 94, 74, 83, -14, 28, -66,
      46, -49, 62, -11, 43, 65, 77, 12, 47, 61, 26, 1, 13, 29, 55, -82, 76, 26, 15, -29, 36, -29, 10, -70, 69, 17, 49],
     [(-82, -11, 93), (-82, 13, 69), (-82, 17, 65), (-82, 21, 61), (-82, 26, 56), (-82, 33, 49), (-82, 34, 48),
      (-82, 36, 46), (-70, -14, 84), (-70, -6, 76), (-70, 1, 69), (-70, 13, 57), (-70, 15, 55), (-70, 21, 49),
      (-70, 34, 36), (-66, -11, 77), (-66, -3, 69), (-66, 1, 65), (-66, 10, 56), (-66, 17, 49), (-49, -6, 55),
      (-49, -3, 52), (-49, 1, 48), (-49, 2, 47), (-49, 13, 36), (-49, 15, 34), (-49, 21, 28), (-43, -14, 57),
      (-43, -6, 49), (-43, -3, 46), (-43, 10, 33), (-43, 12, 31), (-43, 15, 28), (-43, 17, 26), (-29, -14, 43),
      (-29, 1, 28), (-29, 12, 17), (-14, -3, 17), (-14, 1, 13), (-14, 2, 12), (-11, -6, 17), (-11, 1, 10), (-3, 1, 2)]),
]
for test_input, expected_output in test_cases:
    assert sorted(three_sum(test_input)) == sorted(expected_output)
