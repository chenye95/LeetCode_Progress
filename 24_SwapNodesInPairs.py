""""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the
 values in the list's nodes (i.e., only nodes themselves may be changed.)
"""
from typing import Optional

from _Linked_List import ListNode, LinkedList


def swap_pairs(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head:
        return None

    dummy_node, current_node, next_node = ListNode(0, next=head), head, head.next
    previous_node = dummy_node
    while current_node and current_node.next:
        adjacent = current_node.next
        previous_node.next = adjacent
        current_node.next, adjacent.next = adjacent.next, current_node
        previous_node, current_node = current_node, current_node.next

    return dummy_node.next


test_cases = [
    ([1, 2, 3, 4], [2, 1, 4, 3]),
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [2, 1, 4, 3, 5]),
    ([1, 2, 3], [2, 1, 3]),
]
for test_list, expected_list in test_cases:
    result_head = swap_pairs(LinkedList.create_linked_list(test_list).head)
    if expected_list:
        assert result_head.list_from_node() == expected_list, result_head.list_from_node()
    else:
        assert result_head is None
