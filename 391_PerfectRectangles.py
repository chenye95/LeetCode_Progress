"""
Given N axis-aligned rectangles where N > 0, determine if they all together form an exact cover of a rectangular region.

Each rectangle is represented as a bottom-left point and a top-right point. For example, a unit square is represented
as [1,1,2,2]. (coordinate of bottom-left point is (1, 1) and top-right point is (2, 2)).
"""
from collections import defaultdict
from typing import List


def is_rectangle_cover(rectangles: List[List[int]]) -> bool:
    """
    :param rectangles: n axis aligned rectangles [bottom_left_x, bottom_left_y, top_right_x, top_right_y]
    :return: whether rectangles all together from an exact cover of a rectangular region
    """

    def merge_y_intervals(intervals: List[List[int]]) -> List[List[int]]:
        """
        :param intervals: intervals y coverage at a given x value
        :return: combined intervals of y
        """
        return_list = []
        intervals.sort()
        for interval in intervals:
            if not return_list or return_list[-1][1] < interval[0]:
                # gaps between intervals
                # could be a rectangle that sticks in between two intervals
                return_list.append(interval)
            elif return_list[-1][1] == interval[0]:
                return_list[-1][1] = interval[1]
            else:
                # overlapping intervals, meaning rectangles double cover a certain area
                return []
        return return_list

    rectangles.sort()
    left_x = rectangles[0][0]
    right_x = max(rectangle_i[2] for rectangle_i in rectangles)

    interval_dict = defaultdict(list)
    for x1, y1, x2, y2 in rectangles:
        # {(x, is_left): [[bottom_left_y, top_right_y]]}
        interval_dict[(x1, True)] += [[y1, y2]]
        interval_dict[(x2, False)] += [[y1, y2]]

    for x, is_rectangle_left in interval_dict.keys():
        if is_rectangle_left:
            counter_key = (x, False) if x != left_x else (right_x, False)
            start_here = merge_y_intervals(interval_dict[(x, is_rectangle_left)])
            end_here = merge_y_intervals(interval_dict[counter_key])
            if not start_here or not end_here or start_here != end_here:
                # rectangles that start at x and rectangles that end at x should have exactly matched merged y intervals
                # else either overlapping coverage or missing coverage
                return False

    return True


test_cases = [([[1, 1, 3, 3],
                [3, 1, 4, 2],
                [3, 2, 4, 4],
                [1, 3, 2, 4],
                [2, 3, 3, 4], ], True),
              ([[1, 1, 2, 3],
                [1, 3, 2, 4],
                [3, 1, 4, 2],
                [3, 2, 4, 4], ], False),
              ([[1, 1, 3, 3],
                [3, 1, 4, 2],
                [1, 3, 2, 4],
                [3, 2, 4, 4], ], False),
              ([[1, 1, 3, 3],
                [3, 1, 4, 2],
                [1, 3, 2, 4],
                [2, 2, 4, 4], ], False), ]
for test_rectangle, expected_outcome in test_cases:
    assert is_rectangle_cover(rectangles=test_rectangle) is expected_outcome
