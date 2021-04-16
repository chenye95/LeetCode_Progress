"""
There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and
 city b is connected directly with city c, then city a is connected indirectly with city c.

A province is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly
 connected, and isConnected[i][j] = 0 otherwise.

Return the total number of provinces.
"""
from collections import deque
from typing import List


def find_circle_num(is_connected: List[List[int]]) -> int:
    """
    BFS Algorithm

    :param is_connected: connection matrix of 0 and 1 such that is_connected[i][j] = 1 if i and j are directly connected
    :return: number of connected components
    """
    connected_components = 0
    visited = [False] * len(is_connected)

    for i in range(len(is_connected)):
        if not visited[i]:
            connected_components += 1

            next_visit = deque([i])
            visited[i] = True

            while next_visit:
                next_i = next_visit.popleft()
                for j, c_ij in enumerate(is_connected[next_i]):
                    if c_ij and not visited[j]:
                        visited[j] = True
                        next_visit.append(j)

    return connected_components


test_cases = [([[1, 1, 0], [1, 1, 0], [0, 0, 1]], 2),
              ([[1, 0, 0], [0, 1, 0], [0, 0, 1]], 3),
              ([[1, 0, 0, 1], [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]], 1), ]
for test_connection, expected_output in test_cases:
    assert find_circle_num(test_connection) == expected_output
