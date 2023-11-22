"""
You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start
 and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval
  newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still
 does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.
"""
from typing import List, Tuple


def insert(intervals: List[Tuple[int, int]], new_interval: Tuple[int, int]) -> List[Tuple[int, int]]:
    return_result = []

    i = 0
    for current_interval in intervals:
        if current_interval[1] < new_interval[0]:
            return_result.append(current_interval)
        elif current_interval[0] > new_interval[1]:
            return_result.append(new_interval)
            return return_result + intervals[i:]
        else:
            # new_interval[0] <= current_interval[1] and current_interval[0] <= new_interval[1]
            # detect an overlap; squash them together
            new_interval = (
                min(new_interval[0], current_interval[0]),
                max(new_interval[1], current_interval[1])
            )
        i += 1

    return_result.append(new_interval)
    return return_result


test_cases = [
    ([(1, 5)], (0, 0), [(0, 0), (1, 5)]),
    ([(3, 5), (12, 15)], (6, 6), [(3, 5), (6, 6), (12, 15)],),
    ([(1, 3), (6, 9)],
     (2, 5),
     [(1, 5), (6, 9)]),
    ([(1, 2), (3, 5), (6, 7), (8, 10), (12, 16)],
     (4, 8),
     [(1, 2), (3, 10), (12, 16)]),
]
for test_intervals, test_new_interval, expected_output in test_cases:
    assert insert(test_intervals, test_new_interval) == expected_output
