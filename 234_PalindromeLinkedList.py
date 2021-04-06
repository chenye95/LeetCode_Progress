"""
Given the head of a singly linked list, return true if it is a palindrome.
"""
from _Linked_List import ListNode, LinkedList


def is_palindrome(head: ListNode) -> bool:
    """
    Destructive operation: it will break the linked list

    :param head: head of a singly linked list
    :return: return whether the linked list is a palindrome
    """
    # find mid point of the linked list, and reverse the first half the linked list
    fast_pointer = slow_pointer = head
    prev_pointer = None
    while fast_pointer and fast_pointer.next:
        fast_pointer = fast_pointer.next.next
        tmp_pointer = slow_pointer.next
        slow_pointer.next = prev_pointer
        prev_pointer = slow_pointer
        slow_pointer = tmp_pointer

    if fast_pointer:
        # odd length case
        slow_pointer = slow_pointer.next

    while slow_pointer:
        if slow_pointer.val != prev_pointer.val:
            return False
        slow_pointer = slow_pointer.next
        prev_pointer = prev_pointer.next

    return True


test_cases = [([1, 2, 2, 1], True),
              ([1, 2], False),
              ([1, 2, 3, 4, 5, 4, 3, 2, 1], True),
              ([1, 2, 3, 4, 4, 3, 2, 1], True),
              ([1, 2, 3, 4, 5, 4, 2, 1], False),
              ([1, 2, 3, 4, 5, 6, 3, 2, 1], False), ]
for test_list, expected_output in test_cases:
    assert is_palindrome(head=LinkedList.create_linked_list(test_list).head) is expected_output
