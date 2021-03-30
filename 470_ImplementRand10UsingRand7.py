"""
Given the API rand7 which generates a uniform random integer in the range 1 to 7, write a function rand10 which
 generates a uniform random integer in the range 1 to 10. You can only call the API rand7 and you shouldn't call any
 other API. Please don't use the system's Math.random().

Notice that Each test case has one argument n, the number of times that your implemented function rand10 will be called
while testing.
"""
from collections import Counter
from random import randint


def rand7() -> int:
    """
    :return: a random integer from 1 to 7
    """
    return randint(1, 7)


def rand10() -> int:
    """
    Rejection sampling

    :return: an int from 1 to 10
    """
    while True:
        a = rand7()
        b = rand7()

        # idx from 1 to 49
        idx = b + (a - 1) * 7
        if idx <= 40:
            # idx - 1 in 0 to 39
            return 1 + (idx - 1) % 10

        # a from 1 to 9
        a = idx - 40
        b = rand7()
        # idx from 1 to 63
        idx = b + (a - 1) * 7
        if idx <= 60:
            # idx - 1 in 0 to 59
            return 1 + (idx - 1) % 10

        # a from 1 to 3
        a = idx - 60
        b = rand7()
        # idx from 1 to 21
        idx = b + (a - 1) * 7
        if idx <= 20:
            # idx - 1 in 0 to 19
            return 1 + (idx - 1) % 10


N = 1_000_000
delta = 1_000
sample_count = Counter([rand10() for _ in range(N)])
# print(sample_count)
for i in sample_count:
    assert N // len(sample_count) - delta <= sample_count[i] <= N // len(sample_count) + delta, i
