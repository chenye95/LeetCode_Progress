"""
You are given an integer array matchsticks where matchsticks[i] is the length of the ith matchstick. You want to use all
 the matchsticks to make one square. You should not break any stick, but you can link them up, and each matchstick must
 be used exactly one time.

Return true if you can make this square and false otherwise.
"""
from typing import List, Dict


def can_make_square_dfs(match_sticks: List[int], n_sides: int = 4) -> bool:
    """
    :param match_sticks: 1 <= len(match_sticks) <= 15 matches with 1 <= match_sticks[i] <= 1e8, to make square
    :param n_sides: default to 4, square
    :return: match sticks can be used to make a square
    """
    if not match_sticks or sum(match_sticks) % n_sides != 0:
        return False

    side_len = sum(match_sticks) // n_sides
    get_len = [0] * n_sides
    n_matches = len(match_sticks)
    match_sticks.sort(reverse=True)

    def put_match(match_i: int) -> bool:
        # DFS recursion function: Try add match_i to one of the n_sides
        if match_i == n_matches:
            return all(len_i == side_len for len_i in get_len)
        for side_i in range(n_sides):
            if get_len[side_i] + match_sticks[match_i] <= side_len:
                get_len[side_i] += match_sticks[match_i]
                if put_match(match_i + 1):
                    return True
                get_len[side_i] -= match_sticks[match_i]
        return False

    return put_match(0)


def can_make_square_simulation(match_sticks: List[int], n_sides: int = 4) -> bool:
    """
    :param match_sticks: 1 <= len(match_sticks) <= 15 matches with 1 <= match_sticks[i] <= 1e8, to make square
    :param n_sides: default to 4, square
    :return: match sticks can be used to make a square
    """
    if not match_sticks or sum(match_sticks) % n_sides != 0:
        return False

    side_len = sum(match_sticks) // n_sides
    n_matches = len(match_sticks)
    memory: Dict[int, bool] = {}

    def build_one_side(used_match_bit: int, side_finished: int, current_side_len: int) -> bool:
        """
        Build the sides of the shape sequentially, using previously unused matches

        :param used_match_bit: binary mask to represent which match is available (1)
        :param side_finished: number of sides finished before placing the last match
        :param current_side_len: sum of all matches used previously mod side_len
        :return: from current state, whether it's possible to finish the square
        """
        if current_side_len == 0:
            side_finished += 1
        if side_finished == n_sides - 1:
            # sum(match_stick) == current_side_len + side_len
            # all remaining matches will form the last side
            return True

        if used_match_bit not in memory:
            # calculate remaining length on current side
            remainder = side_len - current_side_len

            flag_doable = False
            for i, match_len in enumerate(match_sticks):
                bit_i = n_matches - 1 - i
                if match_len <= remainder and used_match_bit & (1 << bit_i):
                    if build_one_side(used_match_bit ^ (1 << bit_i), side_finished,
                                      (current_side_len + match_len) % side_len):
                        flag_doable = True
                        break

            memory[used_match_bit] = flag_doable

        return memory[used_match_bit]

    return build_one_side((1 << n_matches) - 1, -1, 0)


test_cases = [([1, 1, 2, 2, 2], True),
              ([3, 3, 3, 3, 4], False),
              ([1569462, 2402351, 9513693, 2220521, 7730020, 7930469, 1040519, 5767807, 876240, 350944, 4674663,
                4809943, 8379742, 3517287, 8034755], False),
              ([5969561, 8742425, 2513572, 3352059, 9084275, 2194427, 1017540, 2324577, 6810719, 8936380, 7868365,
                2755770, 9954463, 9912280, 4713511], False),
              ([99, 37, 37, 37, 37, 37, 37, 37, 37, 5], False),
              ([5, 5, 5, 5, 4, 4, 4, 4, 3, 3, 3, 3], True),
              ]
for can_make_square in [can_make_square_dfs, can_make_square_simulation, ]:
    for test_match_sticks, expected_value in test_cases:
        assert can_make_square(test_match_sticks) is expected_value, can_make_square.__name__
