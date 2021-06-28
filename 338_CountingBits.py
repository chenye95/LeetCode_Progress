"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's
 in the binary representation of i.
"""
from typing import List


def count_bits_dp(n: int) -> List[int]:
    """
    :param n: 0 <= n <= 1e5
    :return: [# of 1 bits in bin(i) for i in range(n + 1)]
    """
    bit_list = [0] * (n + 1)
    for i in range(1, n + 1):
        bit_list[i] = bit_list[i >> 1] + i % 2
    return bit_list


def count_bits_extend(n: int) -> List[int]:
    """
    :param n: 0 <= n <= 1e5
    :return: [# of 1 bits in bin(i) for i in range(n + 1)]
    """
    bit_list = [0]
    while len(bit_list) < n + 1:
        bit_list.extend([i + 1 for i in bit_list])
    return bit_list[:n + 1]


test_cases = [(0, [0]),
              (1, [0, 1]),
              (2, [0, 1, 1]),
              (5, [0, 1, 1, 2, 1, 2]),
              (100,
               [0, 1, 1, 2, 1, 2, 2, 3, 1, 2, 2, 3, 2, 3, 3, 4, 1, 2, 2, 3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 1, 2, 2,
                3, 2, 3, 3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 1, 2, 2, 3, 2, 3,
                3, 4, 2, 3, 3, 4, 3, 4, 4, 5, 2, 3, 3, 4, 3, 4, 4, 5, 3, 4, 4, 5, 4, 5, 5, 6, 2, 3, 3, 4, 3]), ]
for count_bits in [count_bits_dp, count_bits_extend, ]:
    for test_n, expected_output in test_cases:
        assert count_bits(test_n) == expected_output, count_bits.__name__
