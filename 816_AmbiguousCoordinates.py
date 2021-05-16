"""
We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and
 spaces and ended up with the string s.
    - For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".

Return a list of strings representing all possibilities for what our original coordinates could have been.

Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00",
 "1.0", "001", "00.01", or any other number that can be represented with fewer digits. Also, a decimal point within a
 number never occurs without at least one digit occurring before it, so we never started with numbers like ".1".

The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between
 them (occurring after the comma.)
"""
from itertools import product
from typing import List


def ambiguous_coordinates_itertools(s: str) -> List[str]:
    """
    :param s: '(' + digits + ')', with 4 <= len(s) <= 12
    :return: list of 2-dimensional coordinates '(x, y)' where x and y are real numbers
    """

    def list_one_number(s_i: str) -> List[str]:
        """
        :param s_i: one dimension of the coordinates, either x or y. s_i consists of digits only
        :return: all ways to parse s_i as a valid real number
        """
        n_s = len(s_i)
        for pos_decimal_point in range(1, n_s + 1):
            if (pos_decimal_point == 1 or s_i[0] != '0') and (pos_decimal_point == n_s or s_i[-1] != '0'):
                yield s_i[:pos_decimal_point] + ('.' + s_i[pos_decimal_point:] if pos_decimal_point < n_s else '')

    return ["(%s, %s)" % (x, y)
            for i in range(2, len(s) - 1)
            for x, y in product(list_one_number(s[1: i]), list_one_number(s[i: -1]))]


def ambiguous_coordinates_list(s: str) -> List[str]:
    """
    :param s: '(' + digits + ')', with 4 <= len(s) <= 12
    :return: list of 2-dimensional coordinates '(x, y)' where x and y are real numbers
    """

    def is_valid_real_number(s_i: str) -> bool:
        """
        :return: whether s_i is a valid real number, assume at most one decimal point in s_i
        """
        if len(s_i) == 1:
            return True

        return (s_i[0] != '0' or s_i[1] == '.') and (s_i[-1] != '0' or '.' not in s_i)
        # Leading zeros
        # or trailing zeros after decimal points

    return_list = []
    for i in range(2, len(s) - 1):
        left_choice = [s[1: i]] if i == 2 or s[1] != '0' else []
        left_choice.extend([s for s in [s[1: j] + '.' + s[j: i] for j in range(2, i)] if is_valid_real_number(s)])
        right_choice = [s[i: -1]] if i == len(s) - 2 or s[i] != '0' else []
        right_choice.extend([s for s in [s[i: j] + '.' + s[j: -1] for j in range(i + 1, len(s) - 1)]
                             if is_valid_real_number(s)])
        return_list.extend(['(%s, %s)' % (x, y) for x in left_choice for y in right_choice])

    return return_list


test_cases = [("(123)", {"(1, 2.3)", "(1, 23)", "(1.2, 3)", "(12, 3)"}),
              ("(0123)", {"(0, 1.23)", "(0, 12.3)", "(0, 123)", "(0.1, 2.3)", "(0.1, 23)", "(0.12, 3)"}),
              ("(00011)", {"(0, 0.011)", "(0.001, 1)"}),
              ("(100)", {"(10, 0)"}),
              ("(133569498)",
               {'(1, 33569498)', '(1, 3.3569498)', '(1, 33.569498)', '(1, 335.69498)', '(1, 3356.9498)',
                '(1, 33569.498)', '(1, 335694.98)', '(1, 3356949.8)', '(13, 3569498)', '(13, 3.569498)',
                '(13, 35.69498)', '(13, 356.9498)', '(13, 3569.498)', '(13, 35694.98)', '(13, 356949.8)',
                '(1.3, 3569498)', '(1.3, 3.569498)', '(1.3, 35.69498)', '(1.3, 356.9498)', '(1.3, 3569.498)',
                '(1.3, 35694.98)', '(1.3, 356949.8)', '(133, 569498)', '(133, 5.69498)', '(133, 56.9498)',
                '(133, 569.498)', '(133, 5694.98)', '(133, 56949.8)', '(1.33, 569498)', '(1.33, 5.69498)',
                '(1.33, 56.9498)', '(1.33, 569.498)', '(1.33, 5694.98)', '(1.33, 56949.8)', '(13.3, 569498)',
                '(13.3, 5.69498)', '(13.3, 56.9498)', '(13.3, 569.498)', '(13.3, 5694.98)', '(13.3, 56949.8)',
                '(1335, 69498)', '(1335, 6.9498)', '(1335, 69.498)', '(1335, 694.98)', '(1335, 6949.8)',
                '(1.335, 69498)', '(1.335, 6.9498)', '(1.335, 69.498)', '(1.335, 694.98)', '(1.335, 6949.8)',
                '(13.35, 69498)', '(13.35, 6.9498)', '(13.35, 69.498)', '(13.35, 694.98)', '(13.35, 6949.8)',
                '(133.5, 69498)', '(133.5, 6.9498)', '(133.5, 69.498)', '(133.5, 694.98)', '(133.5, 6949.8)',
                '(13356, 9498)', '(13356, 9.498)', '(13356, 94.98)', '(13356, 949.8)', '(1.3356, 9498)',
                '(1.3356, 9.498)', '(1.3356, 94.98)', '(1.3356, 949.8)', '(13.356, 9498)', '(13.356, 9.498)',
                '(13.356, 94.98)', '(13.356, 949.8)', '(133.56, 9498)', '(133.56, 9.498)', '(133.56, 94.98)',
                '(133.56, 949.8)', '(1335.6, 9498)', '(1335.6, 9.498)', '(1335.6, 94.98)', '(1335.6, 949.8)',
                '(133569, 498)', '(133569, 4.98)', '(133569, 49.8)', '(1.33569, 498)', '(1.33569, 4.98)',
                '(1.33569, 49.8)', '(13.3569, 498)', '(13.3569, 4.98)', '(13.3569, 49.8)', '(133.569, 498)',
                '(133.569, 4.98)', '(133.569, 49.8)', '(1335.69, 498)', '(1335.69, 4.98)', '(1335.69, 49.8)',
                '(13356.9, 498)', '(13356.9, 4.98)', '(13356.9, 49.8)', '(1335694, 98)', '(1335694, 9.8)',
                '(1.335694, 98)', '(1.335694, 9.8)', '(13.35694, 98)', '(13.35694, 9.8)', '(133.5694, 98)',
                '(133.5694, 9.8)', '(1335.694, 98)', '(1335.694, 9.8)', '(13356.94, 98)', '(13356.94, 9.8)',
                '(133569.4, 98)', '(133569.4, 9.8)', '(13356949, 8)', '(1.3356949, 8)', '(13.356949, 8)',
                '(133.56949, 8)', '(1335.6949, 8)', '(13356.949, 8)', '(133569.49, 8)', '(1335694.9, 8)'}), ]
for ambiguous_coordinates in [ambiguous_coordinates_list, ambiguous_coordinates_itertools, ]:
    for test_s, expected_output in test_cases:
        assert set(ambiguous_coordinates(test_s)) == expected_output, ambiguous_coordinates.__name__
