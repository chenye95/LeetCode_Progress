"""
We are given a list schedule of employees, which represents the working time for each employee.

Each employee has a list of non-overlapping Intervals, and these intervals are in sorted order.

Return the list of finite intervals representing common, positive-length free time for all employees, also in sorted
 order.
"""
from collections import defaultdict
from typing import List, NamedTuple, DefaultDict


class Interval(NamedTuple):
    start: int
    end: int

    def __gt__(self, other: 'Interval'):
        return self.start > other.start or self.start == other.start and self.end > other.end


def employee_free_time_sort(schedule: List[List[Interval]]) -> List[Interval]:
    """
    :param schedule: list of list [(i_start, i_end)] with 0 <= i_start < i_end <= 1e8, and 1 <= len(schedule[i]) <= 50
    :return: list of finite intervals where all employees are free
    """
    all_intervals: List[Interval] = []
    for schedule_i in schedule:
        all_intervals.extend(schedule_i)
    all_intervals.sort()

    cover_until = all_intervals[0].end
    free_time: List[Interval] = []
    for interval_i in all_intervals[1:]:
        i_start, i_end = interval_i.start, interval_i.end
        if cover_until < i_start:
            free_time.append(Interval(start=cover_until, end=i_start))
            cover_until = i_end
        else:
            cover_until = max(i_end, cover_until)

    return free_time


def employee_free_time_boundary(schedule: List[List[Interval]]) -> List[Interval]:
    """
    :param schedule: list of list [(i_start, i_end)] with 0 <= i_start < i_end <= 1e8, and 1 <= len(schedule[i]) <= 50
    :return: list of finite intervals where all employees are free
    """
    boundary_count: DefaultDict[int, int] = defaultdict(int)
    for employee_i in schedule:
        for interval_j in employee_i:
            boundary_count[interval_j.start] += 1
            boundary_count[interval_j.end] -= 1

    free_time = []
    active_interval_count = 0
    free_interval_start = None

    for boundary_i, interval_change in sorted(boundary_count.items()):
        active_interval_count += interval_change
        if active_interval_count == 0:
            free_interval_start = boundary_i
        elif free_interval_start is not None:
            free_time.append(Interval(free_interval_start, boundary_i))
            free_interval_start = None

    return free_time


test_cases = [([[(1, 2), (5, 6)], [(1, 3)], [(4, 10)]], [(3, 4)]),
              ([[(1, 3), (6, 7)], [(2, 4)], [(2, 5), (9, 12)]], [(5, 6), (7, 9)]), ]
for employee_free_time in [employee_free_time_sort, employee_free_time_boundary, ]:
    for test_schedule, expected_free_time in test_cases:
        assert employee_free_time([[Interval(start=i_start, end=i_end) for i_start, i_end in employee_i]
                                   for employee_i in test_schedule]) == expected_free_time, employee_free_time.__name__
