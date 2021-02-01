"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the
 lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
from typing import Optional

from _Binary_Tree import TreeNode, ConstructTree


def lowest_common_ancestor_1(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Depth search first to check for p and q
    Recurse and find the lowest common ancestor
    """

    def recurse_tree(current_node: TreeNode) -> bool:
        """
        :return: True if either p or q resides in the subtree from current_node
        """
        nonlocal lca_node

        if not current_node:
            return False

        left_contains = recurse_tree(current_node.left)
        right_contains = recurse_tree(current_node.right)

        current_node_matches = (current_node == p) or (current_node == q)

        if left_contains + right_contains + current_node_matches >= 2:
            # Two of the three flags are true -> found lowest common ancestor
            lca_node = current_node

        return current_node_matches or left_contains or right_contains

    lca_node = None
    recurse_tree(root)
    return lca_node


def lowest_common_ancestor_2(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    # state to mark node exploration
    # defined as number of child node left to be explored
    _node_state_both_pending = 2
    _node_state_left_done = 1
    _node_state_both_done = 0

    # Used for post order traversal of the tree
    recursive_stack = [(root, _node_state_both_pending)]

    # Mark either p or q has been found
    one_node_found = False

    # LCA index within the recursive_stack
    lca_index = -1

    # Post Order Traversal of the Tree
    # Left, Right, Current_Node
    while recursive_stack:

        # Peek top of the stack to get current node
        current_node, current_state = recursive_stack[-1]

        # If current_state equals to _node_state_both_done, and both children have been explored
        # current_node can be popped out
        if current_state == _node_state_both_done:
            # If lca_index is equal to length of stack. Then we decrease lca_index by 1
            # With post order traversal, all subtree of current_node has been explored before current_node
            # Backtrace from current_node to its parent node recursive_stack[lca_index - 1]
            if one_node_found and lca_index == len(recursive_stack) - 1:
                lca_index -= 1
            recursive_stack.pop()
        else:
            # Have yet to explore either left or right child, or both

            # If both child traversals are pending
            if current_state == _node_state_both_pending:

                # Check if the current current_node is either p or q
                if current_node == p or current_node == q:

                    # If one_node_found is set already, this means we have found both the nodes
                    if one_node_found:
                        return recursive_stack[lca_index][0]
                    else:
                        # Otherwise, set one_node_found to True, to mark one of p and q is found
                        one_node_found = True

                        # Save the current top index of stack as the lca_index
                        # start back tracing from current_node
                        lca_index = len(recursive_stack) - 1

                # If both pending, traverse the left child first
                child_node = current_node.left
            else:
                # traverse right child
                child_node = current_node.right

            # Update the node state at the top of the stack, since we have visited one more child
            recursive_stack.pop()
            recursive_stack.append((current_node, current_state - 1))

            # Add the child node to the stack for traversal
            if child_node:
                recursive_stack.append((child_node, _node_state_both_pending))

    return None


test_tree = ConstructTree.build_tree_leetcode(list(range(1, 16)))
node_p = test_tree.root.left.left.right
node_q = test_tree.root.left.right.right
assert lowest_common_ancestor_1(test_tree.root, node_p, node_q).val == 2
assert lowest_common_ancestor_2(test_tree.root, node_p, node_q).val == 2

test_tree = ConstructTree.build_tree_leetcode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
node_p = test_tree.root.left
node_q = test_tree.root.right
assert lowest_common_ancestor_1(test_tree.root, node_p, node_q).val == 3
assert lowest_common_ancestor_2(test_tree.root, node_p, node_q).val == 3

node_q = test_tree.root.left.right.right
assert lowest_common_ancestor_1(test_tree.root, node_p, node_q).val == 5
assert lowest_common_ancestor_2(test_tree.root, node_p, node_q).val == 5

test_tree = ConstructTree.build_tree_leetcode([1, 2])
node_p = test_tree.root
node_q = test_tree.root.left
assert lowest_common_ancestor_1(test_tree.root, node_p, node_q).val == 1
assert lowest_common_ancestor_2(test_tree.root, node_p, node_q).val == 1
