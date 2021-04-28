"""
We write the integers of list_a and list_b (in the order they are given) on two separate horizontal lines.

Now, we may draw connecting lines: a straight line connecting two numbers list_a[i] and list_b[j] such that:
- list_a[i] == list_b[j];
- The line we draw does not intersect any other connecting (non-horizontal) line.

Note that a connecting lines cannot intersect even at the endpoints: each number can only belong to one connecting line.

Return the maximum number of connecting lines we can draw in this way.
"""
from typing import List


def max_uncrossed_lines(list_a: List[int], list_b: List[int]) -> int:
    """
    Dynamic Programming method

    :param list_a: write integers in order in list_a on the top line
    :param list_b: write integers in order in list_b on the bottom line
    :return: maximum number of connecting lines between list_a[i] == list_b[j]
    """
    m, n = len(list_a), len(list_b)
    list_a_til_i_1 = [0] * (n + 1)
    for i in range(m):
        list_a_til_i = [0] * (n + 1)
        for j in range(n):
            # connecting a[i] to b[j], or skipping a[i], or skipping b[j]
            list_a_til_i[j + 1] = max(list_a_til_i_1[j] + (list_a[i] == list_b[j]),
                                      list_a_til_i[j],
                                      list_a_til_i_1[j + 1])
        list_a_til_i_1 = list_a_til_i
    return list_a_til_i_1[-1]


test_cases = [([1, 4, 2], [1, 2, 4], 2),
              ([2, 5, 1, 2, 5], [10, 5, 2, 1, 5, 2], 3),
              ([1, 3, 7, 1, 7, 5], [1, 9, 2, 5, 1], 2),
              ([3, 2], [2, 2, 2, 3], 1),
              ([2, 3, 1, 2, 5, 1, 3, 1, 3, 2, 3, 1, 2, 2, 3, 3, 3, 1, 3, 4, 4, 3, 4, 3, 4, 5, 4, 4, 1, 3],
               [5, 4, 5, 1, 1, 3, 4, 3, 2, 3], 7), ]
for test_a, test_b, expected_output in test_cases:
    assert max_uncrossed_lines(test_a, test_b) == expected_output
