from collections import defaultdict
from typing import Any


class WeightedGraph:
    def __init__(self):
        self.Edge = defaultdict(dict)
        self.Vertex = set()

    def add_vertex(self, v) -> None:
        """
        :param v: Vertex, needs to be hashable
        :return:
        """
        self.Vertex.add(v)

    def add_edge(self, u, v) -> None:
        pass

    def check_vertex(self, v) -> bool:
        return v in self.Vertex

    def check_edge(self, u, v) -> bool:
        return u in self.Vertex and v in self.Vertex and v in self.Edge[u]

    def edge_weight(self, u, v) -> Any or None:
        if u in self.Vertex and v in self.Vertex and v in self.Edge[u]:
            return self.Edge[u][v]
        else:
            return None

    def find_path_generator(self, start, end):
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


new_dg = WeightedGraph()
new_dg.Vertex.add(1)
new_dg.Vertex.add(2)
new_dg.Edge[1][2] = 1.0
