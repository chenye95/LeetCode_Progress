"""
On a broken calculator that has a number showing on its display, we can perform two operations:
- Double: Multiply the number on the display by 2, or;
- Decrement: Subtract 1 from the number on the display.

Initially, the calculator is displaying X. Return the minimum number of operations needed to display Y.
"""


def broken_calculator(x: int, y: int) -> int:
    """
    Instead of multiplying by 2 or subtracting 1 from X, we could divide by 2 (when Y is even) or add 1 to Y
    Greedily divide by 2:
    * if y is even (y + 2) / 2 = y / 2 + 1
    * if y is odd (y + 3) / 2 = （y + 1) / 2 + 1
    """
    if x >= y:
        return x - y

    step_count = 0
    while y > x:
        step_count += 1
        if y % 2:
            y += 1
        else:
            y //= 2

    return step_count + x - y


test_cases = [(2, 3, 2),
              (5, 8, 2),
              (3, 10, 3),
              (1024, 1, 1023),
              ]
for test_x, test_y, expected_count in test_cases:
    assert broken_calculator(test_x, test_y) == expected_count
