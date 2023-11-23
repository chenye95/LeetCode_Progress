import operator
from random import randint

from _Graph_Wgt_MapImplementation import DirectedWeightedGraph, UndirectedWeightedGraph

vertices = [1, 2, 3, 4, 5]
edges = [(1, 2), (1, 3), (1, 5), (2, 1), (3, 1), (4, 2), (5, 2)]
dg = DirectedWeightedGraph()
for i in vertices:
    dg.add_vertex(i)
for u, v in edges:
    weight = randint(u, u * 100)
    assert dg.get_edge_weight(u, v) == dg.EDGE_NOT_FOUND
    dg.add_edge(u, v, weight)
    assert dg.get_edge_weight(u, v) == weight
    new_weight = randint(-100 * u, -u)
    dg.set_edge_weight(u, v, new_weight)
    assert dg.get_edge_weight(u, v) == new_weight
assert dg.get_edge_weight(1, 3) != dg.get_edge_weight(3, 1)
assert all([dg.check_vertex(i) for i in vertices]) and not dg.check_vertex(6)
assert dg.check_edge(4, 2) and not dg.check_edge(2, 4)
assert dg.vertex_no_self_loop(1) and dg.vertex_no_self_loop(2)
dg_cycles = dg.cycles()
assert len(dg_cycles) == 7
assert [1, 2, 1] in dg_cycles and [2, 1, 2] in dg_cycles
assert [1, 3, 1] in dg_cycles and [3, 1, 3] in dg_cycles
assert [1, 5, 2, 1] in dg_cycles and [2, 1, 5, 2] in dg_cycles and [5, 2, 1, 5] in dg_cycles

ug = UndirectedWeightedGraph()
ug.add_vertex(1)
ug.add_vertex(2)
ug.add_vertex(3)
ug.add_edge(1, 2, 0)
ug.add_edge(2, 2, 0)
ug.add_edge(1, 3, 0)
ug.add_edge(2, 3, 0)
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

new_graph = DirectedWeightedGraph.construct_weighted_graph([0, 1], [(0, 1, 0)])
assert isinstance(new_graph, DirectedWeightedGraph)
assert (True, [0, 1]) == new_graph.topological_order(), new_graph.topological_order()
new_graph.add_edge(1, 0, 0)
assert not new_graph.topological_order()[0]

new_graph = DirectedWeightedGraph.construct_weighted_graph([0, 1, 2, 3], [(0, 1, 0), (0, 2, 0), (1, 3, 0), (2, 3, 0)])
assert isinstance(new_graph, DirectedWeightedGraph)
assert new_graph.topological_order()[1] in ([0, 1, 2, 3], [0, 2, 1, 3]), new_graph.topological_order()

new_graph = UndirectedWeightedGraph.construct_weighted_graph([0, 1], [(0, 1, 0)])
assert isinstance(new_graph, UndirectedWeightedGraph)
assert 0 in new_graph.Edge[1]

# Kruskal's MST Algorithm
vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
edges = [('I', 'J', 0), ('A', 'E', 1), ('C', 'I', 1), ('E', 'F', 1), ('G', 'H', 1), ('B', 'D', 2), ('C', 'J', 2),
         ('D', 'E', 2), ('D', 'H', 2), ('A', 'D', 4), ('B', 'C', 4), ('C', 'H', 4), ('G', 'I', 4), ('A', 'B', 5),
         ('D', 'F', 5), ('H', 'I', 6), ('F', 'G', 7), ('D', 'G', 11)]
mst_test_tree = UndirectedWeightedGraph.construct_weighted_graph(vertices=vertex, edges=edges)
assert mst_test_tree.cycles()
total_weight, mst_edges = mst_test_tree.mst_edge_kruskal()
assert mst_test_tree.enforce_mst_kruskal() == total_weight
assert set(mst_test_tree.get_edge_list()) == set(mst_edges)

# Bellman Ford Algorithm testing - Undirected Graph max prob
vertex = list(range(3))
max_prob_tree = UndirectedWeightedGraph.construct_weighted_graph(vertices=vertex, edges=[(0, 1, 0.5)])
weight_map = max_prob_tree.bellman_ford(start_node=0, start_node_value=1.0, path_default_value=0,
                                        path_update_function=operator.mul,
                                        path_selection_function=operator.gt)
assert weight_map.get(2, 0.0) == 0.0

max_prob_tree.set_edge_weight(1, 2, 0.5)
max_prob_tree.set_edge_weight(0, 2, 0.2)
weight_map = max_prob_tree.bellman_ford(start_node=0, start_node_value=1.0, path_default_value=0,
                                        path_update_function=operator.mul,
                                        path_selection_function=operator.gt)
assert weight_map.get(2, 0.0) == 0.25

max_prob_tree.set_edge_weight(0, 2, 0.3)
weight_map = max_prob_tree.bellman_ford(start_node=0, start_node_value=1.0, path_default_value=0,
                                        path_update_function=operator.mul,
                                        path_selection_function=operator.gt)
assert weight_map.get(2, 0.0) == 0.3

# Bellman Ford Algorithm testing - Undirected Graph min weight
vertex = ['A', 'B', 'C', 'D', 'E']
min_weight_tree = UndirectedWeightedGraph.construct_weighted_graph(vertices=vertex,
                                                                   edges=[('A', 'B', 1),
                                                                          ('A', 'C', 4),
                                                                          ('B', 'C', 2),
                                                                          ('B', 'D', 2),
                                                                          ('B', 'E', 10),
                                                                          ('E', 'D', 3)])
weight_map = min_weight_tree.bellman_ford(start_node='A', start_node_value=0, path_default_value=float("inf"),
                                          path_update_function=operator.add,
                                          path_selection_function=operator.lt)
path_expected_weight = [0, 1, 3, 3, 6]
for current_node, current_path in zip(vertex, path_expected_weight):
    assert weight_map[current_node] == current_path, current_node

# Bellman Ford Algorithm testing - Directed Graph min weight
vertex = ['A', 'B', 'C', 'D', 'E']
min_weight_tree = DirectedWeightedGraph.construct_weighted_graph(vertices=vertex,
                                                                 edges=[('A', 'B', -1),
                                                                        ('A', 'C', 4),
                                                                        ('B', 'C', 3),
                                                                        ('B', 'D', 2),
                                                                        ('B', 'E', 2),
                                                                        ('D', 'B', 1),
                                                                        ('E', 'D', -3)])
weight_map = min_weight_tree.bellman_ford(start_node='A', start_node_value=0, path_default_value=float("inf"),
                                          path_update_function=operator.add,
                                          path_selection_function=operator.lt)
path_expected_weight = [0, -1, 2, -2, 1]
for current_node, current_path in zip(vertex, path_expected_weight):
    assert weight_map[current_node] == current_path, current_node
