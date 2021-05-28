"""
Given an n-ary tree, return the level order traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal, each group of children is separated by the
 None value (See examples).
"""
from typing import List, Optional


class TreeNode:
    def __init__(self, val=None, children: Optional[List['TreeNode']] = None):
        self.val = val
        self.children: List[TreeNode] = children if children else []


def create_n_ary_tree(tree_list: List[Optional[int]]) -> Optional[TreeNode]:
    """
    :param tree_list: input Nary-Tree input serialization is represented in their level order traversal, each group of
        children is separated by the None value
    :return: tree node of the n-ary tree created from tree_list
    """
    if not tree_list:
        return None
    tree_root = TreeNode(val=tree_list[0])

    outstanding_node = []
    current_parent = tree_root
    for val_i in tree_list[2:]:
        if val_i is None:
            current_parent = outstanding_node.pop(0)
        else:
            next_node = TreeNode(val=val_i)
            current_parent.children.append(next_node)
            outstanding_node.append(next_node)

    return tree_root


def level_order(root: Optional[TreeNode]) -> List[List[int]]:
    """
    :param root: root of the n ary tree. Can be None
    :return: Level by level order traversal of the tree
    """
    if not root:
        return []

    order_traversal = []
    current_level = [root]
    while current_level:
        next_level = []
        order_traversal.append([current_parent.val for current_parent in current_level])
        for current_parent in current_level:
            if current_parent.children:
                next_level.extend(current_parent.children)
        current_level = next_level

    return order_traversal


