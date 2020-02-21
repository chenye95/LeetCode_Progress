from random import random
class SkipListNode:
    def __init__(self, value, count=0, prev=None, next=None, down=None):
        self.value = value
        self.count = count
        self.prev = prev
        self.next = next
        self.down = down

class Skiplist:
    def __init__(self):
        self.header_value = -1
        self.lists = [[SkipListNode(value=self.header_value, count=1), 0]]
        self.split_threshold = 10
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
        stack = []
        while current_level >= 0:
            while current_node.next is not None and current_node.next.value < num:
                current_node = current_node.next
            if current_node.next is None or current_node.next.value > num:
                stack.append(current_node)
                current_node = current_node.down
                current_level = current_level - 1
            else:  # current_node.next == num and num exists in lists
                found_node = current_node.next
                while found_node:
                    found_node.count += 1
                    found_node = found_node.down
                return

        proceed = True
        next_level_added = None
        while proceed:
            current_level = len(stack) - 1
            current_level_prev = stack.pop()
            added_node = SkipListNode(value=num,
                                      count=1,
                                      down=next_level_added,
                                      prev=current_level_prev,
                                      next=current_level_prev.next)
            if current_level_prev.next is not None:
                current_level_prev.next.prev = added_node
            current_level_prev.next = added_node
            self.lists[current_level][1] += 1
            next_level_added = added_node
            proceed = random() < self.proceed_threshold and stack

        if self.lists[-1][1] > self.split_threshold:
            top_level_node = self.lists[-1][0]
            new_level_head = SkipListNode(value=self.header_value,
                                          count=1,
                                          down=top_level_node)
            new_level_node = new_level_head
            new_level_counter = 0
            while top_level_node.next is not None:
                top_level_node = top_level_node.next
                if random() < self.proceed_threshold:
                    tmp_node = SkipListNode(value=top_level_node.value,
                                            count=top_level_node.count,
                                            down=top_level_node,
                                            prev=new_level_node)
                    new_level_node.next = tmp_node
                    new_level_node = tmp_node
                    new_level_counter += 1
            self.lists.append([new_level_head, new_level_counter])


    def erase(self, num: int) -> bool:
        current_node = self.lists[-1][0]
        current_level = len(self.lists) - 1
        while current_level >= 0:
            while current_node.next is not None and current_node.next.value < num:
                current_node = current_node.next
            if current_node.next is None or current_node.next.value > num:
                current_node = current_node.down
                current_level = current_level - 1
            else:  # current_node.next == num and num exists in lists
                found_node = current_node.next
                while found_node:
                    found_node.count -= 1
                    if found_node.count == 0:
                        found_node.prev.next = found_node.next
                        if found_node.next is not None:
                            found_node.next.prev = found_node.prev
                    found_node = found_node.down
                return True
        return False

test = Skiplist()
N = 20
assert not test.search(N)
for i in range(N):
    test.add(i)
    test.add(i)
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