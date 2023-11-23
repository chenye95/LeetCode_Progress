from __future__ import annotations

import abc
from collections import defaultdict, deque
from types import GeneratorType
from typing import List, Tuple

from _Graph_Shared import GRAPH_NODE_TYPE, DirectedGraph


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

    def number_vertex(self) -> None:
        """
        Reserved for graphs with 0-indexed int nodes
        Run after all vertices are all added
        Update self.Vertex_list and self.Vertex_map properly
        """
        self.Vertex_list = [v for v in self.Vertex]
        self.Vertex_lookup = {v: i for i, v in enumerate(self.Vertex_list)}
        self.n_nodes = len(self.Vertex)

    def find_path_generator(self, start: GRAPH_NODE_TYPE, end: GRAPH_NODE_TYPE) -> GeneratorType:
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

    def _get_neighbor_by_index(self, u_index: int) -> List[int]:
        """
        Assume self.number_vertex() has been properly called
        :param u_index: index of the node that we are exploring
        :return: index of neighboring nodes of u
        """
        return [self.Vertex_lookup[v] for v in self.Edge[self.Vertex_list[u_index]]]


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
    def __init__(self):
        # Calling into UnweightedGraph.__init__()
        super().__init__()
        # helper properties, used for some algorithms, such as Tarjan's algorithm
        self.Vertex_list: List[GRAPH_NODE_TYPE] = []
        self.Vertex_lookup: dict[GRAPH_NODE_TYPE, int] = {}
        self.n_nodes: int = 0
        self.timer: int = 0

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
            for next_node in self.get_neighbors(current_node):
                next_weight, next_path = longest_path_ending_at[next_node]
                if current_weight + node_weights[next_node] > next_weight:
                    longest_path_ending_at[next_node] = (current_weight + node_weights[next_node],
                                                         current_path + [next_node])
                in_degrees[next_node] -= 1
                if in_degrees[next_node] == 0:
                    exploring_queue.append(next_node)

        return max(longest_path_ending_at.values())

    def strongly_connected_components(self, use_recursive: bool = True,
                                      call_number_vertex: bool = False) -> List[set[GRAPH_NODE_TYPE]]:
        if call_number_vertex:
            self.number_vertex()
        if use_recursive:
            return self._strongly_connected_components_recursive()
        else:
            return self._strongly_connected_components_iterative()

    def _strongly_connected_components_iterative(self) -> List[set[GRAPH_NODE_TYPE]]:
        """
        Using Tarjan's algorithm to find strongly connected components (SCC) of a tree
        See https://leetcode.com/discuss/interview-question/1787518/meta-facebook-recruiting-portal-interview-prep-rabbit-hole
        :return: List of strongly connected components in the tree; vertices in each sub list belongs to the same SCC
        """
        self.timer: int = 0

        # Stores discovery times of visited vertices
        first_explore_time = [-1] * self.n_nodes
        # Earliest visited vertex :the vertex with minimum discovery time) that can be reached from subtree rooted with
        #   current vertex
        back_track_ancestor = [-1] * self.n_nodes
        # Bit array for faster check whether a node is currently on the stack
        is_on_stack = [False] * self.n_nodes

        all_scc_indices: List[List[int]] = []
        # Find subtrees under each unconnected component
        for i in range(self.n_nodes):
            if first_explore_time[i] == -1:
                tmp_connected_ancestors: List[int] = []
                self._scc_iterative_util(i, back_track_ancestor, first_explore_time, is_on_stack,
                                         tmp_connected_ancestors, all_scc_indices)

        return [{self.Vertex_list[node_index] for node_index in scc_indices}
                for scc_indices in all_scc_indices]

    def _scc_iterative_util(self, start_node_index: int, earliest_visited_vertex: List[int],
                            first_explore_time: List[int], is_on_stack: List[bool],
                            connected_ancestor: List[int], return_scc_index_list: List[List[int]]) -> None:
        """
        A recursive function that find finds and prints strongly connected components using DFS traversal
        :param return_scc_index_list: return list of indices for the vertices in each strongly connected component
        :param start_node_index: index of the vertex to be visited
        :param earliest_visited_vertex: earliest visited vertex (the vertex with minimum discovery time) that can be
                reached from subtree rooted with current vertex
        :param first_explore_time: stores discovery times of visited vertices, -1 means hasn't visited yet
        :param is_on_stack: bit/index array for faster check whether a node is in DFS stack
        :param connected_ancestor: store all the indexes connected ancestors (could be part of SCC)
        :return: None! in place modifications of return_scc_index_list
        """
        dfs_stack = [start_node_index]
        while dfs_stack:
            current_node_index = dfs_stack[-1]

            if not is_on_stack[current_node_index]:
                # need to check, since dfs could re-eval nodes that has been marked before
                connected_ancestor.append(current_node_index)
                is_on_stack[current_node_index] = True

            if first_explore_time[current_node_index] == -1:
                # need to check, since dfs could re-eval nodes that has been marked before
                first_explore_time[current_node_index] = self.timer
                earliest_visited_vertex[current_node_index] = self.timer
                self.timer += 1

            for next_node_index in self._get_neighbor_by_index(current_node_index):
                if first_explore_time[next_node_index] == -1 and not is_on_stack[next_node_index]:
                    # has not visited the neighbor node
                    # explore first
                    dfs_stack.append(next_node_index)
                    break
                elif is_on_stack[next_node_index]:
                    earliest_visited_vertex[current_node_index] = min(earliest_visited_vertex[current_node_index],
                                                                      earliest_visited_vertex[next_node_index])

            if dfs_stack[-1] == current_node_index:
                # no neighbor added from current_node_index
                # finished processing, pop from the stack

                if first_explore_time[current_node_index] == earliest_visited_vertex[current_node_index]:
                    # current node is a head node of the SCC
                    current_scc_list = []
                    while is_on_stack[current_node_index]:
                        w = connected_ancestor.pop()
                        earliest_visited_vertex[w] = earliest_visited_vertex[current_node_index]
                        is_on_stack[w] = False
                        current_scc_list.append(w)
                    return_scc_index_list.append(current_scc_list)
                dfs_stack.pop()

    def _strongly_connected_components_recursive(self) -> List[set[GRAPH_NODE_TYPE]]:
        """
        Using Tarjan's algorithm to find strongly connected components (SCC) of a tree
        See https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
        :return: List of strongly connected components in the tree; vertices in each sub list belongs to the same SCC
        """
        self.timer: int = 0

        # Stores discovery times of visited vertices
        first_explore_time = [-1] * self.n_nodes
        # Earliest visited vertex :the vertex with minimum discovery time) that can be reached from subtree rooted with
        #   current vertex
        back_track_ancestor = [-1] * self.n_nodes
        # Bit array for faster check whether a node is currently on the stack
        is_on_stack = [False] * self.n_nodes

        all_scc_indices: List[List[int]] = []
        # Find subtrees under unconnected components
        for i in range(self.n_nodes):
            if first_explore_time[i] == -1:
                tmp_connected_ancestors: List[int] = []
                self._scc_recursive_util(i, back_track_ancestor, first_explore_time, is_on_stack,
                                         tmp_connected_ancestors, all_scc_indices)

        return [{self.Vertex_list[node_index] for node_index in scc_indices}
                for scc_indices in all_scc_indices]

    def _scc_recursive_util(self, current_node_index: int, earliest_visited_vertex: List[int],
                            first_explore_time: List[int], is_on_stack: List[bool],
                            connected_ancestor: List[int], return_scc_index_list: List[List[int]]) -> None:
        """
        A recursive function that find finds and prints strongly connected components using DFS traversal
        :param return_scc_index_list: return list of indices for the vertices in each strongly connected component
        :param current_node_index: index of the vertex to be visited
        :param earliest_visited_vertex: earliest visited vertex (the vertex with minimum discovery time) that can be
                reached from subtree rooted with current vertex
        :param first_explore_time: stores discovery times of visited vertices, -1 means hasn't visited yet
        :param is_on_stack: bit/index array for faster check whether a node is in DFS stack
        :param connected_ancestor: store all the indexes connected ancestors (could be part of SCC)
        :return: None! in place modifications of return_scc_index_list
        """
        # set discovery time and earliest time
        first_explore_time[current_node_index] = self.timer
        earliest_visited_vertex[current_node_index] = self.timer
        self.timer += 1
        is_on_stack[current_node_index] = True
        connected_ancestor.append(current_node_index)

        # Iterate through all vertices adjacent to this node
        for next_node_index in self._get_neighbor_by_index(current_node_index):
            if first_explore_time[next_node_index] == -1:
                # If next_node_index has not been visited yet, then recur for it
                self._scc_recursive_util(next_node_index, earliest_visited_vertex, first_explore_time, is_on_stack,
                                         connected_ancestor, return_scc_index_list)

                # Check if the subtree rooted with next_node_index has a connection to one of the ancestors of
                # current_node_index
                earliest_visited_vertex[current_node_index] = min(earliest_visited_vertex[current_node_index],
                                                                  earliest_visited_vertex[next_node_index])
            elif is_on_stack[next_node_index]:
                # Update earliest_visited_vertex value of current_node_index
                # only if next_node_index is still in stack
                # i.e. it's a back edge, not cross edge
                earliest_visited_vertex[current_node_index] = min(earliest_visited_vertex[current_node_index],
                                                                  earliest_visited_vertex[next_node_index])

        if earliest_visited_vertex[current_node_index] == first_explore_time[current_node_index]:
            # current node is a head node of the SCC
            w = -1
            current_scc_index = []
            while w != current_node_index:
                w = connected_ancestor.pop()
                current_scc_index.append(w)
                is_on_stack[w] = False
            return_scc_index_list.append(current_scc_index)
