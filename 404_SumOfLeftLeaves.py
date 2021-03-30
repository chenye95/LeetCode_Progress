"""
Find the sum of all left leaves in a given binary tree.
"""
from _Binary_Tree import TreeNode, ConstructTree


def sum_of_left_leaves(root: TreeNode) -> int:
    """
    :param root: root node of binary tree
    :return: sum of left leaf nodes in the binary tree
    """
    if not root or not (root.left or root.right):
        return 0
    sum_left_leaves = 0
    # stack keep track of left leaf nodes or non leaf nodes
    dfs_stack = [root]
    while dfs_stack:
        current_node = dfs_stack.pop()
        if not current_node.left and not current_node.right:
            sum_left_leaves += current_node.val
        if current_node.left:
            dfs_stack.append(current_node.left)
        if current_node.right and (current_node.right.left or current_node.right.right):
            # filter out right leaf node
            dfs_stack.append(current_node.right)
    return sum_left_leaves


test_cases = [([3, 9, 20, None, None, 15, 7], 24), ([1], 0), ([1, 2], 2), ]
for test_input, expected_output in test_cases:
    assert sum_of_left_leaves(ConstructTree.build_tree_leetcode(test_input).root) == expected_output
