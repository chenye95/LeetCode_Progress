"""
Given a string s and an array of integers cost where cost[i] is the cost of deleting the ith character in s.

Return the minimum cost of deletions such that there are no two identical letters next to each other.

Notice that you will delete the chosen characters at the same time, in other words, after deleting a character, the
 costs of deleting other characters will not change.
"""
from typing import List


def min_cost(s: str, cost: List[int]) -> int:
    """
    :param s: string of lowercase English letters, 1 <= len(s) == len(cost) <= 1e5
    :param cost: 1 <= len(s) == len(cost) <= 1e5， 1 <= cost[i] <= 10000
    :return: min deletion cost to avoid repeating consecutive characters in s
    """
    min_total_cost = 0
    # group consecutive repeating letters
    # record total cost of the group and max cost within the group
    # min deletion group for the group is total_cost - max_cost
    max_group_cost = sum_group_cost = 0
    last_s = None
    for i, (cost_i, s_i) in enumerate(zip(cost, s)):
        if s_i != last_s:
            # start a new group
            min_total_cost += (sum_group_cost - max_group_cost)
            max_group_cost = sum_group_cost = cost_i
        else:
            # continuing in the same group
            sum_group_cost += cost_i
            max_group_cost = max(max_group_cost, cost_i)
        last_s = s_i

    return min_total_cost + sum_group_cost - max_group_cost


