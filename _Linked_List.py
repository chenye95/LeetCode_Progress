from __future__ import annotations

from typing import List, Union, Optional, Tuple

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
        while point_to:
            return_list.append(point_to.val)
            point_to = point_to.next
        return return_list

    def last_node(self) -> ListNode:
        """
        :return: last node in the list, following the next direction
        """
        point_to = self
        while point_to.next:
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

    def midpoint_of_list(self) -> Tuple[int, ListNode]:
        """
        :return: (index of the mid point, mid point of linked list)
            for length of 2n, returns index n
            for length of 2n + 1, returns index n
        """
        fast_pointer = slow_pointer = self.head
        mid_index = 0
        while fast_pointer and fast_pointer.next:
            mid_index += 1
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next

        return mid_index, slow_pointer

    def k_to_last(self, k: int) -> Optional[ListNode]:
        """
        :return: the node k nodes apart from list end,
        i.e. the kth node in the list counting backwards
        i.e. index -k-1,
        """
        fast_pointer = self.head
        for _ in range(k):
            fast_pointer = fast_pointer.next
            if fast_pointer is None:
                return None
        slow_pointer = self.head
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            slow_pointer = slow_pointer.next
        return slow_pointer


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
