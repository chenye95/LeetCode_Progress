"""
Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may
 not pass through the root.

The length of a path between two nodes is represented by the number of edges between them.
"""
from typing import Tuple

from _Binary_Tree import TreeNode, ConstructTree


def diameter_of_binary_tree_local_parameter(root: TreeNode) -> int:
    """
    :param root: root of a binary tree, with 1 <= number of nodes <= 1_000_000
    :return: length of the longest path between any two nodes in the tree
    """

    def _helper_within_sub_tree(current_node: TreeNode) -> Tuple[int, int]:
        """
        :param current_node: inspecting the sub tree beneath current_node. Assuming current_node is not None
        :return: (diameter of the sub tree, 1 + longest path from a leaf to current_node, i.e. no of nodes on the path)
        """
        l_left, l_left_node = _helper_within_sub_tree(current_node.left) if current_node.left else (0, 0)
        l_right, l_right_node = _helper_within_sub_tree(current_node.right) if current_node.right else (0, 0)
        l_diameter_current = max(l_left, l_right, l_left_node + l_right_node)
        l_current_node = 1 + max(l_left_node, l_right_node)
        return l_diameter_current, l_current_node

    return _helper_within_sub_tree(root)[0]


def diameter_of_binary_tree_global_parameter(root: TreeNode) -> int:
    """
    :param root: root of a binary tree, with 1 <= number of nodes <= 1_000_000
    :return: length of the longest path between any two nodes in the tree
    """

    def _helper_within_sub_tree(current_node: TreeNode) -> int:
        """
        :param current_node: inspecting the sub tree beneath current_node. Assuming current_node is not None
        :return: 1 + longest path from a leaf to current_node, i.e. no of nodes on the path
        """
        nonlocal global_max
        l_left_node = _helper_within_sub_tree(current_node.left) if current_node.left else 0
        l_right_node = _helper_within_sub_tree(current_node.right) if current_node.right else 0
        global_max = max(global_max, l_left_node + l_right_node)
        l_current_node = 1 + max(l_left_node, l_right_node)
        return l_current_node

    global_max = 0
    _helper_within_sub_tree(root)
    return global_max


test_cases = [([1, 2, 3, 4, 5], 3),
              ([1, 2], 1),
              ([3, 1, None, 4, None, 2, None, 5], 4),
              ([-64, 12, 18, -4, -53, None, 76, None, -51, None, None, -93, 3, None, -31, 47, None, 3, 53, -81, 33, 4,
                None, -51, -44, -60, 11, None, None, None, None, 78, None, -35, -64, 26, -81, -31, 27, 60, 74, None,
                None, 8, -38, 47, 12, -24, None, -59, -49, -11, -51, 67, None, None, None, None, None, None, None, -67,
                None, -37, -19, 10, -55, 72, None, None, None, -70, 17, -4, None, None, None, None, None, None, None, 3,
                80, 44, -88, -91, None, 48, -90, -30, None, None, 90, -34, 37, None, None, 73, -38, -31, -85, -31, -96,
                None, None, -18, 67, 34, 72, None, -17, -77, None, 56, -65, -88, -53, None, None, None, -33, 86, None,
                81, -42, None, None, 98, -40, 70, -26, 24, None, None, None, None, 92, 72, -27, None, None, None, None,
                None, None, -67, None, None, None, None, None, None, None, -54, -66, -36, None, -72, None, None, 43,
                None, None, None, -92, -1, -98, None, None, None, None, None, None, None, 39, -84, None, None, None,
                None, None, None, None, None, None, None, None, None, None, -93, None, None, None, 98], 18), ]
for diameter_of_binary_tree in [diameter_of_binary_tree_local_parameter, diameter_of_binary_tree_global_parameter, ]:
    for test_tree_list, expected_output in test_cases:
        assert diameter_of_binary_tree(ConstructTree.build_tree_leetcode(test_tree_list).root) \
               == expected_output, diameter_of_binary_tree.__name__
