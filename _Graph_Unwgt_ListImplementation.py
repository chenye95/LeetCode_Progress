from __future__ import annotations

from collections import defaultdict
from types import GeneratorType
from typing import List, Tuple, Union

NODE = Union[str, int]


class UnweightedGraph:
    @classmethod
    def construct_unweighted_graph(cls, vertices: List[NODE], edges: List[Tuple[NODE, NODE]]) -> UnweightedGraph:
        new_graph = cls()
        for vertex in vertices:
            new_graph.add_vertex(vertex)
        for u, v in edges:
            new_graph.add_edge(u, v)
        return new_graph

    def __init__(self):
        self.Edge = defaultdict(set)
        self.Vertex = set()

    def add_vertex(self, v: NODE) -> None:
        """
        :param v: Vertex, needs to be hashable
        """
        self.Vertex.add(v)

    def add_edge(self, u: NODE, v: NODE) -> None:
        pass

    def check_vertex(self, v: NODE) -> bool:
        return v in self.Vertex

    def check_edge(self, u: NODE, v: NODE) -> bool:
        return u in self.Vertex and v in self.Vertex and v in self.Edge[u]

    def vertex_no_self_loop(self, v: NODE) -> bool:
        """
        :return: no direct link from v to itself. Doesn't count for cycles of >1 length
        """
        return v in self.Vertex and v not in self.Edge[v]

    def find_path_generator(self, start: NODE, end: NODE) -> GeneratorType:
        """
        :return: list[list] each list is a valid path from start to end.
        Note: no re-visiting nodes allowed in the path.
        Only exception is start == end, i.e. finding cycles
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

    def find_path(self, start: NODE, end: NODE) -> List[List[NODE]]:
        """
        Cannot reuse node or path

        :return: list[list[node]] each is a valid path from start to end
        """
        pass

    def cycles(self) -> List[List[NODE]]:
        """
        Cannot reuse node or path

        :return: list[list[node]] all cycles in the graph
        """
        pass


class UndirectedUnweightedGraph(UnweightedGraph):
    def add_edge(self, u: NODE, v: NODE) -> None:
        """
        Undirected graph, add both <u, v> and <v, u>
        """
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u].add(v)
        if u != v:
            self.Edge[v].add(u)

    def find_path(self, start: NODE, end: NODE) -> List[List[NODE]]:
        if start != end:
            return [path for path in self.find_path_generator(start, end)]
        else:
            # filtering out reusing path
            return [path for path in self.find_path_generator(start, end) if len(path) != 3]

    def cycles(self) -> List[List[NODE]]:
        return [cycle_v for v in self.Vertex for cycle_v in self.find_path_generator(v, v) if len(cycle_v) != 3]


class DirectedUnweightedGraph(UnweightedGraph):
    def add_edge(self, u: NODE, v: NODE) -> None:
        """
        Directed graph, only <u, v> is added
        """
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u].add(v)

    def find_path(self, start: NODE, end: NODE) -> List[List[NODE]]:
        return [path for path in self.find_path_generator(start, end)]

    def cycles(self) -> List[List[NODE]]:
        return [cycle_v for v in self.Vertex for cycle_v in self.find_path_generator(v, v)]

    def topological_order(self) -> Tuple[bool, List[NODE]]:
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
