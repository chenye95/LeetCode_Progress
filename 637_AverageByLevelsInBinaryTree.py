"""
Given a non-empty binary tree, return the average value of the nodes on each level in the form of an array.
"""
from typing import List

from _Binary_Tree import ConstructTree, TreeNode


def average_of_levels(root: TreeNode) -> List[float]:
    """
    BFS solution

    :param root: root of binary tree
    :return: list of float, each represent average of node values in a level
    """
    if not root:
        return []

    current_level = [root]
    list_avg = []

    while current_level:
        current_level_sum = 0.0
        next_level = []
        for node in current_level:
            current_level_sum += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

        list_avg.append(current_level_sum / len(current_level))
        current_level = next_level

    return list_avg


test_cases = [([3, 9, 20, None, None, 15, 7], [3, 14.5, 11]),
              ([3, 9, 20, 15, 7], [3, 14.5, 11]), ]
for test_tree_list, expected_output in test_cases:
    assert average_of_levels(ConstructTree.build_tree_leetcode(test_tree_list).root) == expected_output
