"""
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error,
one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss
of another number.
You are given an integer array nums representing the data status of this set after the error.
Find the number that occurs twice and the number that is missing and return them in the form of an array.
"""
from typing import List


def find_error_nums(nums: List[int]) -> List[int]:
    """
    only 1 missing_num from sequence 1, ..., n, 1 duplicate_num

    :param nums: total length of n
    :return: [duplicate_num, missing_num] in that order
    """
    last_saw = 0
    missing_num = duplicate_num = None
    for n_i in sorted(nums):
        if n_i == last_saw:
            duplicate_num = last_saw
            if missing_num is not None:
                break
        elif n_i != last_saw + 1:
            missing_num = last_saw + 1
            if duplicate_num is not None:
                break

        last_saw = n_i

    return [duplicate_num, missing_num] if missing_num is not None else [duplicate_num, len(nums)]


test_cases = [([2, 2], [2, 1]),
              ([1, 2, 2, 4], [2, 3]),
              ([1, 1], [1, 2]),
              ([3, 2, 3, 4, 6, 5], [3, 1]), ]
for test_input, expected_output in test_cases:
    assert find_error_nums(test_input) == expected_output
