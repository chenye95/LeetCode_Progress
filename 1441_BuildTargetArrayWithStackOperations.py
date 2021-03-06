"""
Given an array target and an integer n. In each iteration, you will read a number from  list = {1,2,3..., n}.

Build the target array using the following operations:

Push: Read a new element from the beginning list, and push it in the array.
Pop: delete the last element of the array.
If the target array is already built, stop reading more elements.
You are guaranteed that the target array is strictly increasing, only containing numbers between 1 to n inclusive.

Return the operations to build the target array.

You are guaranteed that the answer is unique.
"""
from typing import List


def build_array(target: List[int], n: int) -> List[str]:
    """
    :param target: target array that we want to build
    :param n: target list consists of numbers 1, 2, 3, ..., n
    :return: list of operations of "Push" and "Pop"
    """
    target_i = 0
    i = 1
    return_result = []
    while i <= n and target_i < len(target):
        if i == target[target_i]:
            return_result.append('Push')
            target_i += 1
        else:
            return_result += ['Push', 'Pop']
        i += 1
    return return_result if target_i == len(target) else []


test_cases = [([1, 3], 3, ["Push", "Push", "Pop", "Push"]),
              ([1, 2, 3], 3, ["Push", "Push", "Push"]),
              ([1, 2], 4, ["Push", "Push"]),
              ([2, 3, 4], 4, ["Push", "Pop", "Push", "Push", "Push"]), ]
for test_target, test_n, expected_output in test_cases:
    assert build_array(test_target, test_n) == expected_output
