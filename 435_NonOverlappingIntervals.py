"""
Given a collection of intervals, find the minimum number of intervals you need to remove to make the rest of the
intervals non-overlapping.
"""
from typing import List


def erase_overlap_intervals(intervals: List[List[int]]) -> int:
    """
    repeated keep the interval with the left most end, and remove all intervals overlapping with it
    :param intervals: a collection of intervals list[[start, end]]
    :return: minimum number of intervals you need to remove to make the rest of the intervals non-overlapping
    """
    left_most_end = float("-inf")
    erased_count = 0
    for interval_start, interval_end in sorted(intervals, key=lambda interval_range: interval_range[1]):
        if interval_start >= left_most_end:
            # non overlapping, keep it
            left_most_end = interval_end
        else:
            # overlapping with existing interval, drop it
            erased_count += 1
    return erased_count


assert erase_overlap_intervals([[1, 2], [2, 3], [3, 4], [1, 3]]) == 1
assert erase_overlap_intervals([[1, 2], [1, 2], [1, 2]]) == 2
assert erase_overlap_intervals([[1, 2], [2, 3]]) == 0
