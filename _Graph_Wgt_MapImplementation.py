from __future__ import annotations

from collections import defaultdict
from types import GeneratorType
from typing import List, Tuple, DefaultDict, Dict, Union

from _Union_Find import UnionFind

NODE = Union[str, int]


class WeightedGraph:
    EDGE_NOT_FOUND = -float('inf')

    @classmethod
    def construct_unweighted_graph(cls, vertices: List[NODE], edges: List[Tuple[NODE, NODE, float]]) -> WeightedGraph:
        new_graph = cls()
        for vertex in vertices:
            new_graph.add_vertex(vertex)
        for u, v, weight in edges:
            new_graph.add_edge(u, v, weight)
        return new_graph

    def __init__(self):
        self.Edge: DefaultDict[NODE, Dict[NODE, float]] = defaultdict(dict)
        self.Vertex = set()

    def add_vertex(self, v: NODE) -> None:
        """
        :param v: Vertex, needs to be hashable
        :return:
        """
        self.Vertex.add(v)

    def add_edge(self, u: NODE, v: NODE, weight: float) -> None:
        pass

    def set_edge_weight(self, u: NODE, v: NODE, weight: float) -> None:
        pass

    def check_vertex(self, v: NODE) -> bool:
        return v in self.Vertex

    def check_edge(self, u: NODE, v: NODE) -> bool:
        return u in self.Vertex and v in self.Vertex and v in self.Edge[u]

    def get_edge_weight(self, u: NODE, v: NODE) -> float:
        if u in self.Vertex and v in self.Vertex and v in self.Edge[u]:
            return self.Edge[u][v]
        else:
            return self.EDGE_NOT_FOUND

    def vertex_no_self_loop(self, v: NODE) -> bool:
        return v in self.Vertex and v not in self.Edge[v]

    def find_path_generator(self, start: NODE, end: NODE) -> GeneratorType:
        """
        :param start: Vertex
        :param end: Vertex
        :return: list[list] each list is a valid path from start to end
        Note: no re-visiting nodes allowed in the path.
        Only exception is start == end, i.e finding cycles
        """
        fringe = [(start, [start])]
        while fringe:
            state, path = fringe.pop()
            for next_state in self.Edge[state]:
                if next_state == end and path:
                    yield path + [end]
                    continue
                if next_state in path:
                    continue
                fringe.append((next_state, path + [next_state]))

    def cycles(self) -> List[List[NODE]]:
        """
        Cannot reuse node or path
        :return: list[list[node]]
        """
        pass


class UndirectedWeightedGraph(WeightedGraph):
    def add_edge(self, u: NODE, v: NODE, weight: float) -> None:
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u][v] = weight
        if u != v:
            self.Edge[v][u] = weight

    def set_edge_weight(self, u: NODE, v: NODE, weight: float) -> None:
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u][v] = weight
        if u != v:
            self.Edge[v][u] = weight

    def find_path(self, start: int, end: int) -> List[List[NODE]]:
        if start != end:
            return [path for path in self.find_path_generator(start, end)]
        else:
            # filtering out reusing path
            return [path for path in self.find_path_generator(start, end) if len(path) != 3]

    def cycles(self) -> List[List[NODE]]:
        """
        Cannot reuse node or path
        :return:
        """
        return [cycle_v for v in self.Vertex for cycle_v in self.find_path_generator(v, v) if len(cycle_v) != 3]

    def edge_list(self) -> List[Tuple[NODE, NODE, float]]:
        return [(u, v, self.Edge[u][v]) for u in self.Vertex for v in self.Edge[u] if u <= v]

    def mst_edge_kruskal(self) -> Tuple[float, List[Tuple[NODE, NODE, float]]]:
        """
        Run Kruskal's algorithm to generate one MST from the Undirected Weighted Graph
        please note that MST may not be unique
        :return: list of edges in MST
        """
        total_weight, mst_edges = 0, []
        union_find = UnionFind(list(self.Vertex))
        edge_list = [(self.Edge[u][v], u, v) for u in self.Vertex for v in self.Edge[u] if u < v]
        edge_list.sort()
        for weight, u, v in edge_list:
            if not union_find.is_connected(u, v):
                union_find.unify(u, v)
                mst_edges.append((u, v, weight))
                total_weight += weight
                if union_find.components_count() == 1:
                    break
        return total_weight, mst_edges

    def enforce_mst_kruskal(self) -> float:
        total_weight = 0
        union_find = UnionFind(list(self.Vertex))
        edge_list = [(self.Edge[u][v], u, v) for u in self.Vertex for v in self.Edge[u] if u < v]
        edge_list.sort()
        for weight, u, v in edge_list:
            if union_find.components_count() > 1 and not union_find.is_connected(u, v):
                union_find.unify(u, v)
                total_weight += weight
            else:
                del self.Edge[u][v]
                del self.Edge[v][u]
        return total_weight


class DirectedWeightedGraph(WeightedGraph):
    def add_edge(self, u: NODE, v: NODE, weight: float) -> None:
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u][v] = weight

    def set_edge_weight(self, u: NODE, v: NODE, weight: float) -> None:
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u][v] = weight

    def find_path(self, start: NODE, end: NODE) -> List[List[NODE]]:
        return [path for path in self.find_path_generator(start, end)]

    def cycles(self) -> List[List[NODE]]:
        """
        Cannot reuse node or path
        :return:
        """
        return [cycle_v for v in self.Vertex for cycle_v in self.find_path_generator(v, v)]

    def topological_order(self) -> (bool, List[NODE]):
        """
        :return: a tuple of (bool, list)
            True, list representing topological order of the directed graph, topological order exists
            False, empty list if graph is cyclic
        """
        in_degrees = defaultdict(int)
        for node_src in self.Edge:
            for node_dst in self.Edge[node_src]:
                in_degrees[node_dst] += 1

        zero_in_degree_nodes = [node for node in self.Vertex if node not in in_degrees]
        topological_order_list = []

        while zero_in_degree_nodes:
            node = zero_in_degree_nodes.pop()
            topological_order_list.append(node)
            for neighbor in self.Edge[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    zero_in_degree_nodes.append(neighbor)

        return (True, topological_order_list) if len(topological_order_list) == len(self.Vertex) else (False, [])
