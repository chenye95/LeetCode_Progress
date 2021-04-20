"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false
 otherwise.
"""


def is_pangram(sentence: str) -> bool:
    """
    :param sentence: string of lower case English letters
    :return: if every letter of 26 lower case alphabet appears at least once
    """
    return len(set(sentence)) == 26


test_cases = [("thequickbrownfoxjumpsoverthelazydog", True),
              ("leetcode", False),
              ("qklccnqeicrabxpggieplwjhakurwwhxbugbryvhazoofifidzvxczmpdjfcyiuhqyedxhzexvpitxknjogpetvgxeqrjuuxzzfb" +
               "lhmhbgibocbhtcbgyxzchlawvnhczlecsrioapggorouzcputqsxhvoxbqxxydiumxwg", True), ]
for test_s, expected_outcome in test_cases:
    assert is_pangram(test_s) is expected_outcome
