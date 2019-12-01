from _Binary_Tree import BinaryTree, TreeNode
from _Linked_List import LinkedList


def construct_bst_from_list(values):
    """
    :param values:  Sorted list of values
    :return: TreeNode: root of BST
    """
    def construct_bst_helper(left_bound, right_bound):
        if left_bound > right_bound:
            return None
        mid_point = int((left_bound + right_bound) / 2)
        root_node = TreeNode(values[mid_point])
        root_node.left = construct_bst_helper(left_bound, mid_point - 1)
        root_node.right = construct_bst_helper(mid_point + 1, right_bound)
        return root_node
    if len(values) == 0:
        return None
    else:
        return construct_bst_helper(0, len(values) - 1)

def construct_bst_from_linked_list(linked_list):
    """
    Please note that this method will destruct the linked list, please make a deep copy if you want to preserve the list
    :param linked_list: Sorted linked list
    :return: TreeNode: root of BST
    """
    def construct_bst_helper(list_start):
        if list_start is None:
            return None
        slow_ptr = list_start
        slow_before = None
        fast_ptr = list_start
        while fast_ptr.next and fast_ptr.next.next:
            slow_before = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        root_node = TreeNode(slow_ptr.val)
        if slow_before:
            slow_before.next = None
            root_node.left = construct_bst_helper(list_start)
        if slow_ptr.next:
            root_node.right = construct_bst_helper(slow_ptr.next)
        return root_node
    return construct_bst_helper(linked_list.head)

class BST(BinaryTree):
    def __init__(self, values):
        assert (isinstance(values, list) or isinstance(values, LinkedList)), \
            "Only support initiate from list or linked list"
        assert values, "Empty list not supported"

        if isinstance(values, list):
            values.sort()
            self.root = construct_bst_from_list(values)
        else:
            self.root = construct_bst_from_linked_list(values)

    def traversal(self):
        assert self.root is not None, "Empty Tree"
        return self.inorder_traversal()

    def traverse_range(self, left_bound, right_bound):
        def traverse_range_boundary(root_node):
            return_list = []
            if root_node.val > left_bound and root_node.left:
                return_list.extend(traverse_range_boundary(root_node.left))
            if left_bound <= root_node.val <= right_bound:
                return_list.append(root_node.val)
            if root_node.val <= right_bound and root_node.right:
                return_list.extend(traverse_range_boundary(root_node.right))
            return return_list
        assert self.root is not None, "Empty Tree"
        return traverse_range_boundary(self.root)

    def balance_factor(self):
        assert self.root, "Empty Tree"
        left_height = 0 if self.root.left is None else self.root.left.height_of_subtree()
        right_height = 0 if self.root.right is None else self.root.right.height_of_subtree()
        return left_height - right_height


    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            current_node = self.root
            inserted = False
            while not inserted:
                if value < current_node.val:
                    if not current_node.left:
                        current_node.left = TreeNode(value)
                        inserted = True
                    else:
                        current_node = current_node.left
                else:
                    if not current_node.right:
                        current_node.right = TreeNode(value)
                        inserted = True
                    else:
                        current_node = current_node.right

    def look_up(self, value):
        if self.root is None:
            return False

        current_node = self.root
        while current_node:
            if current_node.val == value:
                return True
            elif value < current_node.val:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False


    def hard_re_balance(self):
        assert self.root, "Empty Tree"
        values = self.inorder_traversal()
        self.root = construct_bst_from_list(values)

    def delete_node(self, value):
        assert self.root, "Empty Tree"
        to_be_deleted = self.root
        parent_node = None
        is_left_child = True
        while to_be_deleted and to_be_deleted.val != value:
            parent_node = to_be_deleted
            if value < to_be_deleted.val:
                to_be_deleted = to_be_deleted.left
                is_left_child = True
            elif value > to_be_deleted.val:
                to_be_deleted = to_be_deleted.right
                is_left_child = False

        # Not Found
        if to_be_deleted is None:
            return False

        # To_be_deleted is a leaf node
        if to_be_deleted.left is None and to_be_deleted.right is None:
            if parent_node and is_left_child:
                parent_node.left = None
            elif parent_node and not is_left_child:
                parent_node.right = None
            else:
                self.root = None
            return True

        # To_be_deleted has only one child: Left Child or Right Child
        if to_be_deleted.left is None or to_be_deleted.right is None:
            replacement_node = to_be_deleted.right if to_be_deleted.right else to_be_deleted.left
            if parent_node and is_left_child:
                parent_node.left = replacement_node
            elif parent_node and not is_left_child:
                parent_node.right = replacement_node
            else:
                self.root = replacement_node
            return True

        # To_be_deleted has both left child and right child - Replace with Min Right
        replacement_node = to_be_deleted.right
        replacement_parent = None
        while replacement_node.left:
            replacement_parent = replacement_node
            replacement_node = replacement_node.left

        if replacement_parent:  # replacement node is not the right child of to_be_deleted
            replacement_parent.left = replacement_node.right
            replacement_node.right = to_be_deleted.right  # need to pick up the right subtree of to_be_deleted
        replacement_node.left = to_be_deleted.left
        if parent_node and is_left_child:  # to be deleted node is not the root node
            parent_node.left = replacement_node
        elif parent_node and not is_left_child:
            parent_node.right = replacement_node
        else:
            self.root = replacement_node

        return True

    def is_valid(self) -> bool:
        """
        For all nodes:
            node.left.val < node.val
            node.right.val >= node.val
        :return: bool
        """
        assert self.root, "Empty Tree"
        to_be_validated = [(self.root, None, None)]
        while to_be_validated:
            validating, lower_limit, upper_limit = to_be_validated.pop()
            if validating.left:
                if validating.left.val >= validating.val or \
                        (lower_limit is not None and lower_limit > validating.left.val):
                    return False
                to_be_validated.append((validating.left, lower_limit, validating.val))
            if validating.right:
                if validating.right.val < validating.val or \
                        (upper_limit is not None and upper_limit <= validating.right.val):
                    return False
                to_be_validated.append((validating.right, validating.val, upper_limit))
        return True

    def is_balanced(self):
        UNBALANCED = -1

        def check_below_node(current_node):
            # UNBALANCED means unbalanced, else return height
            if current_node is None:
                return 0
            left_height = check_below_node(current_node.left)
            right_height = check_below_node(current_node.right)
            if left_height == UNBALANCED or right_height == UNBALANCED or abs(left_height - right_height) > 1:
                return UNBALANCED
            else:
                return 1 + max(left_height, right_height)

        assert self.root, "Empty Tree"
        return check_below_node(self.root) != UNBALANCED

    def kthSmallest(self, k: int):
        traversal_stack = []
        counter = 0
        current_node = self.root
        while traversal_stack or current_node:
            while current_node:
                traversal_stack.append(current_node)
                current_node = current_node.left
            current_node = traversal_stack.pop()
            counter += 1
            if counter == k:
                return current_node.val
            current_node = current_node.right
        return None


