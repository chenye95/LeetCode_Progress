"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B, such that every
 edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j
exists. Each node is an integer between 0 and graph.length - 1. There are no self edges or parallel edges: graph[i] does
not contain i, and it doesn't contain any element twice.
"""
from typing import List


def is_bipartite(graph: List[List[int]]) -> bool:
    """
    :param graph: Connection list representation of the undirected graph
    :return: whether the graph is bipartite
    """
    # set all nodes to either 0 or 1
    node_coloring = {}
    uncolored_node = set(range(len(graph)))

    while uncolored_node:
        start_from = uncolored_node.pop()

        # set start_from to 0
        node_coloring[start_from] = 0
        color_stack = [(start_from, 0)]

        while color_stack:
            current_node, current_color = color_stack.pop()
            next_color = 0 if current_color else 1
            for next_node in graph[current_node]:
                if next_node in node_coloring:
                    if node_coloring[next_node] != next_color:
                        return False
                else:
                    uncolored_node.remove(next_node)
                    node_coloring[next_node] = next_color
                    color_stack.append((next_node, next_color))

    return True


test_cases = [([[1, 3], [0, 2], [1, 3], [0, 2]], True),
              ([[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]], False),
              ([[1, 2], [0], [0], [4], [3], [], [8], [], [6], [10, 11], [9], [9], [14], [], [12], [16, 17], [15], [15],
                [19, 20], [18], [18], [22, 23], [21], [21], [26], [], [24], [28, 29], [27], [27]], True),
              ([[1, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 14, 16, 18, 19], [0, 2, 3, 5, 9, 12, 13, 15, 16, 17, 18],
                [1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 16, 18, 19],
                [0, 1, 2, 4, 5, 6, 7, 8, 11, 12, 13, 15, 16, 17, 18, 19], [0, 2, 3, 5, 7, 8, 9, 12, 13, 15, 17],
                [0, 1, 2, 3, 4, 7, 8, 11, 12, 13, 16, 17, 18], [0, 2, 3, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19],
                [2, 3, 4, 5, 6, 8, 9, 10, 11, 12, 13, 15, 18, 19],
                [0, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 16, 18, 19],
                [0, 1, 2, 4, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 18], [0, 2, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17],
                [0, 2, 3, 5, 6, 7, 8, 9, 12, 13, 15, 16, 17, 19],
                [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 14, 15, 16, 17, 18, 19],
                [0, 1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 16, 17, 18, 19],
                [0, 2, 8, 9, 10, 12, 13, 15, 17, 18, 19], [1, 3, 4, 6, 7, 9, 10, 11, 12, 13, 14, 16, 18, 19],
                [0, 1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 13, 15, 17, 18, 19],
                [1, 3, 4, 5, 6, 9, 10, 11, 12, 13, 14, 16, 18, 19], [0, 1, 2, 3, 5, 6, 7, 8, 9, 12, 13, 14, 15, 16, 17],
                [0, 2, 3, 6, 7, 8, 11, 12, 13, 14, 15, 16, 17]], False), ]
for test_graph, expected_output in test_cases:
    assert is_bipartite(test_graph) is expected_output
