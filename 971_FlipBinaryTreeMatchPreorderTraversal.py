"""
You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are
also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip
the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].
"""
from typing import List

from _Binary_Tree import TreeNode, ConstructTree, TREE_NODE_TYPE


# Global parameters


class FlipMatchVoyage():
    def __init__(self):
        self.voyage_i = 0
        self.flipped_nodes = []

    def flip_match_voyage(self, root: TreeNode, voyage: List[TREE_NODE_TYPE]) -> List[TREE_NODE_TYPE]:
        """
        Depth first approach

        :param root: root node of the binary tree
        :param voyage: desired pre-order traversal of the flipped tree
        :return: list of node values, whose left and right children should be flipped; returned in any order
        """

        def dfs_explore(current_node: TreeNode) -> None:
            """
            :param current_node: DFS currently exploring current_node and its subtree
            """
            if current_node:
                if current_node.val != voyage[self.voyage_i]:
                    # pre-order traversal: current_node is the first in the remainder of the voyage list
                    self.flipped_nodes = [-1]
                    return
                self.voyage_i += 1

                if self.voyage_i < len(voyage):
                    if current_node.left and current_node.left.val != voyage[self.voyage_i]:
                        # current-node's left and right children need to be flipped
                        self.flipped_nodes.append(current_node.val)
                        dfs_explore(current_node.right)
                        dfs_explore(current_node.left)
                    else:
                        # current-node's left and right children don't need to be flipped
                        dfs_explore(current_node.left)
                        dfs_explore(current_node.right)

        dfs_explore(root)
        if self.flipped_nodes and self.flipped_nodes[0] == -1:
            return [-1]
        else:
            return self.flipped_nodes


test_cases = [([1, 2], [2, 1], {-1}),
              ([1, 2, 3], [1, 3, 2], {1}),
              ([1, 2, 3], [1, 2, 3], set()),
              ([1, 5, 6, 7, 2, 4, 3], [1, 5, 2, 6, 3, 4, 7], {-1}),
              ([10, 4, 17, 20, 25, 3, 8, None, 12, 19, 11, None, None, 30, 16, None, None, 2, None, None, None, None,
                None, 18, 1, 22, 27, 6, 5, 28, None, 15, 14, 24, 13, None, 29, None, None, None, None, None, 23, None,
                21, None, None, 9, None, 26, 7],
               [10, 17, 3, 8, 16, 1, 28, 18, 6, 29, 26, 7, 5, 30, 4, 25, 19, 2, 27, 24, 13, 9, 22, 14, 21, 15, 23, 11,
                20, 12], {10, 8, 16, 4, 2, 22}), ]
for test_input, test_voyage, expected_outcome in test_cases:
    solution = FlipMatchVoyage()
    assert set(solution.flip_match_voyage(ConstructTree.build_tree_leetcode(test_input).root, test_voyage)) == \
           expected_outcome, test_voyage
