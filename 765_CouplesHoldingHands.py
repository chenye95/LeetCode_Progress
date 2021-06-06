"""
N couples sit in 2N seats arranged in a row and want to hold hands. We want to know the minimum number of swaps so that
 every couple is sitting side by side. A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1, the couples are numbered in order, the first couple
 being (0, 1), the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person who is initially sitting in the i-th seat.
"""
from copy import deepcopy
from typing import List

from _Union_Find import UnionFindArray


def min_swap_couples_greedy(row: List[int]) -> int:
    """
    At each step, we can make 3 possible moves:
    (1) Move aligned two couples - from (a, b', a', b) to (a, a', b, b')
    (2) Move aligned just one couple - from (a, b', a', c) to (a, a', b', c)
    (3) Move aligned no couple - sub optimal and should not happen with min swap count

    Note Greedy algorithm will execute both (1) and (2) moves

    :param row: 4 <= len(row) <= 60, and row is a permutation of range(len(row))
    :return: minimum number of swaps to make couples (2 * i, 2 * i + 1) sit together
    """

    def swap(person_a: int, person_b: int, i_plus_one: int) -> None:
        """
        Swap seating for person_a and person_b

        :param person_a: original person in seat i_plus_one
        :param person_b: significant other of person in seat i
        :param i_plus_one: old seat for person_a
        """
        row[i_plus_one], row[seat_chart[person_b]], seat_chart[person_a], seat_chart[person_b] = \
            row[seat_chart[person_b]], row[i_plus_one], seat_chart[person_b], i_plus_one

    seat_chart = {person_i: i for i, person_i in enumerate(row)}
    swap_count = 0
    for i in range(0, len(row), 2):
        # couple guaranteed row[i] == row[i + 1] ^ 1
        # (2 * i) ^ 1 = (2 * i + 1)
        # (2 * i + 1) ^ 1 = (2 * i)
        if row[i + 1] != row[i] ^ 1:
            # swap row[i]'s significant other into seat i + 1, so that row[i] and row[i + 1]' will be a couple
            # row[i + 1] will take seat at seat_chart[row[i] ^ 1] instead
            swap(row[i + 1], row[i] ^ 1, i + 1)
            swap_count += 1

    return swap_count


def min_swap_couples_union_find(row: List[int]) -> int:
    """
    * Unify persons sitting in adjacent seats, row[2 * i] and row[2 * i + 1]
    * Unify persons that are couples, 2 * i and 2 * i + 1
    If swaps are needed, there must be some closed cycles where swaps occurred inside the closed cycles

    Now the goal is to compute the minimum number of swaps for each closed cycle then sum them up to get the final
     answer

    Claim 1: For any closed cycle with m persons, we need at most m // 2 - 1 swaps to make all couples in the cycle
        matched
    Proof: For any person, we know whom this person is paired with, so all we need to do it ot just find their partner
        and swap. The worst case is that we need to do thus for m // 2 -1 times, because once we have the first
        m // 2 -1 pairs matched, the last pair is also matched automatically

    Claim 2: For any closed cycle with m persons, we need no less than m // 2 - 1 swaps to make all couple in the cycle
        matched.
    Proof by contradiction: If this was true, then there must be one time when we get two pairs matched with one swap,
        that means there exist two couples which formed a closed cycle among themselves and can be removed from the
        whole closed cycle we start with. This is a contradiction because we start with a cycle that cannot be separate
        further

    Conclusion: with claim 1 and 2: for each cycle, we need exactly m // 2 - 1 swaps to make all couples paired.

    :param row: 4 <= len(row) <= 60, and row is a permutation of range(len(row))
    :return: minimum number of swaps to make couples (2 * i, 2 * i + 1) sit together
    """
    union_find_object = UnionFindArray(len(row))
    for i in range(0, len(row), 2):
        union_find_object.unify(i, i + 1)
        union_find_object.unify(row[i], row[i + 1])

    return sum(size_i // 2 - 1
               for size_i in [union_find_object.component_size(i)
                              for i in range(len(row)) if union_find_object.find(i) == i])


test_cases = [([0, 2, 1, 3], 1),
              ([3, 2, 0, 1], 0),
              ([28, 4, 37, 54, 35, 41, 43, 42, 45, 38, 19, 51, 49, 17, 47, 25, 12, 53, 57, 20, 2, 1, 9, 27, 31, 55, 32,
                48, 59, 15, 14, 8, 3, 7, 58, 23, 10, 52, 22, 30, 6, 21, 24, 16, 46, 5, 33, 56, 18, 50, 39, 34, 29, 36,
                26, 40, 44, 0, 11, 13], 26),
              (list(range(500)), 0),
              ([3, 9, 10, 5, 0, 4, 11, 16, 6, 2, 1, 17, 18, 13, 7, 19, 14, 8, 15, 12], 8),
              ([4, 6, 1, 3, 5, 7, 12, 13, 15, 11, 0, 10, 2, 8, 9, 14], 5), ]
for min_swap_couples in [min_swap_couples_greedy, min_swap_couples_union_find, ]:
    for test_row, expected_count in test_cases:
        assert min_swap_couples(deepcopy(test_row)) == expected_count, min_swap_couples.__name__
