"""
Given the root of a binary tree, return all duplicate subtrees.

For each kind of duplicate subtrees, you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with the same node values.
"""
from collections import defaultdict
from typing import List, Tuple, DefaultDict

from _Binary_Tree import TreeNode, ConstructTree, TREE_NODE_TYPE


def find_duplicate_sub_tree_tuple(root: TreeNode) -> List[TreeNode]:
    """
    :param root: root a non empty binary tree with 1 <= no of nodes <= 10000
    :return: list of TreeNodes, whose subtree has a duplicate in other parts of the bigger binary tree. One node for
        each type of sub tree structure
    """

    def sub_tree_signature(current_node: TreeNode) -> Tuple[TREE_NODE_TYPE, Tuple, Tuple]:
        """
        :param current_node: inspecting the sub tree beneath current_tree_node, assuming current_tree_node is not None
        :return: signature of the sub tree (current_tree_node.val, signature of left sub tree,
            signature of right subtree)
        """
        left_sub_tree_signature = sub_tree_signature(current_node.left) if current_node.left else ()
        right_sub_tree_signature = sub_tree_signature(current_node.right) if current_node.right else ()
        current_tree_signature = (current_node.val, left_sub_tree_signature, right_sub_tree_signature)
        if current_tree_signature not in seen_map:
            seen_map[current_tree_signature] = current_node
        elif seen_map[current_tree_signature] is not None:
            # only return once for each node
            repeated_nodes.append(seen_map[current_tree_signature])
            seen_map[current_tree_signature] = None

        return current_tree_signature

    seen_map = {}
    repeated_nodes: List[TreeNode] = []
    if root.left:
        sub_tree_signature(root.left)
    if root.right:
        sub_tree_signature(root.right)
    return repeated_nodes


def find_duplicate_sub_tree_uuid(root: TreeNode) -> List[TreeNode]:
    """
    :param root: root a non empty binary tree with 1 <= no of nodes <= 10000
    :return: list of TreeNodes, whose subtree has a duplicate in other parts of the bigger binary tree. One node for
        each type of sub tree structure
    """
    # for each unique sub tree signature, get an id
    # sub tree signature defined as (current_node.val, left_tree_signature_id, right_tree_signature_id)
    sub_tree_signature_id: DefaultDict[Tuple[TREE_NODE_TYPE, int, int], int] = defaultdict(int)
    sub_tree_signature_id.default_factory = sub_tree_signature_id.__len__
    seen_map = {}

    def sub_tree_signature(current_node: TreeNode) -> int:
        """
        :param current_node: inspecting the sub tree beneath current_tree_node, assuming current_tree_node is not None
        :return: unique id assigned to the signature of the sub tree
        """
        left_signature = sub_tree_signature(current_node.left) if current_node.left else -1
        right_signature = sub_tree_signature(current_node.right) if current_node.right else -1
        unique_id = sub_tree_signature_id[(current_node.val, left_signature, right_signature)]
        if unique_id not in seen_map:
            seen_map[unique_id] = current_node
        elif seen_map[unique_id] is not None:
            return_list.append(current_node)
            seen_map[unique_id] = None

        return unique_id

    return_list = []
    if root.left:
        sub_tree_signature(root.left)
    if root.right:
        sub_tree_signature(root.right)
    return return_list


test_cases = [([1, 2, 3, 4, None, 2, 4, None, None, 4], [('l', 'rl'), ('ll', 'rll', 'rr'), ]),
              ([2, 1, 1], [('l', 'r'), ]),
              ([2, 2, 2, 3, None, 3, None], [('l', 'r'), ('ll', 'rl'), ]), ]
for test_tree_list, expected_tree_node_list in test_cases:
    test_tree = ConstructTree.build_tree_leetcode(test_tree_list)
    expected_nodes = []
    for subtree_group_list in expected_tree_node_list:
        expected_type_accepted_nodes = set()
        for node_instruction in subtree_group_list:
            current_tree_node = test_tree.root
            for next_step in node_instruction:
                if next_step == 'l':
                    current_tree_node = current_tree_node.left
                else:
                    current_tree_node = current_tree_node.right
            expected_type_accepted_nodes.add(current_tree_node)
        expected_nodes.append(expected_type_accepted_nodes)
    for find_duplicate_sub_tree in [find_duplicate_sub_tree_tuple, find_duplicate_sub_tree_uuid]:
        get_nodes = find_duplicate_sub_tree(test_tree.root)
        assert len(get_nodes) == len(expected_nodes), find_duplicate_sub_tree.__name__
        assert all(any(find_node in expected_type_accepted_nodes for expected_type_accepted_nodes in expected_nodes)
                   for find_node in get_nodes), find_duplicate_sub_tree.__name__
