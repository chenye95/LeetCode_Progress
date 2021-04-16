"""
Given an undirected tree consisting of n vertices numbered from 1 to n. A frog starts jumping from the vertex 1. In one
second, the frog jumps from its current vertex to another unvisited vertex if they are directly connected. The frog can
not jump back to a visited vertex. In case the frog can jump to several vertices it jumps randomly to one of them with
the same probability, otherwise, when the frog can not jump to any unvisited vertex it jumps forever on the same vertex.

The edges of the undirected tree are given in the array edges, where edges[i] = [from_i, to_i] means that exists an edge
connecting directly the vertices from_i and to_i.

Return the probability that after t seconds the frog is on the vertex target.
"""
from typing import List


def frog_position(n: int, edges: List[List[int]], t: int, target: int) -> float:
    """
    :param n: an undirected tree of n vertices numbered 1 to n
    :param edges: undirected edges connecting two vertices from_i and to_i
    :param t: t seconds elapsed
    :param target: target vertex for the frog
    :return: probability that after t seconds the frog is on vertex target
    """
    start_from = 1
    if not edges:
        if target == start_from:
            return 1.0
        else:
            return 0.0
    connected_to = {i: set() for i in range(1, n + 1)}
    for from_i, to_j in edges:
        connected_to[from_i].add(to_j)
        connected_to[to_j].add(from_i)
    visited = {start_from}
    current_step = [(start_from, 1.0)]
    for step in range(t):
        next_step = []
        for current_node, current_prob in current_step:
            available_nodes = connected_to[current_node] - visited
            next_node_prob = current_prob / len(available_nodes) if available_nodes else 0
            for next_node in available_nodes:
                if next_node == target:
                    if not (connected_to[target] - visited) or step == t - 1:
                        return next_node_prob
                    else:
                        return 0
                visited.add(next_node)
                next_step.append((next_node, next_node_prob))
        current_step = next_step
    return 0.0


epsilon = 1e-10
test_cases = [(3, [[2, 1], [3, 2]], 1, 2, 1.0),
              (7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 2, 4, 1.0 / 6),
              (7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 1, 7, 1.0 / 3),
              (7, [[1, 2], [1, 3], [1, 7], [2, 4], [2, 6], [3, 5]], 20, 6, 1.0 / 6),
              (4, [[2, 1], [3, 2], [4, 1]], 4, 1, 0),
              (1, [], 1, 1, 1), ]
for test_n, test_edges, test_t, test_target, expected_output in test_cases:
    assert abs(frog_position(test_n, test_edges, test_t, test_target) - expected_output) < epsilon
