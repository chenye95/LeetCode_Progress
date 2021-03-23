"""
Given a word_list, we want to implement a spellchecker that converts a query word into a correct word.

For a given query word, the spell checker handles two categories of spelling mistakes:
- Capitalization: If the query matches a word in the word_list (case-insensitive), then the query word is returned with
the same case as the case in the word_list.
- Vowel Errors: If after replacing the vowels ('a', 'e', 'i', 'o', 'u') of the query word with any vowel individually,
it matches a word in the word_list (case-insensitive), then the query word is returned with the same case as the match in the word_list.

In addition, the spell checker operates under the following precedence rules:
- When the query exactly matches a word in the word_list (case-sensitive), you should return the same word back.
- When the query matches a word up to capitalization, you should return the first such match in the word_list.
- When the query matches a word up to vowel errors, you should return the first such match in the word_list.

If the query has no matches in the word_list, you should return the empty string.

Given some queries, return a list of words answer, where answer[i] is the correct word for query = queries[i].
"""
from typing import List


def vowel_spellchecker(word_list: List[str], queries: List[str]) -> List[str]:
    """
    :param word_list: a list of string to match to
    :param queries: list of words to match against
    :return: closest match for each query_word in queries
    """

    def de_vowel(word_pre_lower: str) -> str:
        """
        :return: replace vowels e i o u with letter a
        """
        return word_pre_lower.replace('e', 'a').replace('i', 'a').replace('o', 'a').replace('u', 'a')

    def solve_query(query_word: str) -> str:
        """
        :return: closest match in word_list for query_word
        """
        if query_word in word_perfect_match:
            return query_word

        query_word_lower = query_word.lower()
        if query_word_lower in word_capitalization:
            return word_capitalization[query_word_lower]

        return word_vowel.get(de_vowel(query_word_lower), "")

    word_perfect_match = set(word_list)
    word_capitalization = dict()
    word_vowel = dict()

    for word in word_list:
        word_lower = word.lower()
        word_capitalization.setdefault(word_lower, word)
        word_vowel.setdefault(de_vowel(word_lower), word)

    return list(map(solve_query, queries))


assert vowel_spellchecker(word_list=["yellow"], queries=["YellOw"]) == ["yellow"]
assert vowel_spellchecker(word_list=["Yellow"], queries=["yellow"]) == ["Yellow"]
assert vowel_spellchecker(word_list=["yellow"], queries=["yellow"]) == ["yellow"]
assert vowel_spellchecker(word_list=["Yellow"], queries=["yollow"]) == ["Yellow"]
assert vowel_spellchecker(word_list=["Yellow"], queries=["yeellow"]) == [""]
assert vowel_spellchecker(word_list=["Yellow"], queries=["yllw"]) == [""]
assert vowel_spellchecker(word_list=["KiTe", "kite", "hare", "Hare"],
                          queries=["kite", "Kite", "KiTe", "Hare", "HARE", "Hear", "hear", "keti", "keet", "keto"]) \
       == ["kite", "KiTe", "KiTe", "Hare", "hare", "", "", "KiTe", "", "KiTe"]
