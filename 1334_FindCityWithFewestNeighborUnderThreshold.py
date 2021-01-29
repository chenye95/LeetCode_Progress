"""
There are n cities numbered from 0 to n-1. Given the array edges where edges[i] = [fromi, toi, weighti] represents a
bidirectional and weighted edge between cities fromi and toi, and given the integer distanceThreshold.

Return the city with the smallest number of cities that are reachable through some path and whose distance is at most
distanceThreshold, If there are multiple such cities, return the city with the greatest number.

Notice that the distance of a path connecting cities i and j is equal to the sum of the edges' weights along that path.
"""
from collections import defaultdict
from heapq import heappop, heappush
from sys import maxsize
from typing import List


def find_the_city_floyd(n: int, edges: List[List[int]], distance_threshold: int) -> int:
    """
    Floyd's algorithm to find pair wise distance between all i and j
    :param n: number of cities
    :param edges: list of ui, vi, wi such that path between ui and vi weighs wi
    :param distance_threshold: maximum distance to be considered a neighbor
    :return: city with the fewest neighbor
    """
    pairwise_distance = [[maxsize] * n for _ in range(n)]
    for i, j, wij in edges:
        pairwise_distance[i][j] = pairwise_distance[j][i] = wij
    for i in range(n):
        pairwise_distance[i][i] = 0

    # Floyd's algorithm
    for k in range(n):
        for i in range(n):
            for j in range(n):
                pairwise_distance[i][j] = min(pairwise_distance[i][j],
                                              pairwise_distance[i][k] + pairwise_distance[k][j])

    count_neighbors = {sum(dij <= distance_threshold for dij in pairwise_distance[i]): i for i in range(n)}
    return count_neighbors[min(count_neighbors)]


def find_the_city_dijkstra(n: int, edges: List[List[int]], distance_threshold: int) -> int:
    """
    Dijkstra's algorithm with aggressive pruning
    """
    connection_graph = defaultdict(list)
    for ui, vi, wi in edges:
        if wi <= distance_threshold:
            # filter out connections that is longer than distance_threshold itself
            connection_graph[ui].append((vi, wi))
            connection_graph[vi].append((ui, wi))

    def run_dijkstra(start_node: int, prune_max: int) -> int:
        heap_queue = [(0, start_node)]
        distance_list = [distance_threshold + 1] * n
        distance_list[start_node] = 0

        visited = [False] * n
        city_count = 0  # keep track of cities within distance_threshold reach

        while heap_queue:
            current_distance, current_city = heappop(heap_queue)
            if visited[current_city]:
                continue
            visited[current_city] = True
            city_count += 1
            if city_count > prune_max + 1:
                # Aggressive pruning: don't need to search further if we have exceeded prune_max
                return prune_max + 1

            for neighbor_city, path_distance in connection_graph[current_city]:
                if distance_list[neighbor_city] > current_distance + path_distance:
                    distance_list[neighbor_city] = current_distance + path_distance
                    heappush(heap_queue, (distance_list[neighbor_city], neighbor_city))

        return city_count - 1  # subtract one for start_city

    city_id, fewest_neighbor_count = -1, n + 1
    for i in range(n):
        i_neighbor_count = run_dijkstra(i, fewest_neighbor_count)
        if i_neighbor_count <= fewest_neighbor_count:
            city_id, fewest_neighbor_count = i, i_neighbor_count

    return city_id


for find_the_city in [find_the_city_dijkstra, find_the_city_floyd]:
    assert find_the_city(n=4, edges=[[0, 1, 3], [1, 2, 1], [1, 3, 4], [2, 3, 1]], distance_threshold=4) == 3
    assert find_the_city(n=5, edges=[[0, 1, 2], [0, 4, 8], [1, 2, 3], [1, 4, 2], [2, 3, 1], [3, 4, 1]],
                         distance_threshold=2) == 0
