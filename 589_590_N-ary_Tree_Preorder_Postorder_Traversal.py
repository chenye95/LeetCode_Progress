"""
Given the root of an n-ary tree, return the preorder traversal of its nodes' values.

Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the
 None value (See examples)
"""
from collections import deque
from typing import List, Optional


class Node:
    def __init__(self, val, children=None):
        """
        :param val: value of the tree node
        :param children: if not provided, children will be set to an empty list
        """
        self.val = val
        self.children: List[Node] = children if children else []


def construct_tree(construct_list: List) -> Optional[Node]:
    """
    Helper function to construct N-ary tree according to Leetcode rule

    :param construct_list: list of tree node values and None, representing level order traversal of the tree
    :return: root of the N-array tree
    """
    if not construct_list:
        return None

    root = Node(construct_list[0])

    current_node = None
    next_nodes = deque([root])
    for n_i in construct_list[1:]:
        if n_i is None:
            current_node = next_nodes.popleft()
        else:
            new_node = Node(n_i)
            current_node.children.append(new_node)
            next_nodes.append(new_node)

    return root


def pre_order(root: Node) -> List:
    """
    :param root: root of the N-ary tree
    :return: pre-order traversal of the tree
    """
    if not root:
        return []

    pre_order_traversal, traverse_queue = [], [root]
    while traverse_queue:
        current_node = traverse_queue.pop()
        pre_order_traversal.append(current_node.val)
        # add to queue in reversed order so the left children will be popped out first
        traverse_queue += reversed(current_node.children)

    return pre_order_traversal


def post_order(root: Node) -> List:
    """
    :param root: root of the N-ary tree
    :return: post-order traversal of the tree
    """
    if not root:
        return []

    post_order_traversal, traverse_queue = [], [root]
    while traverse_queue:
        current_node = traverse_queue.pop()
        post_order_traversal.append(current_node.val)
        # add children in normal order so the right children will be popped out first
        traverse_queue += current_node.children

    # return in reverse order to maintain left first, root last
    return post_order_traversal[::-1]


test_cases = [([1, None, 3, 2, 4, None, 5, 6], [1, 3, 5, 6, 2, 4], [5, 6, 3, 2, 4, 1]),
              ([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
                None, 14], [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10],
               [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]),
              ([], [], []),
              ([1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
                None, 14], [1, 2, 3, 6, 7, 11, 14, 4, 8, 12, 5, 9, 13, 10],
               [2, 6, 14, 11, 7, 3, 12, 8, 4, 13, 9, 10, 5, 1]),
              ([1], [1], [1]),
              ([1, None], [1], [1]), ]
for test_input, expected_pre, expected_post in test_cases:
    test_root = construct_tree(test_input)
    assert pre_order(test_root) == expected_pre
    assert post_order(test_root) == expected_post
