from math import log2, ceil
from typing import List, Callable


class RangeQueryBase:
    def __init__(self, arr: List[int], merge_function: Callable[[int, int], int]):
        k = ceil(log2(len(arr)))
        self.range_query_tree = [0] * (2 ** (k + 1) - 1)
        self.merge_fn = merge_function
        self.n = len(arr)
        self.build_segment_tree(arr, tree_index=0, lo=0, hi=len(arr) - 1)

    def build_segment_tree(self, arr: List[int], tree_index: int, lo: int, hi: int):
        if lo == hi:
            self.range_query_tree[tree_index] = arr[lo]
        else:
            mid = (lo + hi) // 2
            self.build_segment_tree(arr, 2 * tree_index + 1, lo, mid)
            self.build_segment_tree(arr, 2 * tree_index + 2, mid + 1, hi)
            self.range_query_tree[tree_index] = self.merge_fn(self.range_query_tree[2 * tree_index + 1],
                                                              self.range_query_tree[2 * tree_index + 2])

    def query_segment_tree(self, left_inclusive: int, right_inclusive: int):
        if left_inclusive > right_inclusive:
            return 0
        return self.query_segment_tree_helper(tree_index=0, lo=0, hi=self.n - 1, i=left_inclusive, j=right_inclusive)

    def query_segment_tree_helper(self, tree_index: int, lo: int, hi: int, i: int, j: int):
        pass


class ActiveRangeQuery(RangeQueryBase):
    def __init__(self, arr: List[int],
                 merge_function: Callable[[int, int], int],
                 update_function: Callable[[int, int], int]):
        super(ActiveRangeQuery, self).__init__(arr, merge_function)
        # self.update_function(old_value, update_value) -> new_value
        self.update_function = update_function

    def query_segment_tree_helper(self, tree_index: int, lo: int, hi: int, i: int, j: int):
        if lo > j or hi < i:
            # Segment Completely Outside of Range
            return 0
        if i <= lo and j >= hi:
            # Segment Completely Within the Range
            return self.range_query_tree[tree_index]

        mid = (lo + hi) // 2
        if i > mid:
            return self.query_segment_tree_helper(2 * tree_index + 2, mid + 1, hi, i, j)
        elif j <= mid:
            return self.query_segment_tree_helper(2 * tree_index + 1, lo, mid, i, j)

        left_query_result = self.query_segment_tree_helper(2 * tree_index + 1, lo, mid, i, mid)
        right_query_result = self.query_segment_tree_helper(2 * tree_index + 2, mid + 1, hi, mid + 1, j)
        return self.merge_fn(left_query_result, right_query_result)

    def update_segment_tree(self, at_index: int, value: int) -> bool:
        if 0 <= at_index < self.n:
            self.update_segment_tree_helper(tree_index=0, lo=0, hi=self.n - 1, at_index=at_index, value=value)
            return True
        else:
            return False

    def update_segment_tree_helper(self, tree_index: int, lo: int, hi: int, at_index: int, value: int):
        if lo == hi:
            self.range_query_tree[tree_index] = self.update_function(self.range_query_tree[tree_index], value)
            return

        mid = (lo + hi) // 2
        if at_index > mid:
            self.update_segment_tree_helper(2 * tree_index + 2, mid + 1, hi, at_index, value)
        elif at_index <= mid:
            self.update_segment_tree_helper(2 * tree_index + 1, lo, mid, at_index, value)

        self.range_query_tree[tree_index] = self.merge_fn(self.range_query_tree[2 * tree_index + 1],
                                                          self.range_query_tree[2 * tree_index + 2])


