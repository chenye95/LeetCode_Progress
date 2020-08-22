"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.
"""
from typing import List


def sort_array_by_parity(a: List[int]) -> List[int]:
    """
    :param a: array of non-negative integers, half of which are odd, and half even
    :return: a[i] is odd when i is odd; a[i] is even when i is even
    """
    odd_pointer = 1
    for even_pointer in range(0, len(a), 2):
        if a[even_pointer] % 2:
            # need switch to odd positions
            while a[odd_pointer] % 2:
                odd_pointer += 2
            a[odd_pointer], a[even_pointer] = a[even_pointer], a[odd_pointer]
    return a


test_cases = [[4, 2, 5, 7], [4, 2, 5, 7, 6]]
for test_a in test_cases:
    test_output = sort_array_by_parity(test_a)
    for i in range(len(test_output)):
        assert test_output[i] % 2 == i % 2
