"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
import heapq
from typing import List, Optional

from _Linked_List import ListNode, LinkedList


def merge_k_lists(lists: List[ListNode]) -> Optional[ListNode]:
    """
    Note this will destroy the original linked lists

    :param lists: k head node of sorted linked lists
    :return: merge into one sorted linked list and return head node
    """
    # Add i to break even, < may not be implemented in ListNode class
    current_heap = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i] is not None]
    if not current_heap:
        return None
    heapq.heapify(current_heap)
    head = current_node = None
    while current_heap:
        _, next_i, next_node = heapq.heappop(current_heap)
        if not head:
            head = current_node = next_node
        else:
            current_node.next = next_node
            current_node = current_node.next
        if next_node.next:
            heapq.heappush(current_heap, (next_node.next.val, next_i, next_node.next))
    return head


test_cases = [([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
              ([[1, 4], [2, 4]], [1, 2, 4, 4]),
              ([[]], None)]
for case_i, expected_output in test_cases:
    result_head = merge_k_lists(lists=[LinkedList.create_linked_list(list_j).head for list_j in case_i])
    if expected_output:
        assert result_head.list_from_node() == expected_output, result_head.list_from_node()
    else:
        assert expected_output is None
