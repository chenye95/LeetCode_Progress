"""
An n x n grid is composed of 1 x 1 squares where each 1 x 1 square consists of a '/', '\', or blank space ' '. These
 characters divide the square into contiguous regions.

Given the grid grid represented as a string array, return the number of regions.

Note that backslash characters are escaped, so a '\' is represented as '\\'.
"""
from typing import List

from _Union_Find import UnionFindArray


def regions_by_slashes(grid: List[str]) -> int:
    """
    For each grid cell split into 4 sub cells: [0 - up, 1 - left, 2 - right, 3 - down]

    :param grid: 1 <= len(grid) == len(grid[0]) <= 30, and grid[i][j] in ('/', '\', ' ')
    :return: number of regions in the grid
    """
    n = len(grid)
    union_find_object = UnionFindArray(4 * n * n)
    for r, row_r in enumerate(grid):
        for c, cell_r_c in enumerate(row_r):
            cell_up_position = 4 * (r * n + c)
            if cell_r_c == '/':
                union_find_object.unify(cell_up_position + 0, cell_up_position + 1)
                union_find_object.unify(cell_up_position + 2, cell_up_position + 3)
            elif cell_r_c == '\\':
                union_find_object.unify(cell_up_position + 0, cell_up_position + 2)
                union_find_object.unify(cell_up_position + 1, cell_up_position + 3)
            else:
                union_find_object.unify(cell_up_position + 0, cell_up_position + 1)
                union_find_object.unify(cell_up_position + 0, cell_up_position + 2)
                union_find_object.unify(cell_up_position + 0, cell_up_position + 3)

            # Connect up
            if r > 0:
                union_find_object.unify(cell_up_position + 0, cell_up_position - 4 * n + 3)
            # Connect down
            if r + 1 < n:
                union_find_object.unify(cell_up_position + 3, cell_up_position + 4 * n + 0)
            # Connect left
            if c > 0:
                union_find_object.unify(cell_up_position + 1, cell_up_position - 4 + 2)
            # Connect right
            if c + 1 < n:
                union_find_object.unify(cell_up_position + 2, cell_up_position + 4 + 1)

    return union_find_object.components_count()


test_cases = [([" /", "/ "], 2),
              ([" /", "  "], 1),
              (["\\/", "/\\"], 4),
              (["/\\", "\\/"], 5),
              (["//", "/ "], 3),
              (["\\/\\\\\\/", "\\/\\\\/\\", "\\/// /", " \\ ///", " \\/\\ /", "//\\//\\"], 9),
              (["\\\\/// \\\\\\\\ //\\ \\\\ \\/\\\\// \\/\\//", "/\\\\/ \\//////\\  \\///\\ /\\/\\/\\/\\\\",
                "\\/ /\\\\//\\\\//\\//// /\\ ///\\/\\\\ \\", "\\\\// / \\\\ \\\\/\\ /\\\\\\/\\\\/  \\\\/\\\\",
                " /// \\\\\\\\ //\\ \\\\\\/\\//// \\\\\\/  ", "\\/\\\\\\//\\ /\\ \\\\\\/\\   \\/ //\\ \\//",
                "/\\//\\\\// /\\\\\\\\\\// \\\\ //\\/\\\\ /\\", "/\\/  /\\\\  \\\\//\\/ //\\\\///\\\\ \\\\/",
                "//\\ //\\ \\/\\\\/\\/\\/ ///\\\\\\\\\\\\\\//", "\\/\\/// \\\\\\//\\\\// \\//\\/\\\\/ \\ / ",
                "\\ / \\\\//\\\\ \\\\/\\//\\// \\/  \\/\\\\\\", "\\\\ /\\\\\\// \\/// / ///\\/// /  \\ ",
                "/\\\\\\  /\\/\\ \\\\//// \\\\/ /\\\\/\\\\//", " \\\\\\/ \\\\/ /\\\\//\\/\\\\\\\\\\ \\//// \\",
                "\\// //\\/\\////// \\\\/ / \\\\///\\\\/", " //\\\\ \\\\  /\\\\\\/\\  \\\\ \\\\/ \\/\\ \\",
                "////\\/\\\\ //\\/\\ /\\///\\///\\ \\\\//", " /\\ \\\\\\\\\\ \\  //\\/\\\\/\\\\\\/\\\\/\\\\/",
                "/\\//\\ / / ///\\/ \\\\/\\/\\\\//\\/ \\\\", "\\\\\\/\\/////\\/ ///// //  \\\\/ \\\\ ",
                "//\\\\ / /  ///// //// \\\\\\\\//\\/\\", "////\\ ///\\///\\\\/\\\\ \\\\\\/\\ /\\\\/ ",
                "/\\//\\\\/ /\\ \\ \\\\/\\ \\/\\// \\\\/\\/ ", "/\\// /\\\\ \\ \\ /\\\\\\ \\////\\ \\\\\\/\\",
                "/\\/ \\//\\\\\\\\\\//\\/ \\  //\\ \\// //", "//   /\\  \\\\ / / //// \\// /\\ \\/",
                "\\/\\ /\\/\\\\// \\\\\\ \\ / \\///\\// /\\", "/ /\\\\\\// \\ ///\\ \\ \\\\ \\/\\\\ /\\/ ",
                "\\\\\\ ///\\\\\\\\\\\\\\ /\\ \\/\\\\/ /  \\\\\\", " / /\\  \\  //\\//// \\/\\\\ / /\\/\\/"], 51),
              ([" \\/ /\\/  /\\////\\////", "\\\\//\\\\/  /// \\//\\//\\", "   \\\\\\/ \\/\\//\\// /  ",
                "\\\\/\\/\\\\\\\\/\\\\/\\/// /\\", "\\\\////\\\\\\  \\// ////\\", "\\\\\\/ /\\/ /\\\\///\\/\\\\/",
                "\\/\\/ \\\\\\\\\\/\\\\// \\///", "/ /  //\\/\\\\\\ \\\\\\\\\\ \\", "\\\\\\\\\\ ///\\  ///\\\\ //",
                " \\\\ \\//\\/\\/ \\/\\/\\  /", "\\\\\\/\\\\/ \\\\ \\ \\\\ //\\ ", "/\\ //\\\\\\/ \\\\\\/ // /\\",
                "/\\\\// /\\\\\\/\\\\\\/// \\ ", "\\// / /////\\ /  \\\\\\ ", " \\\\//\\   \\\\//\\\\ \\\\ \\",
                "/\\//\\/// /\\ ///\\ \\\\\\", "\\\\\\\\\\\\/// \\ \\//\\///\\", "\\//// \\\\/\\// \\ // //",
                " /// \\ //\\///  \\\\// ", " \\\\\\\\/\\\\/\\ \\\\//\\\\///"], 29), ]
for test_grid, expected_count in test_cases:
    assert regions_by_slashes(test_grid) == expected_count, test_grid
