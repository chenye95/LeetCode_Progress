"""
Given a weighted undirected connected graph with n vertices numbered from 0 to n-1, and an array edges where edges[i] =
 [from_i, to_i, weight_i] represents a bidirectional and weighted edge between nodes from_i and to_i. A minimum spanning
 tree (MST) is a subset of the edges of the graph that connects all vertices without cycles and with the minimum
 possible total edge weight.

Find all the critical and pseudo-critical edges in the minimum spanning tree (MST) of the given graph. An MST edge whose
 deletion from the graph would cause the MST weight to increase is called a critical edge. A pseudo-critical edge, on
  the other hand, is that which can appear in some MSTs but not all.

Note that you can return the indices of the edges in any order.
"""
from collections import defaultdict
from typing import List

from _Union_Find import UnionFindArray


def find_critical_and_pseudo_critical_edges(n: int, edges: List[List[int]]) -> List[List[int]]:
    """
    Progressively add edges, ranked in reverse order of edge weight
    Collapse original union_graph into union_graph of Unions after adding each batch of edges
    Run DFS algorithm to find critical connections in the Union Graph

    :param n: number of nodes in the original union_graph
    :param edges: list of edges in the original Weighted Undirected union_graph
    :return: [edges_critical, edges_pseudos]
    """

    _dfs_not_visited = -1

    def find_critical_connection(current_node: int, level: int = 0, previous_node: int = _dfs_not_visited) -> int:
        """
        Find critical connections in an union graph, among edges out of current_node by searching for cycles.
        Those not part of a cycle will be marked as critical

        :param current_node: finding critical edge out of current_node
        :param level: levels through DFS, used to find cycle
        :param previous_node: used to remember incoming path. Do NOT traverse the edge <previous_node, current_node>
        :return: level of current_node
        """
        levels[current_node] = level
        for child, edge_i in union_graph[current_node]:
            if child == previous_node:
                # do not go back from the incoming path
                continue
            elif levels[child] == _dfs_not_visited:
                levels[current_node] = min(levels[current_node],
                                           find_critical_connection(child, level + 1, current_node))
            else:
                levels[current_node] = min(levels[current_node], levels[child])
            if levels[child] >= level + 1 and edge_i not in edge_pseudos:
                # critical edge in current snapshot, as edge_i connecting current_node to child is not part of a cycle
                # no smaller weight edges has previously connection union_u and union_v
                # critical connection in the current snapshot will also be a critical edge in MST
                edge_critical.add(edge_i)
        return levels[current_node]

    # Initialize critical and pseudo-critical edge set
    edge_critical, edge_pseudos = set(), set()

    # use weight_distribution to break edges into weight classes
    weight_distribution = defaultdict(list)
    for i, (u, v, w) in enumerate(edges):
        weight_distribution[w].append((u, v, i))

    # define union find set
    union_set = UnionFindArray(n, use_recursion=True)

    # iterate through all weights in ascending order
    for weight_class in sorted(weight_distribution):
        # connections_between[(union_u, union_v)] contains all edges connecting union union_u and union_v,
        # where union_u and union_v are the previous_node nodes of their corresponding groups
        connections_between = defaultdict(set)
        # populate connections_between
        for u, v, i in weight_distribution[weight_class]:
            union_u, union_v = union_set.find(u), union_set.find(v)

            if union_u != union_v:
                # Skip the edge that creates cycle and links two already connected graphs
                # otherwise edge edge_i connects union_u and union_v
                connections_between[min(union_u, union_v), max(union_u, union_v)].add(i)

        # w_edges contains all edges of weight_class that we may add to MST
        # i.e. edges in w_edges either belong to edge_critical or edge_pseudos
        w_edges = []
        # construct a snapshot of current graph of Unions to run DFS on
        union_graph = defaultdict(list)
        for union_u, union_v in connections_between:
            # if exists more than 1 edge can connect union_u and union_v, then these edges are pseudo-critical
            if len(connections_between[union_u, union_v]) > 1:
                edge_pseudos |= connections_between[union_u, union_v]

            # Connect union_u and union_v in the Union Graph
            # using one edge only, to avoid cycles
            edge_idx = connections_between[union_u, union_v].pop()
            union_graph[union_u].append((union_v, edge_idx))
            union_graph[union_v].append((union_u, edge_idx))
            w_edges.append((union_u, union_v, edge_idx))
            union_set.unify(union_u, union_v)

        # run find_critical_connection to mark all critical w_edges
        levels = [_dfs_not_visited] * n
        for u, v, i in w_edges:
            if levels[u] == _dfs_not_visited:
                find_critical_connection(u)

        # the edges in w_edges cycles are pseudo-critical
        for u, v, i in w_edges:
            if i not in edge_critical:
                edge_pseudos.add(i)

    return [sorted(list(edge_critical)), sorted(list(edge_pseudos))]


test_cases = [
    (5, [[0, 1, 1], [1, 2, 1], [2, 3, 2], [0, 3, 2], [0, 4, 3], [3, 4, 3], [1, 4, 6]], ([0, 1], [2, 3, 4, 5])),
    (4, [[0, 1, 1], [1, 2, 1], [2, 3, 1], [0, 3, 1]], ([], [0, 1, 2, 3])),
    (6, [[0, 1, 1], [1, 2, 1], [0, 2, 1], [2, 3, 4], [3, 4, 2], [3, 5, 2], [4, 5, 2]], ([3], [0, 1, 2, 4, 5, 6])), ]
for test_n, test_edges, expected_output in test_cases:
    expected_critical, expected_pseudo = expected_output
    got_critical, got_pseudo = find_critical_and_pseudo_critical_edges(test_n, test_edges)
    assert got_critical == expected_critical and got_pseudo == expected_pseudo
