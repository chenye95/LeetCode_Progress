"""
639. Decode Ways II
A encoded_message containing letters from A-Z is being encoded to numbers using the following mapping way:
    A -> 1
    B -> 2
    ...
    Z -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from
1 to 9.
Given the encoded encoded_message containing digits and the character '*', return the total number of ways to decode it.
Also, since the answer may be very large, you should return the output mod 10^9 + 7.
"""


def num_decoding(encoded_message: str) -> int:
    """
    :param encoded_message: string of digits and '*'
    :return: numbers of ways to decode message mod 10^9 + 7
    """
    M = 10 ** 9 + 7
    ways = [0] * (len(encoded_message) + 1)
    ways[0] = 1
    for i in range(len(encoded_message)):
        point_i = i + 1
        if encoded_message[i] == '*':
            ways[point_i] = 9 * ways[point_i - 1]
            if i > 0 and (encoded_message[i - 1] == '1' or encoded_message[i - 1] == '*'):  # 11-19 as * can be 1-9
                ways[point_i] = (ways[point_i] + 9 * ways[point_i - 2]) % M
            if i > 0 and (encoded_message[i - 1] == '2' or encoded_message[i - 1] == '*'):  # 21-26
                ways[point_i] = (ways[point_i] + 6 * ways[point_i - 2]) % M
        else:
            ways[point_i] = ways[point_i - 1] if encoded_message[i] != '0' else 0
            if i > 0 and encoded_message[i - 1] == '1':  # 1x
                ways[point_i] = (ways[point_i] + ways[point_i - 2]) % M
            elif i > 0 and encoded_message[i - 1] == '2' and encoded_message[i] <= '6':  # 2x for 1 <= x <= 6
                ways[point_i] = (ways[point_i] + ways[point_i - 2]) % M
            elif i > 0 and encoded_message[i - 1] == '*':
                ways[point_i] = (ways[point_i] + 2 * ways[point_i - 2]) % M if encoded_message[i] <= '6' \
                    else (ways[point_i] + ways[point_i - 2]) % M
    return ways[-1]


test_cases = [("*", 9), ("2*9", 16), ("1*", 18), ("2*", 15), ]
for test_str, expected_output in test_cases:
    assert num_decoding(encoded_message=test_str) == expected_output
