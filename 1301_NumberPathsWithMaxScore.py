"""
You are given a square board of characters. You can move on the board starting at the bottom right square marked with the character 'S'.

You need to reach the top left square marked with the character 'E'. The rest of the squares are labeled either with a numeric character 1, 2, ..., 9 or with an obstacle 'X'. In one move you can go up, left or up-left (diagonally) only if there is no obstacle there.

Return a list of two integers: the first integer is the maximum sum of numeric characters you can collect, and the second is the number of such paths that you can take to get that maximum sum, taken modulo 10^9 + 7.

In case there is no path, return [0, 0].
"""

from typing import List


def pathsWithMaxScore(board: List[str]) -> List[int]:
    n = len(board)
    MOD = 10 ** 9 + 7
    invalid = (float('-inf'), 0)

    # Reverse the traversal order, from E to S
    dp_prev_row = [invalid] * n

    for r in range(n):
        dp_curr_row = []
        for c in range(n):
            if board[r][c] == 'E':
                dp_curr_row.append((0, 1))
            elif board[r][c] == 'X':
                dp_curr_row.append(invalid)
            else:
                # move from up
                curr_val, curr_step = dp_prev_row[c]

                if c > 0:
                    # move from left
                    if dp_curr_row[-1][0] == curr_val:
                        curr_step += dp_curr_row[-1][1]
                    elif dp_curr_row[-1][0] > curr_val:
                        curr_val, curr_step = dp_curr_row[-1]

                    # move from up-left
                    if dp_prev_row[c - 1][0] == curr_val:
                        curr_step += dp_prev_row[c - 1][1]
                    elif dp_prev_row[c - 1][0] > curr_val:
                        curr_val, curr_step = dp_prev_row[c - 1]

                curr_val += int(board[r][c]) if board[r][c] not in 'SE' else 0
                curr_step %= MOD
                dp_curr_row.append((curr_val, curr_step))
        dp_prev_row = dp_curr_row

    return list(dp_prev_row[-1]) if dp_prev_row[-1][1] > 0 else [0, 0]


assert pathsWithMaxScore(board=["E23", "2X2", "12S"]) == [7, 1]
assert [1773, 690285631] == pathsWithMaxScore(
    board=["E999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "9999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999",
           "999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999S"])
