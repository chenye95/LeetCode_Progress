"""
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given
depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes
 with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree
 of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If
 depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole
 original tree, and the original tree is the new root's left subtree.
"""
from _Binary_Tree import TreeNode, ConstructTree, BinaryTree


def add_one_row(root: TreeNode, value: int, depth: int) -> TreeNode:
    """
    :param root: root of a proper binary tree
    :param value: add a new row at level depth with all nodes set to value
    :param depth: add a new row at level depth with all nodes set to value
    :return: root of the new binary tree
    """
    if depth == 1:
        return TreeNode(value, left=root)

    current_level = [root]
    current_depth = 1

    while current_depth < depth - 1:
        next_level = [node.left for node in current_level if node.left is not None]
        next_level.extend([node.right for node in current_level if node.right is not None])
        current_depth += 1
        current_level = next_level

    for node in current_level:
        node.left = TreeNode(value, left=node.left)
        node.right = TreeNode(value, right=node.right)

    return root


test_cases = [([], 99, 1, [99]),
              ([4, 2, 6, 3, 1, 5], 1, 1, [1, 4, None, 2, 6, 3, 1, 5]),
              ([4, 2, 6, 3, 1, 5], 1, 2, [4, 1, 1, 2, None, None, 6, 3, 1, 5]),
              ([4, 2, None, 3, 1], 1, 3, [4, 2, None, 1, 1, 3, None, None, 1]),
              ([1], 3, 1, [3, 1]),
              ([1, 5, 8, 9, 7, 7, 8, 1, 4, 8, 1, 9, 0, 8, 7, 1, 7, 4, 2, 9, 8, 2, 4, None, None, 9, None, None, None, 6,
                0, 9, 4, 1, 0, 1, 8, 9, 0, 1, 8, 9, 1, 0, 9, 6, 2, 5, None, 2, 3, 0, 2, 4, 8, 8, 8, 5, 0, 0, 9, 4, 9, 1,
                None, 0, 7, 2, 2, 3, None, 6, 1, 0, 8, 9, 9, 9, 4, 8, 4, 3, 4, 4, 0, None, None, 8, 3, 8, None, None, 0,
                None, 0, 4, 9, 1, 2, None, 4, 4, 0, 4, 3, 5, 5, 7, 4, 1, 6, None, 1, 0, None, None, None, 2, 8, 7, 7,
                None, None, 0, 2, 5, 5, 9, 3, 3, None, 7, 6, 6, 7, 9, 8, 1, 7, 7, 7, 2, 6, None, 7, None, 4, 6, 4, 6,
                None, None, 9, 1, None, None, None, 5, 5, 5, 4, 2, 2, 8, 5, 1, 1, 3, 1, 3, 7, None, 2, None, 9, 1, 4, 4,
                7, 7, None, 1, 5, 6, 2, 7, 3, None, 9, 1, None, 2, 4, 4, 8, None, None, 7, None, 6, None, 7, 4, 3, 5, 8,
                4, 8, 5, None, None, 8, None, None, None, 4, 4, None, None, None, None, 8, 3, 5, 5, None, None, None, 1,
                2, 0, None, None, 9, 3, None, 8, 3, 7, 1, 8, 9, 0, 1, 8, 2, None, 4, None, None, 8, None, None, None,
                None, 2, None, 4, 8, 5, 5, 3, 1, None, None, 6, None, 1, None, None, 6, None, None, None, None, 7, 3,
                None, None, None, 8, 6, 4, None, 6, 9, 0, 7, 8, None, None, 0, 6, 7, None, None, 0, 0, 7, 2, 3, 2, None,
                0, 2, 3, None, 0, 1, 7, 9, 0, 7, None, None, None, None, 5, 8, 2, 6, 3, 2, 0, 4, None, None, 0, 9, 1, 1,
                1, None, 1, 3, None, 7, 9, 1, 3, 3, 8, None, None, None, None, 6, None, None, None, None, 9, 8, 1, 3, 8,
                3, 0, 6, None, None, 8, 5, 6, 5, 2, 1, None, 5, None, 7, 0, 0, None, 9, 3, 9, None, 3, 0, 0, 9, 1, 7, 0,
                2, None, 6, 8, 5, None, None, None, None, None, 7, None, 2, 5, None, None, 9, None, None, None, None,
                None, None, None, None, None, None, None, 4, 1, None, 3, 6, 6, 2, 5, 5, 9, None, None, 7, 8, None, None,
                2, 7, 3, 7, 2, 5, None, 1, 3, 4, None, None, 8, 3, 6, 9, None, 1, None, None, None, None, 9, 7, 5, 2,
                None, 5, None, 6, 4, 5, None, 1, 2, 0, 6, None, 1, 6, None, None, 5, None, 7, 8, 4, 7, 8, 6, 4, None, 5,
                6, 7, 9, 1, 0, 4, None, None, None, 6, 4, 8, 4, 5, None, 0, 4, 4, 0, 1, 7, 1, None, 1, None, 3, 6, None,
                None, None, None, 8, None, 5, 0, 7, 5, None, None, 5, 8, None, None, 3, None, None, 8, None, 2, 4, None,
                None, None, None, None, None, None, 9, None, 9, None, 9, None, None, None, None, 7, 1, None, None, 2,
                None, None, 5, 5, 5, 5, 6, 4, None, None, 1, 6, 4, 0, None, 0, 6, 3, 0, None, 5, 5, None, None, None,
                None, 2, None, 3, 6, None, 3, 0, 5, 0, 1, 0, 3, 4, 9, 9, 2, 7, 3, 8, 6, 9, None, 5, 8, None, None, None,
                None, 9, 8, 0, 7, None, None, 8, 8, 6, 6, 0, 2, 7, 4, 2, 3, 8, 6, 4, None, 8, None, None, None, 2, 0,
                None, 1, 3, 5, 4, 2, 2, 5, 8, 8, None, 3, 0, None, 1, 6, 0, None, None, 9, None, 2, None, 6, 8, 2, None,
                None, 5, None, None, None, 9, 6, 6, 4, 2, 0, None, None, 1, None, 0, None, None, None, 6, 6, None, None,
                None, 4, 7, 9, None, 0, 1, None, None, 9, None, None, None, 4, None, 8, None, None, None, None, None,
                None, 4, None, 6, None, 3, None, None, 5, 1, 2, 5, None, 0, 7, 8, None, 7, None, None, 4, None, 4, 4,
                None, 2, None, 6, None, None, None, 7, None, None, None, None, 6, 4, None, 6, None, 6, 9, None, None,
                None, 9, 6, None, 9, None, 3, None, 2, None, 7, 7, None, None, 0, None, 6, 3, None, None, None, None,
                None, None, 1, None, None, None, 6, 9, 7, None, 7, None, 9, 3, 3, None, None, None, None, 4, None, None,
                3, None, None, None, 3, 9, None, 0, 3, 1, 9, 6, 7, 9, 4, 8, None, None, 6, None, 1, 3, 7, None, None,
                None, 3, None, 2, None, 8, 1, 1, None, None, 6, None, 7, 3, 5, None, 6, 3, 4, None, None, 5, 7, 1, None,
                None, 6, 4, 6, None, None, None, None, 5, 7, 0, 7, 0, None, 5, 8, 5, 5, 4, 5, None, None, None, None,
                None, None, 1, 7, None, None, 7, None, 9, 9, 6, 4, None, None, 3, 2, 1, None, 0, None, 0, 6, None, None,
                None, 1, 5, None, None, None, 8, None, None, None, None, 3, 4, 8, None, None, 9, 6, 4, None, None, None,
                None, 8, 9, None, 1, None, None, None, 7, None, None, None, None, None, 9, None, None, None, 4, 1, 6, 7,
                0, None, None, None, 7, None, None, 8, None, None, None, None, None, None, None, 4, None, 9, None, None,
                None, None, 3, 0, 6, None, 5, None, 9, 9, None, None, 4, 3, 4, None, None, None, None, 8, None, 5, None,
                None, None, None, 5, 2, None, None, None, None, None, None, None, 2, None, None, 2, 1, 8, 5, None, 0,
                None, 0, 3, 2, 4, 5, None, None, None, None, None, 7, None, None, 0, None, 0, None, None, None, 0, 3, 9,
                None, None, None, None, 5, None, None, 0, 5, 0, 0, None, 9, None, None, None, None, None, None, None,
                None, 8, None, 9, 3, 5, 9, 0, 5, 9, None, None, 9, 4, None, 0, 2, 0, None, None, 7, None, 7, None, 5, 7,
                8, 7, None, None, None, 3, 0, 3, None, None, None, None, None, 4, 5, None, None, 2, 3, None, 2, None,
                None, 7, None, None, 9, None, None, 9, 7, 1, None, None, 1, 6, 1, 8, None, None, 5, None, None, 3, 7, 9,
                6, None, None, None, None, 1, None, None, None, 3, 7, 3, 2, 3, 3, None, 1, None, None, None, 1, None,
                None, 4, 3, 4, 8, 7, None, 0, 3, 0, None, 1, 1, None, None, None, None, None, 5, None, 6, 0, None, 3, 1,
                None, 6, None, None, 4, 0, 1, None, 6, 1, None, None, 9, 6, 4, 9, 0, 8, 9, 3, 3, 6, None, None, None,
                None, None, None, None, None, None, None, None, None, 2, None, None, None, None, None, 8, 5, 8, 3, 5, 4,
                None, 6, None, 0, None, None, 6, None, 4, 3, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, 7, 3, None, None, 1, None, 2, 4, None, None, None, 6, None, None, None, 6, None,
                5, None, None, None, None, 1, None, None, 3, None, 1, None, 7, 1, None, None, 7, 1, 3, 4, 8, None, None,
                None, None, None, 4, None, None, 4, None, None, None, 7, None, 6, None, None, 1, None, None, None, 7, 3,
                3, None, None, None, None, 3, 0, None, None, 4, None, None, None, None, None, None, None, None, None,
                None, 8, None, None, 9, None, None, 6, 6, 5, 2, None, 8, 3, 8, None, None, None, None, 6, 7, 0, None,
                None, None, None, 1, 1, 5, None, 0, 5, None, 5, None, None, None, 1, 2, None, 2, 9, 1, None, 2, 4, 1,
                None, None, None, 1, 8, 4, 4, 5, 2, None, None, 6, 4, 7, 5, 2, 9, None, 4, None, None, None, None, None,
                3, None, None, 5, 9, None, None, None, None, 9, None, 9, None, None, None, 2, None, 1, 9, None, None,
                None, None, None, 1, 9, 3, None, None, 1, 9, None, 5, 2, 1, 0, None, None, 1, 9, 8, 4, 7, None, None, 5,
                7, None, None, None, None, 1, 2, 8, None, 6, 0, None, None, None, None, 0, None, None, None, 6, None, 2,
                3, 0, 9, None, None, 1, 4, 6, None, 8, None, None, 5, None, 3, 0, None, 6, None, None, None, None, None,
                2, None, None, None, None, None, None, 2, 5, 8, 6, 9, None, None, None, 8, None, None, 9, 6, None, None,
                None, None, 3, None, None, None, None, 9, None, None, 2, None, None, None, None, None, None, 8, 8, None,
                None, None, None, None, 9, None, 6, None, 2, 5, None, None, 1, 2, None, 4, None, None, 4, None, None, 3,
                5, None, 3, 3, None, None, 1, None, None, None, None, 4, None, 2, 3, None, 4, 5, 3, None, 7, None, None,
                None, 7, 6, None, None, 1, 3, None, 4, 9, 8, None, None, 0, None, 3, 4, None, 8, None, 1, None, None, 2,
                2, None, None, 4, None, None, None, 3, None, None, 2, None, None, None, 4, None, 5, None, None, None,
                None, 2, None, 5, None, None, None, None, None, None, 2, 7, 5, None, 6, None, None, None, None, 2, None,
                0, None, 3, None, 1, None, 9, 4, None, 3, None, None, None, None, None, None, None, 5, 5, 7, None, None,
                1, None, 4, 6, None, None, None, 2, None, 5, 9, 0, 6, 2, None, None, None, None, None, None, None, None,
                None, None, None, None, 5, None, 7, None, 2, 9, None, None, 1, None, None, None, 1, 6, None, 6, None,
                None, 0, 8, None, 4, None, None, None, None, 4, None, None, 0, None, 6, 0, None, None, None, 4, None,
                None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, 0, 5,
                4, 2, 6, 4, 5, 3, 4, None, None, 5, None, None, None, None, 4, None, None, 3, 6, 2, 0, None, 6, 6, None,
                None, None, None, 0, 6, None, None, None, 3, 9, 4, None, None, None, None, None, 0, None, None, 6, 7, 0,
                None, 9, 2, None, 3, 3, None, None, 8, None, 3, None, None, None, 8, 5, 3, None, 2, 4, None, 9, 6, 9,
                None, None, None, None, 6, None, 6, None, 5, 3, None, None, None, None, 4, None, None, None, 9, 0, 9, 7,
                1, 1, None, 1, None, 1, 6, None, 5, None, 6, None, None, 1, None, None, None, None, None, None, 5, None,
                None, None, None, None, 3, None, 6, 1, None, 0, 2, None, None, 0, None, None, 0, None, None, None, None,
                None, 3, None, None, 8, None, None, 5, 3, 3, None, None, None, None, None, None, None, 3, None, None, 0,
                8, 7, None, None, 8, 1, None, None, None, None, None, None, 7, None, None, None, None, None, None, None,
                None, None, None, None, 5, 2, None, 2, 6, None, None, None, None, None, None, None, 1, 5, 0, None, None,
                2, None, 7, None, None, 6, None, None, None, None, None, None, None, None, None, None, None, None, None,
                8, None, None, None, None, 3, None, None, 4, None, None, 2, None, None, None, None, 0, 3, None, None,
                None, None, None, 7, None, 8, None, None, None, None, 8, 5, None, 3, 4, None, None, None, 8, None, None,
                None, None, None, None, None, None, None, 3, 7, None, None, None, 4, 0, 3, None, None, 6, None, None,
                None, None, None, None, None, None, None, None, None, None, 8, None, None, None, None, None, 2, None,
                None, None, None, None, None, None, None, None, 0, None, None, None, 2, None, None, None, 8, 2, None,
                None, None, None, None, None, None, 8, None, None, None, None, None, None, None, None, None, None, 2,
                None, None, None, 2, 5, None, None, None, None, None, None, None, None, None, None, None, 2, None, None,
                None, None, None, 8, None, None, None, None, None, None, None, None, None, None, 0, 5], 1, 24,
               [1, 5, 8, 9, 7, 7, 8, 1, 4, 8, 1, 9, 0, 8, 7, 1, 7, 4, 2, 9, 8, 2, 4, None, None, 9, None, None, None, 6,
                0, 9, 4, 1, 0, 1, 8, 9, 0, 1, 8, 9, 1, 0, 9, 6, 2, 5, None, 2, 3, 0, 2, 4, 8, 8, 8, 5, 0, 0, 9, 4, 9, 1,
                None, 0, 7, 2, 2, 3, None, 6, 1, 0, 8, 9, 9, 9, 4, 8, 4, 3, 4, 4, 0, None, None, 8, 3, 8, None, None, 0,
                None, 0, 4, 9, 1, 2, None, 4, 4, 0, 4, 3, 5, 5, 7, 4, 1, 6, None, 1, 0, None, None, None, 2, 8, 7, 7,
                None, None, 0, 2, 5, 5, 9, 3, 3, None, 7, 6, 6, 7, 9, 8, 1, 7, 7, 7, 2, 6, None, 7, None, 4, 6, 4, 6,
                None, None, 9, 1, None, None, None, 5, 5, 5, 4, 2, 2, 8, 5, 1, 1, 3, 1, 3, 7, None, 2, None, 9, 1, 4, 4,
                7, 7, None, 1, 5, 6, 2, 7, 3, None, 9, 1, None, 2, 4, 4, 8, None, None, 7, None, 6, None, 7, 4, 3, 5, 8,
                4, 8, 5, None, None, 8, None, None, None, 4, 4, None, None, None, None, 8, 3, 5, 5, None, None, None, 1,
                2, 0, None, None, 9, 3, None, 8, 3, 7, 1, 8, 9, 0, 1, 8, 2, None, 4, None, None, 8, None, None, None,
                None, 2, None, 4, 8, 5, 5, 3, 1, None, None, 6, None, 1, None, None, 6, None, None, None, None, 7, 3,
                None, None, None, 8, 6, 4, None, 6, 9, 0, 7, 8, None, None, 0, 6, 7, None, None, 0, 0, 7, 2, 3, 2, None,
                0, 2, 3, None, 0, 1, 7, 9, 0, 7, None, None, None, None, 5, 8, 2, 6, 3, 2, 0, 4, None, None, 0, 9, 1, 1,
                1, None, 1, 3, None, 7, 9, 1, 3, 3, 8, None, None, None, None, 6, None, None, None, None, 9, 8, 1, 3, 8,
                3, 0, 6, None, None, 8, 5, 6, 5, 2, 1, None, 5, None, 7, 0, 0, None, 9, 3, 9, None, 3, 0, 0, 9, 1, 7, 0,
                2, None, 6, 8, 5, None, None, None, None, None, 7, None, 2, 5, None, None, 9, None, None, None, None,
                None, None, None, None, None, None, None, 4, 1, None, 3, 6, 6, 2, 5, 5, 9, None, None, 7, 8, None, None,
                2, 7, 3, 7, 2, 5, None, 1, 3, 4, None, None, 8, 3, 6, 9, None, 1, None, None, None, None, 9, 7, 5, 2,
                None, 5, None, 6, 4, 5, None, 1, 2, 0, 6, None, 1, 6, None, None, 5, None, 7, 8, 4, 7, 8, 6, 4, None, 5,
                6, 7, 9, 1, 0, 4, None, None, None, 6, 4, 8, 4, 5, None, 0, 4, 4, 0, 1, 7, 1, None, 1, None, 3, 6, None,
                None, None, None, 8, None, 5, 0, 7, 5, None, None, 5, 8, None, None, 3, None, None, 8, None, 2, 4, None,
                None, None, None, None, None, None, 9, None, 9, None, 9, None, None, None, None, 7, 1, None, None, 2,
                None, None, 5, 5, 5, 5, 6, 4, None, None, 1, 6, 4, 0, None, 0, 6, 3, 0, None, 5, 5, None, None, None,
                None, 2, None, 3, 6, None, 3, 0, 5, 0, 1, 0, 3, 4, 9, 9, 2, 7, 3, 8, 6, 9, None, 5, 8, None, None, None,
                None, 9, 8, 0, 7, None, None, 8, 8, 6, 6, 0, 2, 7, 4, 2, 3, 8, 6, 4, None, 8, None, None, None, 2, 0,
                None, 1, 3, 5, 4, 2, 2, 5, 8, 8, None, 3, 0, None, 1, 6, 0, None, None, 9, None, 2, None, 6, 8, 2, None,
                None, 5, None, None, None, 9, 6, 6, 4, 2, 0, None, None, 1, None, 0, None, None, None, 6, 6, None, None,
                None, 4, 7, 9, None, 0, 1, None, None, 9, None, None, None, 4, None, 8, None, None, None, None, None,
                None, 4, None, 6, None, 3, None, None, 5, 1, 2, 5, None, 0, 7, 8, None, 7, None, None, 4, None, 4, 4,
                None, 2, None, 6, None, None, None, 7, None, None, None, None, 6, 4, None, 6, None, 6, 9, None, None,
                None, 9, 6, None, 9, None, 3, None, 2, None, 7, 7, None, None, 0, None, 6, 3, None, None, None, None,
                None, None, 1, None, None, None, 6, 9, 7, None, 7, None, 9, 3, 3, None, None, None, None, 4, None, None,
                3, None, None, None, 3, 9, None, 0, 3, 1, 9, 6, 7, 9, 4, 8, None, None, 6, None, 1, 3, 7, None, None,
                None, 3, None, 2, None, 8, 1, 1, None, None, 6, None, 7, 3, 5, None, 6, 3, 4, None, None, 5, 7, 1, None,
                None, 6, 4, 6, None, None, None, None, 5, 7, 0, 7, 0, None, 5, 8, 5, 5, 4, 5, None, None, None, None,
                None, None, 1, 7, None, None, 7, None, 9, 9, 6, 4, None, None, 3, 2, 1, None, 0, None, 0, 6, None, None,
                None, 1, 5, None, None, None, 8, None, None, None, None, 3, 4, 8, None, None, 9, 6, 4, None, None, None,
                None, 8, 9, None, 1, None, None, None, 7, None, None, None, None, None, 9, None, None, None, 4, 1, 6, 7,
                0, None, None, None, 7, None, None, 8, None, None, None, None, None, None, None, 4, None, 9, None, None,
                None, None, 3, 0, 6, None, 5, None, 9, 9, None, None, 4, 3, 4, None, None, None, None, 8, None, 5, None,
                None, None, None, 5, 2, None, None, None, None, None, None, None, 2, None, None, 2, 1, 8, 5, None, 0,
                None, 0, 3, 2, 4, 5, None, None, None, None, None, 7, None, None, 0, None, 0, None, None, None, 0, 3, 9,
                None, None, None, None, 5, None, None, 0, 5, 0, 0, None, 9, None, None, None, None, None, None, None,
                None, 8, None, 9, 3, 5, 9, 0, 5, 9, None, None, 9, 4, None, 0, 2, 0, None, None, 7, None, 7, None, 5, 7,
                8, 7, None, None, None, 3, 0, 3, None, None, None, None, None, 4, 5, None, None, 2, 3, None, 2, None,
                None, 7, None, None, 9, None, None, 9, 7, 1, None, None, 1, 6, 1, 8, None, None, 5, None, None, 3, 7, 9,
                6, None, None, None, None, 1, None, None, None, 3, 7, 3, 2, 3, 3, None, 1, None, None, None, 1, None,
                None, 4, 3, 4, 8, 7, None, 0, 3, 0, None, 1, 1, None, None, None, None, None, 5, None, 6, 0, None, 3, 1,
                None, 6, None, None, 4, 0, 1, None, 6, 1, None, None, 9, 6, 4, 9, 0, 8, 9, 3, 3, 6, None, None, None,
                None, None, None, None, None, None, None, None, None, 2, None, None, None, None, None, 8, 5, 8, 3, 5, 4,
                None, 6, None, 0, None, None, 6, None, 4, 3, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, 7, 3, None, None, 1, None, 2, 4, None, None, None, 6, None, None, None, 6, None,
                5, None, None, None, None, 1, None, None, 3, None, 1, None, 7, 1, None, None, 7, 1, 3, 4, 8, None, None,
                None, None, None, 4, None, None, 4, None, None, None, 7, None, 6, None, None, 1, None, None, None, 7, 3,
                3, None, None, None, None, 3, 0, None, None, 4, None, None, None, None, None, None, None, None, None,
                None, 8, None, None, 9, None, None, 6, 6, 5, 2, None, 8, 3, 8, None, None, None, None, 6, 7, 0, None,
                None, None, None, 1, 1, 5, None, 0, 5, None, 5, None, None, None, 1, 2, None, 2, 9, 1, None, 2, 4, 1,
                None, None, None, 1, 8, 4, 4, 5, 2, None, None, 6, 4, 7, 5, 2, 9, None, 4, None, None, None, None, None,
                3, None, None, 5, 9, None, None, None, None, 9, None, 9, None, None, None, 2, None, 1, 9, None, None,
                None, None, None, 1, 9, 3, None, None, 1, 9, None, 5, 2, 1, 0, None, None, 1, 9, 8, 4, 7, None, None, 5,
                7, None, None, None, None, 1, 2, 8, None, 6, 0, None, None, None, None, 0, None, None, None, 6, None, 2,
                3, 0, 9, None, None, 1, 4, 6, None, 8, None, None, 5, None, 3, 0, None, 6, None, None, None, None, None,
                2, None, None, None, None, None, None, 2, 5, 8, 6, 9, None, None, None, 8, None, None, 9, 6, None, None,
                None, None, 3, None, None, None, None, 9, None, None, 2, None, None, None, None, None, None, 8, 8, None,
                None, None, None, None, 9, None, 6, None, 2, 5, None, None, 1, 2, None, 4, None, None, 4, None, None, 3,
                5, None, 3, 3, None, None, 1, None, None, None, None, 4, None, 2, 3, None, 4, 5, 3, None, 7, None, None,
                None, 7, 6, None, None, 1, 3, None, 4, 9, 8, None, None, 0, None, 3, 4, None, 8, None, 1, None, None, 2,
                2, None, None, 4, None, None, None, 3, None, None, 2, None, None, None, 4, None, 5, None, None, None,
                None, 2, None, 5, None, None, None, None, None, None, 2, 7, 5, None, 6, None, None, None, None, 2, None,
                0, None, 3, None, 1, None, 9, 4, None, 3, None, None, None, None, None, None, None, 5, 5, 7, None, None,
                1, None, 4, 6, None, None, None, 2, None, 5, 9, 0, 6, 2, None, None, None, None, None, None, None, None,
                None, None, None, None, 5, None, 7, None, 2, 9, None, None, 1, None, None, None, 1, 6, None, 6, None,
                None, 0, 8, None, 4, None, None, None, None, 4, None, None, 0, None, 6, 0, None, None, None, 4, None,
                None, None, None, None, 0, None, None, None, None, None, None, None, None, None, None, None, None, 0, 5,
                4, 2, 6, 4, 5, 3, 4, None, None, 5, None, None, None, None, 4, None, None, 3, 6, 2, 0, None, 6, 6, None,
                None, None, None, 0, 6, None, None, None, 3, 9, 4, None, None, None, None, None, 0, None, None, 6, 7, 0,
                None, 9, 2, None, 3, 3, None, None, 8, None, 3, None, None, None, 8, 5, 3, None, 2, 4, None, 9, 6, 9,
                None, None, None, None, 6, None, 6, None, 5, 3, None, None, None, None, 4, None, None, None, 9, 0, 9, 7,
                1, 1, None, 1, None, 1, 6, None, 5, None, 6, None, None, 1, None, None, None, None, None, None, 5, None,
                None, None, None, None, 3, None, 6, 1, None, 0, 2, None, None, 0, None, None, 0, None, None, None, None,
                None, 3, None, None, 8, None, None, 5, 3, 3, None, None, None, None, None, None, None, 3, None, None, 0,
                8, 7, None, None, 8, 1, None, None, None, None, None, None, 7, None, None, None, None, None, None, None,
                None, None, None, None, 5, 2, None, 2, 6, None, None, None, None, None, None, None, 1, 5, 0, None, None,
                2, None, 7, None, None, 6, None, None, None, None, None, None, None, None, None, None, None, None, None,
                8, None, None, None, None, 3, None, None, 4, None, None, 2, None, None, None, None, 0, 3, None, None,
                None, None, None, 7, None, 8, None, None, None, None, 8, 5, None, 3, 4, None, None, None, 8, None, None,
                None, None, None, None, None, None, None, 3, 7, None, None, None, 4, 0, 3, None, None, 6, None, None,
                None, None, None, None, None, None, None, None, None, None, 8, None, None, None, None, None, 2, None,
                None, None, None, None, None, None, None, None, 0, None, None, None, 2, None, None, None, 8, 2, None,
                None, None, None, None, None, None, 8, None, None, None, None, None, None, None, None, None, None, 2,
                None, None, None, 2, 5, None, None, None, None, None, None, None, None, None, None, None, 2, None, None,
                None, None, None, 8, None, None, None, None, None, None, None, None, None, None, 0, 5, None, 1, 1]), ]
for test_tree_list, test_value, test_depth, expected_output in test_cases:
    get_tree = BinaryTree(add_one_row((ConstructTree.build_tree_leetcode(test_tree_list).root if test_tree_list
                                       else None), test_value, test_depth))
    output_traversal = get_tree.leetcode_traversal()
    assert output_traversal[:len(expected_output)] == expected_output
    assert output_traversal[len(expected_output):] == [None] * (len(output_traversal) - len(expected_output))
