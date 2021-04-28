"""
You have n gardens, labeled from 1 to n, and an array paths where paths[i] = [xi, yi] describes a bidirectional path
between garden xi to garden yi. In each garden, you want to plant one of 4 types of flowers.

All gardens have at most 3 paths coming into or leaving it.

Your task is to choose a flower type for each garden such that, for any two gardens connected by a path, they have
different types of flowers.

Return any such a choice as an array answer, where answer[i] is the type of flower planted in the (i+1)th garden. The
flower types are denoted 1, 2, 3, or 4. It is guaranteed an answer exists.
"""
from typing import List, Tuple


def garden_no_adjacent(n: int, paths: List[Tuple[int, int]]) -> List[int]:
    """
    Greedily color code each garden sequentially.
    Since each garden is connected to up to 3 gardens, and there are 4 flower patterns, it is guaranteed to have a valid
    color schema

    :param n: 1-indexed n gardens 1 to n
    :param paths: list of (xi, yi) representing a bidirectional path connection garden xi to yi
    :return: any valid coloring of the n gardens using only 1, 2, 3, 4 patterns, such that any two connected garden
        use different patterns
    """
    # Set all gardens to uncolored
    color_pattern = [0] * n
    connection_map = [[] for _ in range(n)]
    for garden_x, garden_y in paths:
        # gardens are 1 indexed
        connection_map[garden_x - 1].append(garden_y - 1)
        connection_map[garden_y - 1].append(garden_x - 1)
    for garden_i in range(n):
        # Avoid colors of adjacent gardens
        color_pattern[garden_i] = ({1, 2, 3, 4} - {color_pattern[garden_j]
                                                   for garden_j in connection_map[garden_i]}).pop()

    return color_pattern


test_cases = [(3, [(1, 2), (2, 3), (3, 1)]),
              (10000, []),
              (8, [(1, 4), (1, 5), (6, 8), (3, 5), (7, 5), (3, 2), (3, 6), (2, 7), (7, 8), (1, 2), (4, 6)]),
              (4, [(1, 2), (3, 4)]),
              (4, [(1, 2), (2, 3), (3, 4), (4, 1), (1, 3), (2, 4)]), ]
for n_garden, connections in test_cases:
    got_color_pattern = garden_no_adjacent(n=n_garden, paths=connections)
    for g_i, g_j in connections:
        assert got_color_pattern[g_i - 1] != got_color_pattern[g_j - 1], connections
