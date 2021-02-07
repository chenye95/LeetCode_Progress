"""
Given a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see
ordered from top to bottom.
"""
# Only as placeholder for test cases
from _Binary_Tree import ConstructTree

test_case = ConstructTree.build_tree_leetcode([1, 2, 3, None, 5, None, 4])
assert test_case.right_side_view() == [1, 3, 4]
