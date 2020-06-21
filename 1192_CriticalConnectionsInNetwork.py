"""
There are n servers numbered from 0 to n-1 connected by undirected server-to-server connections forming a network where
connections[i] = [a, b] represents a connection between servers a and b. Any server can reach any other server directly
or indirectly through the network.

A critical connection is a connection that, if removed, will make some server unable to reach some other server.

Return all critical connections in the network in any order.
"""
from typing import List


def criticalConnections(n: int, connections: List[List[int]]) -> List[List[int]]:
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
                # lowest_rank never been changed, still equals to -1
                _dfs(current_level+1, next_neighbor, current_node)

            lowest_rank[current_node] = min(lowest_rank[current_node], lowest_rank[next_neighbor])
            if lowest_rank[next_neighbor] >= current_level + 1:
                return_result.append([current_node, next_neighbor])

    return_result = []
    _dfs(current_level=0, current_node=0, previous_node=-1)
    return return_result


assert criticalConnections(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]) == [[1, 3], ]
