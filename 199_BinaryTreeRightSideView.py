"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.
"""
# Only as placeholder for test cases
from _Binary_Tree import ConstructTree

test_cases = [([1, 2, 3, None, 5, None, 4], [1, 3, 4]),
              ([1, None, 3], [1, 3]),
              ([], []),
              ([23, 28, None, 21, None, 6, 19, 48, 8, None, None, None, None, 22, 31, None, None, 4, 36, 34, 30, None,
                None, None, None, 27, 2, None, None, 3, 26, None, None, 55, None, 1, None, 15, 41, None, None, 37, 39,
                14, 51, None, None, None, None, 46, None, 32, 12, None, None, 45, 9, None, None, 29, 10, None, None,
                None, 18, 43, 25, 47, 50, None, 7, None, None, None, None, 40, 44, 17, None, None, None, 49, None, 35,
                20, 11, 54, 53, 5, None, None, 52, 33, None, None, None, 16, None, None, 42, 38, None, None, None, None,
                13, 24, None, None, None, None],
               [23, 28, 21, 19, 8, 31, 36, 30, 2, 26, 55, 1, 41, 39, 51, 46, 12, 9, 10, 18, 25, 7, 44, 17, 49, 20, 5,
                16, 38, 24]), ]
for test_tree, expected_output in test_cases:
    if expected_output:
        assert ConstructTree.build_tree_leetcode(test_tree).right_side_view() == expected_output
    else:
        assert ConstructTree.build_tree_leetcode(test_tree) is None
