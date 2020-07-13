from math import log2, ceil
from typing import List, Callable


class RangeQueryBase:
    def __init__(self, value_array: List[int], merge_function: Callable[[int, int], int]):
        k = ceil(log2(len(value_array)))
        self.range_query_tree = [0] * (2 ** (k + 1) - 1)
        self.merge_fn = merge_function
        self.n = len(value_array)
        self._build_segment_tree(value_array, root_idx=0, array_left=0, array_right=len(value_array) - 1)

    def _build_segment_tree(self, value_array: List[int], root_idx: int, array_left: int, array_right: int) -> None:
        """
        Helper function to build the segment tree
        :param value_array: list of values to be stored in segment tree
        :param root_idx: computing segment_tree[root_idx] and its subtree
        :param array_left: currently processing value_array[array_left:array_right+1]
        :param array_right: currently processing value_array[array_left:array_right+1]
        """
        if array_left == array_right:
            self.range_query_tree[root_idx] = value_array[array_left]
        else:
            mid = (array_left + array_right) // 2
            self._build_segment_tree(value_array, 2 * root_idx + 1, array_left, mid)
            self._build_segment_tree(value_array, 2 * root_idx + 2, mid + 1, array_right)
            self.range_query_tree[root_idx] = self.merge_fn(self.range_query_tree[2 * root_idx + 1],
                                                            self.range_query_tree[2 * root_idx + 2])

    def query_segment_tree(self, left_inclusive: int, right_inclusive: int) -> int:
        """
        Entry point to query value_array[left_inclusive:right_inclusive+1]
        """
        if left_inclusive > right_inclusive:
            return 0
        return self._query_segment_tree_helper(root_idx=0, tree_lo=0, tree_hi=self.n - 1,
                                               array_left=left_inclusive, array_right=right_inclusive)

    def _query_segment_tree_helper(self, root_idx: int, tree_lo: int, tree_hi: int,
                                   array_left: int, array_right: int) -> int:
        """
        Helper function
        :param root_idx: currently processing segment_tree[root_idx]
        :param tree_lo: looking at segment_tree[tree_lo, tree_hi]
        :param tree_hi: looking at segment_tree[tree_lo, tree_hi]
        :param array_left: query value_array[array_left:array_right+1]
        :param array_right: query value_array[array_left:array_right+1]
        """
        pass


class ActiveRangeQuery(RangeQueryBase):
    def __init__(self, value_array: List[int],
                 merge_function: Callable[[int, int], int],
                 update_function: Callable[[int, int], int]):
        """
        Supports update at index, one at a time; used for small and frequent updates
        :param value_array: list of values to be stored in segment tree
        :param merge_function: merge_function used to compute Segment tree, e.g. sum, max
        :param update_function: update_function used to update segment tree, e.g. add, replace
        """
        super(ActiveRangeQuery, self).__init__(value_array, merge_function)
        # self.update_function(old_value, update_value) -> new_value
        self.update_function = update_function

    def _query_segment_tree_helper(self, root_idx: int, tree_lo: int, tree_hi: int,
                                   array_left: int, array_right: int) -> int:
        if tree_lo > array_right or tree_hi < array_left:
            # Segment Completely Outside of Range
            return 0
        if array_left <= tree_lo and array_right >= tree_hi:
            # Segment Completely Within the Range
            return self.range_query_tree[root_idx]

        mid = (tree_lo + tree_hi) // 2
        # Only needs one child of the segment tree
        if array_left > mid:
            return self._query_segment_tree_helper(2 * root_idx + 2, mid + 1, tree_hi, array_left, array_right)
        elif array_right <= mid:
            return self._query_segment_tree_helper(2 * root_idx + 1, tree_lo, mid, array_left, array_right)

        # needs to look at both child tree
        left_query_result = self._query_segment_tree_helper(2 * root_idx + 1, tree_lo, mid, array_left, mid)
        right_query_result = self._query_segment_tree_helper(2 * root_idx + 2, mid + 1, tree_hi, mid + 1, array_right)
        return self.merge_fn(left_query_result, right_query_result)

    def update_segment_tree(self, at_index: int, value: int) -> bool:
        """
        Updates at_index to value
        :return: if at_index is within range of value_list
        """
        if 0 <= at_index < self.n:
            self._update_segment_tree_helper(tree_index=0, tree_lo=0, tree_hi=self.n - 1,
                                             at_index=at_index, value=value)
            return True
        else:
            return False

    def _update_segment_tree_helper(self, tree_index: int, tree_lo: int, tree_hi: int,
                                    at_index: int, value: int) -> None:
        if tree_lo == tree_hi:
            self.range_query_tree[tree_index] = self.update_function(self.range_query_tree[tree_index], value)
            return

        mid = (tree_lo + tree_hi) // 2
        if at_index > mid:
            self._update_segment_tree_helper(2 * tree_index + 2, mid + 1, tree_hi, at_index, value)
        elif at_index <= mid:
            self._update_segment_tree_helper(2 * tree_index + 1, tree_lo, mid, at_index, value)

        self.range_query_tree[tree_index] = self.merge_fn(self.range_query_tree[2 * tree_index + 1],
                                                          self.range_query_tree[2 * tree_index + 2])


