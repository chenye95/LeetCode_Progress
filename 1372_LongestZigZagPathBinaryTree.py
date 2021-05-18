"""
You are given the root of a binary tree.

A ZigZag path for a binary tree is defined as follow:
- Choose any node in the binary tree and a direction (right or left).
- If the current direction is right, move to the right child of the current node; otherwise, move to the left child.
- Change the direction from right to left or from left to right.
- Repeat the second and third steps until you can't move in the tree.

Zigzag length is defined as the number of nodes visited - 1. (A single node has a length of 0).

Return the longest ZigZag path contained in that tree.
"""
from typing import Tuple

from _Binary_Tree import TreeNode, ConstructTree


def longest_zig_zag_all(root: TreeNode) -> int:
    """
    :param root: root of a binary tree with 1 <= no of nodes <= 50000
    :return: longest zig zag path in the tree
    """

    def _helper_longest_path(current_node: TreeNode) -> Tuple[int, int]:
        """
        :param current_node: inspecting the sub tree beneath current_node
        :return: (1 + longest path from left node, 1 + longest path from right node)
        """
        nonlocal global_max
        _, path_left_right = _helper_longest_path(current_node.left) if current_node.left else (-1, -1)
        path_right_left, _ = _helper_longest_path(current_node.right) if current_node.right else (-1, -1)
        global_max = max(global_max, 1 + path_right_left, 1 + path_left_right)
        return 1 + path_left_right, 1 + path_right_left

    global_max = 0
    _helper_longest_path(root)
    return global_max


test_cases = [([1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1, None, 1], 3),
              ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4), ]
for longest_zig_zag in [longest_zig_zag_all, ]:
    for test_tree_list, expected_output in test_cases:
        assert longest_zig_zag(ConstructTree.build_tree_leetcode(test_tree_list).root) == expected_output, \
            longest_zig_zag.__name__
