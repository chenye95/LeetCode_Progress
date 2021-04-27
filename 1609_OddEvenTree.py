"""
A binary tree is named Even-Odd if it meets the following conditions:
- The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index
 2, etc.
- For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left
 to right).
- For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left
 to right).

Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.
"""

from _Binary_Tree import TreeNode, ConstructTree


def is_even_odd_tree(root: TreeNode):
    """
    :param root: root of a Binary tree with 1 <= node_count <= 10**5 nodes, i.e. root cannot be None
    :return: the tree is an even odd tree
    """
    next_level = [root]
    is_even_level = False

    while next_level:
        is_even_level = not is_even_level
        previous_val = None
        current_level = next_level
        next_level = []

        for current_node in current_level:
            if (is_even_level and current_node.val % 2 == 0) or (not is_even_level and current_node.val % 2 == 1):
                # Even rows have only odd node values, while odd rows have only even node values
                return False

            if previous_val and ((is_even_level and previous_val >= current_node.val) or
                                 (not is_even_level and previous_val <= current_node.val)):
                # Even rows are strictly increasing while odd rows are strictly decreasing
                return False

            if current_node.left:
                next_level.append(current_node.left)
            if current_node.right:
                next_level.append(current_node.right)

            previous_val = current_node.val

    return True


test_cases = [([1, 10, 4, 3, None, 7, 9, 12, 8, 6, None, None, 2], True),
              ([5, 4, 2, 3, 3, 7], False),
              ([5, 9, 1, 3, 5, 7], False),
              ([1], True),
              ([11, 8, 6, 1, 3, 9, 11, 30, 20, 18, 16, 12, 10, 4, 2, 17], True), ]
for test_tree_list, expected_output in test_cases:
    assert is_even_odd_tree(ConstructTree.build_tree_leetcode(test_tree_list).root) is expected_output, test_tree_list
