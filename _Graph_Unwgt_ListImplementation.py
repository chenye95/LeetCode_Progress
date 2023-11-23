from __future__ import annotations

import abc
from collections import defaultdict, deque
from typing import List, Tuple, Generator

from _Graph_Directed_Interface import GRAPH_NODE_TYPE, DirectedGraph


class UnweightedGraph(metaclass=abc.ABCMeta):
    @classmethod
    def construct_unweighted_graph(cls, vertices: List[GRAPH_NODE_TYPE],
                                   edges: List[Tuple[GRAPH_NODE_TYPE, GRAPH_NODE_TYPE]]) -> UnweightedGraph:
        new_graph = cls()
        for vertex in vertices:
            new_graph.add_vertex(vertex)
        for u, v in edges:
            new_graph.add_edge(u, v)
        return new_graph

    def __init__(self):
        self.Edge: defaultdict[GRAPH_NODE_TYPE, set[GRAPH_NODE_TYPE]] = defaultdict(set)
        self.Vertex: set[GRAPH_NODE_TYPE] = set()

    def add_vertex(self, v: GRAPH_NODE_TYPE) -> None:
        """
        :param v: Vertex, needs to be hashable
        """
        self.Vertex.add(v)

    @abc.abstractmethod
    def add_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE, allow_new_vertex: bool = False) -> None:
        pass

    def check_vertex(self, v: GRAPH_NODE_TYPE) -> bool:
        return v in self.Vertex

    @abc.abstractmethod
    def check_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE) -> bool:
        pass

    def vertex_no_self_loop(self, v: GRAPH_NODE_TYPE) -> bool:
        """
        :return: no direct link from v to itself. Doesn't count for cycles of >1 length
        """
        return v in self.Vertex and v not in self.Edge[v]

    def number_vertex(self) -> Tuple[List[GRAPH_NODE_TYPE], dict[GRAPH_NODE_TYPE, int]]:
        """
        Run after all vertices are all added
        Update self.Vertex_list and self.Vertex_map properly
        """
        vertex_list = [v for v in self.Vertex]
        vertex_lookup = {v: i for i, v in enumerate(vertex_list)}
        return vertex_list, vertex_lookup

    def find_path_generator(self, start: GRAPH_NODE_TYPE, end: GRAPH_NODE_TYPE) -> Generator:
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

    @abc.abstractmethod
    def find_path(self, start: GRAPH_NODE_TYPE, end: GRAPH_NODE_TYPE) -> List[List[GRAPH_NODE_TYPE]]:
        """
        Cannot reuse node or path

        :return: list[list[node]] each is a valid path from start to end
        """
        pass

    @abc.abstractmethod
    def cycles(self) -> List[List[GRAPH_NODE_TYPE]]:
        """
        Cannot reuse node or path

        :return: list[list[node]] all cycles in the graph
        """
        pass

    def get_neighbors(self, u: GRAPH_NODE_TYPE) -> set[GRAPH_NODE_TYPE]:
        return self.Edge[u]


class UndirectedUnweightedGraph(UnweightedGraph):
    def add_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE, allow_new_vertex=False) -> None:
        """
        Undirected graph, add both <u, v> and <v, u>
        """
        if not allow_new_vertex:
            assert u in self.Vertex and v in self.Vertex
        else:
            self.Vertex.add(u)
            self.Vertex.add(v)
        self.Edge[u].add(v)
        if u != v:
            self.Edge[v].add(u)

    def find_path(self, start: GRAPH_NODE_TYPE, end: GRAPH_NODE_TYPE) -> List[List[GRAPH_NODE_TYPE]]:
        if start != end:
            return [path for path in self.find_path_generator(start, end)]
        else:
            # filtering out reusing path
            return [path for path in self.find_path_generator(start, end) if len(path) != 3]

    def cycles(self) -> List[List[GRAPH_NODE_TYPE]]:
        return [cycle_v for v in self.Vertex for cycle_v in self.find_path_generator(v, v) if len(cycle_v) != 3]

    def check_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE) -> bool:
        return u in self.Vertex and v in self.Vertex and v in self.Edge[u] and u in self.Edge[v]


class DirectedUnweightedGraph(UnweightedGraph, DirectedGraph):
    def add_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE, allow_new_vertex=False) -> None:
        """
        Directed graph, only <u, v> is added
        """
        if not allow_new_vertex:
            assert u in self.Vertex and v in self.Vertex
        else:
            self.add_vertex(u)
            self.add_vertex(v)
        self.Edge[u].add(v)

    def check_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE) -> bool:
        return u in self.Vertex and v in self.Vertex and v in self.Edge[u]

    def find_path(self, start: GRAPH_NODE_TYPE, end: GRAPH_NODE_TYPE) -> List[List[GRAPH_NODE_TYPE]]:
        return [path for path in self.find_path_generator(start, end)]

    def cycles(self) -> List[List[GRAPH_NODE_TYPE]]:
        return [cycle_v for v in self.Vertex for cycle_v in self.find_path_generator(v, v)]

    def longest_path(self, node_weights: dict[GRAPH_NODE_TYPE, int] = None) -> Tuple[int, List[GRAPH_NODE_TYPE]]:
        """
        return longest path in the graph, where each node is weighted by node_weights[i]
        :param node_weights: non-negative node_weights of each vertex. Set to none if all node has weight of 1.
                            Order follows self.Vertex_list
        :return: a tuple, total weight of the longest path, and one of the longest path if tie exists
        """
        if not node_weights:
            node_weights = {node_i: 1 for node_i in self.Vertex}
        else:
            assert len(node_weights) == len(self.Vertex)

        in_degrees = defaultdict(int)
        for node_src in self.Edge:
            for node_dst in self.Edge[node_src]:
                in_degrees[node_dst] += 1

        exploring_queue = deque(node for node in self.Vertex if node not in in_degrees)
        longest_path_ending_at: dict[GRAPH_NODE_TYPE, Tuple[int, List[GRAPH_NODE_TYPE]]] = {
            node_i: (node_weights[node_i], [node_i])
            for node_i in self.Vertex}
        while exploring_queue:
            current_node = exploring_queue.popleft()
            current_weight, current_path = longest_path_ending_at[current_node]
            for next_node in self.Edge[current_node]:
                next_weight, next_path = longest_path_ending_at[next_node]
                if current_weight + node_weights[next_node] > next_weight:
                    longest_path_ending_at[next_node] = (current_weight + node_weights[next_node],
                                                         current_path + [next_node])
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    exploring_queue.append(next_node)

        return max(longest_path_ending_at.values())
