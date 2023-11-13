from collections import deque
from typing import List, Dict


def get_cycle_len(node: int, cycle_size: Dict[int, int], cycle_start: Dict[int, int],
                  zero_indexed_l: List[int]) -> int:
    if node in cycle_start:
        return cycle_size[cycle_start[node]]
    cycle_len = 1
    current_node = zero_indexed_l[node]
    while current_node != node:
        cycle_len += 1
        cycle_start[current_node] = node
        current_node = zero_indexed_l[current_node]

    cycle_size[node] = cycle_len
    return cycle_len


def get_max_visitable_webpages(N: int, L: List[int]) -> int:
    zero_indexed_l = [l_i - 1 for l_i in L]

    # use topological sort to find the longest chains
    in_degrees = [0] * N
    chain_len_ending_at = [0] * N

    for web_page in range(N):
        in_degrees[zero_indexed_l[web_page]] += 1

    explore_queue = deque([node_i for node_i, node_degree in enumerate(in_degrees) if node_degree == 0])
    node_visited = [False] * N

    while explore_queue:
        web_page = explore_queue.popleft()
        node_visited[web_page] = True
        next_page = zero_indexed_l[web_page]
        chain_len_ending_at[next_page] = max(chain_len_ending_at[next_page], chain_len_ending_at[web_page] + 1)
        in_degrees[next_page] -= 1
        if in_degrees[next_page] == 0:
            explore_queue.append(next_page)

    # by now node_visited[person] == False means, the web_page is part of a cycle
    cycle_size = {}
    cycle_start = {}

    # Since every webpage has one outgoing link, there's always going to be a cycle in your longest chain.
    # Hence, we find the biggest combination of an inbound chain + cycle.
    max_chain = 0
    for node in range(N):
        if not node_visited[node]:
            max_chain = max(max_chain,
                            chain_len_ending_at[node] + get_cycle_len(node, cycle_size, cycle_start, zero_indexed_l))

    return max_chain


test_cases = [
    ((4, [4, 1, 2, 1]), 4),
    ((4, [4, 1, 2, 4]), 4),
    ((5, [4, 3, 5, 1, 2]), 3),
    ((5, [2, 4, 2, 2, 3]), 4),
]
for (test_N, test_L), expected_value in test_cases:
    assert get_max_visitable_webpages(test_N, test_L) == expected_value
