"""
Remove all elements from a linked list of integers that have value val.
"""
from random import randint
from typing import Optional

from _Linked_List import ListNode, LinkedList


def remove_elements(head: Optional[ListNode], val: int) -> Optional[ListNode]:
    """
    :param head: head of a linked list, can be None
    :param val: remove all elements from linked list that equals to val
    :return: head of the remaining linked list, return None if nothing left
    """
    while head and head.val == val:
        head = head.next
    if head is None:
        return None
    current_node = head
    while current_node.next:
        if current_node.next.val == val:
            current_node.next = current_node.next.next
        else:
            current_node = current_node.next
    return head


N, l = 1000, 300
a, b = -100, 100
for i in range(N):
    test_target = randint(a, b)
    test_input_list = [test_target] + [randint(a, b) for _ in range(l)]
    test_output_list = list(filter(lambda x: x != test_target, test_input_list))
    get_output = remove_elements(LinkedList.create_linked_list(test_input_list).head, test_target)
    assert get_output.list_from_node() == test_output_list
assert remove_elements(LinkedList.create_linked_list([1] * randint(10, 50)).head, 1) is None
assert remove_elements(None, 1) is None
