"""
Given the root of a binary tree, then value v and depth d, you need to add a row of nodes with value v at the given
depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null tree nodes N in depth d-1, create two tree nodes
 with value v as N's left subtree root and right subtree root. And N's original left subtree should be the left subtree
 of the new left subtree root, its original right subtree should be the right subtree of the new right subtree root. If
 depth d is 1 that means there is no depth d-1 at all, then create a tree node with value v as the new root of the whole
 original tree, and the original tree is the new root's left subtree.
"""
from _Binary_Tree import TreeNode, ConstructTree


def add_one_row(root: TreeNode, value: int, depth: int) -> TreeNode:
    # assume proper input
    if depth == 1:
        return TreeNode(value, left=root)

    current_level = [root]
    current_depth = 1

    while current_depth < depth - 1:
        next_level = [node.left for node in current_level if node.left is not None]
        next_level.extend([node.right for node in current_level if node.right is not None])
        current_depth += 1
        current_level = next_level

    for node in current_level:
        node.left = TreeNode(value, left=node.left)
        node.right = TreeNode(value, right=node.right)

    return root


test_cases = [([4, 2, 6, 3, 1, 5], 1, 1, [1, 4, None, 2, 6, 3, 1, 5]),
              ([4, 2, 6, 3, 1, 5], 1, 2, [4, 1, 1, 2, None, None, 6, 3, 1, 5]),
              ([4, 2, None, 3, 1], 1, 3, [4, 2, None, 1, 1, 3, None, None, 1]),
              ([1], 3, 1, [3, 1]),
              ]
for test_tree_list, test_value, test_depth, expected_output in test_cases:
    test_tree = ConstructTree.build_tree_leetcode(test_tree_list)
    test_tree.root = add_one_row(test_tree.root, test_value, test_depth)
    output_traversal = test_tree.leetcode_traversal()
    assert output_traversal[:len(expected_output)] == expected_output
    assert all(node_i is None for node_i in output_traversal[len(expected_output):])
