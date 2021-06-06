"""
There is an infrastructure of n cities with some number of roads connecting these cities. Each roads[i] = [ai, bi]
 indicates that there is a bidirectional road between cities ai and bi.

The network rank of two different cities is defined as the total number of directly connected roads to either city. If a
 road is directly connected to both cities, it is only counted once.

The maximal network rank of the infrastructure is the maximum network rank of all pairs of different cities.

Given the integer n and the array roads, return the maximal network rank of the entire infrastructure.
"""
from typing import List, Tuple


def max_network_rank(n: int, roads: List[Tuple[int, int]]) -> int:
    """
    :param n: number of cities, 2 <= n <= 100
    :param roads: list of (ai, bi) bidirectional connections between ai, bi, where 0 <= ai, bi <= n - 1 and ai != bi;
        no repeated roads
    :return: max network rank in the city map
    """
    degree_count = [0] * n
    is_connected = [[False] * n for _ in range(n)]
    for ai, bi in roads:
        degree_count[ai] += 1
        degree_count[bi] += 1
        if ai < bi:
            is_connected[ai][bi] = True
        else:
            is_connected[bi][ai] = True

    return max(degree_count[ai] + degree_bi - ai_bi_connected
               for ai in range(n - 1)
               for degree_bi, ai_bi_connected in zip(degree_count[ai + 1:], is_connected[ai][ai + 1:]))


test_cases = [(2, [(0, 1)], 1),
              (4, [(0, 1), (0, 3), (1, 2), (1, 3)], 4),
              (5, [(0, 1), (0, 3), (1, 2), (1, 3), (2, 3), (2, 4)], 5),
              (8, [(0, 1), (1, 2), (2, 3), (2, 4), (5, 6), (5, 7)], 5),
              (100, [], 0),
              (10, [], 0),
              (13, [(2, 11), (10, 12), (3, 2), (7, 8), (2, 9), (9, 8), (6, 7), (4, 3), (4, 7), (9, 4), (0, 11), (7, 3),
                    (0, 2), (12, 2), (4, 12), (1, 6), (6, 8), (9, 5), (0, 7), (11, 6), (4, 1), (0, 9), (9, 7), (2, 10),
                    (7, 12), (3, 6), (11, 7), (12, 6), (11, 10), (7, 5), (4, 2), (0, 10), (8, 1), (11, 3), (6, 2),
                    (12, 11), (3, 1), (5, 3), (1, 11), (1, 10), (5, 6), (11, 4), (4, 6), (0, 3), (5, 12), (0, 8),
                    (1, 5), (8, 10), (5, 8), (10, 3), (3, 9), (7, 1), (1, 9), (4, 5), (12, 1), (5, 11), (0, 6), (9, 11),
                    (5, 2), (8, 4), (5, 10), (6, 9), (2, 7), (12, 8), (11, 8), (10, 4), (9, 12), (0, 5), (3, 8),
                    (10, 6), (3, 12), (1, 2), (10, 9), (8, 2), (1, 0), (12, 0), (10, 7), (0, 4)], 23), ]
for test_n, test_roads, expected_value in test_cases:
    assert max_network_rank(test_n, test_roads) == expected_value
