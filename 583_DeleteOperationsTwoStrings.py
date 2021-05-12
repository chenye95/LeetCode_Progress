"""
Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
"""


def min_delete_distance_lcs_search(word1: str, word2: str) -> int:
    """
    :param word1: 1 <= word1.length <= 500, English lowercase letter only
    :param word2: 1 <= word2.length <= 500, English lowercase letter only
    :return: edit distance with deletion operation only
    """
    memorization = [[-1] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    def calculate_longest_common_sequence_dfs(i_1: int, i_2: int) -> int:
        """
        :return: longest common sequence of word1[:i_1] and word2[:i_2]
        """
        if i_1 == 0 or i_2 == 0:
            return 0
        if memorization[i_1][i_2] == -1:
            if word1[i_1 - 1] == word2[i_2 - 1]:
                memorization[i_1][i_2] = 1 + calculate_longest_common_sequence_dfs(i_1 - 1, i_2 - 1)
            else:
                memorization[i_1][i_2] = max(calculate_longest_common_sequence_dfs(i_1, i_2 - 1),
                                             calculate_longest_common_sequence_dfs(i_1 - 1, i_2))
        return memorization[i_1][i_2]

    return len(word1) + len(word2) - 2 * calculate_longest_common_sequence_dfs(len(word1), len(word2))


def min_delete_distance_lcs_dp(word1: str, word2: str) -> int:
    """
    :param word1: 1 <= word1.length <= 500, English lowercase letter only
    :param word2: 1 <= word2.length <= 500, English lowercase letter only
    :return: edit distance with deletion operation only
    """
    # longest common sequence of word1[:i_1] and word2[:i_2]
    lcs_table = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]
    for i_1 in range(1, len(word1) + 1):
        for i_2 in range(1, len(word2) + 1):
            if word1[i_1 - 1] == word2[i_2 - 1]:
                lcs_table[i_1][i_2] = 1 + lcs_table[i_1 - 1][i_2 - 1]
            else:
                lcs_table[i_1][i_2] = max(lcs_table[i_1][i_2 - 1], lcs_table[i_1 - 1][i_2])

    return len(word1) + len(word2) - 2 * lcs_table[-1][-1]


def min_delete_distance_delete_distance(word1: str, word2: str) -> int:
    """
    :param word1: 1 <= word1.length <= 500, English lowercase letter only
    :param word2: 1 <= word2.length <= 500, English lowercase letter only
    :return: edit distance with deletion operation only
    """
    # delete op needed to make word1[:i_1] and word2[:i_2] equal
    delete_op_count = [list(range(len(word2) + 1))] + [[0] * (len(word2) + 1) for _ in range(len(word1))]
    for i_1 in range(1, len(word1) + 1):
        delete_op_count[i_1][0] = i_1

    for i_1 in range(1, len(word1) + 1):
        for i_2 in range(1, len(word2) + 1):
            if word1[i_1 - 1] == word2[i_2 - 1]:
                delete_op_count[i_1][i_2] = delete_op_count[i_1 - 1][i_2 - 1]
            else:
                delete_op_count[i_1][i_2] = 1 + min(delete_op_count[i_1][i_2 - 1], delete_op_count[i_1 - 1][i_2])

    return delete_op_count[-1][-1]


test_cases = [("sea", "eat", 2),
              ("leetcode", "etco", 4),
              ("dinitrophenylhydrazine", "acetylphenylhydrazine", 11),
              ("plasma", "altruism", 8),
              ("szwokpjlgqgogbgpjaczcmtjhzgldwinqfxbcxgghitcinmtdwnnpsmnmhfrhrgwncvcizaze",
               "spjlqggpzcgdxxtdwnrvca", 51), ]
for min_delete_distance in [min_delete_distance_lcs_search,
                            min_delete_distance_lcs_dp,
                            min_delete_distance_delete_distance, ]:
    for test_word_1, test_word_2, expected_output in test_cases:
        assert min_delete_distance(test_word_1, test_word_2) == expected_output, min_delete_distance.__name__
