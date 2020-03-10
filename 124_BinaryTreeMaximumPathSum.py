"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the
parent-child connections. The path must contain at least one node and does not need to go through the root.
"""
from _Binary_Tree import TreeNode


class Solution:
    def maxPathEndAtNode(self, node: TreeNode) -> int:
        """
        :param node:
        :return: max value of the path ends at node. return 0 if the max path is negative
        """
        if not node:
            return 0
        left_max = self.maxPathEndAtNode(node.left)
        right_max = self.maxPathEndAtNode(node.right)
        self.global_max = max(self.global_max, left_max + node.val + right_max)
        return max(node.val + max(left_max, right_max), 0)

    def maxPathSum(self, root: TreeNode) -> int:
        self.global_max = -2 ** 31 + 1
        self.maxPathEndAtNode(root)
        return self.global_max


from _Binary_Tree import ConstructTree

test_cases = [(ConstructTree.build_tree_leetcode([1, 2, 3]), 6),
              (ConstructTree.build_tree_leetcode([-10, 9, 20, None, None, 15, 7]), 42)]

solution_class = Solution()
for test_tree, expected_value in test_cases:
    assert solution_class.maxPathSum(test_tree.root) == expected_value
