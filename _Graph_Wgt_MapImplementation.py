from __future__ import annotations

import abc
from abc import ABC
from collections import defaultdict, deque
from types import GeneratorType
from typing import List, Tuple, DefaultDict, Dict

from _Graph_Directed_Interface import GRAPH_NODE_TYPE, DirectedGraph
from _Union_Find import UnionFind


class WeightedGraph(metaclass=abc.ABCMeta):
    EDGE_NOT_FOUND = -float('inf')

    @classmethod
    def construct_weighted_graph(cls, vertices: List[GRAPH_NODE_TYPE],
                                 edges: List[Tuple[GRAPH_NODE_TYPE, GRAPH_NODE_TYPE, float]]) -> WeightedGraph:
        new_graph = cls()
        for vertex in vertices:
            new_graph.add_vertex(vertex)
        for u, v, weight in edges:
            new_graph.add_edge(u, v, weight)
        return new_graph

    def __init__(self):
        self.Edge: DefaultDict[GRAPH_NODE_TYPE, Dict[GRAPH_NODE_TYPE, float]] = defaultdict(dict)
        self.Vertex = set()

    def add_vertex(self, v: GRAPH_NODE_TYPE) -> None:
        """
        :param v: Vertex, needs to be hashable
        """
        self.Vertex.add(v)

    @abc.abstractmethod
    def add_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE, weight: float) -> None:
        pass

    @abc.abstractmethod
    def set_edge_weight(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE, weight: float) -> None:
        pass

    def check_vertex(self, v: GRAPH_NODE_TYPE) -> bool:
        return v in self.Vertex

    def check_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE) -> bool:
        return u in self.Vertex and v in self.Vertex and v in self.Edge[u]

    def get_edge_weight(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE) -> float:
        if u in self.Vertex and v in self.Vertex and v in self.Edge[u]:
            return self.Edge[u][v]
        else:
            return self.EDGE_NOT_FOUND

    def vertex_no_self_loop(self, v: GRAPH_NODE_TYPE) -> bool:
        return v in self.Vertex and v not in self.Edge[v]

    @abc.abstractmethod
    def find_path(self, start: GRAPH_NODE_TYPE, end: GRAPH_NODE_TYPE) -> List[List[GRAPH_NODE_TYPE]]:
        pass

    def find_path_generator(self, start: GRAPH_NODE_TYPE, end: GRAPH_NODE_TYPE) -> GeneratorType:
        """
        :return: list[list] each list is a valid path from start to end
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
    def cycles(self) -> List[List[GRAPH_NODE_TYPE]]:
        """
        Cannot reuse node or path

        :return: list[list[node]] each is a cycle in the graph
        """
        pass

    def bellman_ford(self, start_node: GRAPH_NODE_TYPE, start_node_value: float, path_default_value: float,
                     path_update_function,
                     path_selection_function) -> Dict[GRAPH_NODE_TYPE, float]:
        """
        Implements Bellman Fort algorithm to compute weight path from start_node.
        Supports negative weight in Directed Acyclic Graph

        :param start_node: start node to compute path from
        :param start_node_value: value for path from start_node to start_node
        :param path_default_value: initial value for path start at start_node, as well as default value for unknown path
        :param path_update_function: Callable[[float, float], float], function to include one new edge
        :param path_selection_function: Callable[[float, float], bool] function to choose whether to include a new edge
        :return: path weight for paths from start_node to all nodes in the graph
        """
        node_queue = deque([start_node])
        path_weight: Dict[GRAPH_NODE_TYPE, float] = dict()
        path_weight[start_node] = start_node_value

        while node_queue:
            current_node = node_queue.popleft()
            for neighbor_node in self.Edge[current_node]:
                current_neighbor_path = path_weight.get(neighbor_node, path_default_value)
                update_neighbor_path = path_update_function(self.Edge[current_node][neighbor_node],
                                                            path_weight[current_node])
                if path_selection_function(update_neighbor_path, current_neighbor_path):
                    path_weight[neighbor_node] = update_neighbor_path
                    node_queue.append(neighbor_node)

        return path_weight


class UndirectedWeightedGraph(WeightedGraph):
    def add_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE, weight: float) -> None:
        """
        Undirected graph, both <u, v> and <v, u> are added and set to weight
        """
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u][v] = weight
        if u != v:
            self.Edge[v][u] = weight

    def set_edge_weight(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE, weight: float) -> None:
        """
        Undirected graph, both <u, v> and <v, u> will be updated to weight
        """
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u][v] = weight
        if u != v:
            self.Edge[v][u] = weight

    def find_path(self, start: GRAPH_NODE_TYPE, end: GRAPH_NODE_TYPE) -> List[List[GRAPH_NODE_TYPE]]:
        """
        Cannot reuse node or path
        """
        if start != end:
            return [path for path in self.find_path_generator(start, end)]
        else:
            # filtering out reusing path
            return [path for path in self.find_path_generator(start, end) if len(path) != 3]

    def cycles(self) -> List[List[GRAPH_NODE_TYPE]]:
        return [cycle_v for v in self.Vertex for cycle_v in self.find_path_generator(v, v) if len(cycle_v) != 3]

    def get_edge_list(self, allow_self_loop: bool = True) -> List[Tuple[GRAPH_NODE_TYPE, GRAPH_NODE_TYPE, float]]:
        if allow_self_loop:
            return [(u, v, self.Edge[u][v]) for u in self.Vertex for v in self.Edge[u] if u <= v]
        else:
            return [(u, v, self.Edge[u][v]) for u in self.Vertex for v in self.Edge[u] if u < v]

    def mst_edge_kruskal(self) -> Tuple[float, List[Tuple[GRAPH_NODE_TYPE, GRAPH_NODE_TYPE, float]]]:
        """
        Run Kruskal's algorithm to generate one Minimum Spanning Tree from the Undirected Weighted Graph
        please note that MST may not be unique

        :return: weight of MST and list of edges in MST
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
        """
        remove edges from the tree so that the remaining graph is a Minimum Spanning Tree
        MST found through Kruskal methods
        please note that the result is a MST, not necessarily the unique MST

        :return: weight of MST
        """
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


class DirectedWeightedGraph(WeightedGraph, DirectedGraph):
    def add_edge(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE, weight: float) -> None:
        """
        Directed graph, only add <u, v>
        """
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u][v] = weight

    def set_edge_weight(self, u: GRAPH_NODE_TYPE, v: GRAPH_NODE_TYPE, weight: float) -> None:
        """
        Directed graph, only weight of <u, v> will be updated
        """
        assert u in self.Vertex and v in self.Vertex
        self.Edge[u][v] = weight

    def find_path(self, start: GRAPH_NODE_TYPE, end: GRAPH_NODE_TYPE) -> List[List[GRAPH_NODE_TYPE]]:
        return [path for path in self.find_path_generator(start, end)]

    def cycles(self) -> List[List[GRAPH_NODE_TYPE]]:
        return [cycle_v for v in self.Vertex for cycle_v in self.find_path_generator(v, v)]