class LazyQueryRange(RangeQueryBase):
    """
    :param range_update_function self.range_update_function(old_value, lo, hi, value) -> new_value
    """

    def __init__(self, arr: List[int],
                 merge_function: Callable[[int, int], int],
                 range_update_function: Callable[[int, int, int, int], int]):
        super(LazyQueryRange, self).__init__(arr, merge_function)
        self.lazy_changes = [0] * len(self.range_query_tree)
        # self.range_update_function(old_value, lo, hi, value) -> new_value
        self.range_update_fn = range_update_function

    def range_update(self, left_inclusive: int, right_inclusive: int, value: int) -> bool:
        if 0 <= left_inclusive <= right_inclusive < self.n:
            self.range_update_helper(tree_index=0, lo=0, hi=self.n - 1, i=left_inclusive, j=right_inclusive,
                                     value=value)
            return True
        else:
            return False

    def range_update_helper(self, tree_index: int, lo: int, hi: int, i: int, j: int, value: int):
        if self.lazy_changes[tree_index] != 0:
            # Settle Outstanding Changes
            self.range_query_tree[tree_index] = self.range_update_fn(self.range_query_tree[tree_index],
                                                                     lo, hi, self.lazy_changes[tree_index])
            if lo != hi:
                # Push down deferred changes to children node
                self.lazy_changes[2 * tree_index + 1] = \
                    self.merge_fn(self.lazy_changes[2 * tree_index + 1], self.lazy_changes[tree_index])
                self.lazy_changes[2 * tree_index + 2] = \
                    self.merge_fn(self.lazy_changes[2 * tree_index + 2], self.lazy_changes[tree_index])
            self.lazy_changes[tree_index] = 0

        if lo > hi or lo > j or hi < i:
            # current segment out of range
            return

        if i <= lo and hi <= j:
            self.range_query_tree[tree_index] = self.range_update_fn(self.range_query_tree[tree_index],
                                                                     lo, hi, value)
            if lo != hi:
                # Push down deferred changes to children node
                self.lazy_changes[2 * tree_index + 1] = self.merge_fn(self.lazy_changes[2 * tree_index + 1], value)
                self.lazy_changes[2 * tree_index + 2] = self.merge_fn(self.lazy_changes[2 * tree_index + 2], value)
            return

        mid = (lo + hi) // 2
        self.range_update_helper(2 * tree_index + 1, lo, mid, i, j, value)
        self.range_update_helper(2 * tree_index + 2, mid + 1, hi, i, j, value)
        self.range_query_tree[tree_index] = self.merge_fn(self.range_query_tree[2 * tree_index + 1],
                                                          self.range_query_tree[2 * tree_index + 2])

    def query_segment_tree_helper(self, tree_index: int, lo: int, hi: int, i: int, j: int):
        if lo > hi or lo > j or hi < i:
            # current segment out of range
            return 0

        if self.lazy_changes[tree_index] != 0:
            # Settle Outstanding Changes
            self.range_query_tree[tree_index] = self.range_update_fn(self.range_query_tree[tree_index],
                                                                     lo, hi, self.lazy_changes[tree_index])
            if lo != hi:
                # Push down deferred changes to children node
                self.lazy_changes[2 * tree_index + 1] = \
                    self.merge_fn(self.lazy_changes[2 * tree_index + 1], self.lazy_changes[tree_index])
                self.lazy_changes[2 * tree_index + 2] = \
                    self.merge_fn(self.lazy_changes[2 * tree_index + 2], self.lazy_changes[tree_index])
            self.lazy_changes[tree_index] = 0

        if i <= lo and hi <= j:
            return self.range_query_tree[tree_index]

        mid = (lo + hi) // 2
        if i > mid:
            return self.query_segment_tree_helper(2 * tree_index + 2, mid + 1, hi, i, j)
        elif j <= mid:
            return self.query_segment_tree_helper(2 * tree_index + 1, lo, mid, i, j)

        left_query = self.query_segment_tree_helper(2 * tree_index + 1, lo, mid, i, j)
        right_query = self.query_segment_tree_helper(2 * tree_index + 2, mid + 1, hi, i, j)

        return self.merge_fn(left_query, right_query)
