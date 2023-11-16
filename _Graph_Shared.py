import abc
from typing import Union, List

GRAPH_NODE_TYPE = Union[str, int]


class DirectedGraph(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def topological_order(self) -> (bool, List[GRAPH_NODE_TYPE]):
        """
        :return: a tuple of (bool, list)
            True, list representing topological order of the directed graph, topological order exists
            False, empty list if graph is cyclic
        """
        pass
