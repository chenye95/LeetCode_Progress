"""
You are given an array of strings of the same length words.

In one move, you can swap any two even indexed characters or any two odd indexed characters of a string words[i].

Two strings words[i] and words[j] are special-equivalent if after any number of moves, words[i] == words[j].

For example, words[i] = "zzxy" and words[j] = "xyzz" are special-equivalent because we may make the moves
 "zzxy" -> "xzzy" -> "xyzz".
A group of special-equivalent strings from words is a non-empty subset of words such that:

Every pair of strings in the group are special equivalent, and
The group is the largest size possible (i.e., there is not a string words[i] not in the group such that words[i] is
 special-equivalent to every string in the group).
Return the number of groups of special-equivalent strings from words.
"""
from typing import List


def num_special_equivalent(words: List[str]) -> int:
    return len({"".join(sorted(word_i[0::2])) + "".join(sorted(word_i[1::2])) for word_i in words})


test_cases = [
    (["abcd", "cdab", "cbad", "xyzz", "zzxy", "zzyx"], 3),
    (["abc", "acb", "bac", "bca", "cab", "cba"], 3),
    (["n", "e", "c", "h", "y", "y", "y", "v", "p", "c", "w", "p", "j", "z", "z", "o", "o", "v", "x", "o", "c", "e", "a",
      "l", "s", "k", "s", "e", "u", "f", "m", "z", "v", "j", "s", "s", "u", "s", "w", "v", "f", "v", "y", "z", "j", "c",
      "s", "p", "e", "v", "y", "z", "j", "c", "j", "v", "p", "s", "o", "s", "j", "c", "n", "u", "o", "c", "e", "j", "c",
      "c", "l", "z", "j", "v", "s", "s", "w", "v", "o", "e", "w", "z", "k", "c", "v", "l", "p", "c", "j", "j", "c", "c",
      "o", "j", "c", "e", "j", "c", "o", "e", "e", "c", "o", "c", "l", "j", "m", "f", "e", "e", "m", "l", "y", "v", "l",
      "c", "u", "s", "c", "w", "s", "w", "l", "c", "s", "w", "w", "e", "y", "l", "p", "l", "j", "e", "z", "s", "z", "m",
      "s", "m", "z", "e", "v", "j", "o", "c", "c", "n", "c", "j", "m", "s", "c", "v", "c", "c", "l", "w", "e", "j", "z",
      "s", "j", "c", "j", "e", "m", "w", "v", "c", "v", "j", "j", "s", "c", "z", "j", "s", "c", "n", "e", "c", "j", "o",
      "s", "v", "u", "u", "o", "l", "c", "e", "s", "c", "l", "m", "c", "c", "u", "e", "e", "w", "n", "c", "s", "p", "v",
      "z", "u", "u", "v", "o", "c", "y", "u", "w", "w", "c", "c", "n", "s", "c", "e", "c", "e", "e", "n", "c", "j", "w",
      "v", "s", "m", "o", "e", "s", "o", "m", "c", "j", "w", "e", "u", "c", "j", "s", "s", "c", "o", "c", "c", "l", "c",
      "v", "j", "w", "m", "k", "c", "c", "c", "s", "s", "s", "n", "s", "o", "c", "o", "c", "n", "c", "o", "j", "j", "k",
      "e", "m", "v", "y", "n", "k", "v", "f", "j", "e", "e", "c", "c", "y", "c", "c", "c", "l", "y", "j", "s", "s", "c",
      "v", "e", "u", "o", "s", "o", "j", "y", "c", "v", "u", "s", "y", "c", "s", "l", "v", "j", "c", "z", "j", "u", "s",
      "p", "c", "o", "e", "c", "s", "e", "u", "v", "u", "a", "c", "c", "z", "y", "c", "j", "p", "n", "y", "m", "v", "m",
      "u", "u", "c", "j", "e", "w", "e", "p", "c", "c", "j", "c", "j", "c", "e", "o", "y", "y", "e", "v", "j", "c", "u",
      "s", "c", "e", "y", "z", "y", "n", "m", "e", "e", "v", "x", "c", "c", "v", "w", "o", "n", "n", "u", "j", "e", "s",
      "v", "l", "c", "o", "u", "j", "v", "w", "e", "y", "v", "z", "l", "c", "m", "c", "v", "u", "s", "x", "l", "m", "e",
      "o", "c", "s", "e", "m", "j", "j", "v", "x", "o", "z", "s", "o", "c", "c", "j", "c", "o", "z", "w", "l", "e", "e",
      "s", "c", "p", "c", "c", "c", "j", "m", "o", "n", "l", "y", "c", "c", "o", "o", "e", "e", "s", "v", "u", "e", "s",
      "c", "j", "v", "e", "c", "c", "j", "m", "c", "v", "e", "u", "m", "j", "e", "s", "y", "c", "m", "c", "c", "e", "c",
      "c", "c", "v", "z", "u", "u", "c", "c", "c", "l", "v", "c", "n", "s", "c", "v", "u", "j", "c", "l", "v", "j", "j",
      "j", "j", "e", "m", "c", "v", "o", "j", "s", "m", "j", "u", "c", "n", "e", "y", "w", "m", "c", "c", "c", "e", "y",
      "s", "y", "e", "o", "o", "o", "c", "l", "e", "y", "z", "y", "m", "m", "c", "u", "c", "u", "c", "l", "s", "y", "j",
      "y", "o", "v", "w", "y", "s", "o", "s", "z", "c", "o", "c", "s", "l", "p", "c", "y", "u", "o", "e", "v", "z", "n",
      "u", "s", "x", "c", "u", "l", "c", "l", "c", "m", "j", "c", "s", "y", "w", "v", "c", "c", "c", "c", "m", "e", "c",
      "c", "y", "c", "c", "e", "u", "n", "v", "j", "o", "n", "z", "u", "c", "s", "o", "c", "e", "v", "c", "j", "c", "e",
      "e", "j", "s", "p", "y", "c", "p", "w", "n", "j", "e", "s", "p", "s", "n", "v", "y", "c", "c", "m", "j", "s", "c",
      "s", "y", "c", "c", "j", "s", "e", "v", "s", "c", "w", "f", "e", "y", "p", "m", "e", "z", "c", "c", "c", "v", "j",
      "e", "v", "c", "p", "c", "v", "n", "y", "c", "u", "m", "n", "s", "s", "v", "o", "p", "j", "e", "c", "e", "u", "j",
      "x", "j", "v", "v", "m", "m", "v", "v", "y", "j", "c", "e", "l", "s", "j", "y", "c", "u", "o", "e", "j", "y", "l",
      "c", "s", "j", "v", "n", "x", "m", "s", "y", "s", "s", "u", "w", "e", "s", "j", "l", "c", "w", "m", "c", "c", "o",
      "u", "s", "o", "p", "c", "u", "p", "j", "z", "c", "s", "j", "s", "c", "e", "p", "m", "j", "s", "c", "p", "e", "p",
      "c", "c", "v", "e", "c", "c", "s", "c", "o", "c", "j", "o", "v", "c", "u", "y", "z", "w", "s", "j", "e", "c", "c",
      "o", "n", "z", "p", "v", "s", "c", "j", "v", "e", "v", "u", "s", "c", "y", "y", "v", "y", "c", "j", "m", "v", "c",
      "e", "c", "c", "s", "c", "j", "c", "n", "u", "n", "e", "e", "n", "c", "y", "s", "c", "j", "o", "c", "s", "v", "n",
      "n", "s", "v", "y", "z", "c", "o", "u", "c", "v", "n", "c", "o", "e", "p", "y", "v", "n", "o", "m", "y", "o", "s",
      "o", "j", "j", "p", "c", "j", "e", "v", "y", "j", "c", "e", "o", "s", "z", "n", "n", "e", "l", "z", "c", "c", "c",
      "c", "p", "v", "y", "c", "s", "u", "j", "l", "c", "z", "o", "o", "n", "c", "x", "o", "x", "s", "z", "c", "s", "z",
      "c", "m", "s", "c", "y", "j", "c", "c", "e", "c", "c", "w", "y", "c", "v", "c", "w", "c", "y", "w", "w", "c", "c",
      "u", "s", "c", "n", "u", "c", "j", "p", "u", "c", "s", "c", "p", "c", "s", "s", "c", "z", "c", "y", "e", "c", "o",
      "p", "j", "e", "v", "c", "c", "j", "v", "e", "m", "c", "u", "s", "m", "s", "y", "y", "y", "c", "s", "u", "c", "u",
      "y", "e", "s", "j", "e", "c", "o", "e", "j", "p", "y", "j", "c", "o", "v", "c", "c", "c", "j", "v", "w", "e", "c",
      "n", "u", "l", "n", "z", "s", "f", "s", "c", "s", "j"], 19),
    (["u", "u", "u", "u", "u", "u", "u", "u", "u", "u"], 1),
]
for test_words, expected_value in test_cases:
    assert num_special_equivalent(test_words) == expected_value
