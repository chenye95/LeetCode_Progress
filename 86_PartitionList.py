"""
Given the head of a linked list and a value x, partition it such that all nodes less than x come before nodes greater
 than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.
"""
from _Linked_List import ListNode, LinkedList


def partition(head: ListNode, x: int) -> ListNode:
    """
    :param head: head of a linked list; operation will destruct the linked list
    :param x: all nodes less than x come before nodes greater or equal to x
    :return: head of updated list
    """
    # Two dummy nodes to separate less than and greater than sub lists
    less_dummy = less_current = ListNode(val=None)
    greater_dummy = greater_current = ListNode(val=None)

    while head:
        # use head pointer to iterate through original list
        # and partition into two segments
        if head.val < x:
            less_current.next = head
            less_current = head
        else:
            greater_current.next = head
            greater_current = head
        head = head.next

    greater_current.next = None
    less_current.next = greater_dummy.next

    return less_dummy.next


test_cases = [([1, 4, 3, 2, 5, 2], 3), ([2, 1], 2),
              ([-21, -59, 4, -99, 84, -65, -32, -80, 12, -45, 17, -52, 72, -51, -64, -37, -34, -28, 85, -3, -22, 1, 4,
                -2, 12, -70, -83, 48, -99, 31, -87, -19, 24, 18, -66, 8, 5, 2, -20, -83, 10, 49, -35, -66, 99, -46, -3,
                -83, -22, -65, 14, 8, -12, 71, -94, -100, -99, 75, 48, -98, -42, 62, -65, 82, -68, -78, -58, 37, -24,
                -26, 55, 86, -76, 72, -79, 75, -74, -30, 92, -43, 5, 7, 65, 93, -70, 24, 93, -69, -1, 42, 85, 58, -44,
                73, -8, -12, 95, -13, 77, -29, 61, -16, -90, 37, -91], 53), ]
for test_input, test_x in test_cases:
    assert partition(LinkedList.create_linked_list(test_input).head, test_x).list_from_node() == \
           [x_i for x_i in test_input if x_i < test_x] + [x_i for x_i in test_input if x_i >= test_x]
