"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along
the path equals the given sum.

Note: A leaf is a node with no children.
"""
from _Binary_Tree import TreeNode, ConstructTree


def has_path_sum(root: TreeNode, target_sum: int) -> bool:
    """
    :param root: root node of Binary Tree
    :param target_sum: target sum for path to add up to
    :return: whether the tree has a root-to-leaf path that add up to target sum
    """
    if not root:
        return False
    stack = [(root, target_sum)]
    while stack:
        current_node, sum_left = stack.pop()
        if not current_node.left and not current_node.right and current_node.val == sum_left:
            return True
        if current_node.left:
            stack.append((current_node.left, sum_left - current_node.val))
        if current_node.right:
            stack.append((current_node.right, sum_left - current_node.val))

    return False


test_cases = [([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 0, False),
              ([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, None, 1], 22, True), ]
for test_tree, test_target, expected_output in test_cases:
    assert has_path_sum(ConstructTree.build_tree_leetcode(test_tree).root, test_target) is expected_output
