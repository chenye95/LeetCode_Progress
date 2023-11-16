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
        self.Edge: defaultdict[NODE, set[NODE]] = defaultdict(set)
        self.Vertex: set[NODE] = set()

        # helper properties, used for some algorithms, such as Tarjan's algorithm
        self.Vertex_list: List[NODE] = []
        self.Vertex_lookup: dict[NODE, int] = {}
        self.n_nodes: int = 0

    def add_vertex(self, v: NODE) -> None:
        """
        :param v: Vertex, needs to be hashable
        """
        self.Vertex.add(v)

    def add_edge(self, u: NODE, v: NODE, allow_new_vertex: bool = False) -> None:
        pass

    def check_vertex(self, v: NODE) -> bool:
        return v in self.Vertex

    def check_edge(self, u: NODE, v: NODE) -> bool:
        pass

    def vertex_no_self_loop(self, v: NODE) -> bool:
        """
        :return: no direct link from v to itself. Doesn't count for cycles of >1 length
        """
        return v in self.Vertex and v not in self.Edge[v]

    def number_vertex(self) -> None:
        """
        Run after all vertices are all added
        Update self.Vertex_list and self.Vertex_map properly
        """
        self.Vertex_list = [v for v in self.Vertex]
        self.Vertex_lookup = {v: i for i, v in enumerate(self.Vertex_list)}
        self.n_nodes = len(self.Vertex)

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

    def get_neighbors(self, u: NODE) -> set[NODE]:
        return self.Edge[u]

    def get_neighbor_by_index(self, u_index: int) -> List[int]:
        """
        Assume self.number_vertex() has been properly called
        :param u_index: index of the node that we are exploring
        :return: index of neighboring nodes of u
        """
        return [self.Vertex_lookup[v] for v in self.Edge[self.Vertex_list[u_index]]]


class UndirectedUnweightedGraph(UnweightedGraph):
    def add_edge(self, u: NODE, v: NODE, allow_new_vertex=False) -> None:
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

    def find_path(self, start: NODE, end: NODE) -> List[List[NODE]]:
        if start != end:
            return [path for path in self.find_path_generator(start, end)]
        else:
            # filtering out reusing path
            return [path for path in self.find_path_generator(start, end) if len(path) != 3]

    def cycles(self) -> List[List[NODE]]:
        return [cycle_v for v in self.Vertex for cycle_v in self.find_path_generator(v, v) if len(cycle_v) != 3]

    def check_edge(self, u: NODE, v: NODE) -> bool:
        return u in self.Vertex and v in self.Vertex and v in self.Edge[u] and u in self.Edge[v]


class DirectedUnweightedGraph(UnweightedGraph):
    def __init__(self):
        super().__init__()
        self.timer = None

    def add_edge(self, u: NODE, v: NODE, allow_new_vertex=False) -> None:
        """
        Directed graph, only <u, v> is added
        """
        if not allow_new_vertex:
            assert u in self.Vertex and v in self.Vertex
        else:
            self.add_vertex(u)
            self.add_vertex(v)
        self.Edge[u].add(v)

    def check_edge(self, u: NODE, v: NODE) -> bool:
        return u in self.Vertex and v in self.Vertex and v in self.Edge[u]

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

    def strongly_connected_components(self, use_recursive: bool = True) -> List[set[NODE]]:
        if use_recursive:
            return self._strongly_connected_components_recursive()
        else:
            return self._strongly_connected_components_iterative()

    def _strongly_connected_components_iterative(self) -> List[set[NODE]]:
        """
        Using Tarjan's algorithm to find strongly connected components (SCC) of a tree
        See https://leetcode.com/discuss/interview-question/1787518/meta-facebook-recruiting-portal-interview-prep-rabbit-hole
        :return: List of strongly connected components in the tree; vertices in each sub list belongs to the same SCC
        """
        self.number_vertex()
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

            for next_node_index in self.get_neighbor_by_index(current_node_index):
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

    def _strongly_connected_components_recursive(self) -> List[set[NODE]]:
        """
        Using Tarjan's algorithm to find strongly connected components (SCC) of a tree
        See https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
        :return: List of strongly connected components in the tree; vertices in each sub list belongs to the same SCC
        """
        self.number_vertex()
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
        for next_node_index in self.get_neighbor_by_index(current_node_index):
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
