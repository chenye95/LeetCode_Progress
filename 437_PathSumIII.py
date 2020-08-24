"""
You are given a binary tree in which each node contains an integer value. Find the number of paths that sum to a given
value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes
 to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.
"""
from typing import Dict

from _Binary_Tree import TreeNode


def path_sum(root: TreeNode, target_sum: int) -> int:
    """
    :param root: root of binary tree
    :param target_sum: target sum for a path to add up to
    :return: # of paths that add up to target sum
    """

    def dfs_traverse(current_node: TreeNode, root_to_parent_sum: int, cache: Dict[int, int]) -> int:
        """
        :param current_node: exploring sub path of path root -> current_node
        :param root_to_parent_sum: path sum from root to current_node's parent
        :param cache: among paths from root to ancestors of current_node, {path_sum: path_count}
        :return: # of paths that end at current_node and add up to target_sum + cumulative results from its descendants
        """
        if not current_node:
            return 0

        root_to_node_sum = root_to_parent_sum + current_node.val
        root_to_path_start_sum = root_to_node_sum - target_sum

        # count of paths that end at current_node and add up to target_sum
        path_count = cache.get(root_to_path_start_sum, 0)

        cache[root_to_node_sum] = cache.get(root_to_node_sum, 0) + 1
        path_count += dfs_traverse(current_node.left, root_to_node_sum, cache)
        path_count += dfs_traverse(current_node.right, root_to_node_sum, cache)

        # clear the root -> current_node path before backtracking to a different path
        cache[root_to_node_sum] -= 1

        return path_count

    path_sum_cache = {0: 1}
    return dfs_traverse(root, 0, path_sum_cache)


from _Binary_Tree import ConstructTree

test_tree = ConstructTree.build_tree_leetcode([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
assert path_sum(test_tree.root, 8) == 3
