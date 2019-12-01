from typing import List, Union
from math import log2

class FenwickTree:
    """
    As known as Binary Indexed Tree, for more info please refer to
    https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/
    """
    Numbers = Union[int, float]
    def __init__(self, num_array = List[Numbers]):
        self.bit_array_len = len(num_array) + 1
        self.bit_array = [0] * (self.bit_array_len)
        for i in range(len(num_array)):
            self.__update(i + 1, num_array[i])


    def range_sum(self, start_idx: int = 0,  end_idx: int = -1) -> Numbers:
        end_sum = self.__read(end_idx + 1) if end_idx >= 0 else self.__read(self.bit_array_len - 1)
        start_sum = self.__read(start_idx) if start_idx > 0 else 0
        return end_sum - start_sum

    def __read(self, tree_idx: int) -> Numbers:
        assert tree_idx < self.bit_array_len, "Out of Bound, this Binary Indexed Tree only contains %d elements" % \
                                              (self.bit_array_len - 1)
        sum = 0
        while tree_idx > 0:
            sum += self.bit_array[tree_idx]
            tree_idx -= (tree_idx & -tree_idx)
        return sum

    def __update(self, tree_idx: int, val: Numbers) -> None:
        while tree_idx < self.bit_array_len:
            self.bit_array[tree_idx] += val
            tree_idx += (tree_idx & -tree_idx)

    def at_idx_i(self, i: int) -> Numbers:
        tree_idx = i + 1
        assert tree_idx < self.bit_array_len, "Out of Bound, this Binary Indexed Tree only contains %d elements" % \
                                              (self.bit_array_len - 1)
        res = self.bit_array[tree_idx]
        z = tree_idx - (tree_idx & -tree_idx)
        y = tree_idx - 1
        while y != z:
            res -= self.bit_array[y]
            y -= (y & -y)
        return res

    def scale(self, c: Numbers):
        for i in range(self.bit_array_len):
            self.bit_array[i] /= float(c)

    def increment_at_i(self, i: int, by_val: Numbers):
        tree_idx = i + 1
        while tree_idx < self.bit_array_len:
            self.bit_array[tree_idx] += by_val
            tree_idx += (tree_idx & -tree_idx)

    def set_at_i(self, i: int, old_val: Numbers, new_val: Numbers):
        self.increment_at_i(i, new_val - old_val)


    def find_cumulative_sum(self, cumulative_sum: Numbers):
        """
        Only use this function when all elements in the num_array is non-negative
        :param cumulative_sum: target cumulative sum (from start) to find
        :return: the largest index till which the cumulative sum from beginning equals to target
        """
        tree_idx = 0
        bit_max = 1 << int(log2(self.bit_array_len-1) + 1)
        while bit_max > 0:
            bit_max >>= 1
            temp_idx = tree_idx + bit_max
            if temp_idx >= self.bit_array_len:
                continue
            if cumulative_sum >= self.bit_array[temp_idx]:
                tree_idx = temp_idx
                cumulative_sum -= self.bit_array[temp_idx]

        return tree_idx if cumulative_sum == 0 else -1