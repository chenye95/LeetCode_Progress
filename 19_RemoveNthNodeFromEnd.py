"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
from typing import Optional

from _Linked_List import ListNode, LinkedList


def remove_nth_node(head: ListNode, n: int) -> Optional[ListNode]:
    """
    :param head: head of a linked list
    :param n: remove the nth node from the end of the list, 1 <= n <= length of the list
    :return: return head of the new list
    """
    dummy_node = probe_node = proceeding_node = ListNode(0, next=head)
    for _ in range(n):
        # 1 <= n <= length of list guaranteed; does not need to check for boundary condition
        probe_node = probe_node.next

    while probe_node.next:
        probe_node = probe_node.next
        proceeding_node = proceeding_node.next

    proceeding_node.next = proceeding_node.next.next
    return dummy_node.next


test_cases = [([1, 2, 3, 4, 5], 1, [1, 2, 3, 4]),
              ([1, 2, 3, 4, 5], 2, [1, 2, 3, 5]),
              ([1, 2, 3, 4, 5], 5, [2, 3, 4, 5]),
              ([1], 1, []),
              ([1, 2], 1, [1]),
              ([5, 6, 9, 8, 6, 4, 5, 1, 9, 8, 7, 2, 8, 6, 8, 3, 5, 8, 6], 17,
               [5, 6, 8, 6, 4, 5, 1, 9, 8, 7, 2, 8, 6, 8, 3, 5, 8, 6]), ]
for test_list, test_n, expected_output in test_cases:
    return_head = remove_nth_node(LinkedList.create_linked_list(test_list).head, test_n)
    if expected_output:
        assert return_head.list_from_node() == expected_output
    else:
        assert return_head is None