class LazyQueryRange(RangeQueryBase):
    def __init__(self, value_array: List[int],
                 merge_function: Callable[[int, int], int],
                 range_update_function: Callable[[int, int, int, int], int]):
        """
        Supports update between range; used for infrequent large updates, e.g. add 1 to [array_left:array_right]
        Lazy update, only updates values when range_query is called; other wise store in lazy_changes
        :param value_array: list of values to be stored in segment tree
        :param merge_function: merge_function used to compute Segment tree, e.g. sum, max
        :param range_update_function: update_function used to update segment tree, e.g. add, replace
        """
        super(LazyQueryRange, self).__init__(value_array, merge_function)
        self.lazy_changes = [0] * len(self.range_query_tree)
        # self.range_update_function(old_value, array_left, array_right, value) -> new_value
        self.range_update_fn = range_update_function

    def range_update(self, left_inclusive: int, right_inclusive: int, value: int) -> bool:
        if 0 <= left_inclusive <= right_inclusive < self.n:
            self._range_update_helper(tree_index=0, tree_lo=0, tree_hi=self.n - 1, array_left=left_inclusive,
                                      array_right=right_inclusive,
                                      value=value)
            return True
        else:
            return False

    def _range_update_helper(self, tree_index: int, tree_lo: int, tree_hi: int,
                             array_left: int, array_right: int, value: int) -> None:
        if self.lazy_changes[tree_index] != 0:
            # Settle Outstanding Changes
            self.range_query_tree[tree_index] = self.range_update_fn(self.range_query_tree[tree_index],
                                                                     tree_lo, tree_hi, self.lazy_changes[tree_index])
            if tree_lo != tree_hi:
                # Push down deferred changes to children node
                self.lazy_changes[2 * tree_index + 1] = \
                    self.merge_fn(self.lazy_changes[2 * tree_index + 1], self.lazy_changes[tree_index])
                self.lazy_changes[2 * tree_index + 2] = \
                    self.merge_fn(self.lazy_changes[2 * tree_index + 2], self.lazy_changes[tree_index])
            self.lazy_changes[tree_index] = 0

        if tree_lo > tree_hi or tree_lo > array_right or tree_hi < array_left:
            # current segment out of range
            return

        if array_left <= tree_lo and tree_hi <= array_right:
            self.range_query_tree[tree_index] = self.range_update_fn(self.range_query_tree[tree_index],
                                                                     tree_lo, tree_hi, value)
            if tree_lo != tree_hi:
                # Push down deferred changes to children node
                self.lazy_changes[2 * tree_index + 1] = self.merge_fn(self.lazy_changes[2 * tree_index + 1], value)
                self.lazy_changes[2 * tree_index + 2] = self.merge_fn(self.lazy_changes[2 * tree_index + 2], value)
            return

        mid = (tree_lo + tree_hi) // 2
        self._range_update_helper(2 * tree_index + 1, tree_lo, mid, array_left, array_right, value)
        self._range_update_helper(2 * tree_index + 2, mid + 1, tree_hi, array_left, array_right, value)
        self.range_query_tree[tree_index] = self.merge_fn(self.range_query_tree[2 * tree_index + 1],
                                                          self.range_query_tree[2 * tree_index + 2])

    def _query_segment_tree_helper(self, root_idx: int, tree_lo: int, tree_hi: int,
                                   array_left: int, array_right: int) -> int:
        if tree_lo > tree_hi or tree_lo > array_right or tree_hi < array_left:
            # current segment out of range
            return 0

        if self.lazy_changes[root_idx] != 0:
            # Settle Outstanding Changes
            self.range_query_tree[root_idx] = self.range_update_fn(self.range_query_tree[root_idx],
                                                                   tree_lo, tree_hi, self.lazy_changes[root_idx])
            if tree_lo != tree_hi:
                # Push down deferred changes to children node
                self.lazy_changes[2 * root_idx + 1] = \
                    self.merge_fn(self.lazy_changes[2 * root_idx + 1], self.lazy_changes[root_idx])
                self.lazy_changes[2 * root_idx + 2] = \
                    self.merge_fn(self.lazy_changes[2 * root_idx + 2], self.lazy_changes[root_idx])
            self.lazy_changes[root_idx] = 0

        if array_left <= tree_lo and tree_hi <= array_right:
            return self.range_query_tree[root_idx]

        mid = (tree_lo + tree_hi) // 2
        if array_left > mid:
            return self._query_segment_tree_helper(2 * root_idx + 2, mid + 1, tree_hi, array_left, array_right)
        elif array_right <= mid:
            return self._query_segment_tree_helper(2 * root_idx + 1, tree_lo, mid, array_left, array_right)

        left_query = self._query_segment_tree_helper(2 * root_idx + 1, tree_lo, mid, array_left, array_right)
        right_query = self._query_segment_tree_helper(2 * root_idx + 2, mid + 1, tree_hi, array_left, array_right)

        return self.merge_fn(left_query, right_query)
