"""
Given an integer array nums where the elements are sorted in ascending order, convert it to a height-balanced binary
 search tree.

A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by
 more than one.
"""
from typing import List

from _BST import BST, TREE_NODE_TYPE


def sorted_array_bst(values: List[TREE_NODE_TYPE]) -> BST:
    """
    :param values: 1 <= number of nodes <= 10000
    :return: root of the TreeNode
    """
    return BST(values)


test_cases = [[-10, -3, 0, 5, 9],
              [1, 3],
              [-99, -98, -97, -96, -94, -93, -91, -90, -88, -87, -86, -85, -83, -81, -80, -79, -78, -76, -73, -72, -70,
               -69, -66, -65, -64, -63, -61, -59, -57, -56, -55, -54, -53, -52, -51, -48, -45, -44, -43, -42, -41, -40,
               -39, -37, -34, -33, -32, -31, -30, -28, -26, -24, -22, -20, -19, -18, -16, -15, -14, -12, -10, -9, -8,
               -6, -5, -4, -3, -2, -1, 0, 1, 2, 5, 7, 8, 9, 10, 11, 15, 16, 17, 19, 20, 21, 23, 24, 26, 27, 28, 30, 33,
               35, 36, 38, 49, 50, 51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 64, 65, 67, 69, 70, 71, 72, 73, 74, 77, 79,
               81, 82, 85, 86, 87, 88, 90, 91, 94, 95, 96, 97, 99],
              [9, 12, 14, 17, 19, 23, 50, 54, 67, 72, 76],
              [100],
              ]
for test_sorted_list in test_cases:
    assert sorted_array_bst(test_sorted_list).is_valid()
