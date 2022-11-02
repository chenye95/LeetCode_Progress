from typing import Optional

from _Linked_List import LinkedList, ListNode


def insertion_sort_list(head: Optional[ListNode]) -> Optional[ListNode]:
    if head is None:
        return None

    current_node = head.next
    head.next = None

    while current_node:
        unsorted_list = current_node.next
        if current_node.val < head.val:
            # insert to the front of sorted list
            current_node.next = head
            head = current_node
        else:
            insert_position = head
            while insert_position.next and insert_position.next.val < current_node.val:
                insert_position = insert_position.next
            tmp = insert_position.next
            insert_position.next = current_node
            current_node.next = tmp
        current_node = unsorted_list

    return head


test_cases = [([4, 2, 1, 3], [1, 2, 3, 4]),
              ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
              ([6, 5, 3, 1, 8, 7, 2, 4], [1, 2, 3, 4, 5, 6, 7, 8]), ]
for test_in, expected_output in test_cases:
    test_list = LinkedList.create_linked_list(test_in)
    return_head = insertion_sort_list(test_list.head)
    assert return_head.list_from_node() == expected_output
