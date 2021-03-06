"""
Given a list of non-overlapping axis-aligned rectangles, write a function pick which randomly and uniformly picks
an integer point in the space covered by the rectangles.
"""
from bisect import bisect_right
from itertools import accumulate
from random import randint
from typing import List, Tuple


class RandomPointNonOverlappingRectangles:
    def __init__(self, rectangles: List[List[int]]):
        """
        :param rectangles: non overlapping axis aligned rectangles,
            where [x1, y1, x2, y2] where (x1, y1) is bottom left and (x2, y2) is top right corner
            and 1 <= len(rectangles) <= 300
        """
        self.rectangles = rectangles
        self.cumulative_area = list(accumulate([(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rectangles]))

    def pick(self) -> Tuple[int, int]:
        """
        :return: integer coordinates [px, py] that reside in the cover areas of self.rectangles
        """
        select_point = randint(0, self.cumulative_area[-1] - 1)
        rect_i = bisect_right(self.cumulative_area, select_point)
        x1, y1, x2, y2 = self.rectangles[rect_i]
        dy, dx = divmod(select_point - self.cumulative_area[rect_i - 1], x2 - x1 + 1) if rect_i > 0 \
            else divmod(select_point, x2 - x1 + 1)
        return x1 + dx, y1 + dy


test_cases = [[[-2, -2, -1, -1], [1, 0, 3, 0]], [[1, 1, 5, 5]], ]
for test_rectangles in test_cases:
    rand_gen = RandomPointNonOverlappingRectangles(test_rectangles)
    n_cycles = 100_000
    for _ in range(n_cycles):
        x, y = rand_gen.pick()
        assert any([x1 <= x <= x2 and y1 <= y <= y2 for x1, y1, x2, y2 in test_rectangles]), \
            "x:%d, y:%d" % (x, y)
