import abc
from typing import Union, List, Tuple
from collections import defaultdict, deque

GRAPH_NODE_TYPE = Union[str, int]


class DirectedGraph(metaclass=abc.ABCMeta):
    def __init__(self):
        # place-holder declaration;
        # not used for instantiation
        self.Edge = None
        self.Vertex = None

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
