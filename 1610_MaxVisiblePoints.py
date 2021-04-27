"""
You are given an array points, an integer angle, and your location, where location = [pos_x, pos_y] and
 points[i] = [xi, yi] both denote integral coordinates on the X-Y plane.

Initially, you are facing directly east from your position. You cannot move from your position, but you can rotate. In
 other words, pos_x and pos_y cannot be changed. Your field of view in degrees is represented by angle, determining how
 wide you can see from any given view direction. Let d be the amount in degrees that you rotate counterclockwise. Then,
 your field of view is the inclusive range of angles [d - angle/2, d + angle/2]

You can see some set of points if, for each point, the angle formed by the point, your position, and the immediate east
 direction from your position is in your field of view.

There can be multiple points at one coordinate. There may be points at your location, and you can always see these
 points regardless of your rotation. Points do not obstruct your vision to other points.

Return the maximum number of points you can see.
"""
from math import pi, atan2
from typing import List, Tuple


def visible_points(points: List[Tuple[int, int]], angle: int, location: Tuple[int, int]) -> int:
    """
    :param points: list of (x_i, y_i) integral coordinates on X-Y plane
    :param angle: positive int, in degrees, representing the wide angles of field of view that person can see
    :param location: (pos_x, pos_y) where person is located
    :return: max number of points within the observer's field of view
    """

    # for each point (x_i, y_i) calculate its radian from location (pos_x, pos_y)
    radian_array = []
    # special cases (x_i, y_i) == (pos_x, pos_y), cannot calculate radian
    # will always be included in the field of view
    spot_on_count = 0

    pos_x, pos_y = location
    for x_i, y_i in points:
        if pos_x == x_i and pos_y == y_i:
            spot_on_count += 1
        else:
            radian_array.append(atan2(y_i - pos_y, x_i - pos_x))

    # use sliding window to find the longest window that satisfies radian_array[r] - radian_array[l] <= angle.
    radian_array.sort()
    # sliding window needs to go around in circle
    radian_array = radian_array + [r + 2.0 * pi for r in radian_array]

    # convert angle to radius
    angle = pi * angle / 180

    # Sliding window to search for global max
    left_bound = return_max = 0
    for right_bound in range(len(radian_array)):
        while radian_array[right_bound] - radian_array[left_bound] > angle:
            left_bound += 1
        return_max = max(return_max, right_bound - left_bound + 1)
        # if left_bound have rotated through the whole circle - no need to continue the search
        if radian_array[left_bound] >= 2 * pi:
            break

    return return_max + spot_on_count


test_cases = [([(2, 1), (2, 2), (3, 3)], 90, (1, 1), 3),
              ([(2, 1), (2, 2), (3, 4), (1, 1)], 90, (1, 1), 4),
              ([(1, 0), (2, 1)], 13, (1, 1), 1),
              ([(1, 1), (2, 2), (1, 2), (2, 1)], 0, (1, 1), 2), ]
for test_points, test_angle, test_position, expected_output in test_cases:
    assert visible_points(test_points, test_angle, test_position) == expected_output, test_points
