"""
There are n different online courses numbered from 1 to n. You are given an array courses where
 courses[i] = [duration_i, lastDay_i] indicate that the ith course should be taken continuously for duration_i days
 and must be finished before or on lastDay_i.

You will start on the 1st day and you cannot take two or more courses simultaneously.

Return the maximum number of courses that you can take.
"""
from heapq import heappush, heappop
from typing import List, Tuple, Dict


def schedule_course_dfs(courses: List[Tuple[int, int]]) -> int:
    """
    Always profitable to take the course with a smaller end day prior to a course with a larger end day.

    :param courses: list of (duration_i, last_day_i) meaning ith course should be taken continuously for duration_i days
     and mush be finished prior to or on last_day_i
    :return: max number of courses you can take from the catalog
    """

    def schedule_course_i(i: int, time_so_far: int) -> int:
        """
        Decide whether to take course i after already decided on previous i - 1 courses to time time_so_far

        :param i: course_i to be evaluated
        :param time_so_far: the time is now time_so_far
        :return: max number of course from catalog course[i:] that can be taken after time_so_far
        """
        if i == len(courses):
            return 0
        if (i, time_so_far) not in recurse_memory:
            if time_so_far + courses[i][0] <= courses[i][1]:
                recurse_memory[(i, time_so_far)] = max(
                    schedule_course_i(i + 1, time_so_far + courses[i][0]) + 1,  # take course i
                    schedule_course_i(i + 1, time_so_far)  # not take course i
                )
            else:
                recurse_memory[(i, time_so_far)] = schedule_course_i(i + 1, time_so_far)  # cannot take course i
        return recurse_memory[(i, time_so_far)]

    recurse_memory: Dict[Tuple[int, int], int] = {}
    courses.sort(key=lambda course_i: course_i[1])
    return schedule_course_i(0, 0)


def schedule_course_heap(courses: List[Tuple[int, int]]) -> int:
    """
    Always profitable to take the course with a smaller end day prior to a course with a larger end day.

    If course_i cannot be taken at this moment, swap with a previously taken courses course_j where
     duration_j > duration_i (and end_j <= end_i)
    Let A be time to handle all courses before j, B be time to handle courses in [j + 1, ..., i - 1], then
        A + duration_i < A + duration_j <= end_j < end_i
        A + duration_i + B < A + duration_j + B <= end_i_minus_1 <= end_i

    In fact, we would swap with the largest duration_j in the taken courses to save more time for future classes

    :param courses: list of (duration_i, last_day_i) meaning ith course should be taken continuously for duration_i days
     and mush be finished prior to or on last_day_i
    :return: max number of courses you can take from the catalog
    """
    current_time = 0
    classes_taken_duration = []  # max heap on duration_i for courses that have been chosen
    courses.sort(key=lambda course_i: course_i[1])

    for duration_i, end_day_i in courses:
        if current_time + duration_i <= end_day_i:
            # can fit course i into our schedule
            heappush(classes_taken_duration, -duration_i)
            current_time += duration_i
        elif len(classes_taken_duration) > 0 and -classes_taken_duration[0] > duration_i:
            # replace course j with course i
            current_time += (duration_i + heappop(classes_taken_duration))
            heappush(classes_taken_duration, -duration_i)

    return len(classes_taken_duration)


test_cases = [([(100, 200), (200, 1300), (1000, 1250), (2000, 3200)], 3),
              ([(1, 2)], 1),
              ([(3, 2), (4, 3)], 0),
              ([(1, 2), (2, 3)], 2),
              ([(914, 9927), (333, 712), (163, 5455), (835, 5040), (905, 8433), (417, 8249), (921, 9553), (913, 7394),
                (303, 7525), (582, 8658), (86, 957), (40, 9152), (600, 6941), (466, 5775), (718, 8485), (34, 3903),
                (380, 9996), (316, 7755)], 18),
              ([(7, 16), (2, 3), (3, 12), (3, 14), (10, 19), (10, 16), (6, 8), (6, 11), (3, 13), (6, 16)], 4)]
for schedule_course in [schedule_course_dfs, schedule_course_heap, ]:
    for test_courses, expected_count in test_cases:
        assert schedule_course(test_courses) == expected_count