test_cases = [("abaac", [1, 2, 3, 4, 5], 3),
              ("abc", [1, 2, 3], 0),
              ("aabaa", [1, 2, 3, 4, 1], 2),
              ("abbbabaaabbbbbbabbaaaabbabbababbababbbabababbbaaababbabbbbbaabaaabbbbaabbaaabaaababbbbbaabaaaaaaaaab",
               [13, 18, 38, 34, 20, 36, 38, 5, 24, 9, 35, 34, 25, 48, 35, 9, 18, 40, 48, 12, 22, 18, 6, 7, 32, 12, 4,
                39, 28, 28, 19, 21, 9, 20, 23, 40, 11, 13, 7, 1, 3, 40, 32, 14, 8, 46, 35, 45, 12, 21, 49, 4, 48, 40,
                34, 29, 7, 49, 43, 16, 38, 15, 47, 44, 19, 18, 29, 49, 18, 2, 38, 9, 40, 1, 45, 6, 8, 26, 15, 30, 14,
                23, 48, 27, 22, 41, 20, 6, 27, 25, 24, 25, 27, 41, 50, 27, 6, 12, 19, 19], 1028),
              ("aaabbacbcbcccbcaabaabacbcbbcaabbcccbcaabaacacaaccaccabcccaababbccccbacbabacabcbbccacaabbbbbcabbccbabc" +
               "babbabacaaacbaccababbabbcbcabcaababbbacccaabccacbaacbbccbbabacabbbabcbacacacbccabcbaabcbccabcaabbcaba" +
               "baaacabbaaaacccabbbcbbabacbbcbabbcacccababcbbaacccbcbccabbcacaacbccbaaaabbcabacabccbcabccabccccaaaabb" +
               "ccaaacbbabbcbbacaaabaaaacbbabbbccbabcbcbbabbaaabbaaccacbbabbbbaaaacaabbbbacabccacbbabbaaaaaaaacabbbbb" +
               "abbbcbcbbcbbaacbaacbcababccaccbabaacbbcaabcacbbcaaabaaacaaaabacabacbccbcaccaaaaabbcaabccaacbabccabccb" +
               "bababcbcbbcbcabcacacbbaacbcbabcbbabcbabcbbcacbcbabbacbaacbcbbbbacccbccabaccbbccbacaaaabbccababcbcbabb" +
               "cbcaaabcbaaaaababbabaaacaabbaaabbaccbbabbacbcbabccbccbccbcbcacccaacacacaacabbcbcbcabccaccacbbcaaacbab" +
               "ccabaabccbccaaccccbbcccaabbccbbcccacbacaacccacacbcbcbbabbbabccbaacabccaccaaaaacacbccbabbcccbabaaaccbb" +
               "acabaacacbabbacababacbccccababbaaaacaacabcccbcbcaabbbabcbcbcbaabccbcbbbcacacaabcbababacaabacabbccabba"
               "abacbcabaaccbaaccbcaacbcababcccbcbcbbabaabbababaabaabbc",
               [35, 19, 44, 29, 38, 5, 46, 44, 17, 41, 39, 38, 22, 2, 11, 22, 4, 19, 2, 22, 37, 4, 22, 17, 7, 4, 36, 2,
                15, 28, 15, 42, 22, 31, 32, 41, 16, 37, 31, 4, 31, 14, 33, 37, 9, 2, 37, 4, 22, 14, 42, 23, 21, 50, 27,
                5, 15, 28, 9, 2, 29, 4, 19, 17, 30, 31, 25, 38, 42, 32, 30, 12, 20, 29, 11, 39, 40, 49, 35, 13, 21, 21,
                25, 33, 31, 16, 29, 35, 49, 21, 5, 13, 5, 38, 27, 22, 43, 19, 39, 21, 38, 7, 25, 22, 25, 39, 50, 8, 22,
                11, 8, 39, 4, 41, 39, 42, 1, 23, 47, 3, 11, 26, 10, 34, 22, 20, 44, 45, 34, 49, 15, 29, 47, 50, 12, 35,
                17, 10, 32, 41, 11, 15, 4, 4, 5, 50, 15, 31, 16, 10, 20, 17, 3, 42, 49, 40, 7, 50, 24, 25, 47, 27, 14,
                38, 28, 34, 11, 13, 30, 19, 32, 50, 4, 44, 16, 20, 15, 35, 6, 22, 34, 14, 41, 17, 24, 9, 36, 24, 50, 34,
                30, 9, 29, 33, 23, 50, 13, 34, 45, 45, 15, 2, 44, 43, 34, 23, 46, 11, 38, 13, 44, 35, 27, 2, 50, 23, 24,
                24, 1, 30, 9, 41, 7, 28, 35, 20, 6, 39, 10, 45, 22, 18, 15, 48, 2, 7, 10, 24, 31, 45, 19, 36, 11, 22, 5,
                9, 15, 5, 30, 43, 19, 33, 35, 11, 24, 47, 40, 35, 35, 35, 47, 25, 17, 7, 39, 45, 7, 25, 37, 3, 38, 43,
                1, 50, 15, 50, 12, 22, 19, 37, 3, 23, 41, 18, 13, 35, 34, 26, 22, 17, 12, 15, 8, 8, 7, 39, 1, 49, 4, 12,
                41, 22, 41, 19, 30, 39, 9, 31, 26, 41, 8, 34, 48, 3, 4, 40, 18, 9, 19, 50, 37, 28, 14, 10, 34, 9, 3, 8,
                13, 1, 44, 37, 12, 15, 21, 28, 35, 8, 28, 16, 42, 26, 14, 6, 29, 19, 6, 25, 30, 38, 46, 32, 11, 21, 20,
                22, 40, 23, 43, 10, 12, 13, 35, 20, 25, 13, 30, 5, 12, 20, 16, 14, 41, 12, 7, 7, 10, 39, 16, 6, 15, 17,
                46, 23, 50, 40, 43, 1, 10, 26, 34, 46, 31, 12, 22, 3, 34, 47, 1, 28, 29, 45, 42, 16, 4, 47, 14, 35, 38,
                4, 34, 14, 4, 27, 12, 50, 42, 19, 43, 4, 49, 23, 33, 50, 47, 32, 32, 13, 1, 50, 3, 18, 38, 32, 27, 37,
                7, 31, 49, 2, 7, 28, 38, 11, 7, 35, 2, 28, 11, 44, 41, 29, 43, 16, 47, 34, 26, 29, 34, 25, 9, 1, 5, 22,
                36, 35, 26, 47, 41, 1, 11, 44, 10, 38, 28, 24, 1, 22, 22, 8, 46, 22, 28, 28, 28, 12, 1, 43, 46, 1, 18,
                1, 19, 21, 28, 43, 22, 14, 44, 36, 38, 6, 47, 38, 2, 23, 36, 18, 19, 12, 18, 31, 38, 40, 31, 33, 20, 7,
                11, 3, 44, 32, 49, 11, 25, 13, 21, 48, 31, 9, 8, 48, 19, 38, 33, 24, 36, 38, 32, 24, 3, 46, 9, 14, 18,
                49, 12, 19, 6, 37, 15, 28, 11, 46, 38, 13, 24, 1, 19, 27, 21, 13, 35, 13, 36, 14, 4, 37, 40, 28, 17, 18,
                38, 1, 11, 38, 9, 28, 47, 5, 27, 33, 17, 23, 14, 23, 30, 46, 20, 1, 6, 20, 12, 1, 42, 10, 47, 1, 41, 10,
                15, 22, 41, 11, 27, 7, 15, 49, 25, 42, 37, 5, 9, 42, 47, 43, 18, 34, 24, 7, 3, 18, 34, 21, 4, 1, 39, 44,
                6, 15, 27, 4, 15, 22, 14, 4, 11, 25, 40, 22, 21, 20, 19, 42, 21, 8, 21, 28, 21, 12, 41, 36, 25, 3, 34,
                12, 7, 14, 31, 13, 15, 26, 26, 22, 42, 13, 36, 32, 15, 17, 38, 30, 3, 18, 17, 46, 13, 8, 46, 45, 5, 40,
                11, 43, 28, 24, 19, 49, 33, 19, 32, 32, 13, 37, 2, 50, 49, 16, 7, 30, 50, 17, 32, 48, 36, 8, 39, 22, 47,
                28, 23, 5, 28, 45, 11, 23, 22, 41, 18, 18, 26, 21, 27, 46, 48, 40, 15, 2, 45, 44, 47, 36, 16, 29, 45,
                48, 30, 7, 29, 28, 47, 1, 31, 28, 9, 37, 19, 39, 30, 19, 32, 49, 5, 10, 47, 24, 38, 34, 24, 9, 28, 20,
                12, 16, 40, 24, 18, 45, 2, 45, 46, 34, 35, 16, 29, 23, 23, 46, 5, 32, 39, 15, 42, 41, 21, 30, 32, 26,
                35, 36, 37, 22, 21, 26, 14, 46, 4, 2, 24, 3, 34, 44, 27, 8, 5, 32, 14, 8, 11, 42, 7, 1, 29, 5, 22, 37,
                18, 26, 20, 35, 36, 46, 34, 16, 42, 17, 38, 44, 3, 43, 35, 23, 8, 38, 13, 14, 1, 41, 20, 18, 23, 40, 13,
                41, 28, 29, 20, 50, 47, 7, 1, 48, 36, 9, 20, 45, 7, 41, 1, 11, 38, 16, 6, 39, 22, 5, 9, 3, 24, 1, 39,
                29, 26, 47, 15, 33, 37, 47, 40, 26, 31, 48, 12, 28, 36, 43, 43, 12, 50, 35, 50, 32, 9, 46, 3, 14, 14,
                20, 40, 38, 43, 9, 18, 23, 13, 34, 24, 7, 1, 34, 7, 36, 18, 47, 28, 15, 18, 5, 11, 2, 40, 46, 1, 40, 35,
                27, 44, 35, 17, 33, 11, 49, 38, 19, 13, 14, 34, 33, 1, 2, 22, 47, 40, 46, 30, 35, 33, 16, 16, 10, 42,
                31, 13, 16, 4, 11, 35, 15, 42, 48, 7, 36, 1, 34], 5295),
              ]
for test_s, test_cost, expected_value in test_cases:
    assert min_cost(test_s, test_cost) == expected_value
