from __future__ import annotations

from typing import List, Union

NodeValueType = Union[str, int, chr]


class DoubleListNode:
    def __init__(self, val: NodeValueType, next: DoubleListNode = None, prev: DoubleListNode = None):
        self.val = val
        self.next = next
        self.prev = prev

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

    def list_before_node(self) -> List[NodeValueType]:
        """
        :return: list of all nodes values before current node, self included. self.value at last
        """
        return_list = []
        point_to = self
        while point_to is not None:
            return_list.append(point_to.val)
            point_to = point_to.prev
        return return_list[::-1]

    def last_node(self) -> DoubleListNode:
        """
        :return: last node in the list, following the next direction
        """
        point_to = self
        while point_to.next is not None:
            point_to = point_to.next
        return point_to

    def first_node(self) -> DoubleListNode:
        """
        :return: first node in the list, following the prev direction
        """
        point_to = self
        while point_to.prev is not None:
            point_to = point_to.prev
        return point_to


class DoubleLinkedList:
    def __init__(self, head: DoubleListNode = None, tail: DoubleListNode = None) -> None:
        self.head = head
        self.tail = tail

    @staticmethod
    def create_linked_list(node_values: List[NodeValueType]) -> DoubleLinkedList:
        """
        :param node_values: list of node values
        :return: create a Double Linked List using the node_values provided
        """
        current_node = head = None
        for node_x in node_values:
            if not current_node:
                current_node = DoubleListNode(node_x)
                head = current_node
            else:
                current_node.next = DoubleListNode(node_x, prev=current_node)
                current_node = current_node.next
        return DoubleLinkedList(head, current_node)

    def append_val_tail(self, val: NodeValueType) -> None:
        """
        Create a DoubleListNode and append to the end of the Double Linked List
        """
        node = DoubleListNode(val, prev=self.tail, next=None)
        self.tail.next = node
        self.tail = node

    def append_val_head(self, val: NodeValueType) -> None:
        """
        Create a DoubleListNode and add to the head of the Double Linked List
        """
        node = DoubleListNode(val, prev=None, next=self.head)
        self.head.prev = node
        self.head = node


class ComplexListNode(DoubleListNode):
    def __init__(self, val, prev=None, next=None, child=None):
        super().__init__(val, next=next, prev=prev)
        self.child = child


class ComplexLinkedList:
    def __init__(self, head: ComplexListNode) -> None:
        self.head = head

    @staticmethod
    def create_linked_list(node_lists: List[NodeValueType]) -> ComplexLinkedList:
        """
        Create Double Linked List with ComplexListNode type. Need to add child connections manually
        """
        current_node = head = None
        for node_x in node_lists:
            if not current_node:
                current_node = ComplexListNode(node_x)
                head = current_node
            else:
                current_node.next = ComplexListNode(node_x, prev=current_node)
                current_node = current_node.next
        return ComplexLinkedList(head)

    def flatten_structure(self) -> None:
        """
        Flatten the Multilevel Complex List into Double Linked list, with no child reference
        method described in Leet Code 430 https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
        insert Linked List stem from Child node right after current node
        i.e. 1 -> 2
               -> 3 -> 4
        becomes 1 -> 3 -> 4 -> 2
        """
        current_node = self.head
        node_stack = []
        while current_node:
            if current_node.child is not None:
                if current_node.next is not None:
                    node_stack.append(current_node.next)
                current_node.next = current_node.child
                current_node.child.prev = current_node
                current_node.child = None
            elif current_node.next is None and current_node.child is None and node_stack:
                next_node = node_stack.pop()
                current_node.next = next_node
                next_node.prev = current_node
            current_node = current_node.next
