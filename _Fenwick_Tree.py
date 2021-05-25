from math import log2
from typing import List, Union, Optional


class FenwickTree:
    """
    Used for storing frequencies and manipulating cumulative frequency table
    As known as Binary Indexed Tree, for more info please refer to
    https://www.topcoder.com/community/competitive-programming/tutorials/binary-indexed-trees/
    """
    NUMBER_TYPE = Union[int, float]

    def __init__(self, init_frequencies=List[NUMBER_TYPE]):
        """
        :param init_frequencies: initial frequencies to be stored in the BIT
        """
        self.bit_array_len = len(init_frequencies) + 1
        # bit_array has a leading zero from index computation purposes
        # need to shift user index +1 in code
        self.bit_array = [0] * self.bit_array_len
        for i, num_i in enumerate(init_frequencies):
            self.__update(i + 1, num_i)

    def range_sum(self, start_idx: int = 0, end_idx: int = -1) -> NUMBER_TYPE:
        """
        :param start_idx: start of range sum query, inclusive
        :param end_idx: end of range sum query, inclusive; set to -1 if want to sum to the end
        :return: inclusive range sum between start_idx and end_idx
        """
        # tree_idx = user_idx + 1 given the leading zero in bit_array
        end_sum = self.__read(end_idx + 1) if end_idx >= 0 else self.__read(self.bit_array_len - 1)
        start_sum = self.__read(start_idx) if start_idx > 0 else 0
        return end_sum - start_sum

    def __read(self, tree_idx: int) -> NUMBER_TYPE:
        """
        Helper function

        :param tree_idx: wants to calculate cumulative sum from the start till tree_idx
        :return: cumulative sum from the start till tree_idx
        """
        assert tree_idx < self.bit_array_len, "Out of Bound, this Binary Indexed Tree only contains %d elements" % \
                                              (self.bit_array_len - 1)
        cumulative_sum = 0
        while tree_idx > 0:
            cumulative_sum += self.bit_array[tree_idx]
            tree_idx -= (tree_idx & -tree_idx)
        return cumulative_sum

    def __update(self, tree_idx: int, val: NUMBER_TYPE) -> None:
        """
        Helper function

        :param tree_idx: Update frequency at tree_idx position to val
        :param val: Update frequency at tree_idx position to val
        """
        while tree_idx < self.bit_array_len:
            self.bit_array[tree_idx] += val
            tree_idx += (tree_idx & -tree_idx)

    def at_idx_i(self, idx: int) -> NUMBER_TYPE:
        """
        :return: return frequency of index idx
        """
        tree_idx = idx + 1
        assert tree_idx < self.bit_array_len, "Out of Bound, this Binary Indexed Tree only contains %d elements" % \
                                              (self.bit_array_len - 1)
        res = self.bit_array[tree_idx]
        z = tree_idx - (tree_idx & -tree_idx)
        y = tree_idx - 1
        while y != z:
            res -= self.bit_array[y]
            y -= (y & -y)
        return res

    def scale(self, c: NUMBER_TYPE) -> None:
        """
        :param c: scale all frequencies by a factor of 1/c
        """
        for i in range(self.bit_array_len):
            self.bit_array[i] /= float(c)

    def increment_at_i(self, idx: int, by_val: NUMBER_TYPE) -> None:
        """
        :param idx: increment frequency at idx position +by_val
        :param by_val: increment frequency at idx position +by_val
        """
        tree_idx = idx + 1
        while tree_idx < self.bit_array_len:
            self.bit_array[tree_idx] += by_val
            tree_idx += (tree_idx & -tree_idx)

    def set_at_i(self, i: int, old_val: Optional[NUMBER_TYPE] = None, new_val: NUMBER_TYPE = 0) -> None:
        """
        :param i: Replace frequency at idx position by new_val
        :param old_val: Old frequency at idx; can use None to stand in for old_val
        :param new_val: Replace frequency at idx position by new_val
        """
        if old_val is not None:
            self.increment_at_i(i, new_val - old_val)
        else:
            self.increment_at_i(i, new_val - self.at_idx_i(i))

    def find_cumulative_sum(self, cumulative_sum: NUMBER_TYPE) -> int:
        """
        Only use this function when all elements in the init_frequencies is non-negative

        :param cumulative_sum: target cumulative sum (from start) to find
        :return: the largest index till which the cumulative sum from beginning equals to target, -1 if not found
        """
        tree_idx = 0
        bit_max = 1 << int(log2(self.bit_array_len - 1) + 1)
        while bit_max > 0:
            bit_max >>= 1
            temp_idx = tree_idx + bit_max
            if temp_idx >= self.bit_array_len:
                continue
            if cumulative_sum >= self.bit_array[temp_idx]:
                tree_idx = temp_idx
                cumulative_sum -= self.bit_array[temp_idx]

        return tree_idx if cumulative_sum == 0 else -1
