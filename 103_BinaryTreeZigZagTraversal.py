"""
Given a binary tree, return the zigzag level order traversal of its nodes' values. (ie, from left to right, then right
to left for the next level and alternate between).
"""
from typing import List

from _Binary_Tree import TreeNode, ConstructTree


def zigzag_level_order(root: TreeNode) -> List[List[int]]:
    """
    :param root: root of the binary tree
    :return: zig zag traversal order of the binary tree
    """
    if not root:
        return []

    return_result = []
    current_level_queue = [root]
    level_i = 0
    while current_level_queue:
        level_i += 1
        if level_i % 2:
            return_result.append([current_node.val for current_node in current_level_queue])
        else:
            return_result.append([current_node.val for current_node in current_level_queue][::-1])
        next_level_queue = []
        for current_node in current_level_queue:
            if current_node.left:
                next_level_queue.append(current_node.left)
            if current_node.right:
                next_level_queue.append(current_node.right)
        current_level_queue = next_level_queue

    return return_result


test_tree_node = ConstructTree.build_tree_leetcode([3, 9, 20, None, None, 15, 7]).root
assert [[3], [20, 9], [15, 7]] == zigzag_level_order(test_tree_node)
