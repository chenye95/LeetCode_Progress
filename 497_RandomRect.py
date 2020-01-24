"""
Given a list of non-overlapping axis-aligned rectangles rectangles, write a function pick which randomly and uniformly picks
an integer point in the space covered by the rectangles.
"""
from typing import List
from itertools import accumulate
from random import randint
from bisect import bisect_right

class RandomPointNonOverlappingRectangles:

    def __init__(self, rectangles: List[List[int]]):
        self.rectangles = rectangles
        self.map = list(accumulate([(x2 - x1 + 1) * (y2 - y1 + 1) for x1, y1, x2, y2 in rectangles]))

    def pick(self) -> List[int]:
        diff = randint(0, self.map[-1]-1)
        rect_i = bisect_right(self.map, diff)
        x1, y1, x2, y2 = self.rectangles[rect_i]
        if rect_i > 0:
            dy, dx = divmod(diff - self.map[rect_i-1], (x2 - x1 + 1))
        else:
            dy, dx = divmod(diff, (x2 - x1 + 1))
        return x1 + dx, y1 + dy

test_cases = [[[-2, -2, -1, -1], [1, 0, 3, 0]]] # [[1,1,5,5]],
for rectangles in test_cases:
    rand_gen = RandomPointNonOverlappingRectangles(rectangles)
    n_cycles = 100000
    for _ in range(n_cycles):
        x, y = rand_gen.pick()
        assert any([x1 <= x and x <= x2 and y1 <= y and y <= y2 for x1, y1, x2, y2 in rectangles]), \
            "x:%d, y:%d" % (x, y)

