"""
The circular queue is a linear data structure in which the operations are performed based on FIFO (First In First Out)
principle and the last position is connected back to the first position to make a circle. It is also called "Ring
Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue. In a normal
queue, once the queue becomes full, we cannot insert the next element even if there is a space in front of the queue.
But using the circular queue, we can use the space to store new values.
"""
from typing import List, Any


class RingBuffer:
    # Interface class

    NONE_VALUE = -1

    def __init__(self, k: int):
        """
        :param k: initializes the object with the size of the queue to be k
        """
        self.queue_capacity = k

    def enqueue(self, value: Any) -> bool:
        """
        Inserts an element into the circular queue.

        :return: whether the operation is successful
        """
        pass

    def dequeue(self) -> bool:
        """
        Delete an element from the circular queue.

        :return: whether the operation is
        """
        pass

    def front(self) -> Any:
        """
        Operation does not pop the first element from the queue

        :return: the first item from the queue. return NONE_VALUE if queue is empty
        """
        pass

    def rear(self) -> Any:
        """
        Operation does not pop the last element from the queue

        :return: the last item from the queue. return NONE_VALUE if queue is empty
        """
        pass

    def is_empty(self) -> bool:
        """
        :return: whether the circular queue is empty
        """
        pass

    def is_full(self) -> bool:
        """
        :return: whether the circular queue is full.
        """
        pass


class RingBufferList(RingBuffer):
    def __init__(self, k: int):
        super().__init__(k)
        self.queue_list: List[Any] = []

    def enqueue(self, value: Any) -> bool:
        if len(self.queue_list) >= self.queue_capacity:
            return False
        else:
            self.queue_list.append(value)
            return True

    def dequeue(self) -> bool:
        if not self.queue_list:
            return False
        else:
            self.queue_list.pop(0)
            return True

    def front(self) -> Any:
        return self.queue_list[0] if self.queue_list else self.NONE_VALUE

    def rear(self) -> Any:
        return self.queue_list[-1] if self.queue_list else self.NONE_VALUE

    def is_empty(self) -> bool:
        return not self.queue_list

    def is_full(self) -> bool:
        return len(self.queue_list) >= self.queue_capacity


class RingBufferTwoPointer(RingBuffer):
    def __init__(self, k: int):
        super().__init__(k)
        self.queue_list: List[Any] = [self.NONE_VALUE] * k
        self.queue_head: int = 0
        self.queue_tail: int = -1
        self.queue_count: int = 0

    def enqueue(self, value: Any) -> bool:
        if self.queue_count >= self.queue_capacity:
            return False
        else:
            self.queue_tail = (self.queue_tail + 1) % self.queue_capacity
            self.queue_list[self.queue_tail] = value
            self.queue_count += 1
            return True

    def dequeue(self) -> bool:
        if self.queue_count == 0:
            return False
        else:
            self.queue_head = (self.queue_head + 1) % self.queue_capacity
            self.queue_count -= 1
            return True

    def front(self) -> Any:
        return self.NONE_VALUE if self.queue_count == 0 else self.queue_list[self.queue_head]

    def rear(self) -> Any:
        return self.NONE_VALUE if self.queue_count == 0 else self.queue_list[self.queue_tail]

    def is_empty(self) -> bool:
        return self.queue_count == 0

    def is_full(self) -> bool:
        return self.queue_count >= self.queue_capacity
