"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:
- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.
"""
from typing import Tuple

from _Binary_Tree import TreeNode, ConstructTree


def is_valid_BST(root: TreeNode) -> bool:
    """
    No equality supported here; left sub tree < current node < right sub tree

    :param root: root of a binary tree
    :return: whether the tree is a valid Binary Search Tree
    """
    _invalid_bst_lower, _invalid_bst_upper = 1, 0

    def BST_checker(current_node: TreeNode) -> Tuple[int, int]:
        """
        :param current_node: scanning the sub tree beneath current_node
        :return: the smallest and the largest value in the sub tree
        """
        if current_node.left:
            left_lower, left_upper = BST_checker(current_node.left)
            # Left tree contains nodes with keys strictly less than node's key
            if left_lower > left_upper or left_upper >= current_node.val:
                return _invalid_bst_lower, _invalid_bst_upper
        else:
            left_lower = current_node.val
        if current_node.right:
            right_lower, right_upper = BST_checker(current_node.right)
            # Right tree contains nodes with keys strictly greater than node's key
            if right_lower > right_upper or right_lower <= current_node.val:
                return _invalid_bst_lower, _invalid_bst_upper
        else:
            right_upper = current_node.val

        return left_lower, right_upper

    if not root:
        return True

    tree_lower, tree_upper = BST_checker(root)
    return tree_lower <= tree_upper


test_cases = [([1, 1], False), ([1, 0], True), ([1, None, 2], True), ([1, None, 1], False), ]
for test_tree, expected_output in test_cases:
    assert is_valid_BST(root=ConstructTree.build_tree_leetcode(test_tree).root) is expected_output
