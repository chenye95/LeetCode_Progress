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
    INDEX_OUT_OF_BOUND = -1

    def __init__(self, head: DoubleListNode = None, tail: DoubleListNode = None, list_len: int = 0) -> None:
        self.head = head
        self.tail = tail
        self.list_len = list_len

    def __len__(self) -> int:
        return self.list_len

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
        return DoubleLinkedList(head, current_node, len(node_values))

    def add_at_tail(self, val: NodeValueType) -> None:
        """
        Create a DoubleListNode and append to the end of the Double Linked List
        """
        if self.list_len:
            node = DoubleListNode(val, prev=self.tail, next=None)
            self.tail.next = node
            self.tail = node
            self.list_len += 1
        else:
            self.head = self.tail = DoubleListNode(val)
            self.list_len = 1

    def add_at_head(self, val: NodeValueType) -> None:
        """
        Create a DoubleListNode and add to the head of the Double Linked List
        """
        if self.list_len:
            node = DoubleListNode(val, prev=None, next=self.head)
            self.head.prev = node
            self.head = node
            self.list_len += 1
        else:
            self.head = self.tail = DoubleListNode(val)
            self.list_len = 1

    def delete_at_tail(self) -> None:
        """
        Remove tail node
        """
        if self.list_len > 1:
            self.tail.prev.next = None
            self.tail = self.tail.prev
            self.list_len -= 1
        elif self.list_len == 1:
            self.head = self.tail = None
            self.list_len = 0

    def delete_at_head(self) -> None:
        """
        Remove tail node
        """
        if self.list_len > 1:
            self.head.next.prev = None
            self.head = self.head.next
            self.list_len -= 1
        else:
            self.head = self.tail = None
            self.list_len = 0

    def get_at_index(self, index: int) -> NodeValueType:
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """
        if index < 0 or index >= self.list_len:
            return self.INDEX_OUT_OF_BOUND
        if index == 0:
            return self.head.val
        if index == self.list_len - 1:
            return self.tail.val
        if index <= self.list_len // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
            return current_node.val
        else:
            current_node = self.tail
            for _ in range(self.list_len - 1 - index):
                current_node = current_node.prev
            return current_node.val

    def add_at_index(self, index: int, val: NodeValueType) -> None:
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        """
        if index < 0 or index > self.list_len:
            # not valid index, ignore
            return
        if index == 0:
            # add to head
            self.add_at_head(val)
            return
        if index == self.list_len:
            # add to tail
            self.add_at_tail(val)
            return

        if index <= self.list_len // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.list_len - 1 - index):
                current_node = current_node.prev

        new_node = DoubleListNode(val=val, next=current_node, prev=current_node.prev)
        current_node.prev = new_node
        new_node.prev.next = new_node
        self.list_len += 1

    def delete_at_index(self, index: int) -> None:
        """
        Delete the index-th node in the linked list, if the index is valid.
        """
        if index < 0 or index >= self.list_len:
            # not valid index, ignore
            return
        if index == 0:
            # add to head
            self.delete_at_head()
            return
        if index == self.list_len - 1:
            # add to tail
            self.delete_at_tail()
            return

        if index <= self.list_len // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.list_len - 1 - index):
                current_node = current_node.prev

        current_node.prev.next = current_node.next
        current_node.next.prev = current_node.prev
        self.list_len -= 1


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
