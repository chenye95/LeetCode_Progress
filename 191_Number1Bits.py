"""
Write a function that takes an unsigned integer and returns the number of '1' bits it has (also known as the Hamming
weight).
"""


def hamming_weight(n: int) -> int:
    """
    :return: count of '1' in binary representation of n
    """
    counter = 0
    while n > 0:
        counter += (n % 2)
        n >>= 1
    return counter


test_cases = ['00000000000000000000000000001011',
              '00000000000000000000000010000000',
              '11111111111111111111111111111101', ]
for test_input in test_cases:
    assert hamming_weight(n=int(test_input, 2)) == test_input.count('1')
