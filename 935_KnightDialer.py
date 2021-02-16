"""
The chess knight has a unique movement, it may move two squares vertically and one square horizontally, or two squares
horizontally and one square vertically (with both forming the shape of an L).

We have a chess knight and a phone pad, the knight can only stand on a numeric cell

Given an integer n, return how many distinct phone numbers of length n we can dial.
"""


def knight_dialer(n: int) -> int:
    mod_val = 10 ** 9 + 7
    movement_map = [[4, 6], [6, 8], [7, 9], [4, 8], [3, 9, 0], [], [1, 7, 0], [2, 6], [1, 3], [2, 4]]

    dp_current = [1] * 10
    for _ in range(n - 1):
        dp_next = [0] * 10
        for current_no, move_count in enumerate(dp_current):
            for next_no in movement_map[current_no]:
                dp_next[next_no] += move_count
                dp_next[next_no] %= mod_val

        dp_current = dp_next

    return sum(dp_current) % mod_val


test_cases = [(1, 10),
              (2, 20),
              (3, 46),
              (4, 104),
              (3131, 136_006_598)]
for test_input, expected_output in test_cases:
    assert knight_dialer(test_input) == expected_output
