"""
Given a string s, check if the letters can be rearranged so that two characters that are adjacent to each other are not
 the same.

If possible, output any possible result.  If not possible, return the empty string.
"""
import heapq
from collections import Counter


def reorganize_string(s: str) -> str:
    """
    :param s: 1 <= len(s) <= 500
    :return: reorganized s such that no adjacent characters are the same, "" if no such arrangement exists
    """
    if len(s) == 1:
        return s

    reorganized_s = [''] * len(s)
    most_frequent_c = [(-freq, c) for c, freq in Counter(s).items()]
    heapq.heapify(most_frequent_c)

    if -most_frequent_c[-1][0] > len(s) // 2:
        # if one character is more than half of the total length, cannot reorganize
        return ""

    i = 0
    # used to hold of characters not be inserted twice consecutively
    minus_previous_freq, previous_c = 0, ''
    while most_frequent_c:
        minus_current_freq, current_c = heapq.heappop(most_frequent_c)
        reorganized_s[i] = current_c
        i += 1
        if minus_previous_freq < 0:
            # previous_c still has some left
            heapq.heappush(most_frequent_c, (minus_previous_freq, previous_c))
        minus_previous_freq, previous_c = minus_current_freq + 1, current_c

    return ''.join(reorganized_s) if i == len(s) else ""


def reorganize_string_extremely_smart(s: str) -> str:
    """
    Just copied here for inspiration https://leetcode.com/problems/reorganize-string/discuss/113435/4-lines-Python

    :param s: 1 <= len(s) <= 500
    :return: reorganized s such that no adjacent characters are the same, "" if no such arrangement exists
    """
    # sort c in s by repetition count
    a = sorted(sorted(s), key=s.count)
    half_len = len(a) // 2
    # try to put the most common letters at even indices, and less common ones at odd indices
    a[1::2], a[::2] = a[:half_len], a[half_len:]

    return ''.join(a) if a[-1:] != a[-2:-1] else ""


def verify_reorganization(output_string: str) -> True:
    """
    :param output_string: output string from reorganize_string()
    :return: True if output_string is not empty and does not have two consecutive characters that are the same
    """
    if not output_string:
        return False

    previous_c = output_string[0]
    for next_c in output_string[1:]:
        if next_c == previous_c:
            return False
        previous_c = next_c

    return True


test_cases = [('a', True),
              ("aa", False),
              ("aaab", False),
              ("aab", True),
              ("bbbbbbb", False),
              ("rvhrlpiesrrryrbrrrrrxrkirranrrrrbdrrzgasoxrrr", True),
              ("snnnnbpngobwznvnnnlnwhvnnnnfjnnlnnnnnnbnknnqkndzefncknnnnnaiqrntnndnnnjninnnunnunqhndnnqnnsjqnnpiqshn" +
               "tnnncnvnnnncnnqenlnninyndnnnljongnnjwnnnngllnnngkbnllnnnnontlbpngjnnenqnsnnnnnjeqqghnfpngepnodnnnnnnv" +
               "nsrnughbnipvnhqmnzonoonnnjotnnonoennnpnfnnkdnnbmnmnpnqninnxronnnnvnlanlnnnebnnnlnvnfknsnbincnttnmnguq" +
               "enhnnxunnnntnnnnhnqnzehvunfnvnndvnjnnnbnnpxnqipwnmnonnndlnsnonnninnxnnnjnnnnnesennmyiednnnnnnnnnhimtn" +
               "nnonjlicnwnwvnntaxmnrntnnnnsnbnanninnecbcfjxncnnkvnnqgnunensanpnngjnzxjnopnnyvnnxskniyytnsnnnnx", True),
              ]
for test_s, expected_output in test_cases:
    assert verify_reorganization(reorganize_string(test_s)) is expected_output
    assert verify_reorganization(reorganize_string_extremely_smart(test_s)) is expected_output
