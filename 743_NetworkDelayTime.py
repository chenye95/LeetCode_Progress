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
    :param n: number of nodes in graph
    :param k: start from node k
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
                heappush(heap_queue, (delay[neighbor_node], neighbor_node))

    return -1 if len(visited) < n else max(delay[1:])


test_cases = [([(1, 2, 1), (2, 3, 7), (1, 3, 4), (2, 1, 2)], 3, 2, 6),
              ([(2, 1, 1), (2, 3, 1), (3, 4, 1)], 4, 2, 2),
              ([(1, 2, 1)], 2, 1, 1),
              ([(1, 2, 1)], 2, 2, -1),
              (
                  [(3, 5, 78), (2, 1, 1), (1, 3, 0), (4, 3, 59), (5, 3, 85), (5, 2, 22), (2, 4, 23), (1, 4, 43),
                   (4, 5, 75),
                   (5, 1, 15), (1, 5, 91), (4, 1, 16), (3, 2, 98), (3, 4, 22), (5, 4, 31), (1, 2, 0), (2, 5, 4),
                   (4, 2, 51),
                   (3, 1, 36), (2, 3, 59)], 5, 5, 31), ]
for test_network_delay, test_n, test_k, expected_output in test_cases:
    assert network_delay(test_network_delay, test_n, test_k) == expected_output
