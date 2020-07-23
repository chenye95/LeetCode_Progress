"""
Given a directed, acyclic graph of N nodes.  Find all possible paths from node 0 to node N-1, and return them in any
order.

The graph is given as follows:  the nodes are 0, 1, ..., graph.length - 1.  graph[i] is a list of all nodes j for which
the edge (i, j) exists.
"""
from typing import List


def all_paths_source_target(graph: List[List[int]]) -> List[List[int]]:
    """
    :param graph: an acyclic graph, where graph[i] list all directed edge out of node i
    :return: list of all paths from node 0 to node N-1
    """
    target_node = len(graph) - 1
    return_list = []
    running_path = [[0], ]

    while running_path:
        current_path = running_path.pop()
        current_node = current_path[-1]
        for next_node in graph[current_node]:
            if next_node == target_node:
                return_list.append(current_path + [next_node])
            else:
                running_path.append(current_path + [next_node])

    return return_list


assert sorted(all_paths_source_target([[1, 2], [3], [3], []])) == [[0, 1, 3], [0, 2, 3]]
