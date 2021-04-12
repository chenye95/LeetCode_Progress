"""
Given two integers n and k, you need to construct a list which contains n different positive integers ranging from 1 to
 n and obeys the following requirement:

Suppose this list is [a1, a2, a3, ... , an], then the list [|a1 - a2|, |a2 - a3|, |a3 - a4|, ... , |an-1 - an|] has
 exactly k distinct integers.

If there are multiple answers, print any of them.
"""
from collections import Counter
from typing import List


def construct_array(n: int, k: int) -> List[int]:
    """
    :param n: a permutations of 1, ..., n
    :param k: at least k different values for differences between two consecutive terms of the permutation
    :return: any permutation that satisfies the difference rule
    """
    # prefix list with [1, ..., n - k - 1], so that consecutive difference will be 1
    return_list = list(range(1, n - k))

    # use remaining k + 1 numbers [n - k, n - k + 1, n - k + 2, n - k + 3, ..., n] to get k - 1 distinct values
    # on even element, choose from head: n - k + i // 2
    # on odd element, choose from end: n - i // 2
    # i.e. sequence [n - k, n, n - k + 1, n - 1, n - k + 2, n - 2, ... ]
    for i in range(k + 1):
        if i % 2:
            return_list.append(n - i // 2)
        else:
            return_list.append(n - k + i // 2)

    return return_list


def verify_array(got_array: List[int]) -> Counter:
    """
    :param got_array: return values from implementation
    :return: Counter for differences between two consecutive terms of the permutation
    """
    assert len(got_array) > 1
    return Counter([abs(got_array[i] - got_array[i + 1]) for i in range(len(got_array) - 1)])


test_cases = [(3, 1), (3, 2), (92, 80), ]
for test_n, test_k in test_cases:
    difference_count = verify_array(construct_array(test_n, test_k))
    # print(difference_count)
    assert len(difference_count) == test_k
