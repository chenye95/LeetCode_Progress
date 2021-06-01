"""
You are given an integer n, which indicates that there are n courses labeled from 1 to n. You are also given an array
 relations where relations[i] = [prevCourse, nextCourse], representing a prerequisite relationship between course
 prevCourse and course nextCourse: course prevCourse has to be taken before course nextCourse. Also, you are given the
 integer k.

In one semester, you can take at most k courses as long as you have taken all the prerequisites in the previous semester
 for the courses you are taking.

Return the minimum number of semesters needed to take all courses. The testcases will be generated such that it is
 possible to take every course.
"""
from functools import cache
from itertools import combinations
from typing import List, Tuple


def min_number_semesters_bfs(n: int, relations: List[Tuple[int, int]], k: int) -> int:
    """
    :param n: n courses labelled 1 to n (1 indexed), 1 <= n <= 15
    :param relations: list of unique (prerequisite, course_to_take) pairs, 0 <= len(relations) <= n * (n - 1) / 2;
        relations represent a direct acyclic graph
    :param k: 1 <= k <= n
    :return: minimum semesters needed to take all n courses while honoring prerequisites and take at most k courses per
        semester
    """

    @cache
    def can_take(have_taken_mask: int) -> List[int]:
        """
        :param have_taken_mask: bit mask representing courses taken so far
        :return: list of courses that have not been taken, and whose prerequisites have been satisfied. Represented as
            list of 1-bit integers
        """
        enabled_courses = []
        for course_i in range(n):
            if not ((1 << course_i) & have_taken_mask) and \
                    (dependencies[course_i] & have_taken_mask == dependencies[course_i]):
                enabled_courses.append(1 << course_i)
        return enabled_courses

    @cache
    def min_semester_after(have_taken_mask: int = 0) -> int:
        """
        :param have_taken_mask: bit mask representing courses taken so far
        :return: # semesters after taken have_taken_mask
        """
        if have_taken_mask + 1 == 1 << n:
            return 0
        next_batch = can_take(have_taken_mask)
        if len(next_batch) <= k:
            return 1 + min_semester_after(have_taken_mask + sum(next_batch))
        else:
            # choose k courses to take this semester
            return 1 + min(min_semester_after(have_taken_mask + sum(current_semester))
                           for current_semester in combinations(next_batch, k))

    # bit semester_mask to represent prerequisites of course_i + 1
    # dependencies is zero-indexed
    dependencies = [0] * n
    for prerequisite, next_course in relations:
        dependencies[next_course - 1] |= (1 << (prerequisite - 1))
    return min_semester_after()


test_cases = [(4, [(2, 1), (3, 1), (1, 4)], 2, 3),
              (5, [(2, 1), (3, 1), (4, 1), (1, 5)], 2, 4),
              (11, [], 2, 6),
              (13, [(12, 8), (2, 4), (3, 7), (6, 8), (11, 8), (9, 4), (9, 7), (12, 4), (11, 4), (6, 4), (1, 4), (10, 7),
                    (10, 4), (1, 7), (1, 8), (2, 7), (8, 4), (10, 8), (12, 7), (5, 4), (3, 4), (11, 7), (7, 4), (13, 4),
                    (9, 8), (13, 8)], 9, 3),
              (15, [(12, 11)], 12, 2), ]
for min_number_semesters in [min_number_semesters_bfs, ]:
    for test_n, test_relations, test_k, expected_count in test_cases:
        assert min_number_semesters(test_n, test_relations, test_k) == expected_count
