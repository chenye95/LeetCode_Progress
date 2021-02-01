"""
Design a SkipList without using any built-in libraries.

A SkipList is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black
tree which has the same function and performance, the code length of SkipList can be comparatively short and the idea
behind Skip Lists are just simple linked lists.

- 0 <= value, target <= 20000
- At most 50000 calls will be made to search, add, and erase.
"""
from __future__ import annotations

from random import random
from typing import Union, List, Optional

SkipList_Value_Type = Union[int, chr, str]


class SkipListNode:
    def __init__(self, value: SkipList_Value_Type = -1, count: int = 1,
                 next: SkipListNode = None,
                 down: SkipListNode = None):
        """
        Compress duplicate nodes under one nodes and keep track of duplicate count
        :param value: value of SkipListNode, needs to be comparable
        :param count: duplicate count
        :param next: SkipListNode: point to next neighbor in the current level
        :param down: SkipListNode: point to the reference node in the next level
        """
        self.value = value
        self.count = count
        self.next = next
        self.down = down


class SkipList:
    """
    See 1206 Design Skip List
    """

    def __init__(self, initial_levels: int = 4, split_threshold: int = 50, proceed_threshold: float = .12):
        """
        :param initial_levels: upon creation, create a SkipList with initial_levels levels
        :param split_threshold: create another level if the bottom level reaches the split_threshold
        :param proceed_threshold: with probability proceed_threshold, a reference node will be created in the next level
        """
        self.lists = [[SkipListNode(), 0] for i in range(initial_levels)]
        for current_head, next_head in zip(self.lists[:-1], self.lists[1:]):
            next_head[0].down = current_head[0]
        self.split_threshold = split_threshold
        self.proceed_threshold = proceed_threshold

    def search(self, target: SkipList_Value_Type) -> bool:
        """
        :return: whether target exists in SkipList
        """
        current_node = self.lists[-1][0]
        current_level = len(self.lists) - 1
        while current_level >= 0:
            while current_node.next is not None and current_node.next.value < target:
                current_node = current_node.next
            if current_node.next is None or current_node.next.value > target:
                current_node = current_node.down
                current_level = current_level - 1
            else:
                return True
        return False

    def add(self, value: SkipList_Value_Type) -> None:
        """
        if value exists in SkipList, increase count by 1
        if doesn't exist yet, create a node for value
        """
        current_node = self.lists[-1][0]
        current_level = len(self.lists) - 1
        stack: List[Optional[SkipListNode]] = [None] * len(self.lists)
        while current_node:
            if current_node.next is None or current_node.next.value > value:
                stack[len(self.lists) - 1 - current_level] = current_node  # FIFO
                current_node = current_node.down
                current_level -= 1
            elif current_node.next.value == value:
                # Existing Values Update Count
                current_node.next.count += 1
                return
            else:
                current_node = current_node.next

        # New Values Add Node
        proceed = True
        prev_level_added = None
        current_level = 0
        while proceed:
            current_level_prev: SkipListNode = stack.pop()
            current_level_prev.next = SkipListNode(value=value,
                                                   next=current_level_prev.next,
                                                   down=prev_level_added, )
            prev_level_added = current_level_prev.next
            self.lists[current_level][1] += 1
            proceed = random() < self.proceed_threshold and stack
            current_level += 1

        if self.lists[-1][1] > self.split_threshold:
            self.add_new_level()

    def add_new_level(self) -> None:
        """
        Helper function to create a new level for faster lookup
        """
        top_level_node = self.lists[-1][0]
        new_level_head = SkipListNode(down=top_level_node)
        new_level_node = new_level_head
        new_level_counter = 0
        while top_level_node.next is not None:
            top_level_node = top_level_node.next
            if random() < self.proceed_threshold:
                new_level_node.next = SkipListNode(value=top_level_node.value,
                                                   count=top_level_node.count,
                                                   down=top_level_node)
                new_level_node = new_level_node.next
                new_level_counter += 1
        self.lists.append([new_level_head, new_level_counter])

    def erase(self, num: SkipList_Value_Type) -> bool:
        """
        if value exists in SkipList, decreases count by 1
        if drops to zero, remove the node
        """
        erased = remove_node = False
        current_node, current_level = self.lists[-1][0], len(self.lists) - 1
        while current_node is not None:
            if current_node.next is None or current_node.next.value > num:
                current_node = current_node.down
                current_level -= 1
            elif current_node.next.value == num:
                if not erased:
                    current_node.next.count -= 1
                    remove_node = current_node.next.count == 0
                    erased = True
                if remove_node:
                    current_node.next = current_node.next.next
                    self.lists[current_level][1] -= 1
                current_node = current_node.down
                current_level -= 1
            else:
                current_node = current_node.next
        return erased
