"""
Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the
smallest possible.

Note:
- The length of num is less than 10002 and will be ≥ k.
- The given num does not contain any leading zero.
"""


def remove_k_digits(num: str, k: int) -> str:
    """
    Greedy algorithm, want to smaller digits in high positions

    :param num: a string of length <= 10_002, representing a non-negative integer
    :param k: an integer less than length of num
    :return: smallest number by removing k digits from num
    """
    if k == len(num):
        return '0'

    need_to_drop = k
    output_list = []

    for digit in num:
        # drop bigger digits for high positions
        while need_to_drop and output_list and output_list[-1] > digit:
            output_list.pop()
            need_to_drop -= 1
        output_list.append(digit)

    # Special cases, last few digits are equal
    # more digits than needed in output_list
    if need_to_drop:
        output_list = output_list[:-need_to_drop]

    return ''.join(output_list).lstrip('0') or '0'


test_cases = [("112", 1, "11"),
              ("1432219", 3, "1219"),
              ("10200", 1, "200"),
              ("10", 2, "0"),
              ("10", 1, "0"),
              ("1234567890", 10, "0"),
              ("1234567890", 9, "0"),
              ("43214321", 4, "1321"), ]
for test_num, test_k, expected_output in test_cases:
    assert remove_k_digits(num=test_num, k=test_k) == expected_output
