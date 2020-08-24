"""
Given a binary tree, return the sum of values of its deepest leaves.
"""
from _Binary_Tree import TreeNode


def deepest_leaves_sum(root: TreeNode) -> int:
    """
    :param root: root of the binary tree
    :return: sum of node values for its deepest leaves
    """
    if not root:
        return 0

    next_level = [root]
    current_level_sum = 0

    while next_level:
        current_level = next_level
        current_level_sum = 0
        next_level = []
        for node in current_level:
            if not next_level:
                # only add to current_level_sum if we haven't found a node in next level yet
                current_level_sum += node.val
            if node.left:
                next_level.append(node.left)
            if node.right:
                next_level.append(node.right)

    return current_level_sum


from _Binary_Tree import ConstructTree

test_tree = ConstructTree.build_tree_leetcode([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
assert deepest_leaves_sum(test_tree.root) == 15
