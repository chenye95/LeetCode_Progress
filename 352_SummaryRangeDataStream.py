"""
Given a data stream folder_structure of non-negative integers a1, a2, ..., an, ..., summarize the numbers seen so far as a list of
disjoint intervals.
"""
from typing import List


class SummaryRange:
    """
    Process a data stream of non-negative integers, and summarize the numbers seen so far as disjoint intervals
    """

    def __init__(self):
        self.intervals = []  # list of [interval_left, interval_right], inclusive both ends

    def add_number(self, val: int) -> None:
        """
        :param val: process a non negative integer from data stream
        """
        n = len(self.intervals)

        # Binary search on existing intervals
        left_interval, right_interval = 0, n - 1
        while left_interval <= right_interval:
            m = (left_interval + right_interval) // 2
            interval_m = self.intervals[m]

            if interval_m[0] <= val <= interval_m[1]:
                return
            elif interval_m[0] > val:
                right_interval = m - 1
            else:
                left_interval = m + 1

        self.intervals.insert(left_interval, [val, val])
        if left_interval < n and val + 1 == self.intervals[left_interval + 1][0]:  # merge with next intervals
            self.intervals[left_interval][1] = self.intervals[left_interval + 1][1]
            del self.intervals[left_interval + 1]
        if left_interval > 0 and val - 1 == self.intervals[left_interval - 1][1]:  # merge with previous intervals
            self.intervals[left_interval][0] = self.intervals[left_interval - 1][0]
            del self.intervals[left_interval - 1]

    def get_intervals(self) -> List[List[int]]:
        """
        :return: list of disjoint intervals that summarize the non-negative integers seen so far
        """
        return self.intervals


test_cases = [[(1, [[1, 1]]),
               (3, [[1, 1], [3, 3]]),
               (7, [[1, 1], [3, 3], [7, 7]]),
               (2, [[1, 3], [7, 7]]),
               (6, [[1, 3], [6, 7]]), ],
              [(1, [[1, 1]]),
               (2, [[1, 2]]),
               (3, [[1, 3]]),
               (3, [[1, 3]]),
               (5, [[1, 3], [5, 5]]),
               (4, [[1, 5]]), ], ]
for case_i in test_cases:
    summary_i = SummaryRange()
    for add_j, expected_j in case_i:
        summary_i.add_number(add_j)
        assert summary_i.get_intervals() == expected_j
