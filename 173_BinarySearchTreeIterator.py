"""
Implement the BSTIterator class that represents an iterator over the in-order traversal of a binary search tree (BST):
- BSTIterator(TreeNode root) Initializes an object of the BSTIterator class. The root of the BST is given as part of the
 constructor. The pointer should be initialized to a non-existent number smaller than any element in the BST.
- boolean hasNext() Returns true if there exists a number in the traversal to the right of the pointer, otherwise
 returns false.
- int next() Moves the pointer to the right, then returns the number at the pointer.
- Notice that by initializing the pointer to a non-existent smallest number, the first call to next() will return the
 smallest element in the BST.

You may assume that next() calls will always be valid. That is, there will be at least a next number in the in-order
 traversal when next() is called.
"""
from typing import Optional

from _Binary_Tree import TreeNode, TREE_NODE_TYPE, ConstructTree


class BinaryTreeIterator:
    def __init__(self, root: TreeNode):
        """
        :param root: root a Binary Search Tree
        """
        self.root = root
        self.current_node = root

    def next(self) -> Optional[TREE_NODE_TYPE]:
        """
        :return: moves the pointer to the right, then returns the value at the pointer
        """
        pass

    def has_next(self) -> bool:
        """
        :return: if there exists a number in the traversal to the right of the pointer
        """
        pass


class BSTIteratorStack(BinaryTreeIterator):
    def __init__(self, root: TreeNode):
        """
        This iterator will not destruct the original tree structure

        :param root: root a Binary Search Tree
        """
        super().__init__(root)
        self.traversal_stack = []

    def has_next(self) -> bool:
        return len(self.traversal_stack) > 0 or self.current_node is not None

    def next(self) -> Optional[TREE_NODE_TYPE]:
        """
        This call will not destruct the tree structure

        :return: moves the pointer to the right, then returns the value at the pointer
        """
        if not self.current_node and not self.traversal_stack:
            return None

        while self.current_node:
            self.traversal_stack.append(self.current_node)
            self.current_node = self.current_node.left
        self.current_node = self.traversal_stack.pop()
        return_val = self.current_node.val
        self.current_node = self.current_node.right
        return return_val


class BSTIteratorMorrisTraversal(BinaryTreeIterator):
    def __init__(self, root: TreeNode):
        """
        Runs Morris Traversal algorithm. It will temporarily destruct the tree structure

        :param root: root node of a binary search tree
        """
        super().__init__(root)

    def has_next(self) -> bool:
        return self.current_node is not None

    def next(self) -> Optional[TREE_NODE_TYPE]:
        """
        This call will not destruct the tree structure

        :return: moves the pointer to the right, then returns the value at the pointer
        """
        while self.current_node:
            if self.current_node.left is None:
                return_val = self.current_node.val
                self.current_node = self.current_node.right
                return return_val
            else:
                # Find the inorder predecessor of current
                predecessor = self.current_node.left
                while predecessor.right is not None and predecessor.right != self.current_node:
                    predecessor = predecessor.right

                # Make current_node the right child of its inorder predecessor
                if predecessor.right is None:
                    predecessor.right = self.current_node
                    self.current_node = self.current_node.left
                # Revert the changes made in if part to restore the original tree
                # i.e., fix the right child of predecessor
                else:
                    predecessor.right = None
                    return_val = self.current_node.val
                    self.current_node = self.current_node.right
                    return return_val
        return None


for bst_iterator_type in [BSTIteratorMorrisTraversal, BSTIteratorStack, ]:
    test_bst_iterator = bst_iterator_type(ConstructTree.build_tree_leetcode([7, 3, 15, None, None, 9, 20]).root)
    assert test_bst_iterator.has_next()
    assert 3 == test_bst_iterator.next()
    assert 7 == test_bst_iterator.next()
    assert test_bst_iterator.has_next()
    assert 9 == test_bst_iterator.next()
    assert test_bst_iterator.has_next()
    assert 15 == test_bst_iterator.next()
    assert test_bst_iterator.has_next()
    assert 20 == test_bst_iterator.next()
    assert not test_bst_iterator.has_next()
    assert test_bst_iterator.next() is None
    assert test_bst_iterator.next() is None
