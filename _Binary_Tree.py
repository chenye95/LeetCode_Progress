from __future__ import annotations

from collections import deque
from typing import Union, List, Optional

TREE_NODE_TYPE = Union[str, int, chr, float]


def get_height(current_node: TreeNode) -> int:
    """
    :param current_node: evaluating the subtree beneath current_node
    :return: height of the subtree, i.e. max level of any descendant of current_node
    """
    if current_node is None:
        return 0
    else:
        return 1 + max(get_height(current_node.left), get_height(current_node.right))


class TreeNode:
    def __init__(self, x: TREE_NODE_TYPE, left: TreeNode = None, right: TreeNode = None):
        self.val = x
        self.left = left
        self.right = right

    def height_of_subtree(self):
        return get_height(self)


class BinaryTree:
    def __init__(self, root: Optional[TreeNode] = None):
        self.root = root

    def __eq__(self, other: BinaryTree) -> bool:
        """
        :return: whether a BinaryTree is identical to another. Structure and value wise
        """
        if not other:
            return False
        if not isinstance(other, BinaryTree):
            return False
        if self.root is None and other.root is None:
            return True
        elif self.root is None or other.root is None:
            return False
        traverse_stack_self = [self.root]
        traverse_stack_other = [other.root]
        while traverse_stack_self:
            current_node_self = traverse_stack_self.pop()
            current_node_other = traverse_stack_other.pop()
            if current_node_self.val != current_node_other.val:
                return False
            if current_node_self.left:
                if current_node_other.left:
                    traverse_stack_self.append(current_node_self.left)
                    traverse_stack_other.append(current_node_other.left)
                else:
                    return False
            elif current_node_other.left:
                # current_node_self.left is None, so current_node_other.left has to be None
                return False
            if current_node_self.right:
                if current_node_other.right:
                    traverse_stack_self.append(current_node_self.right)
                    traverse_stack_other.append(current_node_other.right)
                else:
                    return False
            elif current_node_other.right:
                # current_node_self.right is None, so current_node_other.right has to be None
                return False
        return True

    def __ne__(self, other: BinaryTree) -> bool:
        """
        :return: same as not .__eq__(other)
        """
        return not self.__eq__(other)

    def height(self) -> int:
        """
        :return: the maximum height of the node
        :rtype: int
        """
        return get_height(self.root)

    def print_tree(self, filler: TREE_NODE_TYPE = None) -> List[List[TREE_NODE_TYPE]]:
        """
        :param filler: Default filler for empty cells
        :return: 2D representation of the binary tree
        """

        def fill(current_node: TreeNode, layer: int, left: int, right: int) -> None:
            if not current_node:
                return
            midpoint = (left + right) // 2
            right_tree_left_bound = (left + right + 1) // 2
            if current_node.val is not None:
                print_array[layer][midpoint] = current_node.val
            fill(current_node.left, layer + 1, left, midpoint)
            fill(current_node.right, layer + 1, right_tree_left_bound, right)

        tree_height = self.height()
        tree_width = 2 ** tree_height - 1
        print_array = [[filler for _ in range(tree_width)] for _ in range(tree_height)]
        fill(self.root, 0, 0, tree_width)
        return print_array

    def preorder_traversal(self) -> List[TREE_NODE_TYPE]:
        """
        :return: pre-order traversal of the Binary Tree
        """
        current_node = self.root
        traverse_stack = [None]
        result_order = []
        while current_node:
            while current_node:
                result_order.append(current_node.val)
                if current_node.right:
                    traverse_stack.append(current_node.right)
                current_node = current_node.left
            current_node = traverse_stack.pop()
        return result_order

    def inorder_traversal(self) -> List[TREE_NODE_TYPE]:
        """
        Implements Morris Traversal: without recursion or stack. Modifies the tree and reverts the changes afterwards

        :return: in order traversal of the Binary Tree
        """
        result_order = []
        current_node = self.root
        while current_node is not None:
            if current_node.left is None:
                result_order.append(current_node.val)
                current_node = current_node.right
            else:
                # Find the inorder predecessor of current
                predecessor = current_node.left
                while predecessor.right is not None and predecessor.right != current_node:
                    predecessor = predecessor.right

                # Make current_node the right child of its inorder predecessor
                if predecessor.right is None:
                    predecessor.right = current_node
                    current_node = current_node.left
                # Revert the changes made in if part to restore the original tree
                # i.e., fix the right child of predecessor
                else:
                    predecessor.right = None
                    result_order.append(current_node.val)
                    current_node = current_node.right

        return result_order

    def postorder_traversal(self) -> List[TREE_NODE_TYPE]:
        """
        :return: post order traversal of the Binary Tree
        """
        if self.root is None:
            return []
        traverse_stack: List[TreeNode] = [self.root]
        result_order = []
        prev_node = None
        while traverse_stack:
            current_node = traverse_stack[-1]
            if (not prev_node or prev_node.left is current_node or prev_node.right is current_node) and \
                    (current_node.left or current_node.right):  # traversing down and not at leaf node
                if current_node.left:  # visit left kid first
                    traverse_stack.append(current_node.left)
                else:  # current node only has right kid
                    traverse_stack.append(current_node.right)
            elif current_node.left is prev_node and current_node.right:  # traversing up from left and has right kid
                traverse_stack.append(current_node.right)
            else:  # (1) leaf (2) no right kid and left kid visited (3) traversing up from right
                result_order.append(traverse_stack.pop().val)
            prev_node = current_node
        return result_order

    def layer_traversal(self) -> List[TREE_NODE_TYPE]:
        """
        :return: all nodes layer by layer in a single list, remove all None/empty child nodes
        """
        if self.root is None:
            return []
        traverse_queue = deque([self.root])
        result_order = []
        while traverse_queue:
            current_node = traverse_queue.popleft()
            result_order.append(current_node.val)
            if current_node.left:
                traverse_queue.append(current_node.left)
            if current_node.right:
                traverse_queue.append(current_node.right)
        return result_order

    def layer_traversal_by_layer(self) -> List[List[TREE_NODE_TYPE]]:
        """
        :return: all nodes layer by layer in list of lists, remove all None/empty child nodes
        """
        if self.root is None:
            return []
        return_list, traversal_queue = [], deque([self.root])
        while traversal_queue:
            current_level = []
            for _ in range(len(traversal_queue)):
                current_node = traversal_queue.popleft()
                current_level.append(current_node.val)
                if current_node.left:
                    traversal_queue.append(current_node.left)
                if current_node.right:
                    traversal_queue.append(current_node.right)
            return_list.append(current_level)

        return return_list

    def leetcode_traversal(self) -> List[TREE_NODE_TYPE]:
        """
        Helper function for Leetcode problems

        :return: Leetcode traversal
        """
        if self.root is None:
            return []
        traverse_queue = deque()
        result_order = []
        traverse_queue.append(self.root)
        while traverse_queue:
            current_node = traverse_queue.popleft()
            if not current_node:
                result_order.append(None)
            else:
                result_order.append(current_node.val)
                traverse_queue.append(current_node.left)
                traverse_queue.append(current_node.right)
        return result_order

    def right_side_view(self) -> List[TREE_NODE_TYPE]:
        """
        :return: list of the right most nodes per layer
        """

        def right_view_add_new_depth(node: TreeNode, depth: int) -> None:
            if node:
                if depth == len(right_view):
                    right_view.append(node.val)
                right_view_add_new_depth(node.right, depth + 1)
                right_view_add_new_depth(node.left, depth + 1)

        right_view = []
        right_view_add_new_depth(self.root, 0)
        return right_view

    def left_side_view(self) -> List[TREE_NODE_TYPE]:
        """
        :return: list of the left most nodes per layer
        """

        def left_view_add_new_layer(node: TreeNode, depth: int) -> None:
            if node:
                if depth == len(left_view):
                    left_view.append(node.val)
                left_view_add_new_layer(node.left, depth + 1)
                left_view_add_new_layer(node.right, depth + 1)

        left_view = []
        left_view_add_new_layer(self.root, 0)
        return left_view

    def max_width(self) -> int:
        """
        :return: maximum width in the tree
        """
        if self.root is None:
            return 0

        current_level = deque([(self.root, 0)])  # (node, node_id)
        max_width = 0

        while current_level:
            current_level_node_count = len(current_level)
            start_id = current_id = current_level[0][1]
            for _ in range(current_level_node_count):
                current_node, current_id = current_level.popleft()
                if current_node.left:
                    current_level.append((current_node.left, 2 * current_id))
                if current_node.right:
                    current_level.append((current_node.right, 2 * current_id + 1))

            end_id = current_id
            max_width = max(max_width, end_id - start_id + 1)

        return max_width


