"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) sub array of A.

Since the answer may be large, return the answer modulo 10^9 + 7.
"""
from typing import List


def sum_sub_array(A: List[int]) -> int:
    """
    :param A: an array of integers
    :return: sum sum of min(B), where B ranges over every (contiguous) sub array of A; result module 10^9+7
    """
    MOD_VALUE = 10 ** 9 + 7

    min_stack = []
    return_value = sum_sub_array_til_j = 0
    for j, a_j in enumerate(A):
        # a_j_min_count records among all sub array [i, j] where i < = j, # of times a_j is the min value
        a_j_min_count = 1

        # process min values for all sub arrays [i, j] where i <= j
        while min_stack and min_stack[-1][0] >= a_j:
            # [k, i] has min value a_i, now [k, j] has min value a_j
            # hasn't been popped yet guaranteed a_o > a_i for i < o < j
            # a_i_min_count such k exists
            a_i, a_i_min_count = min_stack.pop()
            a_j_min_count += a_i_min_count
            sum_sub_array_til_j -= a_i * a_i_min_count

        min_stack.append((a_j, a_j_min_count))
        sum_sub_array_til_j += a_j * a_j_min_count
        return_value += sum_sub_array_til_j

    return return_value % MOD_VALUE


assert sum_sub_array([3, 1, 2, 4]) == 17
assert sum_sub_array([5, 4, 3, 2, 1]) == 35
