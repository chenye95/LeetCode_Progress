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
            next_color = (current_color + 1) % 2
            for next_node in graph[current_node]:
                if next_node in node_coloring:
                    if node_coloring[next_node] != next_color:
                        return False
                else:
                    uncolored_node.remove(next_node)
                    node_coloring[next_node] = next_color
                    color_stack.append((next_node, next_color))

    return True


assert is_bipartite(graph=[[1, 3], [0, 2], [1, 3], [0, 2]]) is True
assert is_bipartite(graph=[[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]) is False
