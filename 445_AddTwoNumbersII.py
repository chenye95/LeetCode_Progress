"""
You are given two non-empty linked lists representing two non-negative integers. The most significant digit comes first
 and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""
from _Linked_List import ListNode, LinkedList


def add_two_numbers_stack(l1: ListNode, l2: ListNode) -> ListNode:
    """
    :param l1: non-empty linked list representing a non-negative integer. Most significant digit comes first and each
     node contains a digit, and contains no leading zero
    :param l2: non-empty linked list representing a non-negative integer. Most significant digit comes first and each
     node contains a digit, and contains no leading zero
    :return: sum as a linked list with most significant digit comes first
    """
    l1_list, l2_list = [], []
    for point_to, append_to in [(l1, l1_list), (l2, l2_list)]:
        while point_to:
            append_to.append(point_to.val)
            point_to = point_to.next

    return_head = None
    carry_over = 0
    while l1_list or l2_list:
        l1_val = l1_list.pop() if l1_list else 0
        l2_val = l2_list.pop() if l2_list else 0
        return_head = ListNode(val=(l1_val + l2_val + carry_over) % 10, next=return_head)
        carry_over = (l1_val + l2_val + carry_over) // 10

    if carry_over:
        return_head = ListNode(val=carry_over, next=return_head)

    return return_head


def add_two_numbers_int(l1: ListNode, l2: ListNode) -> ListNode:
    """
    :param l1: non-empty linked list representing a non-negative integer. Most significant digit comes first and each
     node contains a digit, and contains no leading zero
    :param l2: non-empty linked list representing a non-negative integer. Most significant digit comes first and each
     node contains a digit, and contains no leading zero
    :return: sum as a linked list with most significant digit comes first
    """
    n1 = n2 = 0
    while l1:
        n1 = n1 * 10 + l1.val
        l1 = l1.next
    while l2:
        n2 = n2 * 10 + l2.val
        l2 = l2.next

    n3 = n1 + n2
    return_head = None
    while n3 > 0:
        return_head = ListNode(n3 % 10, next=return_head)
        n3 //= 10

    return return_head if return_head else ListNode(0)


test_cases = [([7, 2, 4, 3], [5, 6, 4], [7, 8, 0, 7]),
              ([2, 4, 3], [5, 6, 4], [8, 0, 7]),
              ([0], [0], [0]),
              ([9, 9, 3], [1], [9, 9, 4]),
              ([9, 9, 3], [7], [1, 0, 0, 0]),
              ([5, 5, 5], [4, 9, 5], [1, 0, 5, 0]), ]
for add_two_numbers in [add_two_numbers_stack]:
    for test_l1_list, test_l2_list, expected_output in test_cases:
        assert add_two_numbers(LinkedList.create_linked_list(test_l1_list).head,
                               LinkedList.create_linked_list(test_l2_list).head).list_from_node() == expected_output
