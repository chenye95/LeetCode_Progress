"""
Given a list of words, each word consists of English lowercase letters.

Let's say word1 is a predecessor of word2 if and only if we can add exactly one letter anywhere in word1 to make it
 equal to word2. For example, "abc" is a predecessor of "abac".

A word chain is a sequence of words [word_1, word_2, ..., word_k] with k >= 1, where word_1 is a predecessor of word_2,
 word_2 is a predecessor of word_3, and so on.

Return the longest possible length of a word chain with words chosen from the given list of words.
"""
from typing import List


def longest_str_chain_top_down(words: List[str]) -> int:
    """
    :param words: 1 <= len(words) <= 1000 and 1 <= max(len(words[i])) <= 16
    :return: length of longest string chain in words
    """
    if not words:
        return 0

    def longest_chain_ending_with(ending_word: str) -> int:
        """
        :param ending_word: a valid word in the original words list
        :return: longest chain ending with word_i
        """
        if ending_word not in dfs_memory:
            local_max = 1
            for split_j in range(len(ending_word)):
                remove_one_chr = ending_word[:split_j] + ending_word[split_j + 1:]
                if remove_one_chr in words_set:
                    local_max = max(local_max, 1 + longest_chain_ending_with(remove_one_chr))

            dfs_memory[ending_word] = local_max

        return dfs_memory[ending_word]

    dfs_memory = {}
    words_set = set(words)
    return max(longest_chain_ending_with(word_i) for word_i in words_set)


def longest_str_chain_bottom_up(words: List[str]) -> int:
    """
    :param words: 1 <= len(words) <= 1000 and 1 <= max(len(words[i])) <= 16
    :return: length of longest string chain in words
    """
    if not words:
        return 0

    chain_length = {}
    global_max = 1

    for word_i in sorted(words, key=lambda s: len(s)):
        if word_i not in chain_length:
            chain_length[word_i] = 1 + max(chain_length.get(word_i[:split_j] + word_i[split_j + 1:], 0)
                                           for split_j in range(len(word_i)))
            if chain_length[word_i] > global_max:
                global_max = chain_length[word_i]

    return global_max


test_cases = [(["a", "b", "ba", "bca", "bda", "bdca"], 4),
              (["xbc", "pcxbcf", "xb", "cxbc", "pcxbc"], 5),
              (["ksqvsyq", "ks", "kss", "czvh", "zczpzvdhx", "zczpzvh", "zczpzvhx", "zcpzvh", "zczvh", "gr", "grukmj",
                "ksqvsq", "gruj", "kssq", "ksqsq", "grukkmj", "grukj", "zczpzfvdhx", "gru"], 7),
              (["czgxmxrpx", "lgh", "bj", "cheheex", "jnzlxgh", "nzlgh", "ltxdoxc", "bju", "srxoatl", "bbadhiju",
                "cmpx", "xi", "ntxbzdr", "cheheevx", "bdju", "sra", "getqgxi", "geqxi", "hheex", "ltxdc", "nzlxgh",
                "pjnzlxgh", "e", "bbadhju", "cmxrpx", "gh", "pjnzlxghe", "oqlt", "x", "sarxoatl", "ee", "bbadju",
                "lxdc", "geqgxi", "oqltu", "heex", "oql", "eex", "bbdju", "ntxubzdr", "sroa", "cxmxrpx", "cmrpx",
                "ltxdoc", "g", "cgxmxrpx", "nlgh", "sroat", "sroatl", "fcheheevx", "gxi", "gqxi", "heheex"], 9),
              (["cozddh", "ferawpnpff", "ivftewfdn", "mq", "zmq", "nwzmbq", "rcozyddh", "rcozyddhm", "czddh",
                "hrcozyddhm", "vftewfdn", "vtefdn", "rpeyrgwm", "wcjaki", "jiddfyh", "nzmbq", "xnvzrzc", "zdh", "utcc",
                "peyrgwm", "pergwm", "vftefdn", "rcozddh", "h", "zddh", "tcc", "nnwhszmbuq", "utgcc", "nnwszmbq",
                "jiddfh", "zmbq", "ivtftewfdn", "vefdn", "ferawpnff", "xnvzrc", "nnwhszmbq", "dh", "nwszmbq"], 10), ]
for longest_str_chain in [longest_str_chain_bottom_up, longest_str_chain_top_down, ]:
    for test_words, expected_count in test_cases:
        assert longest_str_chain(test_words) == expected_count, longest_str_chain(test_words)
