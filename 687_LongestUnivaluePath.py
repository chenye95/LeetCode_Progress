"""
Given a binary tree, find the length of the longest path where each node in the path has the same value. This path may
or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.
"""
from _Binary_Tree import TreeNode


class Solution:
    def __init__(self):
        self.global_max = 0

    def longest_uni_value_path(self, root: TreeNode) -> int:
        """
        :param root: root node of a binary tree
        :return: length of the longest path where each node has the same value, noted by number of edges on the path
        """
        if not root:
            return 0
        self.longest_uni_value_path_end_at_node(root)
        return self.global_max

    def longest_uni_value_path_end_at_node(self, node: TreeNode) -> int:
        """
        :return: longest uni_value path that ends at node
        """
        if not node or not (node.left or node.right):
            return 0

        # longest path that ends at node.left
        len_left_child = self.longest_uni_value_path_end_at_node(node.left) if node.left else 0
        # longest path that ends at node.right
        len_right_child = self.longest_uni_value_path_end_at_node(node.right) if node.right else 0

        # longest path through node -> node.left
        len_through_left_child = len_left_child + 1 if node.left and node.left.val == node.val else 0
        # longest path through node -> node.right
        len_through_right_child = len_right_child + 1 if node.right and node.right.val == node.val else 0

        # combining the left child leg and right child leg to build a full path
        self.global_max = max(self.global_max, len_through_left_child + len_through_right_child)

        return max(len_through_left_child, len_through_right_child)


from _Binary_Tree import ConstructTree

test_cases = [(ConstructTree.build_tree_leetcode([5, 4, 5, 1, 1, None, 5]), 2),
              (ConstructTree.build_tree_leetcode([1, 4, 5, 4, 4, None, 5]), 2),
              (ConstructTree.build_tree_leetcode([1, 4, 5, 4, 4, 5, None]), 2), ]
solution_class = Solution()
for test_tree, expected_value in test_cases:
    solution_class.global_max = 0
    assert solution_class.longest_uni_value_path(test_tree.root) == expected_value
