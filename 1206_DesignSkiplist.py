"""
Design a Skiplist without using any built-in libraries.

A Skiplist is a data structure that takes O(log(n)) time to add, erase and search. Comparing with treap and red-black
tree which has the same function and performance, the code length of Skiplist can be comparatively short and the idea
behind Skiplists are just simple linked lists.

- 0 <= num, target <= 20000
- At most 50000 calls will be made to search, add, and erase.
"""
from random import random


class SkipListNode:
    def __init__(self, value=-1, count=1, next=None, down=None):
        self.value = value
        self.count = count
        self.next = next
        self.down = down

class Skiplist:
    def __init__(self, initial_levels=4):
        self.lists = [[SkipListNode(), 0] for i in range(initial_levels)]
        for current_head, next_head in zip(self.lists[:-1], self.lists[1:]):
            next_head[0].down = current_head[0]
        self.split_threshold = 50
        self.proceed_threshold = .12

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
            if current_node.next is None or current_node.next.value > num:
                stack[len(self.lists) - 1 - current_level] = current_node # FIFO
                current_node = current_node.down
                current_level -= 1
            elif current_node.next.value == num:
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
            current_level_prev = stack.pop()
            current_level_prev.next = SkipListNode(value=num,
                                                   next=current_level_prev.next,
                                                   down=prev_level_added,)
            prev_level_added = current_level_prev.next
            self.lists[current_level][1] += 1
            proceed = random() < self.proceed_threshold and stack
            current_level += 1

        if self.lists[-1][1] > self.split_threshold:
            self.add_new_level()

    def add_new_level(self) -> None:
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

    def erase(self, num: int) -> bool:
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


from datetime import datetime
from random import randint


def test_case_1(N=10000):
    previous_time_stamp = datetime.now()
    test = Skiplist()
    assert not test.search(N)
    print("Test Add Operations")
    for i in range(N):
        test.add(i)
        test.add(i)
        # print("Added %d" % i)
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Test Search Operations")
    for i in range(N):
        assert test.search(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Test First Erase Operations")
    for i in range(N):
        assert test.erase(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Confirm First Erase Operations")
    for i in range(N):
        assert test.search(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Test Second Erase Operations")
    for i in range(N):
        assert test.erase(i)
        assert not test.search(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    print("Confirm Second Erase Operations")
    for i in range(N):
        assert not test.search(i)
    previous_time_stamp = current_time_stamp
    current_time_stamp = datetime.now()
    print("\tDuration", current_time_stamp - previous_time_stamp)
    assert not test.search(N)


def test_case_2(N=100000):
    test_class = Skiplist()
    action_list = [0, 0, 0]

    start_time = datetime.now()
    for _ in range(N):
        take_step, param = randint(0, 2), randint(0, 1000)
        if take_step == 0:
            test_class.add(param)
        elif take_step == 1:
            test_class.erase(param)
        else:
            test_class.search(param)
        action_list[take_step] += 1
    print("Test 2: %d Actions Total Duration" % N, datetime.now() - start_time)
    print(action_list)


if __name__ == '__main__':
    test_case_1()
    test_case_2()
