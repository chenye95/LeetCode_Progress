"""
Invert a binary tree Left and Right
"""
from typing import Optional

from _Binary_Tree import TreeNode, BinaryTree


def invertTree(root: TreeNode) -> Optional[TreeNode]:
    if root is None:
        return None
    right = invertTree(root.right) if root.right is not None else None
    left = invertTree(root.left) if root.left is not None else None
    root.left = right
    root.right = left
    return root


node = TreeNode(4)
node.left = TreeNode(2)
node.left.left = TreeNode(1)
node.left.right = TreeNode(3)
node.right = TreeNode(7)
node.right.left = TreeNode(6)
node.right.right = TreeNode(9)

tree = BinaryTree(node)
print(tree.preorder_traversal())
print(tree.inorder_traversal())
print(tree.layer_traversal_by_layer())

new_tree_root = invertTree(node)
new_tree = BinaryTree(new_tree_root)
print(new_tree.layer_traversal_by_layer())
