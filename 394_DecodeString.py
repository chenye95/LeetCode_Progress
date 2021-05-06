"""
Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k
 times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat
 numbers, k. For example, there won't be input like 3a or 2[4].
"""


def decode_string(s: str) -> str:
    """
    :param s: encoded string following rule k[encoded_string] = encoded_string * k
    :return: fully decoded string
    """
    current_decoding, current_k = "", 0
    operation_stack = []
    for c in s:
        if c.isdigit():
            current_k = current_k * 10 + int(c)
        elif c == '[':
            operation_stack.append((current_k, current_decoding))
            current_decoding, current_k = "", 0
        elif c == ']':
            previous_k, previous_encoding = operation_stack.pop()
            current_decoding = previous_encoding + current_decoding * previous_k
            current_k = 0
        else:
            current_decoding += c

    return current_decoding


test_cases = [("3[a]2[bc]", "aaabcbc"),
              ("3[a2[c]]", "accaccacc"),
              ("2[abc]3[cd]ef", "abcabccdcdcdef"),
              ("abc3[cd]xyz", "abccdcdcdxyz"),
              ("3[z]2[2[y]pq4[2[jk]e1[f]]]ef", "zzzyypqjkjkefjkjkefjkjkefjkjkefyypqjkjkefjkjkefjkjkefjkjkefef"), ]
for test_s, expected_output in test_cases:
    assert decode_string(test_s) == expected_output
