from __future__ import annotations
from typing import List, Any


class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def list_from_node(self) -> List[Any]:
        return_list = []
        point_to = self
        while point_to is not None:
            return_list.append(point_to.val)
            point_to = point_to.next
        return return_list

    def last_node(self) -> ListNode:
        point_to = self
        while point_to.next is not None:
            point_to = point_to.next
        return point_to

class LinkedList:
    def __init__(self, head):
        self.head = head

    @staticmethod
    def create_linked_list(node_lists: List[Any]) -> LinkedList:
        current_node = None
        head = None
        for node_x in node_lists:
            if not current_node:
                current_node = ListNode(node_x)
                head = current_node
            else:
                current_node.next = ListNode(node_x)
                current_node = current_node.next
        return LinkedList(head=head)

class PrintableListNode(ListNode):
    def __repr__(self):
        return str(self.val)

class PrintableLinkedList(LinkedList):
    @staticmethod
    def create_linked_list(node_lists) -> PrintableLinkedList:
        current_node = None
        head = None
        for node_x in node_lists:
            if not current_node:
                current_node = PrintableListNode(node_x)
                head = current_node
            else:
                current_node.next = PrintableListNode(node_x)
                current_node = current_node.next
        return PrintableLinkedList(head=head)

    def __init__(self, head, separator =', '):
        super().__init__(head)
        self.separator = separator

    def __repr__(self):
        return_list = []
        current_node = self.head
        while current_node:
            return_list.append(str(current_node))
            current_node = current_node.next
        return self.separator.join(return_list)
