"""There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]
Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to
finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses,
return an empty array.
"""
from collections import deque
from typing import List


def find_order(num_courses: int, prerequisites: List[List[int]]) -> List[int]:
    """
    BFS - Topological Sort algorithm
    :param num_courses: total number of courses labeled from 0 to n-1
    :param prerequisites: prerequisites to take each course
    :return: the ordering of courses you should take to finish all courses, or [] if not possible
    """
    # Topological Sort
    enable_courses = [[] for _ in range(num_courses)]
    unfinished_prerequisites = [0] * num_courses

    for p in prerequisites:
        unfinished_prerequisites[p[0]] += 1
        enable_courses[p[1]].append(p[0])

    running_deque = deque()
    class_order = []
    for next_course in range(num_courses):
        if unfinished_prerequisites[next_course] == 0:
            running_deque.append(next_course)

    can_do = 0
    while running_deque:
        completed = running_deque.popleft()
        class_order.append(completed)
        can_do += 1
        new_course: int
        for new_course in enable_courses[completed]:
            unfinished_prerequisites[new_course] -= 1
            if unfinished_prerequisites[new_course] == 0:
                running_deque.append(new_course)

    return class_order if can_do == num_courses else []


test_cases = [(2, [[1, 0]], [[0, 1], ]),
              (2, [[1, 0], [0, 1]], [[], ]),
              (4, [[1, 0], [2, 0], [3, 1], [3, 2]], [[0, 1, 2, 3], [0, 2, 1, 3], ]),
              ]
for numCourse, test_prerequisites, expected_out in test_cases:
    assert find_order(numCourse, test_prerequisites) in expected_out
