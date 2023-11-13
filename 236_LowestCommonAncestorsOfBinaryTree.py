"""
Given a binary tree, find the lowest common ancestor (LCA) of two given nodes in the tree.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the
 lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”
"""
from typing import Optional

from _Binary_Tree import TreeNode, ConstructTree


def lowest_common_ancestor_recurse(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Depth search first to check for p and q: recurse and find the lowest common ancestor

    :return: lowest common ancestor of tree node p and q
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
            # Two of the three flags are true -> found the lowest common ancestor
            lca_node = current_node

        return current_node_matches or left_contains or right_contains

    lca_node = None
    recurse_tree(root)
    return lca_node


def lowest_common_ancestor_post_order(root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
    """
    Post order traversal with stack

    :return: lowest common ancestor of tree node p and q
    """
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


test_cases = [(list(range(1, 16)), 'llr', 'lrr', 'l'),
              ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 'l', 'r', ''),
              ([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 'l', 'lrr', 'l'),
              ([1, 2], '', 'l', ''), ]
for lowest_common_ancestor in [lowest_common_ancestor_recurse, lowest_common_ancestor_post_order]:
    for test_tree_list, test_p_steps, test_q_steps, test_both_steps in test_cases:
        test_tree = ConstructTree.build_tree_leetcode(test_tree_list)
        test_pointers = [None, None, None]
        for i, instruction in enumerate([test_p_steps, test_q_steps, test_both_steps]):
            pointer = test_tree.root
            for next_step in instruction:
                if next_step == 'l':
                    pointer = pointer.left
                elif next_step == 'r':
                    pointer = pointer.right
            test_pointers[i] = pointer
        test_p, test_q, test_both = test_pointers
        assert lowest_common_ancestor(test_tree.root, test_p, test_q) is test_both, lowest_common_ancestor.__name__
