"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum
width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in
the level, where the null nodes between the end-nodes are also counted into the length calculation.
"""
from collections import deque

from _Binary_Tree import TreeNode, ConstructTree


def width_of_binary_tree(root: TreeNode) -> int:
    """
    :param root: root of Binary Tree
    :return: maximum width in the tree
    """
    if not root:
        return 0

    current_level = deque([(root, 0)])
    max_width = 0

    while current_level:
        current_level_node_count = len(current_level)
        start_id = current_id = current_level[0][1]
        for _ in range(current_level_node_count):
            current_node, current_id = current_level.popleft()
            if current_node.left:
                current_level.append((current_node.left, 2 * current_id))
            if current_node.right:
                current_level.append((current_node.right, 2 * current_id + 1))

        end_id = current_id

        max_width = max(max_width, end_id - start_id + 1)

    return max_width


test_cases = [([1, 3, 2, 5, 3, None, 9], 4),
              ([1, 3, None, 5, 3, None, None], 2),
              ([1, 3, 2, 5, None, None, None], 2),
              ([1, 3, 2, 5, None, None, 9, 6, None, None, 7, None, None, None, None], 8)]

for tree_list, expected_out in test_cases:
    test_tree = ConstructTree.build_tree_leetcode(tree_list)
    assert width_of_binary_tree(test_tree.root) == expected_out
