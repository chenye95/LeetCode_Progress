"""
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks. The bricks have the same
 height but different width. You want to draw a vertical line from the top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing the width of each brick in
 this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed. You need to find out how to
 draw the line to cross the least bricks and return the number of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case the line will obviously
 cross no bricks.
"""
from typing import List


def least_bricks(wall: List[List[int]]) -> int:
    """
    :param wall: list of integers representing brick length; all layers add up to the same length of the wall
    :return: minimum number of bricks a vertical line have to cut through; (vertical line can not be the two vertical
        edges of the wall
    """
    edge_count = {}
    for layer_i in wall:
        # calculate edges in layer i
        edge = 0
        for brick_j in layer_i[:-1]:
            # does not add the last brick to avoid the ending line of the wall
            edge += brick_j
            edge_count[edge] = edge_count.get(edge, 0) + 1

    # choose the vertical line that overlaps with most edges
    return len(wall) - max(edge_count.values()) if edge_count else len(wall)


test_cases = [([[1], [1], [1]], 3),
              ([[1, 1], [2], [1, 1]], 1),
              ([[1, 2, 2, 1],
                [3, 1, 2],
                [1, 3, 2],
                [2, 4],
                [3, 1, 2],
                [1, 3, 1, 1]], 2), ]
for test_wall, expected_output in test_cases:
    assert least_bricks(test_wall) == expected_output
