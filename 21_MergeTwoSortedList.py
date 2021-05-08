"""
Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of
 the first two lists.
"""
from typing import Optional

from _Linked_List import ListNode, LinkedList


def merge_two_sorted_lists(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    """
    :param l1: sorted linked list with length 0 <= l1.length() <= 50
    :param l2: sorted linked list with length 0 <= l2.length() <= 50
    :return: Operation will destruct l1 and l2; return head of the combined linked list
    """
    dummy_head = ListNode(0)
    current_node = dummy_head

    while l1 and l2:
        if l1.val < l2.val:
            current_node.next = l1
            current_node = l1
            l1 = l1.next
        else:
            current_node.next = l2
            current_node = l2
            l2 = l2.next

    if l1:
        current_node.next = l1
    else:
        current_node.next = l2

    return dummy_head.next


test_cases = [([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4]),
              ([], [], []),
              ([], [0], [0]),
              ([-20, -19, -17, -17, -13, -5, -5, -4, -1, -1, 0, 1, 11, 16, 18, 19, 20, 21, 21, 22, 22, 23, 25, 28, 29],
               [-30, -27, -22, -21, -18, -17, -17, -13, -13, -5, -4, -1, 0, 6, 7, 8, 10, 15, 25, 27],
               [-30, -27, -22, -21, -20, -19, -18, -17, -17, -17, -17, -13, -13, -13, -5, -5, -5, -4, -4, -1, -1, -1, 0,
                0, 1, 6, 7, 8, 10, 11, 15, 16, 18, 19, 20, 21, 21, 22, 22, 23, 25, 25, 27, 28, 29]), ]
for test_l1_list, test_l2_list, expected_output in test_cases:
    if expected_output:
        assert merge_two_sorted_lists(LinkedList.create_linked_list(test_l1_list).head,
                                      LinkedList.create_linked_list(test_l2_list).head).list_from_node() \
               == expected_output
    else:
        assert merge_two_sorted_lists(LinkedList.create_linked_list(test_l1_list).head,
                                      LinkedList.create_linked_list(test_l2_list).head) is None
