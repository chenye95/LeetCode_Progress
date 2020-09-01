"""
Given a non-empty array of unique positive integers num_list, consider the following graph:
- There are num_list.length nodes, labelled num_list[0] to num_list[num_list.length - 1];
- There is an edge between num_list[i] and num_list[j] if and only if num_list[i] and num_list[j] share a common factor
greater than 1.
Return the size of the largest connected component in the graph.
"""
from collections import defaultdict
from math import sqrt
from typing import Set, List

from _Union_Find import UnionFindArray


def prime_set(n: int) -> Set[int]:
    """
    :return: set of prime factors of integer n
    """
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return prime_set(n // i) | {i}
    return {n}


def largest_component_size(num_list: List[int]) -> int:
    """
    :param num_list: a non-empty array of unique positive integers A
    :return: largest component size in the graph
    """
    union_find = UnionFindArray(len(num_list), use_recursion=True)
    primes_list = defaultdict(list)

    for i, num in enumerate(num_list):
        n_prime_set = prime_set(num)
        for p_n in n_prime_set:
            primes_list[p_n].append(i)

    for _, indexes in primes_list.items():
        for i in range(len(indexes) - 1):
            union_find.unify(indexes[i], indexes[i + 1])

    return max(union_find.component_size(i) for i in range(union_find.size()))


assert largest_component_size([4, 6, 15, 35]) == 4
assert largest_component_size([20, 50, 9, 63]) == 2
assert largest_component_size([2, 3, 6, 7, 4, 12, 21, 39]) == 8
