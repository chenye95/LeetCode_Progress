from __future__ import annotations
from typing import List, Any


class DoubleListNode:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def list_from_node(self) -> List[Any]:
        return_list = []
        point_to = self
        while point_to is not None:
            return_list.append(point_to.val)
            point_to = point_to.next
        return return_list

    def list_before_node(self):
        return_list = []
        point_to = self
        while point_to is not None:
            return_list.append(point_to.val)
            point_to = point_to.prev
        return return_list[::-1]

    def last_node(self) -> DoubleListNode:
        point_to = self
        while point_to.next is not None:
            point_to = point_to.next
        return point_to

    def first_node(self):
        point_to = self
        while point_to.prev is not None:
            point_to = point_to.prev
        return point_to

class DoubleLinkedList:
    def __init__(self, head = None, tail = None):
        self.head = head
        self.tail = tail


    @staticmethod
    def create_linked_list(node_lists):
        current_node = None
        head = None
        for node_x in node_lists:
            if not current_node:
                current_node = DoubleListNode(node_x)
                head = current_node
            else:
                current_node.next = DoubleListNode(node_x, prev=current_node)
                current_node = current_node.next
        return DoubleLinkedList(head, current_node)

    def append_val_tail(self, val):
        node = DoubleListNode(val, prev=self.tail, next=None)
        self.tail.next = node
        self.tail = node

    def append_val_head(self, val):
        node = DoubleListNode(val, prev=None, next=self.head)
        self.head.prev = node
        self.head = node

class ComplexListNode(DoubleListNode):
    def __init__(self, val, prev=None, next=None, child=None):
        super().__init__(val, next=next, prev=prev)
        self.child = child

class ComplexLinkedList:
    def __init__(self, head):
        self.head = head

    @staticmethod
    def create_linked_list(node_lists) -> ComplexListNode:
        current_node = None
        head = None
        for node_x in node_lists:
            if not current_node:
                current_node = ComplexListNode(node_x)
                head = current_node
            else:
                current_node.next = ComplexListNode(node_x, prev=current_node)
                current_node = current_node.next
        return head

    def flatten_structure(self):
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