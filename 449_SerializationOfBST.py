"""
Serialization is converting a data structure or object into a sequence of bits so that it can be stored in a file or
memory buffer, or transmitted across a network connection link to be reconstructed later in the same or another computer
 environment.

Design an algorithm to serialize and deserialize a binary search tree. There is no restriction on how your serialization
/deserialization algorithm should work. You need to ensure that a binary search tree can be serialized to a string, and
this string can be deserialized to the original tree structure.

The encoded string should be as compact as possible.
"""
from bisect import bisect
from typing import Optional, List

from _Binary_Tree import TreeNode, ConstructTree, BinaryTree, TREE_NODE_TYPE


class Codec:
    def __init__(self, node_val_type: TREE_NODE_TYPE = int):
        self.node_val_type = node_val_type
        self.split_chr = ','

    def serialize(self, root: TreeNode) -> str:
        """
        Encode a Binary Search Tree into string
        :param root: root node of a valid BST
        :return: pre-order traversal of BST
        """
        current_node = root
        traverse_stack = [None]
        pre_order_traversal = []
        while current_node:
            while current_node:
                pre_order_traversal.append(current_node.val)
                if current_node.right:
                    traverse_stack.append(current_node.right)
                current_node = current_node.left
            current_node = traverse_stack.pop()
        return self.split_chr.join([str(i) for i in pre_order_traversal])

    def deserialize(self, data: str) -> Optional[TreeNode]:
        if not data:
            return None
        data_prep = [self.node_val_type(x) for x in data.split(self.split_chr)]
        return self.deserialize_recurse(data_prep)

    def deserialize_recurse(self, data: List[TREE_NODE_TYPE]) -> Optional[TreeNode]:
        """
        Decode a string into a Binary Search Tree
        :param data: pre-order traversal of the BST
        :return: root node of a valid BST
        """
        if not data:
            return None
        elif len(data) == 1:
            return TreeNode(data[0])
        mid_split = bisect(data, data[0], lo=1)
        return TreeNode(data[0],
                        left=self.deserialize_recurse(data[1:mid_split]),
                        right=self.deserialize_recurse(data[mid_split:]))


test_tree = ConstructTree.build_tree_leetcode([2, 1, 3])
serializer, deserializer = Codec(), Codec()
assert test_tree == BinaryTree(deserializer.deserialize(serializer.serialize(test_tree.root)))
