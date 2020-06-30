"""
Given an equation, represented by words on left side and the result on right side.

You need to check if the equation is solvable under the following rules:
- Each character is decoded as one digit (0 - 9).
- Every pair of different characters they must map to different digits.
- Each words[i] and result are decoded as one number without leading zeros.
- Sum of numbers on left side (words) will equal to the number on right side (result).

Return True if the equation is solvable otherwise return False.
"""
from typing import List


def isSolvable(words: List[str], result: str) -> bool:
    def try_position_i(position_i: int, word_j: int, carry: int):
        # Exceeds the length of result, needs to check no leading 0s
        if position_i == len(result):
            return carry == 0 and all(assignment[word[len(word) - 1]] != 0 for word in words + [result])

        # All position_i have been assigned, check position_i sum match up with result[position_i]
        if word_j == len(words):
            # position_i result has been assigned, so check validity and proceed to position_i+1
            if result[position_i] in assignment:
                return carry % 10 == assignment[result[position_i]] and try_position_i(position_i + 1, 0, carry // 10)
            # Can not reuse already assigned values or place leading 0
            elif (carry % 10) in assignment.values() or (carry % 10 == 0 and position_i == len(result) - 1):
                return False
            assignment[result[position_i]] = carry % 10
            next_position_solvable = try_position_i(position_i + 1, 0, carry // 10)
            del assignment[result[position_i]]
            return next_position_solvable

        # position_i of word_j doesn't exist or has been assigned
        if position_i >= len(words[word_j]) or words[word_j][position_i] in assignment:
            add_position_i = 0 if position_i >= len(words[word_j]) else assignment[words[word_j][position_i]]
            return try_position_i(position_i, word_j + 1, carry + add_position_i)

        # Try to assign position_i of word_j
        for val in range(10):
            # Can not reuse already used values or place leading 0
            if (val != 0 or position_i != len(words[word_j]) - 1) and val not in assignment.values():
                assignment[words[word_j][position_i]] = val
                next_position_solvable = try_position_i(position_i, word_j + 1, carry + val)
                if next_position_solvable:
                    return True
                del assignment[words[word_j][position_i]]

        return False

    if len(result) < max(map(len, words)):
        return False
    result = result[::-1]
    words = [w[::-1] for w in words]
    assignment = dict()
    return try_position_i(0, 0, 0)


assert isSolvable(words=["SEND", "MORE"], result="MONEY") is True
assert isSolvable(words=["SIX", "SEVEN", "SEVEN"], result="TWENTY") is True
assert isSolvable(words=["THIS", "IS", "TOO"], result="FUNNY") is True
assert isSolvable(words=["LEET", "CODE"], result="POINT") is False
