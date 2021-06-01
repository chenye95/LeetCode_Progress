"""
You are given the root of a binary tree with n nodes, where each node is uniquely assigned a value from 1 to n. You are
also given a sequence of n values voyage, which is the desired pre-order traversal of the binary tree.

Flip the smallest number of nodes so that the pre-order traversal of the tree matches voyage.

Return a list of the values of all flipped nodes. You may return the answer in any order. If it is impossible to flip
the nodes in the tree to make the pre-order traversal match voyage, return the list [-1].
"""
from typing import List

from _Binary_Tree import TreeNode, ConstructTree, TREE_NODE_TYPE


class FlipMatchVoyage:
    def __init__(self):
        self.voyage_i = 0
        self.valid_so_far = True
        self.flipped_nodes = []

    def flip_match_voyage(self, root: TreeNode, voyage: List[TREE_NODE_TYPE]) -> List[TREE_NODE_TYPE]:
        """
        Depth first approach

        :param root: root node of the binary tree
        :param voyage: desired pre-order traversal of the flipped tree
        :return: list of node values, whose left and right children should be flipped; returned in any order
        """

        def flip_subtree(current_node: TreeNode) -> None:
            """
            :param current_node: DFS currently exploring current_node and its subtree
            """
            if current_node:
                if current_node.val != voyage[self.voyage_i]:
                    # pre-order traversal: current_node is the first in the remainder of the voyage list
                    self.valid_so_far = False
                    return
                self.voyage_i += 1

                if self.voyage_i < len(voyage) and self.valid_so_far:
                    if current_node.left and current_node.left.val != voyage[self.voyage_i]:
                        # current-node's left and right children need to be flipped
                        self.flipped_nodes.append(current_node.val)
                        flip_subtree(current_node.right)
                        flip_subtree(current_node.left)
                    else:
                        # current-node's left and right children don't need to be flipped
                        flip_subtree(current_node.left)
                        flip_subtree(current_node.right)

        flip_subtree(root)
        return self.flipped_nodes if self.valid_so_far else [-1]


test_cases = [([1, 2], [2, 1], [-1]),
              ([1, 2, 3], [1, 3, 2], [1]),
              ([1, 2, 3], [1, 2, 3], []),
              ([1, 5, 6, 7, 2, 4, 3], [1, 5, 2, 6, 3, 4, 7], [-1]),
              ([10, 4, 17, 20, 25, 3, 8, None, 12, 19, 11, None, None, 30, 16, None, None, 2, None, None, None, None,
                None, 18, 1, 22, 27, 6, 5, 28, None, 15, 14, 24, 13, None, 29, None, None, None, None, None, 23, None,
                21, None, None, 9, None, 26, 7],
               [10, 17, 3, 8, 16, 1, 28, 18, 6, 29, 26, 7, 5, 30, 4, 25, 19, 2, 27, 24, 13, 9, 22, 14, 21, 15, 23, 11,
                20, 12],
               [10, 8, 16, 4, 2, 22]),
              ([80, 16, 27, 75, 60, 28, 68, 96, 7, None, 62, 45, 58, None, None, None, 1, 54, 15, 26, 65, 70, 50, 37,
                None, 88, 22, None, 95, 4, 64, None, 33, 47, 85, 13, None, 35, None, 69, None, 74, 78, None, None, None,
                73, 67, None, 51, 61, None, 24, 55, 32, 93, 66, 79, None, None, None, None, None, None, 76, None, 8, 90,
                82, None, None, None, 39, None, None, None, None, 12, 9, 3, 59, 31, 53, None, 6, None, None, 57, None,
                None, None, None, None, None, None, None, 87, None, 41, 99, None, None, 29, 43, None, 5, 49, None, 30,
                None, None, 2, 89, None, None, 84, None, 21, 52, None, None, 100, None, None, 56, 48, 34, 81, 98, None,
                97, 40, 25, 77, None, 20, 46, 86, None, None, 14, None, None, None, 36, None, None, None, 23, 10, 19,
                None, 72, None, None, None, 91, None, None, None, 92, 17, None, None, None, None, None, None, None, 63,
                11, None, None, None, 71, None, 94, None, None, 44, 42, None, 83, None, None, None, None, 18, None,
                None, None, None, None, None, None, None, None, None, 38],
               [80, 27, 68, 28, 58, 37, 69, 45, 70, 13, 79, 50, 35, 16, 75, 7, 54, 95, 73, 90, 82, 15, 4, 67, 64, 61,
                51, 39, 87, 96, 1, 88, 78, 8, 74, 76, 57, 2, 97, 72, 94, 89, 25, 91, 40, 22, 60, 62, 65, 85, 66, 6, 93,
                31, 5, 56, 49, 34, 48, 36, 53, 30, 81, 23, 11, 63, 98, 19, 71, 18, 38, 10, 47, 32, 59, 43, 100, 14, 3,
                29, 55, 9, 99, 21, 46, 17, 83, 20, 92, 42, 44, 52, 86, 12, 41, 84, 77, 26, 33, 24],
               [80, 27, 28, 75, 64, 88, 89, 62, 65, 85, 49, 23, 98, 47, 32, 55, 21, 92]), ]
for test_input, test_voyage, expected_outcome in test_cases:
    solution = FlipMatchVoyage()
    assert solution.flip_match_voyage(ConstructTree.build_tree_leetcode(test_input).root, test_voyage) == \
           expected_outcome, test_voyage
