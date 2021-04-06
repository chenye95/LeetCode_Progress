"""
You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from
the end (the list is 1-indexed).
"""
from _Linked_List import ListNode, LinkedList


def swap_nodes_reference(head: ListNode, k: int) -> ListNode:
    """
    This implementation swap ListNodes within the LinkedList

    :param head: head of the linked list, the linked list is 1 indexed
    :param k: assume k is less or equal to length of linked list,
            swap the kth node from the beginning and the kth node from the end
    :return: the head of the modified linked list
    """
    # dummy head to solve k = 1 or length of linked list problem
    dummy_head = ListNode(val=-1, next=head)

    first_node_prev = dummy_head
    for i in range(k - 1):
        first_node_prev = first_node_prev.next

    second_node_prev = dummy_head
    second_node_probe = first_node_prev.next.next

    while second_node_probe:
        second_node_probe = second_node_probe.next
        second_node_prev = second_node_prev.next

    first_node = first_node_prev.next
    second_node = second_node_prev.next

    if first_node is not second_node:
        if second_node.next is first_node:
            first_node_after = first_node.next
            second_node_prev.next = first_node
            first_node.next = second_node
            second_node.next = first_node_after
        elif first_node.next is second_node:
            second_node_after = second_node.next
            first_node_prev.next = second_node
            second_node.next = first_node
            first_node.next = second_node_after
        else:
            second_node_after = second_node.next
            first_node_prev.next = second_node
            second_node.next = first_node.next
            second_node_prev.next = first_node
            first_node.next = second_node_after

    return dummy_head.next


def swap_nodes_value(head: ListNode, k: int) -> ListNode:
    """
    This implementation swap values stored in first and second node

    :param head: head of the linked list, the linked list is 1 indexed
    :param k: assume k is less or equal to length of linked list,
            swap the kth node from the beginning and the kth node from the end
    :return: the head of the modified linked list
    """
    first_node = head
    for i in range(k - 1):
        first_node = first_node.next

    second_node = head
    second_node_probe = first_node.next

    while second_node_probe:
        second_node_probe = second_node_probe.next
        second_node = second_node.next

    first_node.val, second_node.val = second_node.val, first_node.val

    return head


test_cases = [([1, 2, 3, 4, 5], 2, [1, 4, 3, 2, 5]),
              ([1], 1, [1]),
              ([1, 2], 2, [2, 1]),
              ([1, 2], 1, [2, 1]),
              ([1, 2, 3], 2, [1, 2, 3]),
              ([7, 9, 6, 6, 7, 8, 3, 0, 9, 5], 5, [7, 9, 6, 6, 8, 7, 3, 0, 9, 5]), ]
for swap_nodes in [swap_nodes_value, swap_nodes_reference]:
    for test_input, test_k, expected_output in test_cases:
        test_linked_list = LinkedList.create_linked_list(test_input)
        test_linked_list.head = swap_nodes(test_linked_list.head, test_k)
        assert test_linked_list.head.list_from_node() == expected_output, swap_nodes.__name__
