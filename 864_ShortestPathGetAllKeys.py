"""
We are given a 2-dimensional grid. "." is an empty cell, "#" is a wall, "@" is the starting point, ("a", "b", ...) are
 keys, and ("A", "B", ...) are locks.

We start at the starting point, and one move consists of walking one space in one of the 4 cardinal directions.  We
 cannot walk outside the grid, or walk into a wall.  If we walk over a key, we pick it up.  We can't walk over a lock
 unless we have the corresponding key.

For some 1 <= K <= 6, there is exactly one lowercase and one uppercase letter of the first K letters of the English
 alphabet in the grid.  This means that there is exactly one key for each lock, and one lock for each key; and also that
 the letters used to represent the keys and locks were chosen in the same order as the English alphabet.

Return the lowest number of moves to acquire all keys.  If it's impossible, return -1.
"""
from collections import deque
from typing import List


def shortest_path_all_keys(grid: List[str]) -> int:
    """
    :param grid: 1 <= len(grid), len(grid[0]) <= 30,
        contains only '.' (empty cell), '#' (wall), '@' (starting point),
            ('a', ..., 'f') are can_step_on, ('A', ..., 'F') are locks
    :return: lowest number of moves to acquire all can_step_on, or -1 if not possible
    """
    _key_string = "abcdef"
    _initial_allowed = ".@" + _key_string

    m, n = len(grid), len(grid[0])
    num_of_keys = 0
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited_states = set()

    start_x = start_y = -1
    for x in range(m):
        for y in range(n):
            if grid[x][y] == '@':
                start_x, start_y = x, y
            elif grid[x][y] in _key_string:
                num_of_keys += 1

    move_deque = deque([(start_x, start_y, 0, "")])
    while move_deque:
        x, y, num_steps, unlocked_str = move_deque.popleft()
        if grid[x][y] in _key_string and grid[x][y].upper() not in unlocked_str:
            unlocked_str = ''.join(sorted(unlocked_str + grid[x][y].upper()))

        if len(unlocked_str) == num_of_keys:
            return num_steps

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < m and 0 <= ny < n and (grid[nx][ny] in unlocked_str or grid[nx][ny] in _initial_allowed):
                if (nx, ny, unlocked_str) not in visited_states:
                    visited_states.add((nx, ny, unlocked_str))
                    move_deque.append((nx, ny, num_steps + 1, unlocked_str))

    return -1


test_cases = [(["@.a.#", "###.#", "b.A.B"], 8),
              (["@..aA", "..B#.", "....b"], 6),
              ([".#.....#..#....",
                "..#..#..#...#..",
                "..#......#...#.",
                "#.#.#.......###",
                ".a.#....#.....#",
                "#.#.#....#..##.",
                "..........#..#.",
                "..@.#.#...#.#..",
                "..#.#.#........",
                "##..#.#..#....#",
                "#.......#......",
                "....##.........",
                "....##..#......",
                "#....#A........",
                "...##.....##..#"], 4),
              (["#..#.#.#..#.#.#.....#......#..",
                ".#.......#....#A.....#.#......",
                "#....#.....#.........#........",
                "...#.#.........#..@....#....#.",
                ".#.#.##...#.........##....#..#",
                "..........#..#..###....##..#.#",
                ".......#......#...#...#.....c#",
                ".#...#.##......#...#.###...#..",
                "..........##...#.......#......",
                "#...#.........a#....#.#.##....",
                "..#..#...#...#..#....#.....##.",
                "..........#...#.##............",
                "...#....#..#.........#..D.....",
                "....#E.#....##................",
                "...........##.#.......#.#....#",
                "...#..#...#.#............#e...",
                "..#####....#.#...........##..#",
                "##......##......#.#...#..#.#..",
                ".#F.......#..##.......#....#..",
                "............#....#..#..#...#..",
                ".............#...#f...#..##...",
                "....#..#...##.........#..#..#.",
                ".....#.....##.###..##.#......#",
                ".#..#.#...#.....#........###..",
                ".....#.#...#...#.....#.....#..",
                "##.....#....B.....#..#b.......",
                ".####....##..#.##..d.#......#.",
                "..#.....#....##........##...##",
                "...#...#...C..#..#....#.......",
                "#.....##.....#.#......#......."], 70), ]
for test_grid, expected_steps in test_cases:
    assert shortest_path_all_keys(test_grid) == expected_steps
