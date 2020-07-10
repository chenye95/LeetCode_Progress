"""
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character
"""


def minDistance(word1: str, word2: str) -> int:
    """
    Dynamic Programming Approach, uses current_iteration and last_iteration to replace 2D table
    Compute Edit Distance between word1[:i] and word[:j]
    :return: edit distance between word1 and word2
    """
    m, n = len(word1), len(word2)
    # Initialize to Edit Distance between '' and word2[:j], i.e. j-1
    last_iteration = list(range(n + 1))

    for i in range(1, len(word1) + 1):
        # Edit Distance between word1[:i] and word[:j]
        # Initialize everything to Edit Distance between word1[:i] and '' = i
        current_iteration = [i] * (n + 1)
        for j in range(1, len(word2) + 1):
            if word1[i - 1] == word2[j - 1]:
                # character match up, nothing to be done here
                # inherit the Edit Distance from (word1[:i-1], word2[:j-1])
                current_iteration[j] = last_iteration[j - 1]
            else:
                # Try Insert, Delete, Replace in that order
                current_iteration[j] = 1 + min(last_iteration[j], current_iteration[j - 1], last_iteration[j - 1])
        last_iteration = current_iteration
    return last_iteration[-1]


assert minDistance(word1="horse", word2="ros") == 3
assert minDistance(word1="intention", word2="execution") == 5
