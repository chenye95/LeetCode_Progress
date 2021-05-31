"""
A rhombus sum is the sum of the elements that form the border of a regular rhombus shape in grid. The rhombus must have
 the shape of a square rotated 45 degrees with each of the corners centered in a grid cell. Below is an image of four
 valid rhombus shapes with the corresponding colored cells that should be included in each rhombus sum.

Note that the rhombus can have an area of 0, which is depicted by the purple rhombus in the bottom right corner.

Return the biggest three distinct rhombus sums in the grid in descending order. If there are less than three distinct
 values, return all of them.
"""
import heapq
from copy import deepcopy
from typing import List


def get_biggest_rhombus_sums_calculate(grid: List[List[int]], top_n: int = 3) -> List[int]:
    """
    :param grid: 1 <= len(grid), len(grid[0]) <= 50, and 1 <= grid[i][j] <= 10**5
    :param top_n: default to 3
    :return: return at most top_n rhombus sums
    """
    m, n = len(grid), len(grid[0])

    top_rhombus_sums = sorted({grid_i_j for grid_i in grid for grid_i_j in grid_i})
    top_rhombus_sums = top_rhombus_sums[-min(top_n, len(top_rhombus_sums)):]

    # side len starting from 0
    max_side = (min(m, n) - 1) // 2
    for side_len in range(1, max_side + 1):
        for start_y in range(m - 2 * side_len):
            for start_x in range(side_len, n - side_len):
                rhombus_sum = grid[start_y][start_x] + grid[start_y + 2 * side_len][start_x]
                for step_i in range(1, side_len + 1):
                    rhombus_sum += grid[start_y + step_i][start_x - step_i]
                    rhombus_sum += grid[start_y + step_i][start_x + step_i]
                for step_i in range(1, side_len):
                    rhombus_sum += grid[start_y + side_len + step_i][start_x - side_len + step_i]
                    rhombus_sum += grid[start_y + side_len + step_i][start_x + side_len - step_i]

                if rhombus_sum not in top_rhombus_sums and rhombus_sum > top_rhombus_sums[0]:
                    heapq.heappush(top_rhombus_sums, rhombus_sum)
                    if len(top_rhombus_sums) > top_n:
                        heapq.heappop(top_rhombus_sums)

    return sorted(top_rhombus_sums, reverse=True)


def get_biggest_rhombus_sums_partial_memory(grid: List[List[int]], top_n: int = 3) -> List[int]:
    """
    :param grid: 1 <= len(grid), len(grid[0]) <= 50, and 1 <= grid[i][j] <= 10**5
    :param top_n: default to 3
    :return: return at most top_n rhombus sums
    """
    m, n = len(grid), len(grid[0])

    top_rhombus_sums = sorted({grid_i_j for grid_i in grid for grid_i_j in grid_i})
    top_rhombus_sums = top_rhombus_sums[-min(top_n, len(top_rhombus_sums)):]

    # side len starting from 0
    max_side = (min(m, n) - 1) // 2
    if not max_side:
        return top_rhombus_sums

    partial_memory = deepcopy(grid)

    for side_len in range(1, max_side + 1):
        for start_y in range(m - 2 * side_len):
            for start_x in range(side_len, n - side_len):
                rhombus_sum = partial_memory[start_y][start_x] + \
                              grid[start_y + side_len][start_x - side_len] + \
                              grid[start_y + side_len][start_x + side_len]
                partial_memory[start_y][start_x] = rhombus_sum

                rhombus_sum += grid[start_y + 2 * side_len][start_x]
                for step_i in range(1, side_len):
                    rhombus_sum += grid[start_y + side_len + step_i][start_x - side_len + step_i]
                    rhombus_sum += grid[start_y + side_len + step_i][start_x + side_len - step_i]

                if rhombus_sum not in top_rhombus_sums and rhombus_sum > top_rhombus_sums[0]:
                    heapq.heappush(top_rhombus_sums, rhombus_sum)
                    if len(top_rhombus_sums) > top_n:
                        heapq.heappop(top_rhombus_sums)

    return sorted(top_rhombus_sums, reverse=True)


