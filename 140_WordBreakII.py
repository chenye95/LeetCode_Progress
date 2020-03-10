"""
Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, add spaces in s to construct
 a sentence where each word is a valid dictionary word. Return all such possible sentences.

Note:
- The same word in the dictionary may be reused multiple times in the segmentation.
- You may assume the dictionary does not contain duplicate words.
"""
from typing import List


def wordBreak(s: str, wordDict: List[str]) -> List[str]:
    beginning_letters = set([w[0] for w in wordDict])
    memory = {len(s): [""]}
    def split_into_sentences(i: int) -> List[str]:
        """
        Depth First Search with Memorization
        :return split s[:i] into list of words
        """
        if i not in memory:
            if s[i] not in beginning_letters:
                return []
            memory[i] = [s[i:j] + (tail and " " + tail)  # if tail is not empty add blank in front, else just add tail
                         for j in range(i+1, len(s)+1)
                         if s[i:j] in wordDict
                         for tail in split_into_sentences(j)]
        return memory[i]
    return split_into_sentences(0)


assert wordBreak(s="catsanddog", wordDict=["cat", "cats", "and", "sand", "dog"]) == ['cat sand dog', 'cats and dog']
