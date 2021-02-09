"""
Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is
changed to the original key plus sum of all keys greater than the original key in BST.
"""
from _Binary_Tree import TreeNode, ConstructTree


def convert_bst_recurse(root: TreeNode) -> TreeNode:
    """
    Recursion with helper function
    In order traversal, from right to left -> from biggest to smallest
    :param root: root node of a binary search tree
    :return: root again, no modification
    """
    accumulator = 0

    def convert_bst_helper(current_node: TreeNode) -> None:
        nonlocal accumulator
        if current_node is not None:
            convert_bst_helper(current_node.right)
            accumulator += current_node.val
            current_node.val = accumulator
            convert_bst_helper(current_node.left)

    convert_bst_helper(root)
    return root


def convert_bst_stack(root: TreeNode) -> TreeNode:
    """
    Iteration with a stack
    In order traversal, from right to left -> from biggest to smallest
    :param root: root node of a binary search tree
    :return: root again, no modification
    """
    accumulator = 0

    current_node = root
    stack = []

    while stack or current_node is not None:
        # push all nodes up to (and including) subtree's maximum onto stack
        while current_node is not None:
            stack.append(current_node)
            current_node = current_node.right

        current_node = stack.pop()
        accumulator += current_node.val
        current_node.val = accumulator

        # all nodes with values between current_node and its parents lie in the left subtree of current_node
        current_node = current_node.left

    return root


def convert_bst_morris(root: TreeNode) -> TreeNode:
    """
    Reversed Morris In-order Traversal
    In order traversal, from right to left -> from biggest to smallest
    :param root: root node of a binary search tree
    :return: root again, no modification
    """
    accumulator = 0
    current_node = root

    while current_node is not None:
        if current_node.right is None:
            # If there is no right subtree under current_node, visit this node and continue traversing left
            accumulator += current_node.val
            current_node.val = accumulator
            current_node = current_node.left
        else:
            # there is a right subtree under current_node: traverse right node first
            # find the left most node in the right subtree of current_node
            successor = current_node.right
            while successor.left is not None and successor.left is not current_node:
                successor = successor.left

            if successor.left is None:
                # no left subtree under successor, make a temporary connection back to current_node
                # for future traversal
                successor.left = current_node
                current_node = current_node.right
            else:
                # there is left subtree: this is the temporary connection created in previous path
                # unlink the path and visit current_node
                successor.left = None
                accumulator += current_node.val
                current_node.val = accumulator
                current_node = current_node.left

    return root


test_cases = [([4, 1, 6, 0, 2, 5, 7, None, None, None, 3, None, None, None, 8],
               [30, 36, 21, 36, 35, 26, 15, None, None, None, 33, None, None, None, 8]),
              ([0, None, 1], [1, None, 1]),
              ([1, 0, 2], [3, 3, 2]),
              ([3, 2, 4, 1], [7, 9, 4, 10])]

for test_input, expected_output in test_cases:
    for convert_bst in [convert_bst_stack, convert_bst_morris, convert_bst_recurse]:
        test_tree = ConstructTree.build_tree_leetcode(test_input)
        test_tree.root = convert_bst(test_tree.root)
        assert test_tree.leetcode_traversal()[:len(expected_output)] == expected_output, convert_bst.__name__
