"""
Given the root of a binary search tree and the lowest and highest boundaries as low and high, trim the tree so that all
its elements lies in [low, high]. Trimming the tree should not change the relative structure of the elements that will
remain in the tree (i.e., any node's descendant should remain a descendant). It can be proven that there is a unique
answer.

Return the root of the trimmed binary search tree. Note that the root may change depending on the given bounds.
"""

from _Binary_Tree import TreeNode, ConstructTree


def trim_BST(root: TreeNode, low: int, high: int) -> TreeNode:
    """
    Recursively trim Binary Search Tree
    """
    if not root:
        return root

    if root.val < low:
        # root and its left tree will be dropped
        return trim_BST(root.right, low, high)
    elif root.val > high:
        # root and its right tree will be dropped
        return trim_BST(root.left, low, high)

    root.left = trim_BST(root.left, low, high)
    root.right = trim_BST(root.right, low, high)
    return root


test_cases = [([1, 0, 2], 1, 2, [1, None, 2]),
              ([3, 0, 4, None, 2, None, None, 1], 1, 3, [3, 2, None, 1]),
              ([1], 1, 2, [1]),
              ([1, None, 2], 1, 3, [1, None, 2]),
              ([1, None, 2], 2, 4, [2]),
              ]

for tree_input, low_input, high_input, expected_output in test_cases:
    test_tree = ConstructTree.build_tree_leetcode(tree_input)
    test_tree.root = trim_BST(test_tree.root, low_input, high_input)
    assert test_tree.leetcode_traversal()[:len(expected_output)] == expected_output
