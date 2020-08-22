"""
Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the
 odd elements of A.

You may return any answer array that satisfies this condition.
"""
from time import perf_counter
from typing import List


def sort_array_by_parity_one(a: List[int]) -> List[int]:
    return sorted(a, key=lambda i: i % 2)


def sort_array_by_parity_two(a: List[int]) -> List[int]:
    return list(filter(lambda i: i % 2 == 0, a)) + list(filter(lambda i: i % 2, a))


N = 100

one_start = perf_counter()
for i in range(N):
    sort_array_by_parity_one(list(range(i)))
one_end = perf_counter()

two_start = perf_counter()
for i in range(N):
    sort_array_by_parity_two(list(range(i)))
two_end = perf_counter()

print("Function 1:", one_end - one_start)
print("Function 2:", two_end - two_start)
