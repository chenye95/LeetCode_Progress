from typing import List

from _Graph_Unwgt_ListImplementation import DirectedUnweightedGraph, UndirectedUnweightedGraph, GRAPH_NODE_TYPE

vertices = [1, 2, 3, 4, 5]
edges = [(1, 2), (1, 3), (1, 5), (2, 1), (3, 1), (4, 2), (5, 2)]
dg = DirectedUnweightedGraph()
for i in vertices:
    dg.add_vertex(i)
for u, v in edges:
    dg.add_edge(u, v)
assert all([dg.check_vertex(i) for i in vertices]) and not dg.check_vertex(6)
assert dg.check_edge(4, 2) and not dg.check_edge(2, 4)
assert dg.vertex_no_self_loop(1) and dg.vertex_no_self_loop(2)
dg_cycles = dg.cycles()
assert len(dg_cycles) == 7
assert [1, 2, 1] in dg_cycles and [2, 1, 2] in dg_cycles
assert [1, 3, 1] in dg_cycles and [3, 1, 3] in dg_cycles
assert [1, 5, 2, 1] in dg_cycles and [2, 1, 5, 2] in dg_cycles and [5, 2, 1, 5] in dg_cycles

ug = UndirectedUnweightedGraph()
ug.add_vertex(1)
ug.add_vertex(2)
ug.add_vertex(3)
ug.add_edge(1, 2)
ug.add_edge(2, 2)
ug.add_edge(1, 3)
ug.add_edge(2, 3)
assert ug.check_vertex(1) and ug.check_vertex(2) and ug.check_vertex(3) and not ug.check_vertex(4)
assert ug.check_edge(1, 2) and ug.check_edge(2, 1)
assert ug.vertex_no_self_loop(1) and not ug.vertex_no_self_loop(2)

ug_path = ug.find_path(1, 2)
assert [1, 2] in ug_path and [1, 3, 2] in ug_path and len(ug_path) == 2
ug_path = ug.find_path(2, 1)
assert [2, 1] in ug_path and [2, 3, 1] in ug_path and len(ug_path) == 2
ug_path = ug.find_path(1, 3)
assert [1, 3] in ug_path and [1, 2, 3] in ug_path and len(ug_path) == 2
ug_path = ug.find_path(3, 1)
assert [3, 1] in ug_path and [3, 2, 1] in ug_path and len(ug_path) == 2
ug_path = ug.find_path(2, 3)
assert [2, 3] in ug_path and [2, 1, 3] in ug_path and len(ug_path) == 2
ug_path = ug.find_path(3, 2)
assert [3, 2] in ug_path and [3, 1, 2] in ug_path and len(ug_path) == 2

ug_path = ug.find_path(1, 1)
assert [1, 2, 3, 1] in ug_path and [1, 3, 2, 1] in ug_path and len(ug_path) == 2
ug_path = ug.find_path(2, 2)
assert [2, 2] in ug_path and [2, 3, 1, 2] in ug_path and [2, 1, 3, 2] in ug_path and len(ug_path) == 3
ug_path = ug.find_path(3, 3)
assert [3, 1, 2, 3] in ug_path and [3, 2, 1, 3] in ug_path and len(ug_path) == 2

ug_cycles = ug.cycles()
assert len(ug_cycles) == 7
assert [1, 2, 3, 1] in ug_cycles and [1, 3, 2, 1] in ug_cycles
assert [2, 2] in ug_cycles and [2, 3, 1, 2] in ug_cycles and [2, 1, 3, 2] in ug_cycles
assert [3, 1, 2, 3] in ug_cycles and [3, 2, 1, 3] in ug_cycles

new_graph = DirectedUnweightedGraph.construct_unweighted_graph([0, 1], [(0, 1)])
assert isinstance(new_graph, DirectedUnweightedGraph)
assert (True, [0, 1]) == new_graph.topological_order(), new_graph.topological_order()
new_graph.add_edge(1, 0)
assert not new_graph.topological_order()[0]

