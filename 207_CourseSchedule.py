"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""
from collections import deque
from typing import List


def can_finish(num_courses: int, prerequisites: List[List[int]]) -> bool:
    """
    :param num_courses: total number of courses labeled from 0 to n-1
    :param prerequisites: prerequisites to take each course
    :return: if it is possible to finish all courses
    """
    # Topological Sort
    enable_courses = [[] for _ in range(num_courses)]
    unfinished_prerequisites = [0] * num_courses

    for p in prerequisites:
        unfinished_prerequisites[p[0]] += 1
        enable_courses[p[1]].append(p[0])

    running_deque = deque()
    for next_course in range(num_courses):
        if unfinished_prerequisites[next_course] == 0:
            running_deque.append(next_course)

    can_do = 0
    while running_deque:
        completed = running_deque.popleft()
        can_do += 1
        new_course: int
        for new_course in enable_courses[completed]:
            unfinished_prerequisites[new_course] -= 1
            if unfinished_prerequisites[new_course] == 0:
                running_deque.append(new_course)

    return can_do == num_courses


test_cases = [(2, [[1, 0]], True),
              (2, [[1, 0], [0, 1]], False)]
for test_NumCourse, test_prerequisites, expected_out in test_cases:
    assert can_finish(test_NumCourse, test_prerequisites) == expected_out
