"""
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following
the next pointer. Internally, test_pos is used to denote the index of the node that tail's next pointer is connected to. Note
 that test_pos is not passed as a parameter.

Notice that you should not modify the linked list.
"""
from typing import List, Optional

from _Linked_List import ListNode, NodeValueType


def detect_cycle(head: ListNode) -> Optional[ListNode]:
    """
    :param head: start of a linked list
    :return: the node where the cycle begins
    """
    fast_pointer = slow_pointer = head
    # Assume the cycle length is l and there is length a path before cycle
    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        slow_pointer = slow_pointer.next
        if fast_pointer == slow_pointer:
            # when fast_pointer and slower_pointer meets
            # slow_pointer travelled x, fast_pointer travelled 2x, and 2x - x = l, length of the cycle
            cycle_start = head
            # slow_pointer is x = l steps before
            # cycle_start needs to travel a steps, before slow_pointer reaches a + l and meets up again
            while cycle_start != slow_pointer:
                cycle_start = cycle_start.next
                slow_pointer = slow_pointer.next

            return cycle_start

    return None


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
    test_head = test_create_test_cases(node_values=test_node_values, pos=test_pos)

    # test implementation of test_create_test_cases()
    test_head_list: List[Optional[ListNode]] = [None] * len(test_node_values)
    current_node = test_head
    for i in range(len(test_node_values)):
        test_head_list[i] = current_node
        current_node = current_node.next
    assert [test_node.val for test_node in test_head_list] == test_node_values
    assert (test_pos != -1 and current_node is test_head_list[test_pos]) or (test_pos == -1 and current_node is None)

    # test implementation of detect_cycle()
    return_node = detect_cycle(head=test_head)
    assert (test_pos == -1 and return_node is None) or (test_pos != -1 and return_node is test_head_list[test_pos])
