"""
Return all non-negative integers of length N such that the absolute difference between every two consecutive digits is K

Note that every number in the answer must not have leading zeros except for the number 0 itself. For example, 01 has one
 leading zero and is invalid, but 0 is valid.

You may return the answer in any order.
"""
from typing import List


def num_same_consecutive_diff(n: int, k: int) -> List[int]:
    """
    Breadth First Search
    :param n: non-negative integers of length N
    :param k: difference between every two consecutive digits is k
    :return: list of such integers in any order
    """
    if n == 1:
        return list(range(10))

    list_len_i = list(range(1, 10))
    for len_n in range(n - 1):
        next_list_len_n = []
        for num in list_len_i:
            tail_digit = num % 10
            for next_digit in [tail_digit, ] if k == 0 else [tail_digit - k, tail_digit + k]:
                if 0 <= next_digit <= 9:
                    next_list_len_n.append(10 * num + next_digit)
        list_len_i = next_list_len_n

    return list_len_i


assert num_same_consecutive_diff(n=3, k=7) == [181, 292, 707, 818, 929]
assert num_same_consecutive_diff(n=2, k=1) == [10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
