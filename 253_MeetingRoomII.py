"""
Given an array of meeting time intervals consisting of start and end times [[s1,e1],[s2,e2],...] find the minimum number
 of conference rooms required.
"""
from collections import defaultdict
from typing import List, NamedTuple, DefaultDict


class Interval(NamedTuple):
    start: int
    end: int


def min_meeting_rooms(intervals: List[Interval]) -> int:
    """
    :param intervals: list of (start_i, end_i) of meeting i
    :return: number of meeting rooms needed to satisfy the meeting request
    """
    boundary_count: DefaultDict[int, int] = defaultdict(int)
    for interval_i in intervals:
        boundary_count[interval_i.start] += 1
        boundary_count[interval_i.end] -= 1

    active_meetings = 0
    room_count = 0
    for _, interval_change in sorted(boundary_count.items()):
        active_meetings += interval_change
        room_count = max(room_count, active_meetings)

    return room_count


test_cases = [([(0, 30), (5, 10), (15, 20)], 2),
              ([(2, 7)], 1),
              ([(4, 30), (10, 28), (8, 34), (17, 22), (18, 22)], 5), ]
for test_intervals, expected_value in test_cases:
    assert min_meeting_rooms([Interval(start_i, end_i) for start_i, end_i in test_intervals]) == expected_value
