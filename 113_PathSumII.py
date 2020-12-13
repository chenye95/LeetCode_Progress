"""
Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.
"""
from typing import List

from _Binary_Tree import TreeNode


def path_sum(root: TreeNode, target_sum: int) -> List[List[int]]:
    """
    DFS Solution
    :param root: root of Binary Tree
    :param target_sum: target sum for root-to-leaf paths add up to
    :return: list of all root-to-leaf paths that add up to target_sum; each path is represented as list of node values
    """

    def dfs_traverse(current_node: TreeNode, remaining_sum: int) -> List[List[int]]:
        """
        :param current_node: start of node-to-leaf path
        :param remaining_sum: target sum for node-to-leaf paths add up to
        :return: list of all node-to-leaf paths that add up to remaining_sum;
                each path is represented as list of node value
        """
        if not current_node.left and not current_node.right:
            if current_node.val == remaining_sum:
                return [[remaining_sum, ]]
            else:
                return []
        
        path_start_at_node = []
        remaining_sum -= current_node.val
        if current_node.left:
            path_start_at_node.extend([[current_node.val] + list_left_node
                                       for list_left_node in dfs_traverse(current_node.left, remaining_sum)])
        if current_node.right:
            path_start_at_node.extend([[current_node.val] + list_right_node
                                       for list_right_node in dfs_traverse(current_node.right, remaining_sum)])
        return path_start_at_node

    if not root:
        return []
    return dfs_traverse(root, target_sum)


from _Binary_Tree import ConstructTree

test_cases = ConstructTree.build_tree_leetcode([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
assert path_sum(test_cases.root, 22) == [[5, 4, 11, 2], [5, 8, 4, 5]]
