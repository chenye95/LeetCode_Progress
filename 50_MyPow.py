"""
Implement pow(x, n), which calculates x raised to the power n (x^n).
"""


def my_pow(x: float, n: int) -> float:
    """
    My implementation of pow(x, n)

    :return: x^n
    """
    if n == 0:
        return 1.0
    elif n < 0:
        return 1.0 / my_pow(x, -n)
    elif n % 2 == 1:
        return x * my_pow(x * x, n // 2)
    else:
        return my_pow(x * x, n // 2)


test_cases = [(2.0, 10, 1024.0),
              (3.0, 2, 9.0), ]
for test_x, test_n, expected_output in test_cases:
    assert my_pow(x=test_x, n=test_n) == expected_output
