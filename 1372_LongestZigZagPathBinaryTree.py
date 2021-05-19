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
              ([1, 1, 1, None, 1, None, None, 1, 1, None, 1], 4),
              ([1, 9, 9, 2, 6, 10, 8, 1, 4, 9, 5, 8, 2, 3, 3, 5, 2, 2, 2, 6, 7, 4, 8, 3, 3, 1, 7, None, None, 1, 6, 6,
                10, 3, 3, 9, None, 6, 9, 7, 2, 3, 7, 10, 6, 9, 5, 1, 10, 1, 1, 4, 2, 4, 5, 9, 10, 1, 6, 8, 6, 6, 7, 7,
                5, 8, None, None, None, 8, 8, 3, None, 8, 1, 8, 1, 4, None, 5, 8, 2, 9, 8, 4, 6, 1, 4, 4, 4, 2, 9, 6,
                None, None, 7, None, 5, 10, None, 2, 9, 10, 5, None, None, 4, None, 2, 5, 10, 6, 2, 3, 7, 10, 2, None,
                8, 10, 3, 9, 5, 5, 5, 4, 6, None, None, None, 10, None, 8, 7, 8, None, 5, 2, 4, 6, 4, 10, 1, None, None,
                4, 9, 3, 5, 3, 8, 4, 8, 8, None, None, None, 2, None, 4, 9, None, None, 3, 2, None, None, 4, 4, 6, 2,
                None, None, None, None, 7, 5, None, None, 8, 4, 10, 6, 10, None, None, 3, None, None, 1, 7, 5, 10, None,
                None, None, 3, 4, 1, 5, 3, 1, 10, 9, 10, 2, 1, None, 6, 4, None, 4, None, None, 1, 9, None, 6, 3, 2,
                None, 9, 9, None, None, None, None, 3, None, None, None, None, None, 2, None, 2, 3, None, None, 5, 3, 3,
                3, 9, None, None, 10, 4, 8, 9, 1, None, None, 2, 3, 5, 10, 4, 3, 8, None, None, 3, None, 6, 5, 10, 5,
                None, None, None, None, 7, 8, 3, None, None, 3, 10, 10, 8, None, None, 5, None, 9, 9, 7, 4, 7, 3, 7, 2,
                None, None, None, None, None, 4, 9, None, None, 9, 5, 4, 10, None, 3, 5, 9, 4, 1, 7, 5, 6, 7, 5, 10, 10,
                None, None, None, 9, 9, 3, 10, 3, 7, 1, None, 10, 2, 9, None, 3, 7, 3, 3, 3, None, 4, 3, 8, 10, 9, 4, 6,
                None, None, None, None, None, None, None, None, 9, None, None, None, None, None, 2, None, 4, 1, 5, None,
                3, 6, 3, None, 8, None, 6, None, 3, None, 5, 4, 9, 10, None, None, None, 5, 6, None, None, None, None,
                None, None, None, None, None, None, 1, None, None, None, None, None, None, None, None, 3, None, 5, 9, 8,
                None, 4, 2, None, None, None, None, None, None, 7, None, None, None, 4, None, 2, None, 2, 7, None, None,
                5, None, None, 5, None, None, 7, 6, 5, 4, None, None, None, None, None, 2, 3, None, 5, 2, 1, 4, 4, 2, 9,
                3, 7, 1, 9, None, None, 10, 10, 9, 7, 1, None, 4, 5, 10, 3, None, 5, 1, None, None, None, None, None,
                None, None, 3, 3, 6, 2, 7, 7, None, None, 10, None, None, None, None, 5, 3, None, 3, 9, 7, 4, 7, None,
                9, 2, 5, None, 4, 1, 3, None, 2, None, 9, 5, 8, None, None, 6, None, 2, None, 4, None, None, None, 6,
                None, None, None, 2, None, 4, 8, None, 10, None, 5, None, None, 7, 7, None, None, None, None, None,
                None, 9, 3, 5, 5, None, 8, None, None, 3, None, None, None, 10, None, None, None, None, 2, None, None,
                None, None, None, 6, 5, None, None, None, 7, 10, None, None, None, 8, None, 5, None, None, None, None,
                5, 8, 7, 3, 6, 6, 6, 8, 5, 6, 5, None, None, None, 3, 4, None, None, None, None, None, None, 10, 5, 3,
                8, None, 9, None, None, 3, 10, 5, None, 7, 8, 6, None, 5, 2, None, None, 7, 3, 2, 7, 1, 3, 10, 6, None,
                None, None, None, None, None, 4, 3, None, None, 6, 8, 2, None, None, None, None, None, None, None, 4, 4,
                8, 3, 9, 9, None, None, None, None, None, None, None, None, 7, None, None, None, None, None, 3, 9, 3, 8,
                6, None, 5, None, None, 2, None, None, 3, None, 10, None, None, 4, None, None, None, None, None, 3,
                None, None, 8, 1, None, None, None, 7, None, None, None, 6, None, 4, 5, 3, 3, None, 10, None, None,
                None, 3, None, 2, 8, 6, None, None, None, 8, 10, 8, 9, 8, 2, 5, 8, None, None, None, 8, 6, None, 7, 5,
                10, 5, 2, 10, 8, None, 4, None, 6, 5, 6, 2, None, 9, 3, None, None, 2, None, 7, None, None, None, 5,
                None, None, 1, 4, None, None, 8, 5, None, None, 7, None, 2, 3, None, 9, 3, None, 5, 7, None, None, 9, 4,
                None, 4, 3, None, None, None, 8, 5, 4, 4, None, 6, 4, 10, 1, 10, None, 6, 2, 5, 5, 5, 9, 3, 9, 4, None,
                None, None, 1, None, None, None, None, None, 2, None, 8, 8, None, 9, 9, None, None, None, 6, 8, None,
                None, None, 2, None, None, 1, None, 5, None, None, None, None, None, None, None, None, 2, 5, 8, 10, 10,
                1, 9, 4, 2, 8, 7, 7, 8, 10, 5, 10, None, 2, 6, 6, 10, 3, None, None, None, 5, None, None, 4, None, 7,
                None, None, 8, None, None, 6, None, None, 3, None, None, 5, None, 3, None, 4, 3, 9, None, None, None,
                None, 2, 8, 8, None, None, None, None, None, None, None, None, None, None, 3, 4, None, None, None, 9,
                None, None, None, None, None, 5, None, None, None, 7, None, None, 4, None, None, 5, None, None, None,
                None, 5, 10, 10, 3, None, None, None, 5, 2, 3, 3, 1, 3, 4, 6, 9, None, None, None, None, None, None,
                None, 7, None, None, None, None, 9, 2, 4, 10, None, None, None, 7, None, None, None, None, 7, None,
                None, None, None, None, None, None, None, 8, 4, 10, None, None, None, None, 2, 10, 9, 4, 1, None, 6, 7,
                10, 2, 8, 6, 1, 7, 8, None, 10, 6, None, None, 3, None, None, None, None, None, 2, None, None, 5, 2, 10,
                5, None, 3, None, None, 10, 6, 8, 7, 6, None, None, None, 4, None, None, 5, 10, 4, None, None, None,
                None, None, None, None, 5, 6, 3, None, None, None, None, None, None, None, None, 10, None, 8, None, 10,
                3, None, None, None, None, 7, None, 5, None, None, None, 5, None, 10, 5, 5, None, 3, 5, 10, None, 2, 1,
                7, None, 5, None, 5, 4, 9, 6, 6, 6, 1, 9, 8, 1, 1, 9, None, None, None, 7, None, None, None, None, None,
                None, None, 9, 3, None, None, None, None, None, 4, None, 3, 10, 7, 6, 10, None, 8, 3, 7, 1, 4, 4, 3, 6,
                5, None, None, 8, 6, None, None, 2, None, None, None, None, 10, 7, 6, None, None, None, None, None,
                None, 7, 1, 1, 2, None, 10, 7, None, None, None, None, None, None, None, None, None, None, 9, None,
                None, None, None, None, 6, None, None, 8, 7, 4, 8, None, 3, 2, None, None, None, None, None, None, None,
                10, None, None, None, None, None, None, None, None, 2, 3, 8, None, 4, 7, 9, None, None, 3, 4, 6, 7,
                None, None, None, None, None, 1, None, None, 5, 7, None, 5, None, None, 4, 10, 9, 5, 5, 4, 3, None,
                None, None, None, None, None, None, None, None, None, None, None, None, 1, 9, 1, 10, 4, 9, 10, 3, 1, 3,
                1, 6, None, None, 2, 6, None, 3, None, 3, 2, 4, None, None, 9, None, None, None, None, 10, 5, None, 3,
                None, 9, None, None, None, 5, None, 3, 5, None, 6, 4, 6, 9, None, None, None, 10, None, 8, None, None,
                None, 10, None, None, 1, None, None, 8, None, None, 7, None, 2, None, 5, None, None, 7, None, None,
                None, None, None, None, None, 3, None, 1, 6, 4, 2, None, 2, None, 7, None, None, None, None, None, None,
                3, None, 1, None, 8, 2, 4, None, None, 6, None, 8, None, 6, 8, None, None, None, None, None, 3, 6, None,
                9, None, None, None, 3, 6, 8, 8, 1, None, 5, 6, 10, 7, 10, 10, 10, 9, None, 10, 1, 7, 1, 5, None, 6,
                None, None, None, None, None, None, None, None, None, 6, None, None, None, 6, None, 2, 4, 2, 4, None, 2,
                4, None, 2, 9, None, None, None, None, 1, 10, 1, 6, None, None, None, None, None, 4, 3, 6, 7, 10, None,
                None, None, None, None, 6, 8, 6, 9, 10, None, 8, None, None, None, None, None, None, None, None, None,
                7, None, 3, 6, 1, 6, 1, 7, None, 10, None, None, None, None, None, None, None, 10, None, None, None,
                None, 5, 5, 6, 7, 7, 6, 9, 2, None, 9, 7, 3, None, 7, 7, None, None, 8, 2, 7, 5, 4, 4, None, None, 10,
                9, None, 9, 2, None, 9, None, 2, None, None, None, None, None, None, None, 2, None, None, None, 1, 4,
                None, 2, None, 4, None, None, 2, None, 1, None, 1, None, None, 4, None, 8, None, 10, None, None, None,
                10, 7, None, None, None, None, None, None, None, None, None, None, None, None, 9, 4, 8, 6, None, None,
                None, None, None, 6, None, 2, 2, None, None, None, None, None, None, None, None, None, None, None, 6,
                10, None, 7, 6, 5, 1, 3, 3, 1, 6, 6, 5, None, None, 5, None, None, None, 2, None, None, None, None, 5,
                2, 1, 4, 9, 6, 10, 5, 6, 3, 6, 3, 4, 7, 1, None, 4, None, None, None, None, 9, None, None, None, None,
                None, 1, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None,
                8, None, None, 2, 3, None, 2, None, None, 5, 10, None, None, 6, None, 10, None, None, 10, 3, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, 9, None, 4, None, 4, 4, 6, 5, 4,
                2, 6, None, 3, 9, None, None, None, None, 10, None, 4, None, 6, None, None, 1, None, None, None, 2,
                None, None, 1, 2, 10, 8, 10, None, 10, 5, 8, None, 8, 5, None, 3, None, None, None, None, 8, None, None,
                None, None, 6, None, None, None, 7, None, None, None, 7, None, None, None, 3, None, None, None, 7, 7,
                None, None, None, 2, None, None, 9, None, 2, 8, 7, 10, 5, None, 9, None, None, None, None, None, None,
                6, 7, None, None, 4, None, None, None, None, None, None, None, None, None, None, None, 2, None, None, 7,
                None, 8, 9, 5, None, 6, 5, None, 5, None, None, None, None, None, None, None, None, None, None, None,
                None, 10, 4, None, None, None, None, None, 1, None, 2, None, None, 8, 3, 6, 4, None, None, 6, 8, None,
                None, None, None, None, None, 1, 8, None, None, None, None, None, 1, None, None, None, None, None, 4,
                None, None, 6, None, 9, None, 1, 8, None, 3, 2, None, None, 2, 7, 3, 1, 1, None, None, 6, None, 6, None,
                None, None, None, None, 3, None, 8, None, None, None, 9, 9, None, 10, 1, None, 6, 4, None, None, None,
                None, 5, 5, None, 9, None, None, None, 8, 6, None, None, None, None, None, None, None, None, None, None,
                None, None, None, 2, None, None, None, 5, 8, None, None, None, None, 3, None, None, None, None, 10, 1,
                4, None, 4, None, 6, 1, None, None, None, 2, 8, 1, None, 10, None, None, None, None, 6, None, None,
                None, 3], 13), ]
for longest_zig_zag in [longest_zig_zag_all, ]:
    for test_tree_list, expected_output in test_cases:
        assert longest_zig_zag(ConstructTree.build_tree_leetcode(test_tree_list).root) == expected_output, \
            longest_zig_zag.__name__
