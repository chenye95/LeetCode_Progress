"""
Given two words word_1 and word_2, find the minimum number of operations required to convert word_1 to word_2.

You have the following 3 operations permitted on a word:
- Insert a character
- Delete a character
- Replace a character
"""


def min_edit_distance(word_1: str, word_2: str) -> int:
    """
    Dynamic Programming Approach, uses current_iteration and last_iteration to replace 2D table.
    Compute Edit Distance between word_1[:i] and word[:j]

    :return: edit distance between word_1 and word_2
    """
    m, n = len(word_1), len(word_2)
    # Initialize to Edit Distance between '' and word_2[:j], i.e. j-1
    last_iteration = list(range(n + 1))

    for i in range(1, len(word_1) + 1):
        # Edit Distance between word_1[:i] and word[:j]
        # Initialize everything to Edit Distance between word_1[:i] and '' = i
        current_iteration = [i] * (n + 1)
        for j in range(1, len(word_2) + 1):
            if word_1[i - 1] == word_2[j - 1]:
                # character match up, nothing to be done here
                # inherit the Edit Distance from (word_1[:i-1], word_2[:j-1])
                current_iteration[j] = last_iteration[j - 1]
            else:
                # Try Insert, Delete, Replace in that order
                current_iteration[j] = 1 + min(last_iteration[j], current_iteration[j - 1], last_iteration[j - 1])
        last_iteration = current_iteration
    return last_iteration[-1]


test_cases = [("horse", "ros", 3),
              ("intention", "execution", 5), ]
for test_word_1, test_word_2, expected_output in test_cases:
    assert min_edit_distance(word_1=test_word_1, word_2=test_word_2) == expected_output
