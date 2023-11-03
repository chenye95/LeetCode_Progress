"""
A company is organizing a meeting and has a list of n employees, waiting to be invited. They have arranged for a large
 circular table, capable of seating any number of employees.

The employees are numbered from 0 to n - 1. Each employee has a favorite person, and they will attend the meeting only
 if they can sit next to their favorite person at the table. The favorite person of an employee is not themselves.

Given a 0-indexed integer array favorite, where favorite[i] denotes the favorite person of the ith employee, return the
 maximum number of employees that can be invited to the meeting.
"""
from collections import deque
from typing import List


def maximum_invitations(favorite: List[int]) -> int:
    n = len(favorite)

    # create topological sort order of the directed graph
    # find chains in the graph
    in_degrees = [0] * n
    chain_len_ending_at = [0] * n

    for person in range(n):
        in_degrees[favorite[person]] += 1

    explore_queue = deque([person_i for person_i, degree_i in enumerate(in_degrees) if degree_i == 0])
    node_visited = [False] * n

    while explore_queue:
        person = explore_queue.popleft()
        node_visited[person] = True
        fav_person = favorite[person]
        chain_len_ending_at[fav_person] = max(chain_len_ending_at[fav_person], chain_len_ending_at[person] + 1)
        in_degrees[fav_person] -= 1
        if in_degrees[fav_person] == 0:
            explore_queue.append(fav_person)

    # Two Types of Invitation List available:
    # (1) Multiple set of 2 Chains Connected by a cycle of length 2
    # (2) A cycle of length > 2

    # by now node_visited[person] == False means, the person is part of a cycle
    type_1_len = type_2_len = 0
    for person in range(n):
        if not node_visited[person]:
            current_person, current_len = person, 0
            while not node_visited[current_person]:
                node_visited[current_person] = True
                current_person = favorite[current_person]
                current_len += 1

            if current_len == 2:
                type_1_len += (chain_len_ending_at[person] + chain_len_ending_at[favorite[person]] + 2)
            else:
                type_2_len = max(type_2_len, current_len)

    return max(type_1_len, type_2_len)


test_cases = [
    ([2, 2, 1, 2], 3),
    ([1, 2, 0], 3),
    ([3, 0, 1, 4, 1], 4),
    ([7, 12, 17, 9, 0, 7, 14, 5, 3, 15, 6, 14, 10, 14, 10, 1, 1, 4], 6),
]
for test_favorite, expected_value in test_cases:
    assert maximum_invitations(test_favorite) == expected_value
