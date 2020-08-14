"""
Design an Iterator class, which has:

A constructor that takes a string characters of sorted distinct lowercase English letters and a number combinationLength
 as arguments.
A function next() that returns the next combination of length combinationLength in lexicographical order.
A function has_next() that returns True if and only if there exists a next combination.
"""


class CombinationIterator:
    """
    Implement with bit manipulation, instead of itertools.combinations
    """

    def __init__(self, characters: str, combination_length: int):
        self.characters = characters
        # initialize current_bit_map to 11..100..0
        self.current_bit_map = list(range(combination_length))
        # end_state_bit_map is 00..011..1
        self.end_state_bit_map = list(range(len(characters) - combination_length, len(characters)))
        self.next_flag = True

    def next(self) -> str:
        """
        :return: next string in combination, or last string if no next exists
        """
        next_combo = ''.join([self.characters[i] for i in self.current_bit_map])  # the combo to return
        if all((x == y for x, y in zip(self.current_bit_map, self.end_state_bit_map))):
            # end_state_bit_map reached, set next_flag as false
            self.next_flag = False
        else:
            # end_state_bit_map not reached, progress to next current_bit_map
            i = len(self.current_bit_map) - 1  # start from the end
            while self.current_bit_map[i] == self.end_state_bit_map[i]:
                # find last 0 in bit map
                i -= 1
            # increment current_bit_map by 1
            # turn the last 0 bit into 1
            # fill last few bits with 1, to honor combination_length
            # reset remaining bits to 0
            self.current_bit_map[i] += 1
            self.current_bit_map = self.current_bit_map[:i + 1] + list(range(self.current_bit_map[i] + 1,
                                                                             self.current_bit_map[i] +
                                                                             len(self.current_bit_map) - i))
        return next_combo

    def has_next(self) -> bool:
        """
        :return: if there exists a next combination
        """
        return self.next_flag


test_iterator = CombinationIterator("abc", 2)
assert test_iterator.next() == "ab"
assert test_iterator.has_next()
assert test_iterator.next() == "ac"
assert test_iterator.has_next()
assert test_iterator.next() == "bc"
assert not test_iterator.has_next()
