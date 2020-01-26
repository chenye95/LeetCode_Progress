"""
Given a data stream input of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of
disjoint intervals.
"""
from typing import List

class SummaryRange:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.intervals = []

    def addNum(self, val: int) -> None:
        n = len(self.intervals)
        l, r = 0, n - 1
        while l <= r:
            m = (l + r) // 2
            x = self.intervals[m]

            if x[0] <= val <= x[1]:
                return
            elif x[0] > val:
                r = m - 1
            else:
                l = m + 1

        self.intervals.insert(l, [val, val])
        if l < n and val + 1 == self.intervals[l + 1][0]:  # merge with next intervals
            self.intervals[l][1] = self.intervals[l + 1][1]
            del self.intervals[l + 1]
        if l > 0 and val - 1 == self.intervals[l - 1][1]:  # merge with previous intervals
            self.intervals[l][0] = self.intervals[l - 1][0]
            del self.intervals[l - 1]

    def getIntervals(self) -> List[List[int]]:
        return self.intervals

test_cases = [[(1, [[1, 1]]),
               (3, [[1, 1], [3, 3]]),
               (7, [[1, 1], [3, 3], [7, 7]]),
               (2, [[1, 3], [7, 7]]),
               (6, [[1, 3], [6, 7]])],
              [(1, [[1, 1]]),
               (2, [[1, 2]]),
               (3, [[1, 3]]),
               (3, [[1, 3]]),
               (5, [[1, 3], [5, 5]]),
               (4, [[1, 5]])]]
for case_i in test_cases:
    summary_i = SummaryRange()
    for add_j, expected_j in case_i:
        summary_i.addNum(add_j)
        assert summary_i.getIntervals() == expected_j