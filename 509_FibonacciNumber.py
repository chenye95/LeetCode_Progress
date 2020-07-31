"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is
the sum of the two preceding ones, starting from 0 and 1. That is,
- F(0) = 0,   F(1) = 1
- F(N) = F(N - 1) + F(N - 2), for N > 1.
"""


def fibonacci(N: int) -> int:
    if N <= 1:
        return N
    two_number = 0
    one_number = current_number = 1
    for i in range(1, N):
        current_number = two_number + one_number
        two_number = one_number
        one_number = current_number
    return current_number


assert fibonacci(0) == 0
assert fibonacci(1) == 1
assert fibonacci(2) == 1
assert fibonacci(3) == 2
assert fibonacci(4) == 3
