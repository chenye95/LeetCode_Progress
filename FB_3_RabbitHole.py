from collections import deque
from typing import List

from _Graph_Unwgt_ListImplementation import DirectedUnweightedGraph


def get_max_visitable_webpages_1(N: int, M: int, A: List[int], B: List[int]) -> int:
    graph_object = DirectedUnweightedGraph()
    for i in range(1, N + 1):
        graph_object.add_vertex(i)
    for a_i, b_i in zip(A, B):
        graph_object.add_edge(a_i, b_i)

    scc_list = graph_object.strongly_connected_components(use_recursive=False, convert_to_list=False)
    new_graph_mapping = {old_id: new_id
                         for new_id, scc_component in enumerate(scc_list)
                         for old_id in scc_component}

    new_graph = DirectedUnweightedGraph()
    for i in range(len(scc_list)):
        new_graph.add_vertex(i)
    for a_i, b_i in zip(A, B):
        if new_graph_mapping[a_i] != new_graph_mapping[b_i]:
            new_graph.add_edge(new_graph_mapping[a_i], new_graph_mapping[b_i])

    return new_graph.longest_path(node_weights={scc_i: len(scc_component)
                                                for scc_i, scc_component in enumerate(scc_list)})[0]


def get_max_visitable_webpages_2(N: int, M: int, A: List[int], B: List[int]) -> int:
    graph_object = DirectedUnweightedGraph()
    for i in range(1, N + 1):
        graph_object.add_vertex(i)
    for a_i, b_i in zip(A, B):
        graph_object.add_edge(a_i, b_i)

    scc_list = graph_object.strongly_connected_components(use_recursive=False, convert_to_list=False)
    new_graph_mapping = {old_id: new_id
                         for new_id, scc_component in enumerate(scc_list)
                         for old_id in scc_component}

    new_edges = [set() for _ in range(len(scc_list))]
    for a_i, b_i in zip(A, B):
        if new_graph_mapping[a_i] != new_graph_mapping[b_i]:
            new_edges[new_graph_mapping[a_i]].add(new_graph_mapping[b_i])

    in_degrees = [0] * len(scc_list)
    for out_node in range(len(scc_list)):
        for to_node in new_edges[out_node]:
            in_degrees[to_node] += 1

    exploring_queue = deque(node_i for node_i, degree_i in enumerate(in_degrees) if degree_i == 0)
    longest_path_ending_at = [len(scc_component) for scc_component in scc_list]
    while exploring_queue:
        current_node = exploring_queue.popleft()
        for next_node in new_edges[current_node]:
            longest_path_ending_at[next_node] = max(longest_path_ending_at[next_node],
                                                    longest_path_ending_at[current_node] + len(scc_list[next_node]))
            in_degrees[next_node] -= 1
            if in_degrees[next_node] == 0:
                exploring_queue.append(next_node)

    return max(longest_path_ending_at)


test_cases = [
    ((4, 4, [1, 2, 3, 4], [4, 1, 2, 1]), 4),
    ((5, 6, [3, 5, 3, 1, 3, 2], [2, 1, 2, 4, 5, 4]), 4),
    ((10, 9, [3, 2, 5, 9, 10, 3, 3, 9, 4], [9, 5, 7, 8, 6, 4, 5, 3, 9]), 5),
]
for get_max_visitable_webpages in [get_max_visitable_webpages_1, get_max_visitable_webpages_2, ]:
    for (test_N, test_M, test_A, test_B), expected_value in test_cases:
        assert get_max_visitable_webpages(test_N, test_M, test_A, test_B) == expected_value \
            , get_max_visitable_webpages.__name__
