"""
You are given an undirected graph. You are given an integer n which is the number of nodes in the graph and an array
 edges, where each edges[i] = [ui, vi] indicates that there is an undirected edge between ui and vi.

A connected trio is a set of three nodes where there is an edge between every pair of them.

The degree of a connected trio is the number of edges where one endpoint is in the trio, and the other is not.

Return the minimum degree of a connected trio in the graph, or -1 if the graph has no connected trios.
"""
from typing import List, Tuple


def min_trio_degree(n: int, edges: List[Tuple[int, int]]) -> int:
    """
    :param n: no. of nodes in graph, 2 <= n <= 400
    :param edges: list of (u_i, v_i); no self loop and no repeated edges; 1 indexed: 1 <= ui, vi <= n
    :return: minimum degree of a connected trio in the graph
    """
    max_degrees = 3 * n
    graph = {i: set() for i in range(1, n + 1)}
    node_degree = {i: 0 for i in range(1, n + 1)}

    for a, b in edges:
        # convert to directed graph, from small node to big node
        graph[min(a, b)].add(max(a, b))
        node_degree[a] += 1
        node_degree[b] += 1

    min_degree = max_degrees
    for node_1 in list(graph):
        for node_2 in graph[node_1]:
            for node_3 in graph[node_1] & graph[node_2]:
                min_degree = min(min_degree, node_degree[node_1] + node_degree[node_2] + node_degree[node_3] - 6)

    return min_degree if min_degree < max_degrees else -1


test_cases = [(6, [(1, 2), (1, 3), (3, 2), (4, 1), (5, 2), (3, 6)], 3),
              (3, [[3, 2], [2, 1]], -1),
              (7, [(1, 3), (4, 1), (4, 3), (2, 5), (5, 6), (6, 7), (7, 5), (2, 6)], 0),
              (6, [[6, 5], [4, 3], [5, 1], [1, 4], [2, 3], [4, 5], [2, 6], [1, 3]], 3),
              (17, [(12, 10), (12, 16), (4, 9), (4, 6), (14, 1), (9, 2), (17, 6), (17, 12), (8, 9), (11, 14), (13, 5),
                    (8, 15), (13, 11), (15, 11), (15, 14), (6, 8), (12, 15), (14, 12), (9, 1), (9, 10), (10, 5),
                    (1, 11), (2, 10), (15, 1), (7, 9), (14, 2), (4, 1), (17, 7), (3, 17), (8, 1), (17, 13), (10, 13),
                    (8, 13), (1, 7), (2, 6), (13, 6), (7, 2), (1, 16), (6, 3), (6, 9), (16, 17), (7, 14)], 7),
              (15,
               [[12, 4], [4, 9], [14, 13], [5, 10], [8, 9], [3, 13], [11, 5], [2, 11], [1, 15], [7, 10], [4, 2], [9, 1],
                [14, 15], [11, 7], [15, 7], [6, 13], [7, 12], [3, 8], [9, 12], [11, 9], [13, 12], [7, 14], [3, 10],
                [13, 5], [15, 2], [1, 3], [14, 3], [14, 12], [5, 9], [9, 7], [13, 7], [6, 1], [15, 13], [12, 8], [3, 5],
                [5, 2], [10, 1], [8, 13], [13, 9], [1, 7], [2, 6], [15, 6], [5, 4], [4, 6], [4, 15], [8, 6], [13, 2],
                [10, 12], [2, 8], [7, 4], [12, 3], [3, 9], [14, 9], [13, 4], [1, 2], [10, 14], [6, 10], [12, 5],
                [14, 2], [14, 11], [8, 1], [8, 10], [11, 6], [11, 15], [2, 12], [6, 12], [15, 8], [6, 5], [4, 14],
                [11, 1], [8, 14], [11, 10], [7, 6], [12, 11], [5, 8], [8, 7], [9, 6], [11, 3], [2, 9], [15, 12]], 21), ]
for test_n, test_graph, expected_degree in test_cases:
    assert min_trio_degree(test_n, test_graph) == expected_degree
