"""
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake.
Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?
"""
from typing import Tuple

from _Binary_Tree import TreeNode, ConstructTree


def recover_bst(root: TreeNode) -> None:
    """
    A valid BST would have inorder traversal in ascending order,
    i.e. for any adjacent node prev, curr in inorder traversal prev.val <= curr.val
    Once we see prev.val > cur.val, we know either prev or cur is out of place
    Since there are exactly two nodes that were swapped, we can encounter the reversed pair up to 2 times
    - if we encounter such pair only once, then prev and curr are swapped
    - if we encounter such pair twice, (prev_1, curr_1) and (prev_2, curr_2), then prev_1 and curr_2 are swapped

    Use Morris inorder traversal to achieve O(1) space

    :param root: root of the BST with minor defect
    :return: in place modifications
    """
    prev_node = None
    first_node = second_node = None
    current_node = root
    while current_node:
        if current_node.left is None:
            # no left subtree of current_node
            # check for reversed pair
            if prev_node and prev_node.val > current_node.val:
                if first_node is None:
                    first_node, second_node = prev_node, current_node
                else:
                    second_node = current_node
            # move onto the right subtree if exists
            # or trace back to its parents
            prev_node = current_node
            current_node = current_node.right
        else:
            # go the right most node in the left subtree of current_node
            tmp_node = current_node.left
            while tmp_node.right and tmp_node.right != current_node:
                tmp_node = tmp_node.right

            if tmp_node.right is None:
                # first time visit the right most node
                # construct link to current_node to push current_node for future consideration
                tmp_node.right = current_node
                current_node = current_node.left
            else:
                # visited before, tmp_node.right = current_node
                if prev_node and prev_node.val > current_node.val:
                    if first_node is None:
                        first_node, second_node = prev_node, current_node
                    else:
                        second_node = current_node

                # need to break the right link
                tmp_node.right = None
                # move to current_node's right tree if exists
                # or back trace to it's parent
                prev_node = current_node
                current_node = current_node.right

    first_node.val, second_node.val = second_node.val, first_node.val


def is_valid_BST(root: TreeNode) -> bool:
    """
    From 98 checker from correct answer, but supports equality

    :param root: root of a binary tree
    :return: whether the tree is a valid Binary Search Tree
    """
    _invalid_bst_lower, _invalid_bst_upper = 1, 0

    def BST_checker(current_node: TreeNode) -> Tuple[int, int]:
        if current_node.left:
            left_lower, left_upper = BST_checker(current_node.left)
            # Left tree contains nodes with keys less than or equal to node's key
            if left_lower > left_upper or left_upper > current_node.val:
                return _invalid_bst_lower, _invalid_bst_upper
        else:
            left_lower = current_node.val
        if current_node.right:
            right_lower, right_upper = BST_checker(current_node.right)
            # Right tree contains nodes with keys greater than or equal to node's key
            if right_lower > right_upper or right_lower < current_node.val:
                return _invalid_bst_lower, _invalid_bst_upper
        else:
            right_upper = current_node.val

        return left_lower, right_upper

    if not root:
        return True

    tree_lower, tree_upper = BST_checker(root)
    return tree_lower <= tree_upper


test_cases = [[3, 1, 4, None, None, 2], [1, 3, None, None, 2], ]
for tree_list in test_cases:
    test_tree = ConstructTree.build_tree_leetcode(tree_list)
    assert not is_valid_BST(root=test_tree.root)
    recover_bst(root=test_tree.root)
    assert is_valid_BST(root=test_tree.root)
