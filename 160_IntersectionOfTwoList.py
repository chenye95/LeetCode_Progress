"""
Write a program to find the node at which the intersection of two singly linked lists begins.
"""
from typing import Optional

from _Linked_List import ListNode, LinkedList


def get_intersection_node(head_a: ListNode, head_b: ListNode) -> Optional[ListNode]:
    """
    let len_a be length of section in list a before intersection
    let len_b be length of section in list b before intersection
    let len_c be length of section after intersection
    if two list intersects, we can find the intersection in len_a + len_b + len_c steps or len_a steps if len_a == len_b
    :param head_a: head node of list a
    :param head_b: head node of list b
    :return: ListNode that is intersection of two linked list, if exists; None otherwise
    """
    if not head_a or not head_b:
        return None

    current_a, continue_a = head_a, True
    current_b, continue_b = head_b, True
    while current_a != current_b:
        if current_a.next:
            # traverse down the list
            current_a = current_a.next
        elif continue_a:
            # switch to list b to finish the remaining len_b steps
            current_a, continue_a = head_b, False
        else:
            # cap out at len_a + len_b + len_c steps
            # no need to traverse more
            return None

        if current_b.next:
            # traverse down the list
            current_b = current_b.next
        elif continue_b:
            # switch to list a to finish the remaining len_a steps
            current_b, continue_b = head_a, False
        else:
            # cap out at len_a + len_b + len_c steps
            # no need to traverse more
            return None

    return current_a


test_cases = [([4, 1], [5, 6, 1], [8, 4, 5]),
              ([1, 9, 1], [3], [2, 4]),
              ([2, 6, 4], [1, 5], []),
              ([4, 1], [5, 6, 1], [8, 4, 5]),
              ([2, 6, 4], [2, 6, 4], []),
              ]
for list_a, list_b, list_c in test_cases:
    test_head_a = LinkedList.create_linked_list(list_a).head
    test_head_b = LinkedList.create_linked_list(list_b).head
    test_head_c = LinkedList.create_linked_list(list_c).head
    test_head_a.last_node().next = test_head_c
    test_head_b.last_node().next = test_head_c
    intersection = get_intersection_node(test_head_a, test_head_b)
    if test_head_c:
        assert intersection.val == list_c[0]
    else:
        assert intersection is None
