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
from typing import List


def network_delay(times: List[List[int]], n: int, k: int) -> int:
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


assert network_delay(times=[[1, 2, 1], [2, 3, 7], [1, 3, 4], [2, 1, 2]], n=3, k=2) == 6
assert network_delay(times=[[2, 1, 1], [2, 3, 1], [3, 4, 1]], n=4, k=2) == 2
assert network_delay(times=[[1, 2, 1]], n=2, k=1) == 1
assert network_delay(times=[[1, 2, 1]], n=2, k=2) == -1