new_graph = DirectedUnweightedGraph.construct_unweighted_graph([0, 1, 2, 3], [(0, 1), (0, 2), (1, 3), (2, 3)])
assert isinstance(new_graph, DirectedUnweightedGraph)
assert new_graph.topological_order()[1] in ([0, 1, 2, 3], [0, 2, 1, 3]), new_graph.topological_order()

new_graph = UndirectedUnweightedGraph.construct_unweighted_graph([0, 1], [(0, 1)])
assert isinstance(new_graph, UndirectedUnweightedGraph)
assert 0 in new_graph.Edge[1]

# Tarjan's SCC Algorithm
test_graphs = [
    (5, [(1, 0), (0, 2), (2, 1), (0, 3), (3, 4)],
     [{0, 1, 2}, {3}, {4}]),
    (4, [(0, 1), (1, 2), (2, 3), ],
     [{3}, {2}, {1}, {0}]),
    (7, [(0, 1), (1, 2), (2, 0), (1, 3), (1, 4), (1, 6), (3, 5), (4, 5)], [{5}, {3}, {4}, {6}, {0, 1, 2}]),
    (11, [(0, 1), (0, 3), (1, 2), (1, 4), (2, 0), (2, 6), (3, 2), (4, 5), (4, 6), (5, 6), (5, 7), (5, 8), (5, 9),
          (6, 4), (7, 9), (8, 9), (9, 8)],
     [{8, 9}, {7}, {4, 5, 6}, {0, 1, 2, 3}, {10}]),
    (5, [(0, 1), (1, 2), (2, 3), (2, 4), (3, 0), (4, 2)],
     [{0, 1, 2, 3, 4}]),
]


def conversion_for_comparison(scc_list: List[set[GRAPH_NODE_TYPE]]) -> str:
    tmp_list = [str(sorted(scc_i)) for scc_i in scc_list]
    return str(sorted(tmp_list))


for test_n, test_edge_list, expected_output in test_graphs:
    new_graph = DirectedUnweightedGraph()
    for u in range(test_n):
        new_graph.add_vertex(u)
    for u, v in test_edge_list:
        new_graph.add_edge(u, v)
    get_scc_list = new_graph.strongly_connected_components(use_recursive=False, call_number_vertex=True)
    assert conversion_for_comparison(get_scc_list) == conversion_for_comparison(expected_output)

    new_graph = DirectedUnweightedGraph()
    for u in range(test_n):
        new_graph.add_vertex(u)
    for u, v in test_edge_list:
        new_graph.add_edge(u, v)
    get_scc_list = new_graph.strongly_connected_components(use_recursive=True, call_number_vertex=True)
    assert conversion_for_comparison(get_scc_list) == conversion_for_comparison(expected_output)

# Longest Path in Graph with Weight
test_cases = [
    (3, [(1, 0), (2, 1)], [2, 1, 1], 4),
    (5, [(4, 2), (3, 1), (4, 2), (1, 0), (4, 3), (2, 0)], [1, 1, 1, 1, 1], 4),
    (5, [(4, 2), (3, 1), (4, 2), (1, 0), (4, 3), (2, 0)], None, 4),
    (8, [(3, 2), (2, 1), (5, 4), (7, 6), (5, 2)], [1, 1, 1, 1, 1, 3, 1, 1], 5),
]
for n_nodes, edge_list_duplicate, node_weights, expected_value in test_cases:
    new_graph = DirectedUnweightedGraph()
    for u in range(n_nodes):
        new_graph.add_vertex(u)
    for u, v in edge_list_duplicate:
        new_graph.add_edge(u, v)
    if node_weights:
        get_path_len, get_path_list = new_graph.longest_path({node_i: node_weight_i
                                                              for node_i, node_weight_i in enumerate(node_weights)})
    else:
        get_path_len, get_path_list = new_graph.longest_path()
    assert get_path_len == expected_value
