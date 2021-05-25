from math import log2, ceil
from typing import List, Callable, Union

RangeQueryValueType = Union[int, float]


class RangeQueryBase:
    def __init__(self, value_array: List[RangeQueryValueType],
                 merge_function: Callable[[RangeQueryValueType, RangeQueryValueType], RangeQueryValueType]):
        k = ceil(log2(len(value_array)))
        self.range_query_tree = [0] * (2 ** (k + 1) - 1)
        self.merge_fn = merge_function
        self.n = len(value_array)
        self._build_segment_tree(value_array, root_idx=0, array_left=0, array_right=len(value_array) - 1)

    def _build_segment_tree(self, value_array: List[RangeQueryValueType],
                            root_idx: int, array_left: int, array_right: int) -> None:
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
        :return: results of calling merge_function on value_array[left_inclusive:right_inclusive+1]
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
    def __init__(self, value_array: List[RangeQueryValueType],
                 merge_function: Callable[[RangeQueryValueType, RangeQueryValueType], RangeQueryValueType],
                 update_function: Callable[[RangeQueryValueType, RangeQueryValueType], RangeQueryValueType]):
        """
        Supports update at index, one at a time; used for small and frequent updates

        :param value_array: list of values to be stored in segment tree
        :param merge_function: merge_function used to compute Segment tree, e.g. sum, max
        :param update_function: update_function used to update segment tree, e.g. add, replace
            lambda old_value, to_new_value:
        """
        super(ActiveRangeQuery, self).__init__(value_array, merge_function)
        # self.update_function(old_value, update_value) -> new_value
        self.update_function = update_function

    def _query_segment_tree_helper(self, root_idx: int, tree_lo: int, tree_hi: int,
                                   array_left: int, array_right: int) -> RangeQueryValueType:
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

    def update_segment_tree(self, at_index: int, value: RangeQueryValueType) -> bool:
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
                                    at_index: int, value: RangeQueryValueType) -> None:
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
    def __init__(self, value_array: List[RangeQueryValueType],
                 merge_function: Callable[[RangeQueryValueType, RangeQueryValueType], RangeQueryValueType],
                 range_update_function: Callable[[RangeQueryValueType, int, int, RangeQueryValueType],
                                                 RangeQueryValueType]):
        """
        Supports update between range; used for infrequent large updates, e.g. add 1 to [array_left:array_right]
        Lazy update, only updates values when range_query is called; other wise store in lazy_changes

        :param value_array: list of values to be stored in segment tree
        :param merge_function: merge_function used to compute Segment tree, e.g. sum, max
        :param range_update_function: update_function used to update segment tree, e.g. add, replace;
            lambda old_value, lo, hi, to_new_value:
        """
        super(LazyQueryRange, self).__init__(value_array, merge_function)
        self.lazy_changes = [0] * len(self.range_query_tree)
        # self.range_update_function(old_value, array_left, array_right, value) -> new_value
        self.range_update_fn = range_update_function

    def range_update(self, left_inclusive: int, right_inclusive: int, value: RangeQueryValueType) -> bool:
        """
        :param left_inclusive: run range_update_function on value_array[left_inclusive: right_inclusive + 1]
        :param right_inclusive: run range_update_function on value_array[left_inclusive: right_inclusive + 1]
        :param value: run range_update_function with value
        :return: if 0 <= left_inclusive <= right_inclusive < self.n
        """
        if 0 <= left_inclusive <= right_inclusive < self.n:
            self._range_update_helper(tree_index=0, tree_lo=0, tree_hi=self.n - 1, array_left=left_inclusive,
                                      array_right=right_inclusive,
                                      value=value)
            return True
        else:
            return False

    def _range_update_helper(self, tree_index: int, tree_lo: int, tree_hi: int,
                             array_left: int, array_right: int, value: RangeQueryValueType) -> None:
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
                                   array_left: int, array_right: int) -> RangeQueryValueType:
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


# Sample Range Query Use Cases
class RangeQueryActiveSumIncrement(ActiveRangeQuery):
    def __init__(self, value_array: List[RangeQueryValueType]):
        from operator import add
        super().__init__(value_array, merge_function=add, update_function=add)


class RangeQueryActiveSumReplacement(ActiveRangeQuery):
    def __init__(self, value_array: List[RangeQueryValueType]):
        from operator import add
        super().__init__(value_array, merge_function=add,
                         update_function=lambda old_value, to_new_value: to_new_value)


class RangeQueryActiveMaxReplacement(ActiveRangeQuery):
    def __init__(self, value_array: List[RangeQueryValueType]):
        super().__init__(value_array, merge_function=max,
                         update_function=lambda old_value, to_new_value: to_new_value)


class RangeQueryLazySumIncrement(LazyQueryRange):
    def __init__(self, value_array: List[RangeQueryValueType]):
        from operator import add
        super().__init__(value_array, merge_function=add,
                         range_update_function=lambda old_value, lo, hi, inc: old_value + (hi - lo + 1) * inc)


class RangeQueryLazySumReplacement(LazyQueryRange):
    def __init__(self, value_array: List[RangeQueryValueType]):
        from operator import add
        super().__init__(value_array, merge_function=add,
                         range_update_function=lambda old_value, lo, hi, to_new_value: (hi - lo + 1) * to_new_value)


class RangeQueryLazyMaxReplacement(LazyQueryRange):
    def __init__(self, value_array: List[RangeQueryValueType]):
        super().__init__(value_array, merge_function=max,
                         range_update_function=lambda old_value, lo, hi, to_new_value: to_new_value)
