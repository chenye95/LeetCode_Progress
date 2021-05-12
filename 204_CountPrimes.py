"""
Count the number of prime numbers less than a non-negative number, n.
"""
from math import sqrt


def count_primes(n: int) -> int:
    """
    Sieve of Eratosthenes algorithm

    :param n: a non negative integer n
    :return: number of primes less than n
    """
    if n <= 2:
        return 0

    is_prime = [True] * n

    for p in range(2, int(sqrt(n)) + 1):
        if is_prime[p]:
            for multiple_of_p in range(p * p, n, p):
                is_prime[multiple_of_p] = False

    return sum(is_prime) - 2  # 0 and 1 are not primes


test_cases = [(10, 4), (0, 0), (1, 0), (3, 1), (4, 2), (10000, 1229), (11, 4), ]
for test_n, expected_count in test_cases:
    assert count_primes(test_n) == expected_count, test_n
