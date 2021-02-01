"""
Today, the bookstore owner has a store open for customers.length minutes.  Every minute, some number of customers
(customers[i]) enter the store, and all those customers leave after the end of that minute.

On some minutes, the bookstore owner is grumpy.  If the bookstore owner is grumpy on the i-th minute, grumpy[i] = 1,
otherwise grumpy[i] = 0.  When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise
they are satisfied.

The bookstore owner knows a secret technique to keep themselves not grumpy for X minutes straight, but can only use it
once.

Return the maximum number of customers that can be satisfied throughout the day.
"""
from typing import List


def max_satisfied(customers: List[int], grumpy: List[int], x: int) -> int:
    """
    Sliding window solution
    - Bookstore owner is grumpy if grumpy[i] = 1
    """

    if x >= len(grumpy):
        return sum(customers)

    window_start_on_i = sum(customers[:x]) + sum([0 if g_i else c_i for c_i, g_i in zip(customers[x:], grumpy[x:])])
    max_satisfaction = window_start_on_i
    for i_minus_1 in range(len(customers) - x):
        if grumpy[i_minus_1]:
            window_start_on_i -= customers[i_minus_1]
        if grumpy[i_minus_1 + x]:
            window_start_on_i += customers[i_minus_1 + x]
        if max_satisfaction < window_start_on_i:
            max_satisfaction = window_start_on_i

    return max_satisfaction


assert max_satisfied(customers=[10, 1, 7], grumpy=[0, 0, 0], x=2) == 18
assert max_satisfied(customers=[4, 10, 10], grumpy=[1, 1, 0], x=2) == 24
assert max_satisfied(customers=[1, 0, 1, 2, 1, 1, 7, 5], grumpy=[0, 1, 0, 1, 0, 1, 0, 1], x=3) == 16
