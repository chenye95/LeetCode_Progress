"""
Given an Iterator class interface with methods: next() and hasNext(), design and implement a PeekingIterator that
support the peek() operation -- it essentially peek() at the element that will be returned by the next call to next().
"""
from typing import List, Optional


class Iterator:
    def __init__(self, nums: List[int]):
        """
#       Initializes an iterator object to the beginning of a list
        """
        self.nums = nums
        self.pointer = 0

    def has_next(self) -> bool:
        """
        Returns true if the iteration has more elements
        """
        return self.pointer < len(self.nums)

    def next(self) -> Optional[int]:
        """
        Returns the next element in the iteration
        """
        if self.pointer < len(self.nums):
            self.pointer += 1
            return self.nums[self.pointer - 1]
        else:
            return None


class PeekingIterator:
    def __init__(self, iterator: Iterator):
        """
        Initialize your data structure here
        """
        self.iterator = iterator
        self.cache = None

    def peek(self) -> Optional[int]:
        """
        Returns the next element in the iteration without advancing the iterator.
        """
        if not self.iterator.has_next():
            return None
        if not self.cache:
            self.cache = self.iterator.next()
        return self.cache

    def next(self) -> Optional[int]:
        if self.cache:
            return_value, self.cache = self.cache, None
            return return_value
        else:
            return self.iterator.next()

    def has_next(self) -> bool:
        if self.cache or self.iterator.has_next():
            return True
        else:
            return False


test_peek_iterator = PeekingIterator(Iterator([1, 2, 3]))
assert test_peek_iterator.next() == 1
assert test_peek_iterator.has_next() is True
assert test_peek_iterator.peek() == 2
assert test_peek_iterator.has_next() is True
assert test_peek_iterator.next() == 2
assert test_peek_iterator.has_next() is True
assert test_peek_iterator.next() == 3
assert test_peek_iterator.has_next() is False
assert test_peek_iterator.peek() is None
assert test_peek_iterator.next() is None
