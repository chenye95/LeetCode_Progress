from typing import List
from _Linked_List import ListNode, LinkedList
import heapq

def mergeKLists(lists: List[ListNode]) -> ListNode:
    current_heap = [(lists[i].val, i, lists[i]) for i in range(len(lists)) if lists[i] is not None]
    if not current_heap:
        return None
    heapq.heapify(current_heap)
    head, current_node = None, None
    while current_node is not None or head is None:
        next_val, next_i, next_node = heapq.heappop(current_heap)
        if head is None:
            head = ListNode(next_node.val)
            current_node = head
        elif next_node is not None:
            current_node.next = ListNode(next_node.val)
            current_node = current_node.next
        if next_node is not None:
            if next_node is None or next_node.next is None:
                heapq.heappush(current_heap, (float("inf"), next_i, None))
            else:
                heapq.heappush(current_heap, (next_node.next.val, next_i, next_node.next))
        else:
            current_node = None
    return head

test_cases = [([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
              ([[1, 4], [2, 4]], [1, 2, 4, 4]),
              ([[]], None)]
for case_i, expected in test_cases:
    linked_case = [LinkedList.create_linked_list(list_j).head for list_j in case_i]
    result_head = mergeKLists(linked_case)
    if result_head:
        assert result_head.list_from_node() == expected
    else:
        assert expected is None