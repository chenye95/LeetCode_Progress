"""
The Tribonacci sequence Tn is defined as follows:
  T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""


def tribonacci(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1

    first_num, second_num, third_num = 0, 1, 1
    for _ in range(n - 2):
        third_num, second_num, first_num = first_num + second_num + third_num, third_num, second_num
    return third_num


test_cases = [(4, 4), (25, 1389537), ]
for test_n, expected_output in test_cases:
    assert tribonacci(test_n) == expected_output
