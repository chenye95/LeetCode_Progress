"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
from _Linked_List import ListNode, LinkedList


def reorder_list(head: ListNode) -> None:
    """
    :param head: head of a linked list
    """
    if not head or not head.next:
        return

    # Split list into two sub lists
    fast_pointer = slow_pointer = head
    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next

    sublist_start = slow_pointer.next
    slow_pointer.next = None

    # reverse 2nd half sub list
    previous_node = None
    current_node = sublist_start
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node = current_node
        current_node = next_node

    # combine 2 sub lists
    current_list_node = head
    next_list_node = previous_node

    while next_list_node:
        tmp = current_list_node.next
        current_list_node.next = next_list_node
        current_list_node = next_list_node
        next_list_node = tmp


test_cases = [(list(range(10)), [0, 9, 1, 8, 2, 7, 3, 6, 4, 5, ]),
              (list(range(9)), [0, 8, 1, 7, 2, 6, 3, 5, 4, ]),
              ([1, ], [1, ]),
              ([1, 2, ], [1, 2, ]), ]
for test_input, test_output in test_cases:
    test_head = LinkedList.create_linked_list(test_input).head
    assert test_head.list_from_node() == test_input
    reorder_list(head=test_head)
    assert test_head.list_from_node() == test_output
