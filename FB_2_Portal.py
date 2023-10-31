import string
from collections import deque
from typing import List

neighbor_steps = [(-1, 0), (1, 0), (0, -1), (0, 1), ]


def get_seconds_required(R: int, C: int, G: List[str]) -> int:
    portal_list = {c_i: [] for c_i in string.ascii_lowercase}
    portal_start = None
    visited = [[False] * C for _ in range(R)]
    for i, row_i in enumerate(G):
        for j, chr_j in enumerate(row_i):
            if 'a' <= chr_j <= 'z':
                portal_list[chr_j].append((i, j))
            elif row_i[j] == 'S':
                portal_start = (i, j)
                visited[i][j] = True

    explore_front = deque([(portal_start, 0), ])
    while explore_front:
        (current_i, current_j), step_so_far = explore_front.popleft()

        if 'a' <= G[current_i][current_j] <= 'z':
            for tunnel_i, tunnel_j in portal_list[G[current_i][current_j]]:
                if not visited[tunnel_i][tunnel_j]:
                    explore_front.append(((tunnel_i, tunnel_j), step_so_far + 1))
                    visited[tunnel_i][tunnel_j] = True

        for move_i, move_j in neighbor_steps:
            if 0 <= current_i + move_i < R and 0 <= current_j + move_j < C:
                if G[current_i + move_i][current_j + move_j] == 'E':
                    return step_so_far + 1
                elif G[current_i + move_i][current_j + move_j] != '#' and \
                        not visited[current_i + move_i][current_j + move_j]:
                    explore_front.append(((current_i + move_i, current_j + move_j), step_so_far + 1))
                    visited[current_i + move_i][current_j + move_j] = True

    return -1


test_cases = [
    ((3, 3, ['.E.', '.#E', '.S#']), 4),
    ((3, 4, ['a.Sa', '####', 'Eb.b']), -1),
    ((3, 4, ['aS.b', '####', 'Eb.a']), 4),
    ((1, 9, ['xS..x..Ex']), 3),
]
for (test_R, test_C, test_G), expected_value in test_cases:
    assert get_seconds_required(test_R, test_C, test_G) == expected_value
