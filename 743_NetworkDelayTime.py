"""
You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed
edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a
signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is
impossible for all the n nodes to receive the signal, return -1.
"""
from collections import defaultdict
from heapq import heappop, heappush
from sys import maxsize
from typing import List, Tuple


def network_delay(times: List[Tuple[int, int, int]], n: int, k: int) -> int:
    """
    Dijkstra's algorithm

    :param times: graph of directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node,
        and wi is the time it takes for a signal to travel from source to target.
    :param n: number of nodes in graph, 1 <= n <= 100, nodes are 1 indexed
    :param k: start from node k, 1 <= k <= 100
    :return: times for all n nodes to receive signal, -1 if not possible
    """
    delay = [maxsize for _ in range(1 + n)]
    connection_graph = defaultdict(dict)
    for ui, vi, wi in times:
        connection_graph[ui][vi] = wi

    delay[k] = 0
    heap_queue = [(0, k)]  # current_delay, current_node
    visited = set()

    while heap_queue:
        current_delay, current_node = heappop(heap_queue)
        visited.add(current_node)
        for neighbor_node, path_add in connection_graph[current_node].items():
            if neighbor_node not in visited and delay[neighbor_node] > current_delay + path_add:
                delay[neighbor_node] = current_delay + path_add
                heappush(heap_queue, (current_delay + path_add, neighbor_node))

    return -1 if len(visited) < n else max(delay[1:])


test_cases = [([(1, 2, 1), (2, 3, 7), (1, 3, 4), (2, 1, 2)], 3, 2, 6),
              ([(2, 1, 1), (2, 3, 1), (3, 4, 1)], 4, 2, 2),
              ([(1, 2, 1)], 2, 1, 1),
              ([(1, 2, 1)], 2, 2, -1),
              ([(3, 5, 78), (2, 1, 1), (1, 3, 0), (4, 3, 59), (5, 3, 85), (5, 2, 22), (2, 4, 23), (1, 4, 43),
                (4, 5, 75), (5, 1, 15), (1, 5, 91), (4, 1, 16), (3, 2, 98), (3, 4, 22), (5, 4, 31), (1, 2, 0),
                (2, 5, 4), (4, 2, 51), (3, 1, 36), (2, 3, 59)], 5, 5, 31),
              ([(14, 1, 8), (11, 2, 25), (14, 15, 37), (3, 7, 70), (11, 7, 60), (13, 11, 87), (15, 10, 67),
                (13, 10, 58), (5, 4, 56), (9, 3, 26), (5, 11, 51), (11, 4, 92), (7, 6, 8), (7, 10, 95), (14, 9, 0),
                (4, 13, 1), (7, 9, 89), (3, 14, 24), (11, 15, 30), (13, 2, 91), (15, 8, 60), (1, 4, 96), (8, 2, 71),
                (6, 8, 38), (14, 13, 46), (2, 12, 48), (10, 11, 92), (8, 12, 28), (8, 7, 12), (9, 13, 82), (8, 6, 27),
                (3, 2, 65), (4, 10, 62), (11, 13, 55), (1, 2, 52), (8, 3, 98), (7, 12, 85), (6, 12, 97), (9, 4, 90),
                (2, 4, 23), (9, 11, 20), (1, 14, 61), (8, 9, 77), (6, 5, 80), (14, 11, 33), (9, 8, 54), (13, 1, 42),
                (13, 8, 13), (10, 14, 40), (9, 7, 18), (14, 3, 50), (14, 6, 83), (14, 8, 14), (2, 1, 86), (9, 5, 54),
                (11, 5, 29), (9, 12, 43), (9, 2, 74), (14, 4, 87), (12, 7, 98), (7, 14, 13), (4, 12, 33), (5, 2, 60),
                (15, 11, 33), (8, 4, 99), (9, 6, 98), (4, 6, 57), (6, 11, 5), (9, 15, 37), (1, 3, 30), (9, 10, 60),
                (13, 12, 73), (13, 14, 56), (1, 11, 13), (14, 2, 8), (4, 15, 60), (11, 3, 90), (2, 5, 86), (11, 1, 1),
                (13, 4, 2), (15, 7, 91), (15, 4, 51), (11, 6, 70), (2, 7, 51), (11, 9, 37), (4, 2, 92), (10, 4, 4),
                (7, 2, 30), (13, 9, 79), (8, 15, 41), (11, 8, 18), (15, 2, 4), (12, 14, 88), (12, 6, 9), (12, 9, 44),
                (1, 6, 87), (15, 14, 42), (4, 9, 41), (7, 15, 90), (4, 1, 84), (7, 11, 9), (3, 11, 75), (5, 9, 2),
                (2, 11, 96), (12, 5, 89), (6, 15, 25), (5, 13, 7), (15, 5, 32), (13, 5, 84), (7, 5, 9), (15, 3, 14),
                (12, 13, 4), (5, 3, 73), (6, 9, 85), (6, 10, 29), (1, 8, 24), (12, 3, 85), (4, 3, 60), (1, 13, 6),
                (1, 5, 58), (2, 3, 29), (14, 5, 67), (13, 15, 70), (5, 14, 94), (15, 1, 95), (3, 1, 17), (10, 2, 6),
                (11, 10, 44), (9, 14, 62), (4, 11, 32), (15, 13, 48), (2, 10, 77), (3, 13, 90), (5, 7, 68), (10, 6, 78),
                (3, 6, 95), (10, 12, 68), (13, 6, 73), (10, 1, 8), (10, 7, 18), (10, 5, 64), (5, 1, 55), (13, 7, 90),
                (1, 9, 67), (3, 12, 76), (14, 10, 22), (12, 8, 83), (4, 7, 76), (8, 13, 25), (5, 6, 57), (13, 3, 90),
                (6, 2, 96), (11, 14, 61), (12, 1, 94), (12, 15, 12), (4, 8, 88), (4, 14, 27), (7, 4, 25), (3, 9, 57),
                (2, 15, 90), (1, 12, 85), (12, 11, 44), (5, 10, 13), (5, 12, 96), (14, 7, 24), (14, 12, 98),
                (10, 9, 36), (15, 6, 17), (8, 10, 11), (2, 13, 5), (10, 3, 78), (6, 13, 11), (5, 15, 34), (12, 10, 12),
                (9, 1, 68), (10, 13, 1), (7, 13, 86), (1, 7, 62), (2, 14, 53), (8, 14, 75), (2, 6, 49), (10, 15, 83),
                (7, 8, 88), (6, 1, 87), (8, 1, 38), (8, 11, 73), (3, 15, 1), (3, 8, 93), (2, 8, 26), (4, 5, 26),
                (3, 4, 58), (7, 1, 55), (7, 3, 84), (5, 8, 97), (12, 4, 42), (6, 3, 71), (6, 7, 48), (15, 12, 3),
                (1, 15, 30), (10, 8, 11), (2, 9, 49), (6, 14, 95), (3, 10, 68), (6, 4, 14), (11, 12, 29), (1, 10, 93),
                (8, 5, 55), (12, 2, 86), (3, 5, 26), (15, 9, 12)], 15, 11, 38), ]
for test_network_delay, test_n, test_k, expected_output in test_cases:
    assert network_delay(test_network_delay, test_n, test_k) == expected_output
