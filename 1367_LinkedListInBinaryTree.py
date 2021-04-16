"""
Given a binary tree root and a linked list with head as the first node.

Return True if all the elements in the linked list starting from the head correspond to some downward path connected in
the binary tree otherwise return False.

In this context downward path means a path that starts at some node and goes downwards.
"""
from _Binary_Tree import TreeNode, ConstructTree
from _Linked_List import ListNode, LinkedList


def is_sub_path(head: ListNode, root: TreeNode) -> bool:
    """
    :param head: head of a linked list
    :param root: probe_root of a Binary Tree
    :return: whether elements from head corresponding to some downward path in binary tree
    """

    def downward_probe(probe_head: ListNode, probe_root: TreeNode) -> bool:
        """
        :return: whether elements in sub list probe_head corresponding to some downward path in sub tree probe_head
        """
        if not probe_head:
            # end of linked list
            return True
        if not probe_root:
            # end of binary tree
            return False
        # Current level match up and next node match up with either child node
        return probe_head.val == probe_root.val and \
               (downward_probe(probe_head.next, probe_root.left) or downward_probe(probe_head.next, probe_root.right))

    if not root:
        # Empty tree
        return False
    # Start downward path from probe_root
    # or wait until child node to start downward path
    return downward_probe(head, root) or is_sub_path(head, root.left) or is_sub_path(head, root.right)


test_cases = [([4, 2, 8], [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3], True),
              ([1, 4, 2, 6], [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3], True),
              ([1, 4, 2, 6, 8], [1, 4, 4, None, 2, 2, None, 1, None, 6, 8, None, None, None, None, 1, 3], False)]
for build_list, build_tree, expected_output in test_cases:
    assert is_sub_path(LinkedList.create_linked_list(build_list).head,
                       ConstructTree.build_tree_leetcode(build_tree).root) is expected_output
