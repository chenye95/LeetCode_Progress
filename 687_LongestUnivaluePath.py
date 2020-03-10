"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may
or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.
"""
from _Binary_Tree import TreeNode


class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.global_max = 0
        self.longestUnivaluePathEndAtNode(root)
        return self.global_max

    def longestUnivaluePathEndAtNode(self, node: TreeNode) -> int:
        if not node:
            return 0
        left_len = self.longestUnivaluePathEndAtNode(node.left) if node.left else 0
        right_len = self.longestUnivaluePathEndAtNode(node.right) if node.right else 0
        traverse_through_left = left_len + 1 if node.left and node.left.val == node.val else 0
        traverse_through_right = right_len + 1 if node.right and node.right.val == node.val else 0
        self.global_max = max(self.global_max, traverse_through_left + traverse_through_right)
        return max(traverse_through_left, traverse_through_right)


from _Binary_Tree import ConstructTree

test_cases = [(ConstructTree.build_tree_leetcode([5, 4, 5, 1, 1, None, 5]), 2),
              (ConstructTree.build_tree_leetcode([1, 4, 5, 4, 4, None, 5]), 2)]
solution_class = Solution()
for test_tree, expected_value in test_cases:
    assert solution_class.longestUnivaluePath(test_tree.root) == expected_value
