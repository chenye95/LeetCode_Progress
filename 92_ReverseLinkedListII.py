"""
Given the head of a singly linked list and two integers left and right where left <= right, reverse the nodes of the
 list from position left to position right, and return the reversed list.
"""
from _Linked_List import ListNode, LinkedList


def reverse_between(head: ListNode, left: int, right: int) -> ListNode:
    """
    :param head: head of the original linked list 1 <= n <= 500
    :param left: 1-indexed left inclusive marker for the reversed segment
    :param right: 1-indexed right inclusive marker for the reversed segment
    :return: (modified in place) head of the updated linked list,
    """
    if left == right:
        return head

    dummy_head = ListNode(0, next=head)
    left_before = dummy_head
    for _ in range(left - 1):
        left_before = left_before.next

    current_node = left_before.next
    next_node = current_node.next
    for _ in range(right - left):
        previous_node = current_node
        current_node = next_node
        next_node = current_node.next
        current_node.next = previous_node
    left_before.next.next = next_node
    left_before.next = current_node

    return dummy_head.next


test_cases = [([1, 2, 3, 4, 5, 6], 2, 5),
              ([1, 2, 3, 4, 5], 2, 4),
              ([5], 1, 1),
              ([-5, 4, -2, -2, -2, 3, -3], 6, 6),
              ([-18, -29, 30, 10, -45, -93, 9, -4, -52, 91, 61, 91, 19, 32, -100, 34, 38, 99, -93, -37, 73, -67, -29,
                52, 6, -50, -87, -33, 6, -72, 72, 89, -51, -48, -52, -45, -41, 7, 1, -42, -3, -38, -52, 66, 44, 99, 0,
                -19, 47, 7, 44, 19, -10, 65, -30, 96, -86, -17, -87, -29, -39, 85, -41, -39, 87, -43, -34, -54, 65, 67,
                4, -39, 79, 2, -73, 23, 0, -23, 54, 97, 34, -2, -35, -77, -88, -14, 69, 78, 19, 82, -52, 81, 17, -43,
                92, 3, 14, -43, 49, -22, 74, -98, -10, 53, 4, -33, -75, 54, 44, 79, 50, -73, -74, 66, -50, -61, -49,
                -82, -84, 70, -100, -86, 0, 17, -29, -59, 70, 85, -2, 19, -87, -78, -29, -47, 75, 26, -30, 100, -21, 64,
                28, 80, 91, 55, 45, -60, 94, 46, -42, 60, 15, -92, 74, -85, -25, -56, -44, -55, 79, 5, 14, 42, -23, 35,
                95, -49, -40, -86, -100, -10, 78, 28, -31, 68, -18, 64, -93, -75, -41, -84, 85, 74, 75, 8, 39, -100, 2,
                46, 96, -69, -100, -41, 73, -23, 94, 18, -22, -46, 32, -22, 44, 10, 56, 63, -23, 89, -24, -65, -87, 35,
                -99, 49, 8, 76, -44, 98, 26, 9, 43, 21, 40, -7, 80, 12, 70, 74, 80, -53, -73, 12, -25, 21, 72, -70, -17,
                -52, -82, 59, -67, 83, -7, -66, 31, 51, 61, 37, 48, -14, -55, -60, 58, 85, 33, 37, -53, -48, -40, -74,
                -51, -63, -12, 24, 58, -41, 5, 91, -42, -27, 49, -9, -95, 92, -24, 36, -7, 87, -77, 91, -78, -82, 82,
                80, 54, -36, -33, -100, 17, 27, 77, 16, 65, -35, -60, -28, 24, -5, -37, 82, 18, 62, -77, 24, 4, -1,
                -41], 209, 286), ]
for test_list, test_left, test_right in test_cases:
    assert reverse_between(LinkedList.create_linked_list(test_list).head, test_left, test_right).list_from_node() == \
           test_list[:test_left - 1] + list(reversed(test_list[test_left - 1: test_right])) + test_list[test_right:]
