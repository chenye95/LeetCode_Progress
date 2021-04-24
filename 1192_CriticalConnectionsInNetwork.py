"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where
connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly
or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.
"""
from typing import List, Tuple


def critical_connections(n: int, connections: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    Tarjan’s algorithm: find critical connections in a undirected graph with n nodes

    :param n: n nodes
    :param connections: list of connections [(a, b)] such that a and b are connected
    :return: list of critical connections in a graph, (a, b) such that a < b
    """
    graph = [[] for _ in range(n)]  # vertex i ==> [neighbors]
    # lowest_rank[i] initialized to current DFS level.
    # If a loop exists to previously visited node, lowest_rank[i] < current_rank
    lowest_rank = [-1] * n

    # build graph:
    for connection in connections:
        graph[connection[0]].append(connection[1])
        graph[connection[1]].append(connection[0])

    def _dfs(current_level: int, current_node: int, previous_node: int):

        lowest_rank[current_node] = current_level

        for next_neighbor in graph[current_node]:
            if next_neighbor == previous_node:
                continue  # exclude the incoming path to this vertex that was just traversed

            if lowest_rank[next_neighbor] == -1:
                # neighbor hasn't been visited yet
                _dfs(current_level + 1, next_neighbor, current_node)

            lowest_rank[current_node] = min(lowest_rank[current_node], lowest_rank[next_neighbor])
            if lowest_rank[next_neighbor] > current_level:
                # no cycle pointing back to current_node
                if current_node < next_neighbor:
                    return_result.append((current_node, next_neighbor))
                else:
                    return_result.append((next_neighbor, current_node))

    return_result = []
    _dfs(current_level=0, current_node=0, previous_node=-1)
    return return_result


test_cases = [(4, [(0, 1), (1, 2), (2, 0), (1, 3)], {(1, 3), }),
              (6, [(0, 1), (1, 2), (2, 0), (1, 3), (3, 4), (4, 5), (5, 3)], {(1, 3), }), ]
for test_n, test_connections, expected_output in test_cases:
    assert set(critical_connections(test_n, test_connections)) == expected_output
