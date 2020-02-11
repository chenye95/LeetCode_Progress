"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented
as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
"""
from typing import List
from collections import defaultdict


def isRectangleCover(rectangles: List[List[int]]) -> bool:
    def mergeIntervals(intervals: List[int]) -> List[List[int]]:
        return_list = []
        intervals.sort()
        for interval in intervals:
            if not return_list or return_list[-1][1] < interval[0]:
                return_list.append(interval)
            elif return_list[-1][1] == interval[0]:
                return_list[-1][1] = interval[1]
            else:
                return []
        return return_list

    rectangles.sort()
    bottom_line = rectangles[0][0]
    top_line = max(rec[2] for rec in rectangles)

    interval_dict = defaultdict(list)
    for x1, y1, x2, y2 in rectangles:
        interval_dict[(x1, True)] += [[y1, y2]]
        interval_dict[(x2, False)] += [[y1, y2]]

    for key in interval_dict.keys():
        if key[1] is True:
            counter_key = (key[0], False) if key[0] != bottom_line else (top_line, False)
            start_here = mergeIntervals(interval_dict[key])
            end_here = mergeIntervals(interval_dict[counter_key])
            if not start_here or not end_here or start_here != end_here:
                return False

    return True

assert isRectangleCover(rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [3,2,4,4],
  [1,3,2,4],
  [2,3,3,4]
])

assert not isRectangleCover(rectangles = [
  [1,1,2,3],
  [1,3,2,4],
  [3,1,4,2],
  [3,2,4,4]
])

assert not isRectangleCover(rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [3,2,4,4]
])

assert not isRectangleCover(rectangles = [
  [1,1,3,3],
  [3,1,4,2],
  [1,3,2,4],
  [2,2,4,4]
]
)