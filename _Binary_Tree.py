from __future__ import annotations
from collections import deque
from typing import Any, List


def get_height(current_node):
    if current_node is None:
        return 0
    else:
        return 1 + max(get_height(current_node.left), get_height(current_node.right))

class TreeNode:
    def __init__(self, x: Any) -> None:
        self.val = x
        self.left = None
        self.right = None

    def height_of_subtree(self):
        return get_height(self)

class BinaryTree:
    def __init__(self, root: TreeNode):
        self.root = root

    def __eq__(self, other: BinaryTree) -> bool:
        if not other: return False
        if not isinstance(other, BinaryTree):
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
            if current_node_self.right:
                if current_node_other.right:
                    traverse_stack_self.append(current_node_self.right)
                    traverse_stack_other.append(current_node_other.right)
                else:
                    return False
        return True

    def __ne__(self, other: BinaryTree) -> bool:
        return not self.__eq__(other)

    def height(self) -> int:
        """
        :return: the maximum height of the node
        :rtype: int
        """
        return get_height(self.root)

    def print_tree(self, filler=None) -> List[List[Any]]:
        """
        Returns a 2D representation of the node
        :param filler: Default filler for empty cells
        :return: List[List[Node.val]]
        """
        def fill(print_array, current_node, layer, left, right):
            if not current_node:
                return
            midpoint = int((left + right) / 2)
            right_tree_left_bound = int((left + right + 1) / 2)
            if current_node.val is not None:
                print_array[layer][midpoint] = current_node.val
            fill(print_array, current_node.left, layer + 1, left, midpoint)
            fill(print_array, current_node.right, layer + 1, right_tree_left_bound, right)

        tree_height = self.height()
        tree_width = 2 ** tree_height - 1
        print_array = [[filler for _ in range(tree_width)] for _ in range(tree_height)]
        fill(print_array, self.root, 0, 0, tree_width)
        return print_array

    def preorder_traversal(self) -> List[Any]:
        """
        :rtype: list[val]
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

    def inorder_traversal(self) -> List[Any]:
        """
        :return: List[val]
        """
        traverse_stack = []
        result_order = []
        current_node = self.root
        while traverse_stack or current_node:
            while current_node:
                traverse_stack.append(current_node)
                current_node = current_node.left
            current_node = traverse_stack.pop()
            result_order.append(current_node.val)
            current_node = current_node.right
        return result_order

    def postorder_traversal(self) -> List[Any]:
        """
        :rtype: list[val]
        """
        if self.root is None:
            return []
        traverse_stack = [self.root]
        result_order = []
        prev_node = None
        while traverse_stack:
            current_node = traverse_stack[-1]
            if (not prev_node or prev_node.left == current_node or prev_node.right == current_node) and \
                    (current_node.left or current_node.right):  # traversing down and not at leaf node
                if current_node.left: # visit left kid first
                    traverse_stack.append(current_node.left)
                else:  # current node only has right kid
                    traverse_stack.append(current_node.right)
            elif current_node.left == prev_node and current_node.right:  # traversing up from left and has right kid
                traverse_stack.append(current_node.right)
            else:  # (1) leaf (2) no right kid and left kid visited (3) traversing up from right
                result_order.append(traverse_stack.pop().val)
            prev_node = current_node
        return result_order

    def layer_traversal(self) -> List[Any]:
        """
        :rtype: list[val]
        """
        if self.root is None:
            return []
        traverse_queue = deque()
        result_order = []
        traverse_queue.append(self.root)
        while traverse_queue:
            current_node = traverse_queue.popleft()
            result_order.append(current_node.val)
            if current_node.left:
                traverse_queue.append(current_node.left)
            if current_node.right:
                traverse_queue.append(current_node.right)
        return result_order

    def layer_traversal_by_layer(self) -> List[List[Any]]:
        """
        :rtype: list[list[val]]
        """
        if self.root is None:
            return []
        return_list, current_level = [], [self.root]
        while current_level:
            return_list.append([node.val for node in current_level])
            next_level_tmp = [(node.left, node.right) for node in current_level]
            current_level = [leaf for lr_pair in next_level_tmp for leaf in lr_pair if leaf]
        return return_list

    def leetcode_traversal(self) -> List[Any]:
        """
        :rtype: list[val]
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

    def right_side_view(self) -> List[Any]:
        def add_new_depth(node, depth):
            if node:
                if depth == len(left_view):
                    left_view.append(node.val)
                add_new_depth(node.right, depth + 1)
                add_new_depth(node.left, depth + 1)

        left_view = []
        add_new_depth(self.root, 0)
        return left_view

    def left_side_view(self) -> List[Any]:
        def add_new_depth(node, depth):
            if node:
                if depth == len(right_view):
                    right_view.append(node.val)
                add_new_depth(node.left, depth + 1)
                add_new_depth(node.right, depth + 1)

        right_view = []
        add_new_depth(self.root, 0)
        return right_view


class ConstructTree:
    """
    Assuming TreeNodes Contain Unique Values
    """
    @staticmethod
    def build_tree_pre_in(preorder, inorder):
        """
        :type preorder: list[val]
        :type inorder: list[val]
        :rtype: TreeNode
        """
        def build_tree_helper(preorder_s, preorder_e, inorder_s, inorder_e):
            current_x = preorder[preorder_s]
            current_root_node = TreeNode(current_x)
            inorder_x = inorder.index(current_x)
            left_tree_len = inorder_x - inorder_s
            if inorder_x > inorder_s:
                left_child = build_tree_helper(preorder_s + 1, preorder_s + left_tree_len, inorder_s, inorder_x - 1)
            else:
                left_child = None
            if inorder_x < inorder_e:
                right_child = build_tree_helper(preorder_s + left_tree_len + 1, preorder_e, inorder_x + 1, inorder_e)
            else:
                right_child = None
            current_root_node.left = left_child
            current_root_node.right = right_child
            return current_root_node

        assert len(preorder) == len(inorder)
        if len(preorder) == 0:
            return None
        root_node = build_tree_helper(0, len(preorder) - 1, 0, len(inorder) - 1)
        return BinaryTree(root=root_node)

    @staticmethod
    def build_tree_in_post(inorder, postorder):
        """
        :type inorder: list[val]
        :type postorder: list[val]
        :rtype: TreeNode
        """
        def build_tree_helper(inorder_s, inorder_e, postorder_s, postorder_e):
            current_x = postorder[postorder_e]
            current_root_node = TreeNode(current_x)
            inorder_x = inorder.index(current_x)
            left_tree_len = inorder_x - inorder_s
            if inorder_x > inorder_s:
                left_child = build_tree_helper(inorder_s, inorder_x-1, postorder_s, postorder_s+left_tree_len-1)
            else:
                left_child = None
            if inorder_x < inorder_e:
                right_child = build_tree_helper(inorder_x+1, inorder_e, postorder_s+left_tree_len, postorder_e-1)
            else:
                right_child = None
            current_root_node.left = left_child
            current_root_node.right = right_child
            return current_root_node

        assert len(inorder) == len(postorder)
        if len(inorder) == 0:
            return None
        root_node = build_tree_helper(0, len(inorder) - 1, 0, len(postorder) - 1)
        return BinaryTree(root=root_node)

    @staticmethod
    def build_tree_leetcode(node_list):
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
