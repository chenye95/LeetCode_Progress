"""
Given a 2D matrix matrix, handle multiple queries of the following type:
 - Calculate the sum of the elements of matrix inside the rectangle defined by its upper left corner (row1, col1) and
  lower right corner (row2, col2).

Implement the NumMatrixCacheRectangle class:
- NumMatrixCacheRectangle(int[][] matrix) Initializes the object with the integer matrix matrix.
- int sumRegion(int row1, int col1, int row2, int col2) Returns the sum of the elements of matrix inside the rectangle
 defined by its upper left corner (row1, col1) and lower right corner (row2, col2).
"""
from copy import deepcopy
from typing import List


class NumMatrixBase:
    def sum_region(self, row_1: int, col_1: int, row_2: int, col_2: int) -> int:
        """
        :return: sum of rectangle defined by its upper left corner (row_1, col_1) and lower right corner (row_2, col_2)
        """
        pass


class NumMatrixCacheRectangle(NumMatrixBase):
    def __init__(self, matrix: List[List[int]]):
        """
        :param matrix: with 1 <= len(matrix) <= 200 and 1 <= len(matrix[0]) <= 200
        """
        m, n = len(matrix), len(matrix[0])
        # cumulative_matrix[i][j]: rectangle with upper left corner at (0, 0) and bottom right corner at (i - 1, j - 1)
        self.cumulative_matrix = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m):
            for j in range(n):
                self.cumulative_matrix[i + 1][j + 1] = self.cumulative_matrix[i + 1][j] + \
                                                       self.cumulative_matrix[i][j + 1] - \
                                                       self.cumulative_matrix[i][j] + matrix[i][j]

    def sum_region(self, row_1: int, col_1: int, row_2: int, col_2: int) -> int:
        return self.cumulative_matrix[row_2 + 1][col_2 + 1] - self.cumulative_matrix[row_2 + 1][col_1] \
               - self.cumulative_matrix[row_1][col_2 + 1] + self.cumulative_matrix[row_1][col_1]


class NumMatrixCacheRow(NumMatrixBase):
    def __init__(self, matrix: List[List[int]]):
        """
        :param matrix: with 1 <= len(matrix) <= 200 and 1 <= len(matrix[0]) <= 200; will destruct matrix
        """
        self.cumulative_matrix = matrix
        m, n = len(matrix), len(matrix[0])
        for row in self.cumulative_matrix:
            for i in range(1, n):
                row[i] += row[i - 1]

    def sum_region(self, row_1: int, col_1: int, row_2: int, col_2: int) -> int:
        return sum(self.cumulative_matrix[row_i][col_2] - (self.cumulative_matrix[row_i][col_1 - 1] if col_1 else 0)
                   for row_i in range(row_1, row_2 + 1))


test_cases = [([[3, 0, 1, 4, 2], [5, 6, 3, 2, 1], [1, 2, 0, 1, 5], [4, 1, 0, 1, 7], [1, 0, 3, 0, 5]],
               [(2, 1, 4, 3, 8), (1, 1, 2, 2, 11), (1, 2, 2, 4, 12)]),
              ([[-5208, 1041, -93779, -64152, 17850, 29055, -63731, -23568, 41170, 58457, -39616, 55683, -51662, -75015,
                 21726],
                [4535, -72412, 86878, -60825, 67088, 48794, -23471, -22403, 58200, -31153, -94668, -27274, -11003,
                 33894, -66125],
                [-9538, -33861, 54822, 42636, 48430, -56030, -33348, -30617, 5219, 56501, -95879, -73537, -18157,
                 -72815, -40977],
                [15602, 40115, -32475, 99011, 47251, 84035, 83793, -74389, -99042, 65460, 11671, -95294, 68311, 47893,
                 71866],
                [69607, 57288, 55022, 36610, -75113, 31344, 34319, -13381, -74800, -71904, -15625, -5398, -29689,
                 -68805, -41994],
                [-32276, 95017, -96452, -47311, 13238, 46324, 95358, 13247, -30930, 5815, -36748, -25712, -83982, 29391,
                 -73922],
                [-29140, -70403, -3168, 12219, -4473, -10013, -85502, 87222, -44858, 66506, -99821, -16992, -80758,
                 59210, 87145],
                [-9557, 67725, -27359, -28647, 46781, -67948, -28154, -3498, 91489, -3887, -96422, 6568, 42380, 73264,
                 -55406],
                [40555, 70153, -51490, -14237, 9684, -54000, -8443, -32063, -96157, -70083, -7050, 56221, 93013, -1157,
                 -45593],
                [-28686, -54296, 628, 11189, 18227, -64455, -10528, -69244, 94796, -39806, 69194, 45024, -14417, -51291,
                 6387],
                [-28485, 36898, 97259, -83875, 83650, -36715, 80692, -55055, 40025, -69379, -1548, -13045, 23318, 79349,
                 -42774],
                [82645, 17721, 84052, -35036, -751, 90269, -77187, 51972, -90217, -5956, -34552, 95560, 40436, 51650,
                 72778],
                [-970, 77788, 10423, -1406, -90844, 6732, -60197, 59393, -82111, 33737, -4731, -52679, -12011, 69741,
                 -91931]],
               [(3, 2, 12, 6, 82331), (11, 10, 11, 12, 101444), (7, 7, 7, 10, -12318), (7, 10, 10, 13, 303401),
                (2, 11, 5, 12, -263458), (10, 8, 10, 12, -20629), (12, 7, 12, 10, 6288), (1, 14, 9, 14, -158619),
                (11, 11, 11, 13, 187646), (7, 7, 9, 10, -162731), (12, 8, 12, 12, -117795), (1, 4, 6, 11, -398560),
                (0, 9, 9, 13, -561164), (9, 6, 9, 13, 23728), (10, 14, 11, 14, 30004), (4, 9, 7, 14, -436786),
                (5, 13, 7, 14, 119682), (12, 0, 12, 14, -139066), (9, 14, 11, 14, 36391), (2, 8, 10, 13, -474370),
                (3, 5, 12, 8, -277877), (5, 3, 11, 10, -516652), (1, 14, 11, 14, -128615), (8, 2, 11, 6, 38933),
                (3, 13, 12, 14, 175801), (4, 9, 11, 12, -278739), (7, 1, 9, 2, 5361), (0, 0, 8, 14, -702643),
                (11, 8, 12, 10, -183830), (1, 1, 10, 13, -279081)]), ]
for NumMatrix in [NumMatrixCacheRectangle, NumMatrixCacheRow, ]:
    for test_matrix, test_operations in test_cases:
        test_object = NumMatrix(deepcopy(test_matrix))
        for test_row_1, test_row_2, test_col_1, test_col_2, expected_count in test_operations:
            assert test_object.sum_region(test_row_1, test_row_2, test_col_1, test_col_2) == expected_count
