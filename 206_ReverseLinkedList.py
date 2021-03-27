"""
Given the head of a singly linked list, reverse the list, and return the reversed list
"""
from _Linked_List import ListNode, LinkedList


def reverse_list(head: ListNode) -> ListNode:
    """
    :param head: head of a singly linked list
    :return: the head of the reversed list
    """
    previous_node, current_node = None, head
    while current_node:
        next_node = current_node.next
        current_node.next = previous_node
        previous_node, current_node = current_node, next_node

    return previous_node


test_cases = [[1, 2, 3, 4, 5],
              [1, 2],
              [], ]
for test_input in test_cases:
    test_list = LinkedList.create_linked_list(test_input)
    test_list.head = reverse_list(head=test_list.head)
    if not test_input:
        assert test_list.head is None
    else:
        assert test_list.head.list_from_node() == test_input[::-1]
