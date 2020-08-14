"""
Given a non-empty string s and a dictionary word_dict containing a list of non-empty words, add spaces in s to construct
 a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.
"""
from typing import List


def word_break(s: str, word_dict: List[str]) -> List[str]:
    """
    :param s: string to break down into words
    :param word_dict: acceptable words in the dict
    :return:
    """
    beginning_letters = {w[0] for w in word_dict}
    memory = {len(s): [""]}

    def split_into_sentences(start_at: int) -> List[str]:
        """
        Depth First Search with Memorization
        :return split s[start_at:] into list of words
        """
        nonlocal memory, beginning_letters
        if start_at not in memory:
            if s[start_at] not in beginning_letters:
                return []
            # if tail is not empty add blank in front, else just add tail
            memory[start_at] = [s[start_at:end_at] + (tail and " " + tail)
                                for end_at in range(start_at + 1, len(s) + 1)
                                if s[start_at:end_at] in word_dict
                                for tail in split_into_sentences(end_at)]
        return memory[start_at]

    return split_into_sentences(0)


assert word_break(s="catsanddog", word_dict=["cat", "cats", "and", "sand", "dog"]) == ['cat sand dog', 'cats and dog']
