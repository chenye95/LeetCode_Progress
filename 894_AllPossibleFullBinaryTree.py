"""
Given an integer n, return a list of all possible full binary trees with n nodes. Each node of each tree in the answer
 must have Node.val == 0.

Each element of the answer is the root node of one possible tree. You may return the final list of trees in any order.

A full binary tree is a binary tree where each node has exactly 0 or 2 children.
"""
from typing import List, Optional

from _Binary_Tree import TreeNode, ConstructTree, CompareTree

_FILLER_VALUE = 0
solution_cache = {
    0: [],
    1: [TreeNode(_FILLER_VALUE)],
}


def all_possible_full_bst(n: int) -> List[Optional[TreeNode]]:
    if n not in solution_cache:
        tree_list = []
        for left_node_count in range(n):
            right_node_count = n - 1 - left_node_count
            for left_tree in all_possible_full_bst(left_node_count):
                for right_tree in all_possible_full_bst(right_node_count):
                    tree_list.append(TreeNode(_FILLER_VALUE, left=left_tree, right=right_tree))
        solution_cache[n] = tree_list

    return solution_cache[n]


test_cases = [
    (3, [[0, 0, 0]]),
    (7, [[0, 0, 0, None, None, 0, 0, None, None, 0, 0], [0, 0, 0, None, None, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, None, None, None, None, 0, 0], [0, 0, 0, 0, 0, None, None, 0, 0]]),
]
for test_n, tree_rep_list in test_cases:
    result_trees = [ConstructTree.build_tree_leetcode(tree_rep).root for tree_rep in tree_rep_list]
    constructed_trees = all_possible_full_bst(test_n)
    assert len(constructed_trees) == len(result_trees)
    for one_tree in constructed_trees:
        assert any(map(lambda ref_tree_root: CompareTree.compare_tree_node(one_tree, ref_tree_root),
                       constructed_trees))
