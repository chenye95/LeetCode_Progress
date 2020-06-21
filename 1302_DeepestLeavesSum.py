"""
Given a binary tree, return the sum of values of its deepest leaves.
"""
from _Binary_Tree import TreeNode, ConstructTree


def deepestLeavesSum(root: TreeNode) -> int:
    if not root:
        return 0
    next_level = {root}
    current_sum = 0
    while next_level:
        current_level = next_level
        current_sum = 0
        next_level = set()
        for node in current_level:
            if not next_level:
                current_sum += node.val
            if node.left:
                next_level.add(node.left)
            if node.right:
                next_level.add(node.right)
    return current_sum


test_tree = ConstructTree.build_tree_leetcode([1, 2, 3, 4, 5, None, 6, 7, None, None, None, None, 8])
assert deepestLeavesSum(test_tree.root) == 15
