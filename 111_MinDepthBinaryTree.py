"""
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.
"""
from typing import Optional

from _Binary_Tree import TreeNode, ConstructTree


def min_depth(root: Optional[TreeNode]) -> int:
    """
    :param root: binary tree with 0 to 100000 nodes
    :return: depth of the nearest leaf node
    """
    if not root:
        return 0

    current_depth = 1
    current_level = [root]

    while current_level:
        next_level = []
        for current_node in current_level:
            if not current_node.left and not current_node.right:
                return current_depth
            if current_node.left:
                next_level.append(current_node.left)
            if current_node.right:
                next_level.append(current_node.right)

        current_depth += 1
        current_level = next_level


test_cases = [([], 0),
              ([3, 9, 20, None, None, 15, 7], 2),
              ([2, None, 3, None, 4, None, 5, None, 6], 5),
              ([0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0,
                None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None,
                0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, None, 0, 0], 1804), ]
for test_tree_list, expected_depth in test_cases:
    if test_tree_list:
        assert min_depth(ConstructTree.build_tree_leetcode(test_tree_list).root) == expected_depth
    else:
        assert min_depth(None) == 0
