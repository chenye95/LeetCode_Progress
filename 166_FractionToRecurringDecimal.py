"""
Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

If multiple answers are possible, just return any of them.
"""


def fraction_to_decimal(numerator: int, denominator: int) -> str:
    """
    :return: convert fraction numerator / denominator to decimals. Use parentheses to enclose repeating parts
    """
    assert denominator != 0, "Invalid Operation, Divided by 0"
    if numerator == 0:
        return "0"
    if (numerator < 0) is not (denominator < 0):
        decimal_str = "-"
    else:
        decimal_str = ""

    abs_numerator, abs_denominator = abs(numerator), abs(denominator)
    n, remainder = divmod(abs_numerator, abs_denominator)
    decimal_str += str(n)
    if remainder == 0:
        return decimal_str

    decimal_str += '.'
    # keep track of repetition in decimal division
    decimal_stack = {}
    while remainder:
        if remainder in decimal_stack:
            decimal_str = decimal_str[:decimal_stack[remainder]] + '(' + decimal_str[decimal_stack[remainder]:] + ')'
            break
        decimal_stack[remainder] = len(decimal_str)
        n, remainder = divmod(remainder * 10, abs_denominator)
        decimal_str += str(n)
    return decimal_str


test_cases = [(1, 2, "0.5"),
              (2, 1, "2"),
              (2, 3, "0.(6)"),
              (25, 13, "1.(923076)"), ]
for test_numerator, test_denominator, expected_output in test_cases:
    assert fraction_to_decimal(test_numerator, test_denominator) == expected_output
