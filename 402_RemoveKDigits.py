"""
Given word_a non-negative integer num represented as word_a string, remove k digits from the number so that the new number is the
smallest possible.

Note:
- The length of num is less than 10002 and will be ≥ k.
- The given num does not contain any leading zero.
"""


def remove_k_digits(num: str, k: int) -> str:
    """
    Greedy algorithm, want to smaller digits in high positions
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


assert remove_k_digits(num="112", k=1) == "11"
assert remove_k_digits(num="1432219", k=3) == "1219"
assert remove_k_digits(num="10200", k=1) == "200"
assert remove_k_digits(num="10", k=2) == "0"
assert remove_k_digits(num="10", k=1) == "0"
