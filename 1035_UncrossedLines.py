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


assert max_uncrossed_lines(list_a=[1, 4, 2], list_b=[1, 2, 4]) == 2
assert max_uncrossed_lines(list_a=[2, 5, 1, 2, 5], list_b=[10, 5, 2, 1, 5, 2]) == 3
assert max_uncrossed_lines(list_a=[1, 3, 7, 1, 7, 5], list_b=[1, 9, 2, 5, 1]) == 2
assert max_uncrossed_lines(list_a=[3, 2], list_b=[2, 2, 2, 3]) == 1
