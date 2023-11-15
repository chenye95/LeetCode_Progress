"""
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red,
 Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share
 vertical or horizontal sides have the same color).

Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large,
 the answer must be computed modulo 109 + 7.
"""


def num_of_ways_math(n: int) -> int:
    """
    :param n: 1 <= n <= 5000
    :return: number of ways to color a n * 3 grid with 3 colors without any adjacent cells have the same color,
        return value mod 10 ** 9 + 7
    """
    # there are 2 types of pattern for each row: use_three_colors 123, and use_two_colors = 121,
    # each type have 6 subtypes (permutations of RGB 3 colors)
    # after use_three_colors 123, we have 212, 231, 232, 312 (use_three_colors * 2 + use_two_colors * 2)
    # after use_two_colors 121, we have 212, 213, 232, 312, 313 (use_three_colors * 2 + use_two_colors * 3)
    use_three_colors = use_two_colors = 6
    _mod_value = 10 ** 9 + 7
    for i in range(n - 1):
        use_three_colors, use_two_colors = (use_three_colors * 2 + use_two_colors * 2) % _mod_value, \
                                           (use_three_colors * 2 + use_two_colors * 3) % _mod_value
    return (use_three_colors + use_two_colors) % _mod_value


test_cases = [(2, 54),
              (3, 246),
              (7, 106494),
              (5000, 30228214), ]
for num_of_ways in [num_of_ways_math, ]:
    for test_n, expected_value in test_cases:
        assert num_of_ways(test_n) == expected_value, num_of_ways.__name__
