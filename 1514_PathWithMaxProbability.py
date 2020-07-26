"""
You are given an undirected weighted graph of n nodes (0-indexed), represented by an edge list where edges[i] = [a, b]
is an undirected edge connecting the nodes a and b with a probability of success of traversing that edge succProb[i].

Given two nodes start and end, find the path with the maximum probability of success to go from start to end and return
its success probability.

If there is no path from start to end, return 0. Your answer will be accepted if it differs from the correct answer by
at most 1e-5.
"""
from collections import defaultdict, deque
from typing import List


def max_prob(n: int, edges: List[List[int]], success_prob: List[float], start: int, end: int) -> float:
    """
    In an undirected weighted graph with n nodes, find the path with maximum probability of success traversal to go
    from start to end
    :param n: n nodes in Undirected Weighted Graph
    :param edges: edge[i] = [a, b] connects node a and b
    :param success_prob: success_prob[i] is the weight for edge[i]
    :param start: start node of the path
    :param end: end node of the path
    :return: max success probability traversing from start to end; return 0 if no path exists
    """
    graph = defaultdict(list)
    for i, (a, b) in enumerate(edges):
        graph[a].append((b, i))
        graph[b].append((a, i))

    node_queue = deque([start])
    path_weight = [0.0] * n
    path_weight[start] = 1.0

    while node_queue:
        current_node = node_queue.popleft()
        for neighbor_node, i in graph[current_node]:
            if path_weight[current_node] * success_prob[i] > path_weight[neighbor_node]:
                path_weight[neighbor_node] = path_weight[current_node] * success_prob[i]
                node_queue.append(neighbor_node)

    return path_weight[end]


assert max_prob(n=3, edges=[[0, 1], [1, 2], [0, 2]], success_prob=[0.5, 0.5, 0.2], start=0, end=2) == 0.25
assert max_prob(n=3, edges=[[0, 1], [1, 2], [0, 2]], success_prob=[0.5, 0.5, 0.3], start=0, end=2) == 0.3
assert max_prob(n=3, edges=[[0, 1]], success_prob=[0.5], start=0, end=2) == 0.0
