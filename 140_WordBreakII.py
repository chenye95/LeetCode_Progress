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

print(wordBreak(s = "catsanddog", wordDict = ["cat", "cats", "and", "sand", "dog"]))
