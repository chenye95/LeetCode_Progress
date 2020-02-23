"""
Given an integer num, find the closest two integers in absolute difference whose product equals num + 1 or num + 2.

Return the two integers in any order.

1 <= num <= 10^9
"""
from typing import List


def closestDivisors(num: int) -> List[int]:
    for a in range(int((num+2) ** 0.5), 0, -1):
        if (num + 1) % a == 0:
            return [a, (num + 1) // a]
        elif (num + 2) % a == 0:
            return [a, (num + 2) // a]


test_cases = [(8, [3, 3]), (123, [5, 25]), (999, [25, 40])]
for input, output in test_cases:
    assert closestDivisors(input) == output
