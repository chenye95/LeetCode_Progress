"""
Given a linked list, determine if it has a cycle in it.
"""
from typing import List

from _Linked_List import ListNode, NodeValueType


def has_cycle(head: ListNode) -> bool:
    """
    :param head: start of a linked list
    :return: whether the linked list contains a cycle
    """
    fast_pointer = slow_pointer = head
    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if fast_pointer == slow_pointer:
            return True

    return False


def test_create_test_cases(node_values: List[NodeValueType], pos: int = -1) -> ListNode:
    """
    create test cases for the problem
    :param node_values: list representing node values
    :param pos: tail connects to pos_th node; -1 if no cycle, else 0 <= test_pos < len(test_node_values)
    """
    assert node_values
    assert -1 <= pos < len(node_values)
    head = previous_node = tail_connect_to = None
    for i in range(len(node_values)):
        if head is None:
            head = ListNode(node_values[i])
            previous_node = head
        else:
            previous_node.next = ListNode(node_values[i])
            previous_node = previous_node.next
        if i == pos:
            tail_connect_to = previous_node
    previous_node.next = tail_connect_to
    return head


test_cases = [([3, 2, 0, -4], 1),
              ([1, 2], 0),
              ([1], -1), ]

for test_node_values, test_pos in test_cases:
    test_head = test_create_test_cases(test_node_values, test_pos)

    # test implementation of test_create_test_cases()
    test_head_list = [None] * len(test_node_values)
    current_node = test_head
    for i in range(len(test_node_values)):
        test_head_list[i] = current_node.val
        current_node = current_node.next
    assert test_head_list == test_node_values
    assert (test_pos != -1 and current_node.val == test_node_values[test_pos]) or \
           (test_pos == -1 and current_node is None)

    # test implementation of has_cycle()
    assert has_cycle(test_head) is (test_pos != -1)
