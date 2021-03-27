"""
Invert a binary tree Left and Right
"""
from typing import Optional

from _Binary_Tree import TreeNode, BinaryTree


def invert_tree(root: TreeNode) -> Optional[TreeNode]:
    """
    :param root: root of a binary tree
    :return: root of the inverted binary tree, after flipping left and right child of each node
    """
    if root is None:
        return None
    right = invert_tree(root.right) if root.right else None
    left = invert_tree(root.left) if root.left else None
    root.left, root.right = right, left
    return root


node = TreeNode(4)
node.left = TreeNode(2)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right = TreeNode(7)
node.right.left = TreeNode(6)
node.right.right = TreeNode(9)

tree = BinaryTree(node)
assert tree.preorder_traversal() == [4, 2, 1, 3, 7, 6, 9]
assert tree.inorder_traversal() == [1, 2, 3, 4, 6, 7, 9]
assert tree.postorder_traversal() == [1, 3, 2, 6, 9, 7, 4]
assert tree.layer_traversal_by_layer() == [[4], [2, 7], [1, 3, 6, 9]]
assert tree.leetcode_traversal() == [4, 2, 7, 1, 3, 6, 9, None, None, None, None, None, None, None, None]

new_tree_root = invert_tree(node)
new_tree = BinaryTree(new_tree_root)
assert new_tree.preorder_traversal() == [4, 7, 9, 6, 2, 3, 1]
assert new_tree.inorder_traversal() == [9, 7, 6, 4, 3, 2, 1]
assert new_tree.postorder_traversal() == [9, 6, 7, 3, 1, 2, 4]
assert new_tree.layer_traversal_by_layer() == [[4], [7, 2], [9, 6, 3, 1]]
assert new_tree.leetcode_traversal() == [4, 7, 2, 9, 6, 3, 1, None, None, None, None, None, None, None, None]
