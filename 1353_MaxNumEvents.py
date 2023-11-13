"""
You are given an array of events where events[i] = [start_day_i, end_day_i]. Every event i starts at start_day_i and
 ends at end_day_i.

You can attend an event i at any day d where start_day_i <= d <= end_day_i. You can only attend one event at any time d.

Return the maximum number of events you can attend.
"""
import heapq
from typing import List


def max_events(events: List[List[int]]):
    # attend an event for at most 1 day

    n_total = len(events)

    # sort by start_day_i, and then end_day_i
    events.sort()

    started_events_end_day = []
    n_attended = event_i = 0

    current_day = events[0][0]
    while event_i < n_total:
        # start all events that start on current_day
        while event_i < n_total and events[event_i][0] == current_day:
            heapq.heappush(started_events_end_day, events[event_i][1])
            event_i += 1

        # attend the started event that ends the earliest
        heapq.heappop(started_events_end_day)
        n_attended += 1
        current_day += 1

        # remove all expired events by current_day
        while started_events_end_day and started_events_end_day[0] < current_day:
            heapq.heappop(started_events_end_day)

        # if no event started, fast-forward current_day to next event start day
        if event_i < n_total and not started_events_end_day:
            current_day = events[event_i][0]

    # Process remaining events that is still in the heap
    while started_events_end_day:
        # Non-expired started event that ends earliest
        if heapq.heappop(started_events_end_day) >= current_day:
            current_day += 1
            n_attended += 1

    return n_attended


test_cases = [
    ([[1, 2], [2, 3], [3, 4]], 3),
    ([[1, 2], [2, 3], [3, 4], [1, 2]], 4)
]
for test_schedule, expected_output in test_cases:
    assert max_events(test_schedule) == expected_output
