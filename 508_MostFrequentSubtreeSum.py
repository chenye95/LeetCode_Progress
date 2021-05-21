"""
Given the root of a binary tree, return the most frequent subtree sum. If there is a tie, return all the values with the
 highest frequency in any order.

The subtree sum of a node is defined as the sum of all the node values formed by the subtree rooted at that node
 (including the node itself).
"""
from collections import defaultdict
from typing import List

from _Binary_Tree import TreeNode, ConstructTree


def find_frequent_tree_sum(root: TreeNode) -> List[int]:
    """
    :param root: root of a non empty binary tree
    :return: list of most frequent sub tree sums
    """
    frequency_map = defaultdict(int)

    def compute_subtree_sum(current_node: TreeNode) -> int:
        """
        :param current_node: can not be None
        :return: sub tree sum for sub tree beneath current_node
        """
        current_sub_tree_sum = current_node.val + \
                               (compute_subtree_sum(current_node.left) if current_node.left else 0) + \
                               (compute_subtree_sum(current_node.right) if current_node.right else 0)
        frequency_map[current_sub_tree_sum] += 1
        return current_sub_tree_sum

    compute_subtree_sum(root)

    return_list = []
    biggest_freq = 0
    for sum_i, freq_i in frequency_map.items():
        if freq_i > biggest_freq:
            return_list = [sum_i]
            biggest_freq = freq_i
        elif freq_i == biggest_freq:
            return_list.append(sum_i)

    return return_list


test_cases = [([5, 2, -3], {2, -3, 4}),
              ([5, 2, -5], {2}),
              ([10, 5, 15, None, None, 6, 20], {5, 6, 20, 41, 56}),
              ([87, 84, 94, 79, None, None, None, 77, None, -82, None, 70, None, 38, None, 36, 45, 22, None, None, None,
                18, 24, 14, None, None, None, 8, None, -93, None, 6, None, -37, None, -21, 4, -32, None, None, None,
                -15, None, -42, None, -63, None, -70, None, -78, None, 75, None, 7, None, -96, None, -98],
               {94, -187, -431, -190, -260, -365, -278, -380, -467, -412, -433, -194, 4, -513, -323, -120, -553, 61,
                -98, -545, -531, 24, -112, -466, -348, 45, -360, -460, -283, -204}), ]
for test_tree_list, expected_output in test_cases:
    assert set(find_frequent_tree_sum(ConstructTree.build_tree_leetcode(test_tree_list).root)) == expected_output
