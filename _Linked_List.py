from __future__ import annotations

from typing import List, Union

NodeValueType = Union[str, int, chr]


class ListNode:
    def __init__(self, val: NodeValueType, next: ListNode = None):
        self.val = val
        self.next = next

    def list_from_node(self) -> List[NodeValueType]:
        """
        :return: list of all nodes values after current node, self included
        """
        return_list = []
        point_to = self
        while point_to is not None:
            return_list.append(point_to.val)
            point_to = point_to.next
        return return_list

    def last_node(self) -> ListNode:
        """
        :return: last node in the list, following the next direction
        """
        point_to = self
        while point_to.next is not None:
            point_to = point_to.next
        return point_to


class LinkedList:
    def __init__(self, head: ListNode) -> None:
        self.head = head

    @staticmethod
    def create_linked_list(node_values: List[NodeValueType]) -> LinkedList:
        """
        :param node_values: list of node values
        :return: create a Linked List using the node_values provided
        """
        current_node = head = None
        for node_x in node_values:
            if not current_node:
                current_node = ListNode(node_x)
                head = current_node
            else:
                current_node.next = ListNode(node_x)
                current_node = current_node.next
        return LinkedList(head=head)


class PrintableListNode(ListNode):
    """
    Override output method
    """

    def __repr__(self):
        return str(self.val)


class PrintableLinkedList(LinkedList):
    """
    Override how Linked List is printed
    """

    @staticmethod
    def create_linked_list(node_values: List[NodeValueType]) -> PrintableLinkedList:
        current_node = None
        head = None
        for node_x in node_values:
            if not current_node:
                current_node = PrintableListNode(node_x)
                head = current_node
            else:
                current_node.next = PrintableListNode(node_x)
                current_node = current_node.next
        return PrintableLinkedList(head=head)

    def __init__(self, head: PrintableListNode, separator: str = ', '):
        super().__init__(head)
        self.separator = separator

    def __repr__(self):
        return_list = []
        current_node = self.head
        while current_node:
            return_list.append(str(current_node))
            current_node = current_node.next
        return self.separator.join(return_list)
