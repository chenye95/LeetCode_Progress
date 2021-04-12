"""
Suppose you have n integers labeled 1 through n. A permutation of those n integers perm (1-indexed) is considered a
 beautiful arrangement if for every i (1 <= i <= n), either of the following is true:
    - perm[i] is divisible by i.
    - i is divisible by perm[i].

Given an integer n, return the number of the beautiful arrangements that you can construct.
"""
from typing import List


def count_arrangement_swap(n: int) -> int:
    """
    Permute through Swap; and aggressively prune after each swaps to ensure lock in values satisfies division rule

    :param n: 1-indexed permutation of n integers 1 <= curr_index <= n
    :return: count of beautiful arrangements with n integers
    """

    def generate_beautiful_permutation(running_permutation: List[int], curr_index: int) -> int:
        """
        Permute through Swap

        :param running_permutation: running_permutation[curr_index - 1:] are locked down and satisfy division rule
        :param curr_index: trying to get value for running_permutation[curr_index]
        :return: number of beautiful count once we lock down running_permutation[curr_index - 1:]
        """
        if curr_index == n:
            # print(running_permutation)
            return 1

        beautiful_count = 0
        for swap_with in range(curr_index, n):
            running_permutation[curr_index], running_permutation[swap_with] = \
                running_permutation[swap_with], running_permutation[curr_index]
            if running_permutation[curr_index] % (curr_index + 1) == 0 or \
                    (curr_index + 1) % running_permutation[curr_index] == 0:
                beautiful_count += generate_beautiful_permutation(running_permutation, curr_index + 1)
            running_permutation[curr_index], running_permutation[swap_with] = \
                running_permutation[swap_with], running_permutation[curr_index]
        return beautiful_count

    return generate_beautiful_permutation(list(range(1, n + 1)), 0)


def count_arrangement_backtrack(n: int) -> int:
    """
    Recurse and back track: attempt to assign integers to each position sequentially

    :param n: 1-indexed permutation of n integers 1 <= curr_index <= n
    :return: count of beautiful arrangements with n integers
    """

    def recurse_position(position: int) -> int:
        """
        :param position: 1-indexed; try to assign an integer 1 <= i <= n to position
        :return: number of beautiful count once we lock down first position - 1 numbers
        """
        if position > n:
            return 1

        beautiful_count = 0
        for i in range(1, n + 1):
            if not visited_list[i] and (position % i == 0 or i % position == 0):
                visited_list[i] = True
                beautiful_count += recurse_position(position + 1)
                visited_list[i] = False
        return beautiful_count

    visited_list = [False] * (n + 1)  # 1 indexed
    return recurse_position(1)


test_cases = [(1, 1), (2, 2), (3, 3), (4, 8), (5, 10), (6, 36), (7, 41), (8, 132), (9, 250), (10, 700), ]
for count_arrangement in [count_arrangement_swap, count_arrangement_backtrack]:
    for test_n, expected_output in test_cases:
        assert count_arrangement(test_n) == expected_output, count_arrangement.__name__
