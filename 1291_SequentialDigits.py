"""
An integer has sequential digits if and only if each digit in the number is one more than the previous digit.

Return a sorted list of all the integers in the range [low, high] inclusive that have sequential digits.
"""
from string import digits
from typing import List


def sequential_digits(low: int, high: int) -> List[int]:
    """
    :param low: looking for sequential digit integer in range [low, high], 10 <= low <= high <= 10^9
    :param high: looking for sequential digit integer in range [low, high], 10 <= low <= high <= 10^9
    :return: sorted list of all integers that have sequential digits
    """
    low_str, high_str = str(low), str(high)
    low_len, high_len = len(low_str), len(high_str)
    results = []
    if low_len == high_len:  # low_len = high_len
        for start in range(int(low_str[0]), min(int(high_str[0]) + 1, 11 - high_len)):
            if start == int(high_str[0]) or start == int(low_str[0]):
                possibility = ''.join(digits[start: start + high_len])
                if low_str <= possibility <= high_str:
                    results.append(int(possibility))
            else:
                results.append(int(''.join(digits[start: start + high_len])))
    else:
        for start in range(int(low_str[0]), 11 - low_len):
            if start == int(low_str[0]):
                possibility = ''.join(digits[start: start + low_len])
                if possibility >= low_str:
                    results.append(int(possibility))
            else:
                results.append(int(''.join(digits[start: start + low_len])))
        for possibility_len in range(low_len + 1, high_len):
            for start in range(1, 11 - possibility_len):
                results.append(int(''.join(digits[start: start + possibility_len])))
        for start in range(1, min(int(high_str[0]) + 1, 11 - high_len)):
            if start == int(high_str[0]):
                possibility = ''.join(digits[start: start + high_len])
                if possibility <= high_str:
                    results.append(int(possibility))
            else:
                results.append(int(''.join(digits[start: start + high_len])))

    return results


test_cases = [(100, 300, [123, 234]),
              (1000, 13000, [1234, 2345, 3456, 4567, 5678, 6789, 12345]),
              (178546104, 812704742, []),
              (31365477, 514800930, [123456789]), ]
for test_low, test_high, expected_output in test_cases:
    assert sequential_digits(test_low, test_high) == expected_output
