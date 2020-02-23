"""
Given an integer array of digits, return the largest multiple of three that can be formed by concatenating some of the
given digits in any order.

Since the answer may not fit in an integer data type, return the answer as a string.

If there is no answer return an empty string.
"""
from typing import List


def largestMultipleOfThree(digits: List[int]) -> str:
    digits.sort(reverse=True)
    if digits[0] == 0:
        return '0'
    total_sum = sum(digits)
    if total_sum % 3 == 0:
        return ''.join([str(c) for c in digits])

    one_remainder = total_sum % 3
    two_remainder = (one_remainder * 2) % 3
    i = len(digits) - 1
    two_indexes = []
    while i >= 0:
        if digits[i] % 3 == one_remainder:
            digits.pop(i)
            return ''.join([str(c) for c in digits])
        elif digits[i] % 3 == two_remainder and len(two_indexes) < 2:
            two_indexes.append(i)
        i -= 1

    if len(two_indexes) == 2:
        digits.pop(two_indexes[0])
        digits.pop(two_indexes[1])
        return ''.join([str(c) for c in digits])
    else:
        return ''


test_cases = [([0,0,0,0,0,0], '0'),
              ([8,1,9], '981'),
              ([1], ''),
              ([8,6,7,1,0], '8760'),
              ([5,8], ''),
              ([1,1,1,2], '111')]
for input, output in test_cases:
    assert largestMultipleOfThree(input) == output