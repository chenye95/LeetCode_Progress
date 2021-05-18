"""
The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value and
 the median is the mean of the two middle values.
- For example, for arr = [2,3,4], the median is 3.
- For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.

Implement the MedianFinder class:
- MedianFinder() initializes the MedianFinder object.
- void addNum(int num) adds the integer num from the data stream to the data structure.
- double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be
 accepted.
"""
import heapq


class MedianFinder:
    def __init__(self):
        self.count = 0
        self.smaller_half = []  # max heap
        self.larger_half = []  # min heap

    def add_number(self, num: int) -> None:
        """
        :param num: ingest num into data stream
        """
        if self.larger_half and num < self.larger_half[0]:
            heapq.heappush(self.smaller_half, -num)
            if self.count % 2 == 0:
                heapq.heappush(self.larger_half, -heapq.heappop(self.smaller_half))
        else:
            heapq.heappush(self.larger_half, num)
            if self.count % 2:
                heapq.heappush(self.smaller_half, -heapq.heappop(self.larger_half))
        self.count += 1

    def find_median(self) -> float:
        """
        :return: median of all numbers that have been added to the stream before
        """
        if self.count % 2:
            return self.larger_half[0]
        else:
            return (self.larger_half[0] - self.smaller_half[0]) / 2.0


test_median_finder = MedianFinder()
test_median_finder.add_number(1)
assert test_median_finder.find_median() == 1
test_median_finder.add_number(2)
assert test_median_finder.find_median() == 1.5
test_median_finder.add_number(3)
assert test_median_finder.find_median() == 2

test_median_finder = MedianFinder()
test_median_finder.add_number(-1)
assert test_median_finder.find_median() == -1
test_median_finder.add_number(-2)
assert test_median_finder.find_median() == -1.5
test_median_finder.add_number(-3)
assert test_median_finder.find_median() == -2
test_median_finder.add_number(-4)
assert test_median_finder.find_median() == -2.5
test_median_finder.add_number(-5)
assert test_median_finder.find_median() == -3
