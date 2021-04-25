"""
Given the head of a linked list, rotate the list to the right by k places.
"""
from _Linked_List import ListNode, LinkedList


def rotate_right(head: ListNode, k: int) -> ListNode:
    """
    :param head: start of a linked list with 0 <= n <= 500 nodes
    :param k: integer 0 <= k <= 2 * 10^9
    :return: start of the rotated list
    """
    if not head or k == 0:
        return head

    # probe to find the kth node from the last
    list_end = head
    list_len = 0
    for _ in range(k):
        if list_end is None:
            # k is larger than length of the list
            return rotate_right(head, k % list_len)
        list_end = list_end.next
        list_len += 1

    if list_end is None:
        # k == list_len
        return head

    # find the kth node from the last: guaranteed k < list_len
    current_node = head
    while list_end.next:
        current_node = current_node.next
        list_end = list_end.next

    # perform rotation
    return_node = current_node.next
    current_node.next = None
    list_end.next = head

    return return_node


test_cases = [([1, 2, 3, 4, 5], 2, [4, 5, 1, 2, 3]),
              ([1, 2, 3, 4, 5], 5, [1, 2, 3, 4, 5]),
              ([0, 1, 2], 4, [2, 0, 1]),
              ([1], 99, [1]),
              ([30, 60, 35, 62, 11, 83, 22, 53, 32, 35, 31, 97, 43, 24, 3, 4, 56, 47, 69, 46, 36, 83, 69, 18, 73, 19,
                59, 20, 59, 49, 79, 41, 62, 14, 4, 25, 49, 78, 78, 33, 13, 9, 30, 9, 85, 85, 13, 41, 84, 34, 40, 21, 17,
                61, 91, 43, 32, 50, 63, 44, 51, 95, 85], 57,
               [22, 53, 32, 35, 31, 97, 43, 24, 3, 4, 56, 47, 69, 46, 36, 83, 69, 18, 73, 19, 59, 20, 59, 49, 79, 41,
                62, 14, 4, 25, 49, 78, 78, 33, 13, 9, 30, 9, 85, 85, 13, 41, 84, 34, 40, 21, 17, 61, 91, 43, 32, 50, 63,
                44, 51, 95, 85, 30, 60, 35, 62, 11, 83]), ]
for test_input, test_k, expected_output in test_cases:
    assert rotate_right(LinkedList.create_linked_list(test_input).head, test_k).list_from_node() == expected_output
