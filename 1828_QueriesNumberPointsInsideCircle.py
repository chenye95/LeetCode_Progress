"""
You are given an array points where points[i] = [xi, yi] is the coordinates of the ith point on a 2D plane. Multiple
 points can have the same coordinates.

You are also given an array queries where queries[j] = [xj, yj, rj] describes a circle centered at (xj, yj) with a
 radius of rj.

For each query queries[j], compute the number of points inside the jth circle. Points on the border of the circle are
 considered inside.

Return an array answer, where answer[j] is the answer to the jth query.
"""
from typing import List, Tuple


def count_points_trigonometry(points: List[Tuple[int, int]], queries: List[Tuple[int, int, int]]) -> List[int]:
    """
    :param points: list of points (x_i, y_i) coordinates of the ith point on a 2D plane; multiple points can overlap
    :param queries: list of circles (x_j, y_j, r_j) describing a circle centered at (x_j, y_j) with radius r_J
    :return: count of points in the jth circle
    """
    point_count = [0] * len(queries)
    j = -1
    for x_j, y_j, r_j in queries:
        j += 1
        for x_i, y_i in points:
            if (x_i - x_j) ** 2 + (y_i - y_j) ** 2 <= r_j ** 2:
                point_count[j] += 1

    return point_count


def count_points_complex(points: List[Tuple[int, int]], queries: List[Tuple[int, int, int]]) -> List[int]:
    """
    :param points: list of points (x_i, y_i) coordinates of the ith point on a 2D plane; multiple points can overlap
    :param queries: list of circles (x_j, y_j, r_j) describing a circle centered at (x_j, y_j) with radius r_J
    :return: count of points in the jth circle
    """
    # convert coordinates to complex numbers
    points = list(map(complex, *zip(*points)))
    queries = [(complex(x_j, y_j), r_j) for x_j, y_j, r_j in queries]
    return [sum(abs(p - q) <= r for p in points) for q, r in queries]


test_cases = [([(1, 3), (3, 3), (5, 3), (2, 2)], [(2, 3, 1), (4, 3, 1), (1, 1, 2)], [3, 2, 2]),
              ([(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], [(1, 2, 2), (2, 2, 2), (4, 3, 2), (4, 3, 3)], [2, 3, 2, 4]),
              ([(99, 113), (150, 165), (23, 65), (175, 154), (84, 83), (24, 59), (124, 29), (19, 97), (117, 182),
                (105, 191), (83, 117), (114, 35), (0, 111), (22, 53)],
               [(105, 191, 155), (114, 35, 94), (84, 83, 68), (175, 154, 28), (99, 113, 80), (175, 154, 177),
                (175, 154, 181), (114, 35, 134), (22, 53, 105), (124, 29, 164), (6, 99, 39), (84, 83, 35)],
               [11, 7, 8, 2, 7, 11, 13, 10, 10, 14, 3, 3])]
for count_points in [count_points_trigonometry, count_points_complex]:
    for test_points, test_circles, expected_count in test_cases:
        assert count_points(test_points, test_circles) == expected_count