test_cases = [([], []),
              ([1, None, 3, 2, 4, None, 5, 6], [[1], [3, 2, 4], [5, 6]]),
              ([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
                None, 14],
               [[1], [2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13], [14]]),
              ([48, None, 79, 0, 94, None, None, 44, 64, None, 69, 71, 46, None, None, 45, None, 2, 9, 22, None, 57, 77,
                31, None, 8, 56, 1, None, 59, 86, 0, None, None, 100, 99, 67, None, 69, 79, 24, None, 2, 66, None, 11,
                76, None, None, 95, 58, 78, None, 97, 53, None, 100, None, 42, None, 38, 99, 54, None, 21, 12, 23, None,
                34, 39, None, None, None, None, None, 100, 82, None, 81, 41, None, None, None, 21, 59, None, None, None,
                12, 16, None, None, None, 57, 99, None, 69, 73, 31, None, 30, 66, 50, None, 34, None, 5, 11, 60, None,
                None, 32, 97, 16, None, 27, None, None, 34, 92, None, 66, 39, 85, None, 6, None, 66, None, 62, None, 60,
                None, None, 95, 91, None, 32, None, None, 5, None, None, 9, 27, None, 36, None, 98, 10, None, None,
                None, 98, None, 68, 4, None, None, 1, None, 82, 78, None, None, 87, 93, None, 70, 73, 69, None, 18, 15,
                None, 19, None, 100, 64, None, 40, 52, None, 49, 78, None, 35, None, None, 38, 1, None, 45, 21, 47,
                None, None, 83, None, 37, None, 8, 65, 8, None, 46, 65, 23, None, 47, 87, None, 92, 41, 29, None, None,
                96, 14, None, 79, 41, None, None, 90, 32, None, 92, 51, None, 96, 80, 98, None, 86, None, None, 53, 45,
                None, 78, 57, 3, None, 98, 6, None, None, 70, None, 27, 14, 42, None, 24, None, 37, 91, None, 38, 48, 8,
                None, None, 56, 32, 53, None, 33, None, 55, 8, 75, None, 17, 39, 92, None, None, 60, 44, 9, None, None,
                63, 35, 11, None, 19, 52, 61, None, 71, 55, None, 53, 95, 0, None, None, 27, 67, None, None, 11, None,
                None, 96, None, 29, None, 75, 40, 15, None, 93, None, 21, 13, None, None, None, 83, 59, 59, None, 72,
                None, 100, 98, None, None, 41, None, None, 2, 96, 16, None, 40, 66, None, None, None, 32, None, 99, 2,
                54, None, 2, 4, 68, None, 25, None, None, 27, 8, 57, None, 42, None, 25, 48, None, 28, 17, 99, None, 84,
                64, 86, None, 22, None, 7, 42, 28, None, 40, 59, 14, None, 6, 12, 42, None, None, None, None, None, 75,
                None, 12, None, 78, 10, 61, None, 40, None, 52, None, None, None, 54, 56, None, 26, 53, None, 82, None,
                None, 68, 59, 4, None, 90, None, 78, 87, None, 79, None, 85, None, 90, 58, None, 10, None, None, 87,
                None, 78, None, 76, None, None, 86, None, 46, 53, None, 20, 21, 51, None, None, 79, 50, 69, None, 94,
                None, None, 20, 3, None, 24, 87, None, 52, 81, 33, None, None, None, 57, 90, 21, None, 56, None, 52, 66,
                None, 76, 94, None, 78, 85, None, 65, 91, None, 19, None, 71, None, None, 84, 36, None, 38, None, None,
                63, 1, 71, None, 38, 93, None, 27, None, 50, None, 39, None, 80, 24, None, 67, 60, None, 41, 19, 87,
                None, 29, 86, 98, None, 79, 33, 57, None, 89, 36, None, 30, None, 13, None, 17, 93, None, None, None,
                None, None, 17, None, 79, None, 44, None, 34, None, 12, 3, 54, None, None, None, 71, 33, None, 9, 0,
                None, 89, 0, None, 0, None, 80, 14, None, 52, None, 45, 18, None, 89, None, None, 13, None, 71, 46, 91,
                None, None, 1, 77, 52, None, 5, None, 36, None, 47, 65, 69, None, None, 83, 91, None, 59, None, 75, 90,
                None, 35, None, 22, 55, None, 56, 7, None, 77, 100, 34, None, 73, 23, None, 7, None, 86, 59, 43, None,
                75, 98, 58, None, 55, 53, None, 76, None, 9, 62, None, 71, 43, None, None, 67, None, 61, 44, 48, None,
                69, 69, None, 39, None, 41, 65, 52, None, 39, 39, 20, None, None, None, None, 6, 77, 83, None, 11, 97,
                None, 81, None, None, 64, 7, None, 50, 9, 0, None, 47, 76, 34, None, None, 30, 16, None, None, None, 3,
                94, 53, None, 61, 23, None, 100, 12, None, 77, 6, None, 32, 5, None, None, 82, 50, 47, None, 76, 39, 72,
                None, None, 84, 8, None, 21, 49, None, 17, 12, 16, None, 33, None, None, 2, 57, None, 60, 24, None, 88,
                27, None, None, None, 48, 88, 55, None, 88, 72, 28, None, 24, 64, 41, None, 56, 16, None, 45, 13, 16,
                None, None, 64, 19, 35, None, None, 45, 81, None, 6, 29, 84, None, 66, None, None, None, None, 65, None,
                None, 19, 61, None, None, None, 68, 50, None, 14, None, None, 11, None, 68, 66, 23, None, None, 33, 79,
                None, 63, None, None, 74, 71, None, 49, None, 1, None, 18, 7, 58, None, 40, 34, None, 37, 44, None,
                None, 89, None, 88, None, None, 69, None, 80, 64, None, 0, 34, 11, None, 69, 40, 81, None, 42, 71, None,
                42, 10, None, None, 98, 49, 17, None, 42, 96, None, 16, 64, None, 92, None, 39, 41, None, 43, 84, None,
                None, 32, 57, 50, None, 68, None, None, None, 59, 13, 43, None, None, 41, None, 5, None, 58, None, 84,
                16, None, 42, None, 42, 37, 40, None, 64, 51, None, 34, None, 4, None, 61, 27, None, 21, None, 88, None,
                71, None, 47, 23, 30, None, None, 46, None, 13, None, 64, 56, 27, None, 43, 39, 95, None, 99, 74, None,
                65, 82, None, None, 28, 75, None, 15, 0, 75, None, 77, 73, None, 45, 93, None, 11, 15, None, None, 79,
                33, 23, None, 8, 17, 76],
               [[48], [79, 0, 94], [44, 64, 69, 71, 46], [45, 2, 9, 22, 57, 77, 31, 8, 56, 1],
                [59, 86, 0, 100, 99, 67, 69, 79, 24, 2, 66, 11, 76, 95, 58, 78, 97, 53, 100],
                [42, 38, 99, 54, 21, 12, 23, 34, 39, 100, 82, 81, 41, 21, 59, 12, 16, 57, 99],
                [69, 73, 31, 30, 66, 50, 34, 5, 11, 60, 32, 97, 16, 27, 34, 92, 66, 39, 85, 6, 66, 62, 60, 95, 91, 32,
                 5],
                [9, 27, 36, 98, 10, 98, 68, 4, 1, 82, 78, 87, 93, 70, 73, 69, 18, 15, 19, 100, 64, 40, 52, 49, 78, 35,
                 38, 1, 45, 21, 47, 83, 37, 8, 65, 8],
                [46, 65, 23, 47, 87, 92, 41, 29, 96, 14, 79, 41, 90, 32, 92, 51, 96, 80, 98, 86, 53, 45, 78, 57, 3, 98,
                 6, 70, 27, 14, 42, 24, 37, 91, 38, 48, 8, 56, 32, 53, 33, 55, 8, 75, 17, 39, 92, 60, 44, 9, 63, 35, 11,
                 19, 52, 61, 71, 55, 53, 95, 0, 27, 67],
                [11, 96, 29, 75, 40, 15, 93, 21, 13, 83, 59, 59, 72, 100, 98, 41, 2, 96, 16, 40, 66, 32, 99, 2, 54, 2,
                 4, 68, 25, 27, 8, 57, 42, 25, 48, 28, 17, 99, 84, 64, 86, 22, 7, 42, 28, 40, 59, 14, 6, 12, 42, 75, 12,
                 78, 10, 61, 40, 52, 54, 56, 26, 53, 82, 68, 59, 4, 90, 78, 87, 79, 85, 90, 58, 10, 87, 78, 76, 86, 46,
                 53, 20, 21, 51],
                [79, 50, 69, 94, 20, 3, 24, 87, 52, 81, 33, 57, 90, 21, 56, 52, 66, 76, 94, 78, 85, 65, 91, 19, 71, 84,
                 36, 38, 63, 1, 71, 38, 93, 27, 50, 39, 80, 24, 67, 60, 41, 19, 87, 29, 86, 98, 79, 33, 57, 89, 36, 30,
                 13, 17, 93, 17, 79, 44, 34, 12, 3, 54, 71, 33, 9, 0, 89, 0, 0, 80, 14, 52, 45, 18, 89, 13, 71, 46, 91,
                 1, 77, 52, 5, 36, 47, 65, 69, 83, 91, 59, 75, 90, 35, 22, 55, 56, 7, 77, 100, 34, 73, 23, 7, 86, 59,
                 43, 75, 98, 58, 55, 53, 76, 9, 62, 71, 43, 67, 61, 44, 48, 69, 69, 39],
                [41, 65, 52, 39, 39, 20, 6, 77, 83, 11, 97, 81, 64, 7, 50, 9, 0, 47, 76, 34, 30, 16, 3, 94, 53, 61, 23,
                 100, 12, 77, 6, 32, 5, 82, 50, 47, 76, 39, 72, 84, 8, 21, 49, 17, 12, 16, 33, 2, 57, 60, 24, 88, 27,
                 48, 88, 55, 88, 72, 28, 24, 64, 41, 56, 16, 45, 13, 16, 64, 19, 35, 45, 81, 6, 29, 84, 66, 65, 19, 61,
                 68, 50, 14, 11, 68, 66, 23, 33, 79, 63, 74, 71, 49, 1, 18, 7, 58, 40, 34, 37, 44, 89, 88, 69, 80, 64,
                 0, 34, 11, 69, 40, 81, 42, 71, 42, 10, 98, 49, 17, 42, 96, 16, 64, 92, 39, 41, 43, 84, 32, 57, 50, 68,
                 59, 13, 43, 41, 5, 58, 84, 16, 42, 42, 37, 40, 64, 51, 34, 4, 61, 27, 21, 88, 71, 47, 23, 30, 46, 13,
                 64, 56, 27, 43, 39, 95, 99, 74, 65, 82, 28, 75, 15, 0, 75, 77, 73, 45, 93, 11, 15, 79, 33, 23, 8, 17,
                 76]]), ]
for test_tree_list, expected_output in test_cases:
    assert level_order(create_n_ary_tree(test_tree_list)) == expected_output
