"""
Given two integer arrays, preorder and postorder where preorder is the preorder traversal of a binary tree of distinct
 values and postorder is the postorder traversal of the same tree, reconstruct and return the binary tree.

If there exist multiple answers, you can return any of them.
"""
from typing import List, Optional

from _Binary_Tree import TreeNode, TREE_NODE_TYPE, BinaryTree


def construct_from_pre_post_in_place(preorder: List[TREE_NODE_TYPE],
                                     postorder: List[TREE_NODE_TYPE]) -> Optional[TreeNode]:
    assert len(preorder) == len(postorder)
    if not preorder:
        return None
    return construct_helper(preorder, postorder, 0, len(preorder) - 1, 0, len(preorder) - 1)


def construct_helper(preorder: List[TREE_NODE_TYPE], postorder: List[TREE_NODE_TYPE],
                     pre_start_idx: int, pre_end_idx: int,
                     post_start_idx: int, post_end_idx: int) -> Optional[TreeNode]:
    # assert preorder[pre_start_idx] == postorder[post_end_idx]
    if pre_start_idx > pre_end_idx:
        return None
    elif pre_start_idx == pre_end_idx:
        return TreeNode(preorder[pre_start_idx])
    elif pre_start_idx == pre_end_idx - 1:
        return TreeNode(preorder[pre_start_idx],
                        left=TreeNode(preorder[pre_start_idx + 1]))
    left_child_pos = postorder.index(preorder[pre_start_idx + 1], post_start_idx, post_end_idx + 1)
    left_tree_len = left_child_pos - post_start_idx + 1
    return TreeNode(preorder[pre_start_idx],
                    left=construct_helper(preorder, postorder,
                                          pre_start_idx + 1, pre_start_idx + left_tree_len,
                                          post_start_idx, left_child_pos),
                    right=construct_helper(preorder, postorder,
                                           pre_start_idx + left_tree_len + 1, pre_end_idx,
                                           left_child_pos + 1, post_end_idx - 1))


def construct_from_pre_post_relist(preorder: List[TREE_NODE_TYPE],
                                   postorder: List[TREE_NODE_TYPE]) -> Optional[TreeNode]:
    if not preorder:
        return None
    if len(preorder) == 1:
        return TreeNode(preorder[0])

    left_child_pos = postorder.index(preorder[1])
    return TreeNode(preorder[0],
                    left=construct_from_pre_post_relist(preorder[1: left_child_pos + 2],
                                                        postorder[:left_child_pos + 1]),
                    right=construct_from_pre_post_relist(preorder[left_child_pos + 2:],
                                                         postorder[left_child_pos + 1: -1]))


test_cases = [
    ([1], [1]),
    ([1, 2, 4, 5, 3, 6, 7], [4, 5, 2, 6, 7, 3, 1]),
    ([2, 1], [1, 2]),
    ([2, 1, 3], [3, 1, 2]),
    ([8, 6, 3, 10, 7, 5, 1, 4, 2, 9, 11], [5, 7, 1, 10, 3, 6, 11, 9, 2, 4, 8]),
    ([12, 6, 5, 17, 10, 18, 21, 2, 19, 11, 20, 16, 9, 8, 1, 7, 13, 14, 3, 4, 15],
     [17, 5, 19, 9, 1, 8, 16, 20, 14, 13, 7, 11, 2, 15, 4, 3, 21, 18, 10, 6, 12]),
    ([2, 14, 21, 22, 15, 16, 8, 4, 10, 19, 12, 26, 24, 1, 20, 9, 6, 25, 23, 7, 5, 13, 3, 18, 11, 17],
     [15, 22, 19, 10, 4, 8, 16, 21, 14, 20, 1, 24, 26, 7, 23, 11, 18, 3, 13, 5, 25, 6, 17, 9, 12, 2]),
]

for construct_from_pre_post in [construct_from_pre_post_in_place, construct_from_pre_post_relist]:
    for test_preorder, test_postorder in test_cases:
        test_tree = BinaryTree(construct_from_pre_post(test_preorder, test_postorder))
        assert test_tree.preorder_traversal() == test_preorder, construct_from_pre_post.__name__
        assert test_tree.postorder_traversal() == test_postorder, construct_from_pre_post.__name__
