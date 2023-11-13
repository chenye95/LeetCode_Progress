"""
Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a
 multiple of k then left-out nodes, in the end, should remain as it is.

You may not alter the values in the list's nodes, only nodes themselves may be changed.
"""
from typing import Optional

from _Linked_List import ListNode, LinkedList


def reverse_k_group_first_count(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    # First count number of nodes in the linked list
    node_count = 0
    temp_pointer = head
    while temp_pointer:
        node_count += 1
        temp_pointer = temp_pointer.next

    n_group = node_count // k
    dummy_node = previous_node = ListNode(0, next=head)
    for _ in range(n_group):
        current_node = previous_node.next
        next_node = current_node.next
        # To reverse the k nodes, we need to reverse k - 1 links in between
        for _ in range(k - 1):
            current_node.next = next_node.next
            next_node.next = previous_node.next
            previous_node.next = next_node
            next_node = current_node.next
            # previous_node stores the node before the group, and points to the last node that has been swapped
            # next_node stores the next node to be swapped
            # current_node stores the original first node of the group, and points to the next node to be swapped

        previous_node = current_node

    return dummy_node.next


def reverse_k_group_no_count(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    temp_pointer = head
    dummy_node = previous_node = ListNode(0, next=head)
    while temp_pointer:
        for i in range(k):
            temp_pointer = temp_pointer.next
            if temp_pointer is None and i < k - 1:
                return dummy_node.next

        current_node = previous_node.next
        next_node = current_node.next
        # To reverse the k nodes, we need to reverse k - 1 links in between
        for _ in range(k - 1):
            # Before
            # previous_node stores the node before the group, and points to the last node that has been swapped
            # current_node stores the original first node of the group, and points to the current node to be swapped
            # next_node stores the current node to be swapped
            current_node.next = next_node.next
            next_node.next = previous_node.next
            previous_node.next = next_node
            next_node = current_node.next
            # previous_node stores the node before the group, and points to the last node that has been swapped
            # current_node stores the original first node of the group, and points to the next node to be swapped
            # next_node stores the next node to be swapped

        previous_node = current_node

    return dummy_node.next


test_cases = [
    ([1, 2, 3, 4, 5], 2, [2, 1, 4, 3, 5]),
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ([], 3, []),
    ([1, 2], 3, [1, 2]),
    ([1, 2], 2, [2, 1]),
]
for reverse_method in [reverse_k_group_no_count, reverse_k_group_first_count, ]:
    for test_list, test_k, expected_list in test_cases:
        result_head = reverse_method(LinkedList.create_linked_list(test_list).head, test_k)
        if expected_list:
            assert result_head.list_from_node() == expected_list, reverse_method.__name__
        else:
            assert result_head is None
