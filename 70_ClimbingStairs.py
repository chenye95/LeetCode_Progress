"""
You are climbing a stair case. It takes n steps to reach to the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
"""


def climb_stairs(n: int) -> int:
    """
    :param n: n stair cases in total
    :return: distinct ways to climb to the top when each step is 1 or 2 stair cases
    """
    if n <= 2:
        return n
    two_steps = one_step = current_step = 1
    for _ in range(1, n):
        current_step = two_steps + one_step
        two_steps = one_step
        one_step = current_step
    return current_step


assert climb_stairs(2) == 2
assert climb_stairs(3) == 3
