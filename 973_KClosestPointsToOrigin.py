"""
Given an array of points where points[i] = (xi, yi) represents a point on the X-Y plane and an integer k, return the k
 closest points to the origin (0, 0).

The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2) ** 2 + (y1 - y2) ** 2).

You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it is in).
"""
from typing import Tuple, List


def k_closest_to_origin(points: List[Tuple[int, int]], k: int) -> List[Tuple[int, int]]:
    """
    :param points: list of (xi, yi) with 1 <= len(points) <= 10000
    :param k: 1 <= k <= len(points)
    :return: k closest points to origin
    """
    return sorted(points, key=lambda x_y: x_y[0] ** 2 + x_y[1] ** 2)[:k]


test_cases = [([(1, 3), (-2, 2)], 1, {(-2, 2)}),
              ([(3, 3), (5, -1), (-2, 4)], 2, {(3, 3), (-2, 4)}),
              ([(-95, 76), (17, 7), (-55, -58), (53, 20), (-69, -8), (-57, 87), (-2, -42), (-10, -87), (-36, -57),
                (97, -39), (97, 49)], 5,
               {(17, 7), (-2, -42), (53, 20), (-36, -57), (-69, -8)}), ]
for test_list, test_k, expected_output in test_cases:
    assert set(k_closest_to_origin(test_list, test_k)) == expected_output
