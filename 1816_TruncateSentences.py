"""
A sentence is a list of words that are separated by a single space with no leading or trailing spaces. Each of the words
 consists of only uppercase and lowercase English letters (no punctuation).

For example, "Hello World", "HELLO", and "hello world hello world" are all sentences.

You are given a sentence s and an integer k. You want to truncate s such that it contains only the first k
 words. Return s after truncating it.
"""


def truncate_sentence(s: str, k: int) -> str:
    """
    :param s: string of english words separated by a single white space, with no leading or trailing spaces, nor
        punctuation
    :param k: 1 <= k <= # words in s
    :return: truncated sentence with only the first k words
    """
    return ' '.join(s.split()[:k])


test_cases = [("Hello how are you Contestant", 4, "Hello how are you"),
              ("What is the solution to this problem", 4, "What is the solution"),
              ("chopper is not a tanuki", 5, "chopper is not a tanuki"), ]
for test_s, test_k, expected_output in test_cases:
    assert truncate_sentence(test_s, test_k) == expected_output
