"""
We are given the head node current_root of a binary tree, where additionally every node's value is either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
"""
from collections import deque
from typing import Optional, List

from _Binary_Tree import TreeNode, BinaryTree


def prune_tree_helper(current_root: TreeNode) -> bool:
    """
    Prune the subtree of current_root
    :param current_root: root node of current sub tree; guaranteed not equals to None
    :return: whether subtree of current_root contains 1
    """
    subtree_contains_1 = False

    if current_root.left:
        if prune_tree_helper(current_root.left):
            subtree_contains_1 = True
        else:
            current_root.left = None

    if current_root.right:
        if prune_tree_helper(current_root.right):
            subtree_contains_1 = True
        else:
            current_root.right = None

    return current_root.val == 1 or subtree_contains_1


def prune_tree(root: TreeNode) -> Optional[TreeNode]:
    """
    :param root: root of binary tree
    :return: in place pruning, return root of TreeNode or None
    """
    if root is None:
        return None

    below_root_contains_1 = prune_tree_helper(root)
    return root if below_root_contains_1 or root.val == 1 else None


def test_build_tree(node_list: List[Optional[int]]) -> BinaryTree:
    if not node_list or node_list[0] is None:
        return BinaryTree(None)
    return_tree = BinaryTree(TreeNode(node_list[0]))
    node_queue = deque([return_tree.root])
    node_child_counter = 0
    current_node = None
    for i in range(1, len(node_list)):
        if node_child_counter == 0:
            current_node = node_queue.popleft()
        if node_list[i] is not None:
            if node_child_counter:
                current_node.right = TreeNode(node_list[i])
                node_queue.append(current_node.right)
            else:
                current_node.left = TreeNode(node_list[i])
                node_queue.append(current_node.left)
        node_child_counter = (node_child_counter + 1) % 2
    return return_tree


test_cases = [([1, None, 0, 0, 1], [1, None, 0, None, 1]),
              ([1, 0, 1, 0, 0, 0, 1], [1, None, 1, None, 1]),
              ([1, 1, 0, 1, 1, 0, 1, 0], [1, 1, 0, 1, 1, None, 1]),
              ([0, 0, 0], None)]
for tree_in, tree_out in test_cases:
    test_tree = test_build_tree(tree_in)
    get_root = prune_tree(test_tree.root)
    if tree_out:
        reference_tree = test_build_tree(tree_out)
        assert test_tree == reference_tree, tree_out
    else:
        assert get_root is None
