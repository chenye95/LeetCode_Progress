"""
Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).
"""
from collections import deque

from _Binary_Tree import TreeNode, ConstructTree


def is_symmetric(root: TreeNode) -> bool:
    """
    :param root: root a non empty binary tree
    :return: whether the tree mirror around the center line
    """
    tree_node_queue = deque([root.left, root.right])
    while tree_node_queue:
        left_tree_node = tree_node_queue.popleft()
        right_tree_node = tree_node_queue.popleft()
        if left_tree_node is None and right_tree_node is None:
            continue
        if left_tree_node is None or right_tree_node is None or left_tree_node.val != right_tree_node.val:
            return False
        tree_node_queue.extend([left_tree_node.left, right_tree_node.right,
                                left_tree_node.right, right_tree_node.left])

    return True


test_cases = [([1, 2, 2, 3, 4, 4, 3], True),
              ([1, 2, 2, None, 3, None, 3], False),
              ([1, 2, 2, 3, None, None, 3], True), ]
for test_tree_list, expected_output in test_cases:
    assert is_symmetric(ConstructTree.build_tree_leetcode(test_tree_list).root) is expected_output
