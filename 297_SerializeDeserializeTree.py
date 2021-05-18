"""
Serialization is the process of converting a data structure or object into a sequence of bits so that it can be stored
 in a file or memory buffer, or transmitted across a network connection link to be reconstructed later in the same or
 another computer environment.

Design an algorithm to serialize and deserialize a binary tree. There is no restriction on how your
 serialization/deserialization algorithm should work. You just need to ensure that a binary tree can be serialized to
 a string and this string can be deserialized to the original tree structure.

Clarification: The input/output format is the same as how LeetCode serializes a binary tree. You do not necessarily
 need to follow this format, so please be creative and come up with different approaches yourself.
"""
from _Binary_Tree import ConstructTree

test_cases = [[1, 2, 3, None, None, 4, 5],
              [],
              [1],
              [1, 2], ]
for test_tree_list in test_cases:
    old_tree = ConstructTree.build_tree_leetcode(test_tree_list)
    if old_tree:
        assert old_tree == ConstructTree.build_tree_leetcode(old_tree.leetcode_traversal())
