"""
Given a string s. Return all the words vertically in the same order in which they appear in s.
Words are returned as a list of strings, complete with spaces when is necessary. (Trailing spaces are not allowed).
Each word would be put on only one column and that in one column there will be only one word.
"""
from typing import List


def printVertically(s: str) -> List[str]:
    words_bank = s.split()
    r, c = max(map(len, words_bank)), len(words_bank)
    return_list = [' ' * c for _ in range(r)]
    running_list = set(range(len(words_bank)))
    i = 0
    while running_list:
        current_line = [' '] * (max(running_list) + 1)
        exhausted_list = set()
        for index in running_list:
            current_line[index] = words_bank[index][i]
            if i == len(words_bank[index]) - 1:
                exhausted_list.add(index)
        return_list[i] = ''.join(current_line)
        running_list -= exhausted_list
        i += 1
    return return_list


assert ["HAY", "ORO", "WEU"] == printVertically(s="HOW ARE YOU")
assert ["TBONTB", "OEROOE", "   T"] == printVertically(s="TO BE OR NOT TO BE")
assert ["CIC", "OSO", "N M", "T I", "E N", "S G", "T"] == printVertically(s="CONTEST IS COMING")
