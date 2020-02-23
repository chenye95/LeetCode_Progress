"""
A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a
distance. Now suppose you are given the locations and height of all the buildings as shown on a cityscape photo
(Figure A), write a program to output the skyline formed by these buildings collectively (Figure B).

The geometric information of each building is represented by a triplet of integers [Li, Ri, Hi], where Li and Ri are
the x coordinates of the left and right edge of the ith building, respectively, and Hi is its height.
"""
import heapq
from typing import List


def getSkyline(buildings: List[List[int]]) -> List[List[int]]:
    skyline_out = []
    adding_i, total_n = 0, len(buildings)
    live_buildings = []  # list of (height, right)
    while adding_i < total_n or live_buildings:
        if not live_buildings or adding_i < total_n and buildings[adding_i][0] <= -live_buildings[0][1]:
            # Start of a new block or continuation of an existing block
            x = buildings[adding_i][0]
            while adding_i < total_n and buildings[adding_i][0] == x:
                heapq.heappush(live_buildings, (-buildings[adding_i][2], -buildings[adding_i][1]))
                adding_i += 1
        else:
            # Scanning through an existing block
            x = -live_buildings[0][1]
            while live_buildings and -live_buildings[0][1] <= x:
                # Pop every interesting point hiding behind the tallest building
                heapq.heappop(live_buildings)

        # Special Case - End of a block: no more live building, height = 0
        height = -live_buildings[0][0] if live_buildings else 0
        if not skyline_out or height != skyline_out[-1][1]:
            skyline_out.append([x, height])
    return skyline_out


test_cases = [  # ([[1,5,8],[2,4,6]],[[1,8],[5,0]]),
    ([[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]],
     [[2, 10], [3, 15], [7, 12], [12, 0], [15, 10], [20, 8], [24, 0]])]
for input, output in test_cases:
    assert getSkyline(input) == output
