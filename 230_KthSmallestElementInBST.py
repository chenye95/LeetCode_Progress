"""
Given the root of a binary search tree, and an integer k, return the kth (1-indexed) smallest element in the tree.
"""
from _BST import BST
from _Binary_Tree import ConstructTree, TreeNode, TREE_NODE_TYPE


def kth_smallest_element(root: TreeNode, k: int) -> TREE_NODE_TYPE:
    """
    :param root: root node of a non empty binary search tree, 1 <= # of nodes <= 10000
    :param k: 1 <= k <= # of nodes
    :return: value of the kth smallest element in the binary search tree
    """
    return BST(root).kth_smallest_element(k)


test_cases = [([3, 1, 4, None, 2], 1, 1),
              ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
              ([41, 37, 44, 24, 39, 42, 48, 1, 35, 38, 40, None, 43, 46, 49, 0, 2, 30, 36, None, None, None, None, None,
                None, 45, 47, None, None, None, None, None, 4, 29, 32, None, None, None, None, None, None, 3, 9, 26,
                None, 31, 34, None, None, 7, 11, 25, 27, None, None, 33, None, 6, 8, 10, 16, None, None, None, 28, None,
                None, 5, None, None, None, None, None, 15, 19, None, None, None, None, 12, None, 18, 20, None, 13, 17,
                None, None, 22, None, 14, None, None, 21, 23], 25, 24),
              ([5, 3, 6, 2, 4, None, None, 1], 6, 6), ]
for test_tree_list, test_k, expected_output in test_cases:
    assert kth_smallest_element(ConstructTree.build_tree_leetcode(test_tree_list).root, test_k) == expected_output