class ConstructTree:

    @staticmethod
    def build_tree_pre_in(preorder: List[TREE_NODE_TYPE], inorder: List[TREE_NODE_TYPE]) -> Optional[BinaryTree]:
        """
        Assuming TreeNodes Contain Unique Values

        :parameter preorder: preorder representation of the tree
        :parameter inorder: inorder representation of the tree
        :return: BinaryTree object of the tree; or None if the lists are empty
        """
        def build_tree_helper(preorder_s: int, preorder_e: int, inorder_s: int, inorder_e: int) -> TreeNode:
            current_x = preorder[preorder_s]
            inorder_x = inorder.index(current_x)
            left_tree_len = inorder_x - inorder_s
            return TreeNode(current_x,
                            left=build_tree_helper(preorder_s + 1, preorder_s + left_tree_len,
                                                   inorder_s, inorder_x - 1)
                            if inorder_x > inorder_s else None,
                            right=build_tree_helper(preorder_s + left_tree_len + 1,
                                                    preorder_e, inorder_x + 1, inorder_e)
                            if inorder_x < inorder_e else None)

        if not preorder or not inorder:
            return None
        assert len(preorder) == len(inorder)
        return BinaryTree(root=build_tree_helper(0, len(preorder) - 1, 0, len(inorder) - 1))

    @staticmethod
    def build_tree_in_post(inorder: List[TREE_NODE_TYPE], postorder: List[TREE_NODE_TYPE]) -> Optional[BinaryTree]:
        """
        Assuming TreeNodes Contain Unique Values

        :parameter inorder: inorder representation of the tree
        :parameter postorder: postorder representation of the tree
        :return: BinaryTree object of the tree; or None if the lists are empty
        """
        def build_tree_helper(inorder_s: int, inorder_e: int, postorder_s: int, postorder_e: int) -> TreeNode:
            current_x = postorder[postorder_e]
            inorder_x = inorder.index(current_x)
            left_tree_len = inorder_x - inorder_s
            return TreeNode(current_x,
                            left=build_tree_helper(inorder_s, inorder_x - 1,
                                                   postorder_s, postorder_s + left_tree_len - 1)
                            if inorder_x > inorder_s else None,
                            right=build_tree_helper(inorder_x + 1, inorder_e,
                                                    postorder_s + left_tree_len, postorder_e - 1)
                            if inorder_x < inorder_e else None)

        if not inorder or not postorder:
            return None
        assert len(inorder) == len(postorder)
        return BinaryTree(root=build_tree_helper(0, len(inorder) - 1, 0, len(postorder) - 1))

    @staticmethod
    def build_tree_leetcode(node_list: List[TREE_NODE_TYPE]) -> Optional[BinaryTree]:
        """
        Helper function to create Binary Tree according to Leetcode representation

        :param node_list: leetcode traversal order
        :return: BinaryTree object of the tree; or None if the lists are empty
        """
        if not node_list:
            return None
        root = TreeNode(node_list[0])
        current_node = root
        current_node_counter = 0
        waiting_nodes = deque()
        for i in range(1, len(node_list)):
            if node_list[i] is not None:
                new_node = TreeNode(node_list[i])
                waiting_nodes.append(new_node)
            else:
                new_node = None
            if current_node_counter == 2:
                current_node = waiting_nodes.popleft()
                current_node_counter = 0
            if current_node_counter == 0:
                current_node.left = new_node
                current_node_counter += 1
            elif current_node_counter == 1:
                current_node.right = new_node
                current_node_counter += 1
        return BinaryTree(root=root)


class CompareTree:
    """
    Compare both tree structure and tree node values
    """

    @staticmethod
    def compare_leetcode_traversal(tree_traversal: List[TREE_NODE_TYPE],
                                   expected_traversal: List[TREE_NODE_TYPE]) -> bool:
        return len(tree_traversal) >= len(expected_traversal) and \
               tree_traversal[:len(expected_traversal)] == expected_traversal and \
               tree_traversal[len(expected_traversal):] == [None] * (len(tree_traversal) - len(expected_traversal))

    @staticmethod
    def compare_binary_tree(this_tree: Optional[BinaryTree], that_tree: Optional[BinaryTree]) -> bool:
        if this_tree is None or that_tree is None:
            return this_tree is that_tree
        return this_tree == that_tree

    @staticmethod
    def compare_tree_node(this_tree_node: Optional[TreeNode], that_tree_node: Optional[TreeNode]) -> bool:
        if this_tree_node is None or that_tree_node is None:
            return this_tree_node is that_tree_node
        return BinaryTree(this_tree_node) == BinaryTree(that_tree_node)
