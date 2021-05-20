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
from typing import List, Tuple


def find_the_city_floyd(n: int, edges: List[Tuple[int, int, int]], distance_threshold: int) -> int:
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


def find_the_city_dijkstra(n: int, edges: List[Tuple[int, int, int]], distance_threshold: int) -> int:
    """
    Dijkstra's algorithm with aggressive pruning

    :param n: number of cities
    :param edges: list of ui, vi, wi such that path between ui and vi weighs wi
    :param distance_threshold: maximum distance to be considered a neighbor
    :return: city with the fewest neighbor
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


test_cases = [(4, [(0, 1, 3), (1, 2, 1), (1, 3, 4), (2, 3, 1)], 4, 3),
              (5, [(0, 1, 2), (0, 4, 8), (1, 2, 3), (1, 4, 2), (2, 3, 1), (3, 4, 1)], 2, 0),
              (34, [(3, 8, 6065), (27, 33, 6596), (1, 21, 5037), (24, 27, 7612), (2, 12, 9802), (0, 22, 5578),
                    (7, 30, 8719), (4, 9, 8316), (9, 29, 2750), (13, 18, 477), (32, 33, 2431), (19, 22, 4099),
                    (4, 15, 3624), (8, 26, 9221), (17, 32, 2186), (9, 24, 1848), (2, 16, 3025), (27, 30, 6736),
                    (11, 12, 821), (7, 10, 1626), (0, 30, 8941), (1, 8, 4354), (2, 32, 1753), (17, 26, 3348),
                    (23, 27, 4288), (8, 23, 1095), (21, 22, 9359), (15, 18, 8625), (18, 24, 1287), (2, 31, 1193),
                    (13, 15, 3562), (5, 8, 2841), (4, 22, 8381), (16, 18, 7080), (16, 33, 358), (1, 14, 9673),
                    (28, 29, 6032), (8, 31, 7974), (23, 28, 4649), (16, 29, 3604), (1, 5, 3284), (9, 15, 9799),
                    (20, 29, 8088), (8, 15, 3854), (6, 25, 6971), (9, 31, 7409), (12, 13, 6016), (13, 24, 8921),
                    (4, 33, 3094), (2, 14, 7900), (10, 21, 1192), (4, 10, 4204), (19, 23, 6674), (6, 14, 3300),
                    (24, 29, 136), (20, 24, 8717), (19, 27, 6238), (5, 27, 8427), (25, 28, 7981), (9, 17, 1252),
                    (1, 15, 6615), (10, 27, 8357), (2, 18, 9475), (2, 33, 9579), (4, 26, 6973), (0, 14, 658),
                    (22, 23, 5765), (6, 11, 7512), (3, 19, 105), (12, 19, 3110), (1, 11, 4905), (3, 28, 91),
                    (4, 28, 8861), (10, 30, 1967), (0, 32, 4959), (5, 18, 8397), (3, 15, 5171), (14, 15, 8897),
                    (15, 27, 9372), (4, 32, 9034), (9, 14, 4629), (4, 25, 8612), (27, 29, 6741), (4, 29, 8881),
                    (6, 13, 8485), (6, 10, 6690), (10, 13, 9876), (7, 31, 9521), (8, 33, 5043), (24, 30, 7415),
                    (0, 33, 4947), (7, 27, 2146), (13, 21, 8296), (2, 5, 7278), (5, 15, 9606), (15, 21, 2300),
                    (5, 11, 9012), (5, 22, 2671), (13, 25, 4141), (3, 20, 158), (24, 25, 6950), (7, 15, 9272),
                    (0, 5, 594), (4, 8, 6036), (0, 17, 6896), (3, 24, 6589), (10, 15, 4613), (17, 23, 301),
                    (8, 18, 1483), (18, 19, 1476), (31, 33, 79), (5, 26, 6282), (23, 29, 4406), (7, 9, 7609),
                    (10, 24, 4456), (17, 24, 6106), (8, 13, 7888), (3, 27, 5514), (6, 18, 6365), (25, 26, 7474),
                    (0, 27, 1909), (3, 25, 7926), (8, 14, 5809), (0, 20, 2371), (17, 28, 6803), (20, 23, 2430),
                    (0, 23, 298), (22, 29, 2820), (0, 19, 4264), (15, 25, 6026), (8, 27, 2083), (22, 24, 9660),
                    (1, 20, 4705), (29, 32, 6766), (2, 28, 4226), (11, 18, 8418), (20, 21, 4707), (3, 17, 6894),
                    (2, 27, 4484), (7, 17, 7103), (5, 12, 5504), (25, 30, 7960), (18, 23, 3531), (13, 26, 8051),
                    (2, 6, 6585), (6, 22, 6966), (21, 33, 1498), (3, 22, 1056), (28, 32, 2122), (2, 9, 3378),
                    (16, 27, 2452), (6, 21, 3756), (23, 31, 429), (1, 17, 1692), (11, 30, 4149), (3, 18, 2552),
                    (25, 29, 7861), (16, 26, 1622), (11, 20, 6540), (9, 11, 3071), (13, 20, 50), (12, 18, 1461),
                    (21, 31, 7008), (0, 10, 834), (21, 27, 9005), (12, 16, 3577), (22, 31, 8758), (30, 31, 6913),
                    (18, 22, 5681), (1, 2, 771), (2, 3, 1691), (9, 21, 9058), (4, 23, 6876), (8, 16, 1944),
                    (10, 16, 4348), (10, 29, 4568), (14, 29, 2934), (12, 27, 7860), (16, 30, 782), (0, 8, 3510),
                    (10, 26, 1429), (16, 20, 6386), (1, 9, 2029), (20, 25, 7329), (11, 27, 4821), (28, 31, 8321),
                    (20, 33, 8159), (3, 6, 6441), (2, 19, 1904), (3, 30, 9931), (13, 28, 7852), (0, 4, 1734),
                    (23, 30, 2444), (0, 21, 6331), (6, 26, 3297), (0, 29, 2739), (17, 22, 8532), (9, 23, 4221),
                    (26, 27, 6826), (2, 4, 8794), (6, 7, 4729), (7, 11, 8069), (1, 23, 8926), (3, 7, 3517),
                    (13, 14, 5523), (4, 19, 7963), (10, 14, 1686), (2, 10, 141), (17, 27, 5684), (18, 25, 4384),
                    (1, 12, 925), (8, 11, 8857), (3, 4, 7214), (3, 23, 4913), (7, 32, 1651), (16, 25, 3745),
                    (19, 28, 8324), (1, 25, 4499), (0, 25, 4430), (1, 13, 4037), (5, 28, 6745), (19, 20, 2431),
                    (0, 31, 2134), (9, 12, 4200), (7, 12, 3200), (26, 32, 6681), (14, 17, 9189), (29, 30, 9806),
                    (8, 28, 958), (10, 23, 8730), (6, 9, 9978), (12, 31, 8346), (12, 20, 2439), (25, 33, 6780),
                    (22, 26, 4427), (0, 9, 4585), (5, 25, 7867), (18, 30, 5011), (6, 16, 4376), (13, 29, 8050),
                    (12, 22, 3513), (15, 23, 8172), (13, 23, 6025), (0, 15, 9815), (0, 12, 7710), (11, 16, 3960),
                    (31, 32, 5545), (10, 20, 2887), (8, 10, 9925), (13, 17, 2969), (11, 17, 9512), (13, 31, 7392),
                    (1, 27, 8762), (0, 28, 2449), (0, 18, 953), (14, 19, 8257), (19, 33, 5342), (1, 28, 8659),
                    (3, 31, 2213), (11, 15, 3493), (5, 9, 5167), (15, 33, 8090), (7, 23, 7871), (14, 28, 5408),
                    (2, 8, 1940), (23, 32, 2096), (7, 33, 2296), (4, 13, 4202), (19, 30, 3687), (7, 25, 1443),
                    (11, 19, 8829), (12, 24, 820), (20, 31, 9226), (14, 20, 2820), (21, 24, 1903), (23, 25, 3707),
                    (5, 13, 9229), (6, 30, 3268), (26, 31, 8242), (3, 33, 9300), (9, 32, 5045), (3, 21, 6919),
                    (24, 31, 5369), (15, 20, 70), (8, 20, 329), (19, 32, 5003), (15, 28, 3609), (6, 24, 1386),
                    (3, 26, 3679), (18, 31, 4591), (19, 24, 5589), (9, 33, 4409), (4, 31, 9850), (11, 33, 8494),
                    (0, 26, 6215), (15, 16, 379), (17, 21, 1994), (11, 32, 5405), (6, 12, 5686), (9, 16, 2285),
                    (16, 32, 1858), (30, 33, 4110), (4, 16, 2348), (5, 21, 9405), (3, 29, 673), (14, 23, 5686),
                    (16, 28, 1268), (18, 21, 1505), (12, 17, 1691), (12, 23, 4915), (4, 20, 5195), (6, 29, 4079),
                    (1, 16, 4413), (2, 20, 8678), (8, 32, 816), (22, 33, 5928), (15, 24, 511), (16, 17, 1284),
                    (24, 33, 2278), (5, 32, 6543), (1, 4, 6096), (7, 14, 3966), (10, 28, 1538), (1, 19, 5388),
                    (13, 16, 4484), (12, 26, 131), (0, 24, 8442), (17, 25, 5273), (8, 12, 1839), (18, 29, 5774),
                    (8, 21, 2063), (4, 11, 9932), (26, 33, 4442), (2, 15, 6639), (5, 6, 1493), (9, 27, 9448),
                    (7, 8, 8647), (4, 14, 7792), (5, 29, 9248), (0, 6, 6861), (11, 13, 8778), (1, 6, 6452),
                    (2, 29, 4934), (4, 17, 3595), (26, 28, 4959), (11, 28, 8997), (2, 17, 2182), (12, 33, 884),
                    (27, 31, 9832), (20, 27, 8332), (11, 26, 1801), (4, 27, 2870), (17, 18, 3942), (11, 31, 3523),
                    (26, 29, 7121), (15, 22, 4498), (1, 3, 8945), (19, 25, 328), (22, 28, 4103), (5, 23, 8829),
                    (6, 31, 4439), (7, 16, 8686), (20, 28, 4289), (6, 23, 7754), (12, 30, 2066), (20, 22, 6608),
                    (9, 18, 1700), (6, 8, 6120), (14, 25, 1132), (9, 20, 8917), (12, 25, 5950), (11, 21, 8926),
                    (15, 32, 9102), (26, 30, 8313), (13, 22, 9517), (15, 30, 499), (13, 27, 5049), (22, 25, 7299),
                    (9, 13, 2167), (21, 32, 2553), (8, 9, 1219), (3, 9, 9491), (24, 28, 2326), (14, 16, 3544),
                    (14, 22, 7932), (13, 32, 5497), (27, 28, 5982), (11, 29, 4790), (21, 25, 2618), (0, 2, 2550),
                    (10, 11, 6255), (18, 32, 7205), (6, 19, 6647), (21, 23, 1932), (12, 14, 9847), (1, 26, 2379),
                    (8, 25, 4420), (18, 20, 4839), (19, 21, 9891), (14, 18, 135), (15, 26, 8803), (5, 24, 159),
                    (6, 28, 2173), (9, 25, 6218)], 9207, 33), ]
for find_the_city in [find_the_city_dijkstra, find_the_city_floyd]:
    for test_n, test_edges, test_threshold, expected_output in test_cases:
        assert find_the_city(n=test_n, edges=test_edges, distance_threshold=test_threshold) == expected_output
