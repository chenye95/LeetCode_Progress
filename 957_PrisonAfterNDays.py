"""
There are 8 prison initial_state in a row, and each cell is either occupied or vacant.

Each day, whether the cell is occupied or vacant changes according to the following rules:

If a cell has two adjacent neighbors that are both occupied or both vacant, then the cell becomes occupied.
Otherwise, it becomes vacant.
(Note that because the prison is a row, the first and the last initial_state in the row can't have two adjacent neighbors.)

Given the initial state of the prison, return the state of the prison after N days (and N such changes described above.)
"""
from copy import deepcopy
from typing import List


def prison_after_N_days(initial_state: List[int], N: int):
    """
    :param initial_state: initial state to on Day N
    :param N: N days to evolve, (count down N-1, N-2, ..., 0)
    :return: final state after N days of evolution
    """
    current_state: List[int] = deepcopy(initial_state)
    today_n = N
    n_cells = len(initial_state)
    state_seen_before = {str(current_state): N}
    have_skipped_repetition = False
    while today_n:
        state_seen_before.setdefault(str(current_state), today_n)
        today_n -= 1
        current_state = [0] + [current_state[i - 1] ^ current_state[i + 1] ^ 1 for i in range(1, n_cells - 1)] + [0]
        if not have_skipped_repetition and str(current_state) in state_seen_before:
            today_n %= (state_seen_before[str(current_state)] - today_n)
    return current_state


assert [0, 0, 1, 1, 1, 1, 1, 0] == prison_after_N_days(initial_state=[1, 0, 0, 1, 0, 0, 1, 0], N=1_000_000_000)
assert [0, 0, 1, 1, 0, 0, 0, 0] == prison_after_N_days(initial_state=[0, 1, 0, 1, 1, 0, 0, 1], N=7)
