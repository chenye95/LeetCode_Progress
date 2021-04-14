"""
Given an array list_of_strings of strings made only from lowercase letters, return a list of all characters that show up
 in all strings within the list (including duplicates).  For example, if a character occurs 3 times in all strings but
 not 4 times, you need to include that character three times in the final answer.

You may return the answer in any order.
"""
from collections import Counter
from typing import List


def common_chars(list_of_strings: List[str]) -> List[str]:
    """
    :param list_of_strings: array of strings made only from lowercase letters
    :return: list of all characters that show up in all strings, include duplicates
    """
    if not list_of_strings:
        return []
    tmp = Counter(list_of_strings[0])
    for s in list_of_strings[1:]:
        tmp &= Counter(s)
    return list(tmp.elements())


test_cases = [(["bella", "label", "roller"], ['e', 'l', 'l']),
              (["cool", "lock", "cook"], ['c', 'o']),
              (["adahafhbgccagdeebcac", "fafgacdacbfafegbaafe", "hdefhchehgaeehegbcdd", "ahgeeafbeeedefbbdeaf",
                "bdbccgbgeffccacehfca", "cfccgbcfedgffdggbbha", "hdbgedhhaahfadaeadeg", "ahefaeacaedfahfagcaa",
                "aadhbfadfhhdehccgbgh", "hcbbddchgbgbdeabdcag", "faabcaccacehchhhdebg", "gcdfceefgbafgghegdcc",
                "cadeffheabbcdcbfeffd", "fdaeeffhfhbfhhgbaecg", "hbghdfcbfhadacdebfag", "gcdeaahegfhgdaggeefc",
                "abgffcehabegfgbbafbg", "egceahedahfhafehfdae", "ccdehaehchaehefadcac", "dfbgdbgcfbceffddehea"],
               ['a', 'e']), ]
for test_input, expected_output in test_cases:
    assert common_chars(test_input) == expected_output
assert common_chars(["bella", "label", "roller"]) == ['e', 'l', 'l']
