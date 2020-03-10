"""
There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed
as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?
"""
from collections import deque
from typing import List


def canFinish(numCourses: int, prerequisites: List[List[int]]) -> bool:
    # Topological Sort
    enable_courses = [[] for _ in range(numCourses)]
    unfinished_prerequisites = [0] * numCourses

    for p in prerequisites:
        unfinished_prerequisites[p[0]] += 1
        enable_courses[p[1]].append(p[0])

    running_deque = deque()
    for next_course in range(numCourses):
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

    return can_do == numCourses


test_cases = [(2, [[1, 0]], True),
              (2, [[1, 0], [0, 1]], False)]
for numCourse, prerequisites, expected_out in test_cases:
    assert canFinish(numCourse, prerequisites) == expected_out
