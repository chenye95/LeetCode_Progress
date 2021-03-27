"""
Given a column title as appear in an Excel sheet, return its corresponding column number.

For example:
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
    ...
"""


def column_to_number(column_name: str) -> int:
    """
    :param column_name: a column title as appear in an Excel sheet
    :return: corresponding column number
    """
    return_row = 0
    ord_base = ord('A') - 1
    for i in range(len(column_name)):
        return_row = 26 * return_row + ord(column_name[i]) - ord_base
    return return_row


test_cases = [("A", 1), ("AB", 28), ("ZY", 701), ]
for test_col, expected_output in test_cases:
    assert column_to_number(column_name=test_col) == expected_output
