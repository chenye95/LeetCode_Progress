"""
You want to form a target string of lowercase letters.

At the beginning, your sequence is target.length '?' marks.  You also have a stamp of lowercase letters.

On each turn, you may place the stamp over the sequence, and replace every letter in the sequence with the corresponding
 letter from the stamp.  You can make up to 10 * target.length turns.

For example, if the initial sequence is "?????", and your stamp is "abc",  then you may make "abc??", "?abc?", "??abc"
in the first turn.  (Note that the stamp must be fully contained in the boundaries of the sequence in order to stamp.)

If the sequence is possible to stamp, then return an array of the index of the left-most letter being stamped at each
turn.  If the sequence is not possible to stamp, return an empty array.

For example, if the sequence is "ababc", and the stamp is "abc", then we could return the answer [0, 2], corresponding
to the moves "?????" -> "abc??" -> "ababc".

Also, if the sequence is possible to stamp, it is guaranteed it is possible to stamp within 10 * target.length moves.
Any answers specifying more than this number of moves will not be accepted.
"""
from collections import deque
from typing import List


def move_to_stamp_backward(stamp: str, target: str) -> List[int]:
    """
    Move backwards: from target remove stamps to get the initial blank string

    :param stamp: letters added/overwrote others after each stamp
    :param target: desired string after all stamping
    :return: positions of stamping, in sequence, to get target string
    """
    len_stamp, len_target = len(stamp), len(target)

    removal_character = deque()
    removed = [False] * len_target
    stamp_order_reversed = []

    outstanding_window = []

    for i in range(len_target - len_stamp + 1):
        # i is start of each window of len(stamp)
        # outstanding_window[i] will store info on matched characters in the window

        matched, not_yet = set(), set()
        window_string = target[i: i + len_stamp]
        for j, c in enumerate(stamp):
            if c == window_string[j]:
                matched.add(i + j)
            else:
                not_yet.add(i + j)
        outstanding_window.append((matched, not_yet))

        # if we can reverse stamp at i immediately
        # enqueue letters from outstanding_window[i] to removal_character
        if not not_yet:
            stamp_order_reversed.append(i)
            for i_plus_j in range(i, i + len_stamp):
                if not removed[i_plus_j]:
                    removal_character.append(i_plus_j)
                    removed[i_plus_j] = True

    # For each queued letter
    while removal_character:
        i_plus_j = removal_character.popleft()

        # Update all windows that might be impacted by the removal
        for i in range(max(i_plus_j - len_stamp + 1, 0), min(i_plus_j, len_target - len_stamp) + 1):
            if i_plus_j in outstanding_window[i][1]:
                # i_plus_j is marked as not_yet in window[i]
                outstanding_window[i][1].discard(i_plus_j)

                if not outstanding_window[i][1]:
                    stamp_order_reversed.append(i)
                    for new_matched_c in outstanding_window[i][0]:
                        removal_character.append(new_matched_c)
                        removed[new_matched_c] = True

    return stamp_order_reversed[::-1] if all(removed) else []


def move_to_stamp_dfs(stamp: str, target: str) -> List[int]:
    """
    Depth first search with memorization approach

    :param stamp: letters added/overwrote others after each stamp
    :param target: desired string after all stamping
    :return: positions of stamping, in sequence, to get target string
    """
    # (position_s, position_t) -> sequence of stamps before matching stamp[position_s] to target[position_t]
    memory = {}
    len_stamp, len_target = len(stamp), len(target)

    def depth_first_search(position_s: int, position_t, partial_sequence: List[int]) -> List[int]:
        if position_t == len_target:
            # stamp[-1] has to be equal to target[-1]
            memory[(position_s, position_t)] = partial_sequence if position_s == len_stamp else []
        elif (position_s, position_t) not in memory:
            if position_s == len_stamp:
                # try any position_s_i that stamp[position_s_i] == target[position_t]
                # stamp at index position_t - position_s_i at the beginning of the sequence
                # so that stamp[:position_s_i] will be overwritten by "later" stamps
                # and we move forward to (position_s_i, position_t)
                is_cached = False
                for position_s_i in range(0, len_stamp):
                    if stamp[position_s_i] == target[position_t]:
                        candidate_sequence = depth_first_search(position_s_i, position_t,
                                                                [position_t - position_s_i] + partial_sequence)
                        if candidate_sequence:
                            is_cached = True
                            memory[(position_s, position_t)] = candidate_sequence
                            break
                if not is_cached:
                    memory[(position_s, position_t)] = []
            elif target[position_t] == stamp[position_s]:
                # previous stamp covers up to position_t in target, try explore position_t + 1 with no additional stamp
                candidate_sequence = depth_first_search(position_s + 1, position_t + 1, partial_sequence)
                if candidate_sequence:
                    memory[(position_s, position_t)] = candidate_sequence
                elif position_t + 1 < len_target and stamp[0] == target[position_t + 1]:
                    # or stamp one more time at position_t + 1
                    # if stamp[0] != target[t+1], there is no way to stamp without overwriting previous stamped sequence
                    memory[(position_s, position_t)] = depth_first_search(0, position_t + 1,
                                                                          partial_sequence + [position_t + 1])
                else:
                    memory[(position_s, position_t)] = []
            else:
                # previous stamp does not cover position_t in target
                # need to retrace and stamp one more time before position_t
                memory[(position_s, position_t)] = []

        return memory[(position_s, position_t)]

    if stamp[0] != target[0] or stamp[-1] != target[-1]:
        # stamp[0] has to match target[0]
        return []

    return depth_first_search(0, 0, [0])


def test_simulator(stamp: str, stamp_sequence: List[int], total_len: int) -> str:
    """
    Simulate stamping stamp in stamp_sequence order

    :param stamp: string on the stamp
    :param stamp_sequence: sequence of stamps, marked by position of stamp start
    :return: string after all stamping
    """
    if not stamp_sequence:
        return "NO_STAMP"
    return_str = [''] * total_len
    for start_i in stamp_sequence:
        for j, c in enumerate(stamp):
            return_str[start_i + j] = c
    return ''.join(return_str)


test_cases = [("abc", "ababc"), ("abca", "aabcaca"), ("ffebb", "fffeffebbb"), ("t", "t" * 100), ]
for move_to_stamp in [move_to_stamp_dfs, move_to_stamp_backward, ]:
    for test_stamp, test_target in test_cases:
        assert test_simulator(stamp=test_stamp,
                              stamp_sequence=move_to_stamp(stamp=test_stamp, target=test_target),
                              total_len=len(test_target)) == test_target, move_to_stamp.__name__
