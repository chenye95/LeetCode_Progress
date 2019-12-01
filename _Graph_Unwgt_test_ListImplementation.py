from _Graph_Unwgt_ListImplementation import DirectedUnweightedGraph, UndirectedUnweightedGraph

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

new_graph = DirectedUnweightedGraph.construct_unweighted_graph([0, 1, 2, 3], [(0, 1), [0, 2], [1, 3], [2, 3]])
assert isinstance(new_graph, DirectedUnweightedGraph)
assert new_graph.topological_order()[1] in ([0, 1, 2, 3], [0, 2, 1, 3]), new_graph.topological_order()

new_graph = UndirectedUnweightedGraph.construct_unweighted_graph([0, 1], [(0, 1)])
assert isinstance(new_graph, UndirectedUnweightedGraph)
assert 0 in new_graph.Edge[1]