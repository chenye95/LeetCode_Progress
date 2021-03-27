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
    if root is None:
        return []

    levels = []
    curr_level = [root]
    next_level = []
    # start at second level
    left_to_right = False
    while curr_level:
        levels.append([x.val for x in curr_level])
        curr_level.reverse()
        for node in curr_level:
            if left_to_right:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            else:
                if node.right:
                    next_level.append(node.right)
                if node.left:
                    next_level.append(node.left)

        curr_level = next_level
        left_to_right = not left_to_right
        next_level = []

    return levels


test_cases = [([3, 9, 20, None, None, 15, 7], [[3], [20, 9], [15, 7]]), ]
for test_tree, expected_output in test_cases:
    assert zigzag_level_order(root=ConstructTree.build_tree_leetcode(test_tree).root) == expected_output
