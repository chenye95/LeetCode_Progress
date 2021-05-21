"""
A complete binary tree is a binary tree in which every level, except possibly the last, is completely filled, and all
 nodes are as far left as possible.

Write a data structure CBTInserter that is initialized with a complete binary tree and supports the following
 operations:
- CBTInserter(TreeNode root) initializes the data structure on a given tree with head node root;
- CBTInserter.insert(int v) will insert a TreeNode into the tree with value node.val = v so that the tree remains
    complete, and returns the value of the parent of the inserted TreeNode;
- CBTInserter.get_root() will return the head node of the tree.
"""
from _Binary_Tree import TreeNode, TREE_NODE_TYPE, ConstructTree, BinaryTree


class CBTInserter:
    def __init__(self, root: TreeNode):
        """
        Inherits the TreeNode objects and structure of the original tree

        :param root: root node of a non-empty binary tree, with 1 <= # of nodes <= 1000
        """
        self.node_not_full = []
        self.root = root
        add_node_deque = [root]
        while add_node_deque:
            parent_node = add_node_deque.pop(0)
            if not parent_node.left or not parent_node.right:
                self.node_not_full.append(parent_node)
            if parent_node.left:
                add_node_deque.append(parent_node.left)
            if parent_node.right:
                add_node_deque.append(parent_node.right)

    def insert(self, v: TREE_NODE_TYPE) -> TREE_NODE_TYPE:
        """
        :param v: insert a TreeNode into the tree with value node.val = v so that the tree remains complete
        :return: the value of the parent of the inserted TreeNode;
        """
        parent_node = self.node_not_full[0]
        self.node_not_full.append(TreeNode(v))
        if not parent_node.left:
            parent_node.left = self.node_not_full[-1]
        else:
            parent_node.right = self.node_not_full[-1]
            self.node_not_full.pop(0)
        return parent_node.val

    def get_root(self) -> TreeNode:
        """
        :return: root of the complete binary tree
        """
        return self.root


test_cases = [([1], (2, 1), [1, 2]),
              ([1, 2, 3, 4, 5, 6], (7, 3), (8, 4), [1, 2, 3, 4, 5, 6, 7, 8]),
              ([43, 7, 46, 23, 31, 5, 50, 27, 2, 8, 26, 13, 43, 18, 37, 8, 26, 18, 14, 42, 40, 23, 49, 42, 8, 10, 6, 26,
                9, 37, 9, 9, 28, 44, 3, 17, 10, 38, 2, 47],
               (15, 42), (2, 40), (6, 40), (9, 23), (49, 23), (23, 49), (7, 49), (4, 42), (4, 42), (14, 8), (28, 8),
               (2, 10), (35, 10), (28, 6), (48, 6), (47, 26), (23, 26), (1, 9), (15, 9), (20, 37), (14, 37), (37, 9),
               (4, 9), (5, 9), (7, 9), (41, 28), (26, 28), (11, 44), (29, 44), (38, 3), (29, 3), (9, 17), (33, 17),
               (13, 10), (44, 10), (23, 38), (16, 38), (48, 2), (0, 2), (34, 47),
               [43, 7, 46, 23, 31, 5, 50, 27, 2, 8, 26, 13, 43, 18, 37, 8, 26, 18, 14, 42, 40, 23, 49, 42, 8, 10, 6, 26,
                9, 37, 9, 9, 28, 44, 3, 17, 10, 38, 2, 47, 15, 2, 6, 9, 49, 23, 7, 4, 4, 14, 28, 2, 35, 28, 48, 47, 23,
                1, 15, 20, 14, 37, 4, 5, 7, 41, 26, 11, 29, 38, 29, 9, 33, 13, 44, 23, 16, 48, 0, 34]), ]
for test_input in test_cases:
    test_object = CBTInserter(ConstructTree.build_tree_leetcode(test_input[0]).root)
    for test_add_val, test_parent_val in test_input[1: -1]:
        assert test_object.insert(test_add_val) == test_parent_val
    get_tree = BinaryTree(test_object.get_root()).leetcode_traversal()
    assert get_tree[:len(test_input[-1])] == test_input[-1]
    assert get_tree[len(test_input[-1]):] == [None] * (len(get_tree) - len(test_input[-1]))
