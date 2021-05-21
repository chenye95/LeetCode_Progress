"""
Given the root of a binary tree, flatten the tree into a "linked list":
- The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list
    and the left child pointer is always None.
- The "linked list" should be in the same order as a pre-order traversal of the binary tree.
"""
from typing import Optional

from _Binary_Tree import TreeNode, ConstructTree, CompareTree


def flatten(root: Optional[TreeNode]) -> None:
    """
    :param root: root of a binary tree
    :return: No return - do not return anything, modify root in-place instead.
    """
    previous_node = None

    def reversed_pre_order_traversal(current_node: TreeNode) -> None:
        """
        :param current_node: flattening sub tree beneath current_node; current_node is not None
        """
        nonlocal previous_node
        if current_node.right:
            reversed_pre_order_traversal(current_node.right)
        if current_node.left:
            reversed_pre_order_traversal(current_node.left)

        current_node.right = previous_node
        current_node.left = None
        previous_node = current_node

    if root is None:
        return
    reversed_pre_order_traversal(root)


test_cases = [([1, 2, 5, 3, 4, None, 6], [1, None, 2, None, 3, None, 4, None, 5, None, 6]),
              ([], []),
              ([0], [0]),
              ([5, 0, -4, -1, -6, -9, None, 7, None, 1, 3, None, 0, None, 9, None, None, 6, 0, None, -7, None, None,
                None, None, None, None, -4, None, 1, None, None, -4],
               [5, None, 0, None, -1, None, 7, None, 9, None, -6, None, 1, None, 3, None, 6, None, 0, None, -4, None,
                -9, None, 0, None, -7, None, -4, None, 1, None, -4]), ]
for test_tree_list, expected_tree_list in test_cases:
    if test_tree_list:
        test_tree = ConstructTree.build_tree_leetcode(test_tree_list)
        flatten(test_tree.root)
        assert CompareTree.compare_leetcode_traversal(test_tree.leetcode_traversal(), expected_tree_list)
