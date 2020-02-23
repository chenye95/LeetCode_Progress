"""
Design a Skiplist without using any built-in libraries.

A Skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black
tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea
behind Skiplists are just simple linked lists.
"""
from random import random

class SkipListNode:
    def __init__(self, value=-1, count=0, next=None, down=None):
        self.value = value
        self.count = count
        self.next = next
        self.down = down

class Skiplist:
    def __init__(self, initial_levels=4):
        self.lists = [[SkipListNode(count=1), 0] for i in range(initial_levels)]
        for current_head, next_head in zip(self.lists[:-1], self.lists[1:]):
            next_head[0].down = current_head[0]
        self.split_threshold = 20
        self.proceed_threshold = 0.5

    def search(self, target: int) -> bool:
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


    def add(self, num: int) -> None:
        current_node = self.lists[-1][0]
        current_level = len(self.lists) - 1
        stack = [None] * len(self.lists)
        while current_node:
            if current_node.next is None or current_node.value < num < current_node.next.value:
                if current_node is None:
                    print("weird")
                stack[len(self.lists) - 1 - current_level] = current_node
                current_node = current_node.down
                current_level -= 1
            elif current_node.next.value == num:
                # Existing Values Update Count
                found_node = current_node.next
                while found_node:
                    found_node.count += 1
                    found_node = found_node.down
                return
            else:
                current_node = current_node.next

        # New Values Add Node
        proceed = True
        prev_level_added = None
        current_level = 0
        while proceed:
            current_level_prev = stack.pop()
            added_node = SkipListNode(value=num,
                                      count=1,
                                      next=current_level_prev.next,
                                      down=prev_level_added)
            current_level_prev.next = added_node
            self.lists[current_level][1] += 1
            prev_level_added = added_node
            proceed = random() < self.proceed_threshold and stack
            current_level += 1

        if self.lists[-1][1] > self.split_threshold:
            self.add_new_level()

    def add_new_level(self) -> None:
        top_level_node = self.lists[-1][0]
        new_level_head = SkipListNode(count=1,
                                      down=top_level_node)
        new_level_node = new_level_head
        new_level_counter = 0
        while top_level_node.next is not None:
            top_level_node = top_level_node.next
            if random() < self.proceed_threshold:
                tmp_node = SkipListNode(value=top_level_node.value,
                                        count=top_level_node.count,
                                        down=top_level_node)
                new_level_node.next = tmp_node
                new_level_node = tmp_node
                new_level_counter += 1
        self.lists.append([new_level_head, new_level_counter])

    def erase(self, num: int) -> bool:
        erased, current_node, current_level = False, self.lists[-1][0], len(self.lists) - 1
        while current_node is not None:
            if current_node.next is None or current_node.value < num < current_node.next.value:
                current_node = current_node.down
                current_level -= 1
            elif current_node.next.value == num:
                erased = True
                current_node.next.count -= 1
                if current_node.next.count == 0:
                    current_node.next = current_node.next.next
                    self.lists[current_level][1] -= 1
                current_node = current_node.down
                current_level -= 1
            else:
                current_node = current_node.next
        return erased

test = Skiplist()
N = 50000
assert not test.search(N)
for i in range(N):
    test.add(i)
    test.add(i)
    # print("Added %d" % i)
for i in range(N):
    assert test.search(i)
for i in range(N):
    assert test.erase(i)
for i in range(N):
    assert test.search(i)
for i in range(N):
    assert test.erase(i)
    assert not test.search(i)
for i in range(N):
    assert not test.search(i)
assert not test.search(N)