test_cases = [
    ([[3, 4, 5, 1, 3], [3, 3, 4, 2, 3], [20, 30, 200, 40, 10], [1, 5, 5, 4, 1], [4, 3, 2, 2, 5]], [228, 216, 211]),
    ([[1, 2, 3], [4, 5, 6], [7, 8, 9]], [20, 9, 8]),
    ([[7, 7, 7]], [7]),
    ([[8, 20, 12, 14, 12, 18],
      [8, 17, 6, 4, 4, 10],
      [20, 13, 7, 18, 19, 16],
      [3, 17, 20, 5, 18, 13],
      [2, 7, 17, 12, 6, 7],
      [19, 2, 10, 11, 20, 2],
      [1, 1, 17, 1, 14, 4],
      [9, 11, 2, 14, 11, 16],
      [14, 7, 2, 5, 11, 20]], [111, 103, 101]),
    ([[92504, 93344, 61229, 59462, 41072, 3482, 50747, 32759, 94801, 16599, 90142],
      [89375, 61007, 26445, 26904, 23773, 32743, 13136, 61574, 38350, 91779, 93896],
      [87566, 99334, 4628, 3331, 38408, 83010, 80830, 90192, 95004, 92843, 17699],
      [93686, 78031, 70434, 91407, 66065, 75298, 80500, 92142, 60061, 61851, 19609],
      [19238, 71907, 17547, 45770, 80709, 77802, 14470, 81567, 98660, 7857, 32538],
      [52812, 53468, 88189, 14834, 49629, 19570, 83404, 28705, 70596, 11762, 99643],
      [19811, 37801, 67774, 92057, 67855, 79048, 15301, 63865, 39385, 61163, 48913],
      [45547, 55732, 11722, 6588, 46639, 94519, 41384, 65537, 6519, 10384, 99234],
      [48563, 71407, 39615, 59367, 92211, 22603, 78084, 34608, 23754, 24763, 95710],
      [13890, 43881, 73356, 75789, 28405, 80659, 5601, 6965, 24436, 65882, 12074],
      [50468, 73615, 24521, 31094, 85222, 51212, 61075, 11844, 3078, 47570, 4617],
      [78952, 29183, 41707, 86805, 98986, 8923, 85277, 78594, 31018, 85650, 76159],
      [50627, 62221, 4068, 90514, 18244, 67489, 48008, 83642, 3702, 86052, 34269],
      [65610, 91921, 22471, 80028, 87185, 58903, 10091, 39863, 14811, 29042, 91684],
      [79247, 45684, 57048, 69720, 64383, 31764, 4974, 97587, 61140, 3216, 61696],
      [82762, 87537, 34414, 86132, 19050, 29382, 71681, 117, 22308, 9065, 32497],
      [79795, 59689, 96114, 47102, 31846, 37743, 14430, 30486, 35413, 17902, 90172],
      [56360, 97782, 40177, 41547, 49171, 48376, 28173, 5044, 44313, 83019, 99331],
      [90388, 90654, 47894, 49072, 64040, 48189, 23650, 37526, 92497, 18346, 54857],
      [5797, 33321, 68457, 15144, 96449, 44850, 94833, 32940, 28708, 73705, 39390],
      [85357, 8270, 96839, 83874, 53276, 71481, 54040, 44462, 10318, 51707, 82802],
      [64024, 49515, 87766, 37084, 9980, 53564, 55177, 59162, 66336, 72957, 55637],
      [38254, 67239, 31965, 38362, 933, 3798, 88485, 17099, 74614, 60868, 90663],
      [78260, 70575, 66507, 25934, 4548, 50422, 63260, 54240, 84418, 96975, 14365],
      [81530, 5802, 77912, 87501, 21510, 7126, 90224, 12341, 25278, 85748, 16244],
      [87708, 50791, 32320, 31184, 96154, 41460, 4030, 26938, 82816, 68850, 65126]], [1248094, 1122514, 1122351]),
]
for get_biggest_rhombus_sums in [get_biggest_rhombus_sums_calculate, get_biggest_rhombus_sums_partial_memory, ]:
    for test_grid, expected_value in test_cases:
        assert get_biggest_rhombus_sums(test_grid) == expected_value, get_biggest_rhombus_sums.__name__
