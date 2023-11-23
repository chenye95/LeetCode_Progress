import abc
from collections import defaultdict, deque
from typing import Union, List, Tuple, Optional

GRAPH_NODE_TYPE = Union[str, int]


class DirectedGraph(metaclass=abc.ABCMeta):
    def __init__(self):
        # place-holder declaration;
        # not used for instantiation
        self.Edge = None
        self.Vertex = None

    @abc.abstractmethod
    def number_vertex(self) -> Tuple[List[GRAPH_NODE_TYPE], dict[GRAPH_NODE_TYPE, int]]:
        pass

    def topological_order(self) -> Tuple[bool, List[GRAPH_NODE_TYPE]]:
        """
        :return: a tuple of (bool, list)
            True, list representing topological order of the directed graph, topological order exists
            False, empty list if graph is cyclic
        """
        in_degrees = defaultdict(int)
        for node_src in self.Edge:
            for node_dst in self.Edge[node_src]:
                in_degrees[node_dst] += 1

        exploring_queue = deque([node for node in self.Vertex if node not in in_degrees])
        topological_order_list = []

        while exploring_queue:
            node = exploring_queue.popleft()
            topological_order_list.append(node)
            for neighbor in self.Edge[node]:
                in_degrees[neighbor] -= 1
                if in_degrees[neighbor] == 0:
                    exploring_queue.append(neighbor)

        return (True, topological_order_list) if len(topological_order_list) == len(self.Vertex) else (False, [])

    def strongly_connected_components(self, use_recursive: bool = True,
                                      convert_to_list: bool = False,
                                      vertex_lookup: Optional[dict[GRAPH_NODE_TYPE, int]] = None,
                                      vertex_list: Optional[list[GRAPH_NODE_TYPE]] = None) -> List[
        set[GRAPH_NODE_TYPE]]:
        """
        :param use_recursive: set to False, with large number of nodes
        :param convert_to_list: set to True, with large number of nodes, and node is not zero_indexed
        :param vertex_lookup: useful only when convert_to_list is set to True; use for pre-computation;
            dictionary to look up node to its position in the list
        :param vertex_list: useful only when convert_to_list is set to True; use for pre-computation;
            list of graph nodes
        :return:
        """
        if convert_to_list:
            if use_recursive:
                return self._strongly_connected_components_recursive_with_list()
            else:
                return self._strongly_connected_components_iterative_with_list(vertex_lookup, vertex_list)
        else:
            if use_recursive:
                return self._strongly_connected_components_recursive_with_map()
            else:
                return self._strongly_connected_components_iterative_with_map()

    def _get_neighbor_by_index(self, u_index: int,
                               vertex_lookup: dict[GRAPH_NODE_TYPE, int],
                               vertex_list: list[GRAPH_NODE_TYPE]) -> List[int]:
        """
        :param u_index: index of the node that we are exploring
        :param vertex_list: list of graph nodes
        :param vertex_lookup: dictionary to look up node to its position in the list
        :return: index of neighboring nodes of u
        """
        return [vertex_lookup[v] for v in self.Edge[vertex_list[u_index]]]

    def _strongly_connected_components_iterative_with_list(self,
                                                           vertex_lookup: Optional[dict[GRAPH_NODE_TYPE, int]] = None,
                                                           vertex_list: Optional[list[GRAPH_NODE_TYPE]] = None) \
            -> List[set[GRAPH_NODE_TYPE]]:
        """
        Using Tarjan's algorithm to find strongly connected components (SCC) of a tree
        See https://leetcode.com/discuss/interview-question/1787518/meta-facebook-recruiting-portal-interview-prep-rabbit-hole
        :param vertex_lookup: use for pre-computation; dictionary to look up node to its position in the list
        :param vertex_list: use for pre-computation; list of graph nodes
        :return: List of strongly connected components in the tree; vertices in each sub list belongs to the same SCC
        """

        def _scc_iterative_util(start_node_index: int,
                                connected_ancestor: List[int], return_scc_index_list: List[List[int]],
                                timer: int) -> int:
            """
            A recursive function that find finds and prints strongly connected components using DFS traversal
            :param return_scc_index_list: return list of indices for the vertices in each strongly connected component
            :param start_node_index: index of the vertex to be visited
            :param connected_ancestor: store all the indexes connected ancestors (could be part of SCC)
            :param timer: counter for steps
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
                    first_explore_time[current_node_index] = timer
                    earliest_visited_vertex[current_node_index] = timer
                    timer += 1

                for next_node_index in self._get_neighbor_by_index(current_node_index, vertex_lookup,
                                                                   vertex_list):
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
            return timer

        current_timer: int = 0
        if vertex_list is None or vertex_lookup is None:
            vertex_list, vertex_lookup = self.number_vertex()
        n_nodes = len(vertex_list)

        # Stores discovery times of visited vertices
        first_explore_time = [-1] * n_nodes
        # Earliest visited vertex (the vertex with minimum discovery time) that can be reached from subtree rooted with
        #   current vertex
        earliest_visited_vertex = [-1] * n_nodes
        # Bit array for faster check whether a node is currently on the stack
        is_on_stack = [False] * n_nodes

        all_scc_indices: List[List[int]] = []
        # Find subtrees under each unconnected component
        for i in range(n_nodes):
            if first_explore_time[i] == -1:
                tmp_connected_ancestors: List[int] = []
                current_timer = _scc_iterative_util(i, tmp_connected_ancestors, all_scc_indices, current_timer)

        return [{vertex_list[node_index] for node_index in scc_indices}
                for scc_indices in all_scc_indices]

    def _strongly_connected_components_recursive_with_list(self,
                                                           vertex_lookup: Optional[dict[GRAPH_NODE_TYPE, int]] = None,
                                                           vertex_list: Optional[list[GRAPH_NODE_TYPE]] = None) \
            -> List[set[GRAPH_NODE_TYPE]]:
        """
        Using Tarjan's algorithm to find strongly connected components (SCC) of a tree
        See https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
        :param vertex_lookup: use for pre-computation; dictionary to look up node to its position in the list
        :param vertex_list: use for pre-computation; list of graph nodes
        :return: List of strongly connected components in the tree; vertices in each sub list belongs to the same SCC
        """

        def _scc_recursive_util(current_node_index: int,
                                connected_ancestor: List[int], return_scc_index_list: List[List[int]],
                                timer: int) -> int:
            """
            A recursive function that find finds and prints strongly connected components using DFS traversal
            :param return_scc_index_list: return list of indices for the vertices in each strongly connected component
            :param current_node_index: index of the vertex to be visited
            :param connected_ancestor: store all the indexes connected ancestors (could be part of SCC)
            :param timer: counter to keep track of vist order
            :return: updated timer
            """
            # set discovery time and earliest time
            first_explore_time[current_node_index] = timer
            earliest_visited_vertex[current_node_index] = timer
            timer += 1
            is_on_stack[current_node_index] = True
            connected_ancestor.append(current_node_index)

            # Iterate through all vertices adjacent to this node
            for next_node_index in self._get_neighbor_by_index(current_node_index, vertex_lookup, vertex_list):
                if first_explore_time[next_node_index] == -1:
                    # If next_node_index has not been visited yet, then recur for it
                    timer = _scc_recursive_util(next_node_index, connected_ancestor, return_scc_index_list, timer)

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

            return timer

        current_timer: int = 0
        if vertex_list is None or vertex_lookup is None:
            vertex_list, vertex_lookup = self.number_vertex()
        n_nodes = len(vertex_list)

        # Stores discovery times of visited vertices
        first_explore_time = [-1] * n_nodes
        # Earliest visited vertex (the vertex with minimum discovery time) that can be reached from subtree rooted with
        #   current vertex
        earliest_visited_vertex = [-1] * n_nodes
        # Bit array for faster check whether a node is currently on the stack
        is_on_stack = [False] * n_nodes

        all_scc_indices: List[List[int]] = []
        # Find subtrees under unconnected components
        for i in range(n_nodes):
            if first_explore_time[i] == -1:
                tmp_connected_ancestors: List[int] = []
                current_timer = _scc_recursive_util(i, tmp_connected_ancestors, all_scc_indices, current_timer)

        return [{vertex_list[node_index] for node_index in scc_indices}
                for scc_indices in all_scc_indices]

    def _strongly_connected_components_iterative_with_map(self) -> List[set[GRAPH_NODE_TYPE]]:
        """
        Using Tarjan's algorithm to find strongly connected components (SCC) of a tree
        See https://leetcode.com/discuss/interview-question/1787518/meta-facebook-recruiting-portal-interview-prep-rabbit-hole
        :return: List of strongly connected components in the tree; vertices in each sub list belongs to the same SCC
        """

        def _scc_iterative_util(start_node: GRAPH_NODE_TYPE,
                                connected_ancestor: List[GRAPH_NODE_TYPE],
                                timer: int) -> int:
            """
            A recursive function that find finds and prints strongly connected components using DFS traversal
            :param start_node: index of the vertex to be visited
            :param connected_ancestor: store all the connected ancestors (could be part of SCC)
            :param timer: counter for steps
            :return: None! in place modifications of return_scc_list
            """
            dfs_stack: list[GRAPH_NODE_TYPE] = [start_node]
            while dfs_stack:
                exploring_node = dfs_stack[-1]

                if not is_on_stack[exploring_node]:
                    # need to check, since dfs could re-eval nodes that has been marked before
                    connected_ancestor.append(exploring_node)
                    is_on_stack[exploring_node] = True

                if exploring_node not in first_explore_time:
                    # need to check, since dfs could re-eval nodes that has been marked before
                    first_explore_time[exploring_node] = timer
                    earliest_visited_vertex[exploring_node] = timer
                    timer += 1

                for next_node in self.Edge[exploring_node]:
                    if next_node not in first_explore_time and not is_on_stack[next_node]:
                        # has not visited the neighbor node
                        # explore first
                        dfs_stack.append(next_node)
                        break
                    elif is_on_stack[next_node]:
                        earliest_visited_vertex[exploring_node] = min(earliest_visited_vertex[exploring_node],
                                                                      earliest_visited_vertex[next_node])

                if dfs_stack[-1] == exploring_node:
                    # no neighbor added from exploring_node
                    # finished processing, pop from the stack

                    if first_explore_time[exploring_node] == earliest_visited_vertex[exploring_node]:
                        # current node is a head node of the SCC
                        current_scc = set()
                        while is_on_stack[exploring_node]:
                            w = connected_ancestor.pop()
                            earliest_visited_vertex[w] = earliest_visited_vertex[exploring_node]
                            is_on_stack[w] = False
                            current_scc.add(w)
                        all_scc_list.append(current_scc)
                    dfs_stack.pop()
            return timer

        current_timer: int = 0

        # Stores discovery times of visited vertices
        first_explore_time: dict[GRAPH_NODE_TYPE, int] = {}
        # Earliest visited vertex (the vertex with minimum discovery time) that can be reached from subtree rooted with
        #   current vertex
        earliest_visited_vertex: dict[GRAPH_NODE_TYPE, int] = {}
        # Bit array for faster check whether a node is currently on the stack
        is_on_stack: dict[GRAPH_NODE_TYPE, bool] = {node: False for node in self.Vertex}

        all_scc_list: List[set[GRAPH_NODE_TYPE]] = []
        # Find subtrees under each unconnected component
        for current_node in self.Vertex:
            if current_node not in first_explore_time:
                tmp_connected_ancestors: List[int] = []
                current_timer = _scc_iterative_util(current_node, tmp_connected_ancestors, current_timer)

        return all_scc_list

    def _strongly_connected_components_recursive_with_map(self) -> List[set[GRAPH_NODE_TYPE]]:
        """
        Using Tarjan's algorithm to find strongly connected components (SCC) of a tree
        See https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
        :return: List of strongly connected components in the tree; vertices in each sub list belongs to the same SCC
        """

        def _scc_recursive_util(exploring_node: int, connected_ancestor: List[int], timer: int) -> int:
            """
            A recursive function that find finds and prints strongly connected components using DFS traversal
            :param exploring_node: index of the vertex to be visited
            :param connected_ancestor: store all the indexes connected ancestors (could be part of SCC)
            :param timer: counter to keep track of vist order
            :return: updated timer
            """
            # set discovery time and earliest time
            first_explore_time[exploring_node] = timer
            earliest_visited_vertex[exploring_node] = timer
            timer += 1
            is_on_stack[exploring_node] = True
            connected_ancestor.append(exploring_node)

            # Iterate through all vertices adjacent to this node
            for next_node in self.Edge[exploring_node]:
                if next_node not in first_explore_time:
                    # If next_node has not been visited yet, then recur for it
                    timer = _scc_recursive_util(next_node, connected_ancestor, timer)

                    # Check if the subtree rooted with next_node has a connection to one of the ancestors of
                    # exploring_node
                    earliest_visited_vertex[exploring_node] = min(earliest_visited_vertex[exploring_node],
                                                                  earliest_visited_vertex[next_node])
                elif is_on_stack[next_node]:
                    # Update earliest_visited_vertex value of exploring_node
                    # only if next_node is still in stack
                    # i.e. it's a back edge, not cross edge
                    earliest_visited_vertex[exploring_node] = min(earliest_visited_vertex[exploring_node],
                                                                  earliest_visited_vertex[next_node])

            if earliest_visited_vertex[exploring_node] == first_explore_time[exploring_node]:
                # current node is a head node of the SCC
                w = -1
                current_scc: set[GRAPH_NODE_TYPE] = set()
                while w != exploring_node:
                    w = connected_ancestor.pop()
                    current_scc.add(w)
                    is_on_stack[w] = False
                all_scc_list.append(current_scc)

            return timer

        current_timer: int = 0

        # Stores discovery times of visited vertices
        first_explore_time: dict[GRAPH_NODE_TYPE, int] = {}
        # Earliest visited vertex (the vertex with minimum discovery time) that can be reached from subtree rooted with
        #   current vertex
        earliest_visited_vertex: dict[GRAPH_NODE_TYPE, int] = {}
        # Bit array for faster check whether a node is currently on the stack
        is_on_stack: dict[GRAPH_NODE_TYPE, bool] = {node: False for node in self.Vertex}

        all_scc_list: List[set[GRAPH_NODE_TYPE]] = []
        # Find subtrees under unconnected components
        for current_node in self.Vertex:
            if current_node not in first_explore_time:
                tmp_connected_ancestors: List[int] = []
                current_timer = _scc_recursive_util(current_node, tmp_connected_ancestors, current_timer)

        return all_scc_list
