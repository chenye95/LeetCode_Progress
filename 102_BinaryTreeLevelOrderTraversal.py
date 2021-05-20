"""
Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right,
 level by level).
"""
from typing import List, Optional

from _Binary_Tree import TreeNode, ConstructTree, BinaryTree, TREE_NODE_TYPE


def level_order(root: Optional[TreeNode]) -> List[List[TREE_NODE_TYPE]]:
    """
    :param root: root node of a binary tree
    :return: layer by layer traversal of the tree
    """
    if root is None:
        return []

    return_list, current_level = [], [root]
    while current_level:
        return_list.append([node.val for node in current_level])
        current_level = [leaf for lr_pair in [(node.left, node.right) for node in current_level]
                         for leaf in lr_pair if leaf]
    return return_list


test_cases = [([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
              ([1], [[1]]),
              ([], []),
              (
                  [69, 73, 68, 18, 20, 18, 39, 7, -3, 13, -1, 42, 5, 93, 70, 63, 17, None, 91, -4, 30, None, -1, 64, -4,
                   16,
                   49, 48, 78, 51, 43, 92, 45, None, 53, 9, 36, 80, -6, 58, 78, None, None, 41, 81, 89, 67, 71, None,
                   25,
                   None, 82, 54, 28, 14, 61, 57, 35, 5, 83, 9, 18, None, -9, -9, 50, 92, 93, None, 0, 80, 62, 1, 28, 29,
                   27,
                   89, 21, None, 85, -9, None, 56, 56, -9, None, None, 43, None, 29, 97, -7, None, 35, 25, 90, 67, 53,
                   18,
                   61, 7, 23, 81, 37, 19, 26, 2, 0, 19, None, None, 77, 37, -2, None, 49, 39, 28, 1, 37, 11, 87, 83, 68,
                   55,
                   53, 33, -2, 22, 7, 52, None, 14, None, 18, 50, 97, -8, -7, None, 21, 59, 72, 27, None, 64, None,
                   None,
                   47, None, None, 38, 46, None, None, 99, None, None, 48, 13, 85, 78, 7, 64, 43, 59, 71, 11, 37, 12,
                   37,
                   50, 2, None, None, 89, 87, None, 78, 97, None, 31, 86, 37, 96, 34, 38, 6, 36, None, None, 99, 63,
                   None,
                   12, None, 82, None, 81, 70, 19, None, 81, 32, None, None, None, None, 79, 10, None, 91, 48, -3, 94,
                   65,
                   None, 20, 26, 96, 21, 92, 91, None, 89, 9, 74, None, None, 96, None, 64, 67, 50, 96, None, None,
                   None,
                   None, None, None, 40, 78, None, 27, 3, 17, None, None, 2, 45, None, None, None, None, None, 13, None,
                   None, 17, 45, 69, 30, None, None, 43, None, 4, 13, -6, 66, 6, None, 16, 48, 55, 98, 69, 57, None, 5,
                   9,
                   65, -9, 55, 2, None, None, None, None, None, None, 68, None, None, None, 5, 61, 51, None, None, 32,
                   43,
                   None, 35, 20, None, -7, 38, 30, 1, 80, None, None, 42, 86, 42, None, None, None, None, 47, None,
                   None,
                   None, 62, 29, -9, 83, 60, 71, 48, None, 24, None, 76, 6, 65, 18, 95, 29, 11, None, 38, None, None,
                   None,
                   None, 21, 3, 6, 23, 36, None, 45, None, 34, None, None, None, None, None, None, 41, None, 57, 13, 18,
                   92,
                   43, 83, None, None, None, None, None, None, None, 2, -4, 97, None, 93, None, 62, None, None, 48, 18,
                   71,
                   92, 53, 89, None, None, None, 95, None, 16, None, None, None, 83, 87, 5, None, None, 3, -8, -4, 65,
                   None,
                   None, None, 22, None, 31, None, None, None, 63, None, None, 62, None, 57, 12, 85, 45, 23, 55, None,
                   None,
                   None, 81, 83, 23, None, 3, None, 83, None, -4, None, None, None, None, None, 64, None, 15, 50, 57,
                   None,
                   None, None, 4, None, None, None, 29, None, None, 87, None, 22, 92, None, None, 67, 90, None, 93, 47,
                   46,
                   None, None, None, 28, 72, 18, 59, 25, 3, 74, None, None, None, -5, 28, -1, 61, 15, None, None, None,
                   None, 79, None, 16, None, None, 59, 47, -7, 98, 31, 50, None, None, None, None, 19, None, 93, None,
                   22,
                   None, None, -5, 40, None, None, None, 75, 30, None, 7, 53, 76, None, None, None, None, None, 68, 19,
                   None, 63, 41, 91, None, 43, None, 49, None, None, None, None, None, 46, None, None, 87, 74, 49, 1,
                   21,
                   62, 6, 34, 77, None, None, None, None, None, None, -9, 61, None, None, None, 7, None, 45, None, None,
                   63,
                   None, None, 7, None, None, 16, 86, None, None, 63, None, 61, 72, None, 13, None, 24, 91, None, None,
                   59,
                   None, None, 48, 14, 77, None, None, None, None, 92, None, None, None, None, None, None, 84, None,
                   None,
                   76, 82, 63, 84, 84, 94, None, None, None, None, None, 47, 40, None, None, None, None, 75, 20, None,
                   None,
                   None, -9, None, None, 24, 74, None, 51, None, None, 91, None, 83, 17, None, None, None, 42, 49, 88,
                   57,
                   85, 1, None, 94, None, 28, 36, 78, None, 53, None, 27, 25, 46, 97, 58, None, None, None, None, None,
                   None, None, None, 12, 33, None, None, 6, None, None, None, 87, None, None, None, None, None, None,
                   None,
                   9, None, 83, None, None, None, 90, 11, None, 61, None, 89, None, 46, None, 86, 81, None, None, None,
                   None, None, None, None, 53, None, None, 59, None, None, None, None, None, None, None, 29, None, 47,
                   97,
                   0, None, None, None, None, 9, None, 17, None, 91, 45, 9, 61, 21, None, None, 64, None, 69, None, 44,
                   None, None, None, None, 12, None, 2, -8, 88, None, None, None, None, None, -8, None, 93, None, None,
                   None, 86, None, None, 97, None, None, None, None, 72, None, None, None, None, None, 50, None, None,
                   None,
                   None, None, 47, 70, None, 62, None, -3, -5, 59, 15, None, -3, 37, None, None, None, None, 20, -2,
                   None,
                   8, 90, None, None, None, 61, None, None, None, None, None, None, None, 15, 12, 95, None, None, 73,
                   11,
                   76, 76, 49, None, None, 51, None, None, None, None, None, None, None, None, None, None, None, None,
                   None,
                   42, None, None, -9, None, None, None, None, None, None, None, None, 80, None, None, 70, 31, 78, 98,
                   None,
                   None, None, None, None, None, None, None, None, None, None, None, 7, None, None, None, None, 57,
                   None,
                   None, None, None, -3, None, None, -7, None, 31, 42, None, None, None, None, 62, 17, 7, None, None,
                   63,
                   None, None, None, None, 83, 51, None, 76, 77, None, None, 40, None, None, 95, None, 27, 55, 61, None,
                   None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                   None, 95, None, 93, 19, None, 37, None, 73, None, None, None, None, None, 75, None, None, None, None,
                   None, 22, None, None, None, None, None, -7, 99, None, None, None, None, None, 94, 63, None, None,
                   None,
                   None, None, None, None, 39, 77, None, -2, 15, None, 69, 33, 9, None, None, None, None, None, None,
                   None,
                   None, None, 42, None, None, None, 69, 35, None, 36, None, 11, None, None, None, 52, None, None, None,
                   None, None, None, None, 51, 50, None, None, None, None, None, None, 30, None, None, None, None, None,
                   63,
                   None, None, None, None, None, None, 56, 28],
                  [[69], [73, 68], [18, 20, 18, 39], [7, -3, 13, -1, 42, 5, 93, 70],
                   [63, 17, 91, -4, 30, -1, 64, -4, 16, 49, 48, 78, 51, 43],
                   [92, 45, 53, 9, 36, 80, -6, 58, 78, 41, 81, 89, 67, 71, 25, 82, 54, 28, 14, 61, 57, 35, 5],
                   [83, 9, 18, -9, -9, 50, 92, 93, 0, 80, 62, 1, 28, 29, 27, 89, 21, 85, -9, 56, 56, -9, 43, 29, 97, -7,
                    35,
                    25, 90, 67, 53, 18, 61, 7, 23, 81, 37, 19],
                   [26, 2, 0, 19, 77, 37, -2, 49, 39, 28, 1, 37, 11, 87, 83, 68, 55, 53, 33, -2, 22, 7, 52, 14, 18, 50,
                    97,
                    -8, -7, 21, 59, 72, 27, 64, 47, 38, 46, 99, 48, 13, 85, 78, 7, 64, 43, 59, 71, 11, 37, 12, 37, 50,
                    2,
                    89, 87, 78, 97],
                   [31, 86, 37, 96, 34, 38, 6, 36, 99, 63, 12, 82, 81, 70, 19, 81, 32, 79, 10, 91, 48, -3, 94, 65, 20,
                    26,
                    96, 21, 92, 91, 89, 9, 74, 96, 64, 67, 50, 96, 40, 78, 27, 3, 17, 2, 45, 13, 17, 45, 69, 30, 43, 4,
                    13,
                    -6, 66, 6, 16, 48, 55, 98, 69, 57, 5, 9, 65, -9, 55, 2, 68],
                   [5, 61, 51, 32, 43, 35, 20, -7, 38, 30, 1, 80, 42, 86, 42, 47, 62, 29, -9, 83, 60, 71, 48, 24, 76, 6,
                    65,
                    18, 95, 29, 11, 38, 21, 3, 6, 23, 36, 45, 34, 41, 57, 13, 18, 92, 43, 83, 2, -4, 97, 93, 62, 48, 18,
                    71,
                    92, 53, 89, 95, 16, 83, 87, 5, 3, -8, -4, 65, 22, 31, 63, 62, 57, 12, 85, 45, 23, 55],
                   [81, 83, 23, 3, 83, -4, 64, 15, 50, 57, 4, 29, 87, 22, 92, 67, 90, 93, 47, 46, 28, 72, 18, 59, 25, 3,
                    74,
                    -5, 28, -1, 61, 15, 79, 16, 59, 47, -7, 98, 31, 50, 19, 93, 22, -5, 40, 75, 30, 7, 53, 76, 68, 19,
                    63,
                    41, 91, 43, 49, 46, 87, 74, 49, 1, 21, 62, 6, 34, 77, -9, 61, 7, 45, 63, 7, 16],
                   [86, 63, 61, 72, 13, 24, 91, 59, 48, 14, 77, 92, 84, 76, 82, 63, 84, 84, 94, 47, 40, 75, 20, -9, 24,
                    74,
                    51, 91, 83, 17, 42, 49, 88, 57, 85, 1, 94, 28, 36, 78, 53, 27, 25, 46, 97, 58, 12, 33, 6, 87, 9, 83,
                    90,
                    11, 61, 89, 46, 86, 81, 53, 59],
                   [29, 47, 97, 0, 9, 17, 91, 45, 9, 61, 21, 64, 69, 44, 12, 2, -8, 88, -8, 93, 86, 97, 72, 50, 47, 70,
                    62,
                    -3, -5, 59, 15, -3, 37, 20, -2, 8, 90, 61, 15, 12, 95, 73, 11, 76, 76, 49, 51],
                   [42, -9, 80, 70, 31, 78, 98, 7, 57, -3, -7, 31, 42, 62, 17, 7, 63, 83, 51, 76, 77, 40, 95, 27, 55,
                    61],
                   [95, 93, 19, 37, 73, 75, 22, -7, 99, 94, 63, 39, 77, -2, 15], [69, 33, 9, 42, 69, 35, 36, 11, 52],
                   [51, 50, 30], [63], [56], [28]]), ]
for test_tree_list, expected_output in test_cases:
    if test_tree_list:
        assert ConstructTree.build_tree_leetcode(test_tree_list).layer_traversal_by_layer() == expected_output
    else:
        assert BinaryTree(root=None).layer_traversal_by_layer() == expected_output
for test_tree_list, expected_output in test_cases:
    assert level_order((ConstructTree.build_tree_leetcode(test_tree_list).root if test_tree_list else None)) == \
           expected_output
