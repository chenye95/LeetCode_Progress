"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order,
 and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from _Linked_List import ListNode, LinkedList


def add_two_number(l1: ListNode, l2: ListNode) -> ListNode:
    """
    :param l1: head of a non-empty linked lists representing a non-negative integers, one node per digit
    :param l2: head of a non-empty linked lists representing a non-negative integers, one node per digit
    :return: head of a non-empty linked lists representing sum of two integers, one node per digit
    """
    if not l1:
        return l2
    if not l2:
        return l1

    dummy_node = current_node = ListNode(0)
    carry_over = 0
    while l1 and l2:
        current_node.next = ListNode((l1.val + l2.val + carry_over) % 10)
        carry_over = (l1.val + l2.val + carry_over) // 10
        current_node = current_node.next
        l1 = l1.next
        l2 = l2.next

    remaining_list = l1 if l1 else l2
    while remaining_list and carry_over:
        current_node.next = ListNode((remaining_list.val + carry_over) % 10)
        carry_over = (remaining_list.val + carry_over) // 10
        current_node = current_node.next
        remaining_list = remaining_list.next

    if remaining_list:
        current_node.next = remaining_list
    elif carry_over:
        current_node.next = ListNode(carry_over)

    return dummy_node.next


test_cases = [([2, 4, 3], [5, 6, 4], [7, 0, 8]),
              ([0], [0], [0]),
              ([1, 8], [0], [1, 8]),
              ([9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9], [8, 9, 9, 9, 0, 0, 0, 1]),
              ([2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4,
                3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 9],
               [5, 6, 4, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4,
                3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 2, 4, 3, 9, 9, 9, 9],
               [7, 0, 8, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8,
                6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 4, 8, 6, 1, 4, 3, 9, 1]), ]
for input_1, input_2, expected_output in test_cases:
    assert add_two_number(l1=LinkedList.create_linked_list(input_1).head,
                          l2=LinkedList.create_linked_list(input_2).head).list_from_node() == expected_output
