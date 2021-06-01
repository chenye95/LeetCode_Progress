"""
The letter value of a letter is its position in the alphabet starting from 0 (i.e. 'a' -> 0, 'b' -> 1, 'c' -> 2, etc.).

The numerical value of some string of lowercase English letters s is the concatenation of the letter values of each
 letter in s, which is then converted into an integer.
- For example, if s = "acb", we concatenate each letter's letter value, resulting in "021". After converting it, we get
    21.
You are given three strings firstWord, secondWord, and targetWord, each consisting of lowercase English letters 'a'
through 'j' inclusive.

Return true if the summation of the numerical values of firstWord and secondWord equals the numerical value of
 targetWord, or false otherwise.
"""


def is_sum_equal(first_word: str, second_word, target_word: str) -> bool:
    """
    :param first_word: 1 <= len(first_word) <= 8, consists of lower case letter 'a' to 'j'
    :param second_word: 1 <= len(second_word) <= 8, consists of lower case letter 'a' to 'j'
    :param target_word: 1 <= len(target_word) <= 8, consists of lower case letter 'a' to 'j'
    :return: whether first_word + second_word == target_word
    """
    letter_lookup = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7, 'i': 8, 'j': 9}

    def word_value(word: str) -> int:
        int_value = 0
        for c in word:
            int_value = 10 * int_value + letter_lookup[c]
        return int_value

    return word_value(first_word) + word_value(second_word) == word_value(target_word)


test_cases = [("acb", "cba", "cdb", True),
              ("aaa", "a", "aab", False),
              ("aaa", "a", "aaaa", True),
              ("fhjfdghj", "h", "ejjbghch", False),
              ("jfjfjbcj", "i", "jfjfjbdh", True),
              ("h", "fhjfdghj", "fhjfdgig", True),
              ("i", "jfjfjbcj", "iffacheb", False), ]
for test_one_word, test_two_word, test_target_word, expected_value in test_cases:
    assert is_sum_equal(test_one_word, test_two_word, test_target_word) is expected_value
