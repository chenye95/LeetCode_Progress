"""
Starting with a positive integer N, we reorder the digits in any order (including the original order) such that the leading digit is not zero.

Return true if and only if we can do this in a way such that the resulting number is a power of 2.
"""
from itertools import permutations


def reordered_power_of_2_str(n: int) -> bool:
    n_str = sorted(str(n))
    return any(n_str == sorted(str(1 << b)) for b in range(31))


def reordered_power_of_2_permutation(n: int) -> bool:
    return any(candidate[0] != '0' and bin(int(''.join(candidate))).count('1') == 1
               for candidate in permutations(str(n)))


test_cases = [(1, True),
              (10, False),
              (16, True),
              (24, False),
              (46, True), ]
for reordered_power in [reordered_power_of_2_str, reordered_power_of_2_permutation]:
    for test_n, expected_output in test_cases:
        assert reordered_power(test_n) is expected_output
