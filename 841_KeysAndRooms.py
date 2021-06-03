"""
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have
 some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N =
rooms.length.  A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.
"""
from typing import List


def can_visit_all_rooms_set(rooms: List[List[int]]) -> bool:
    """
    :param rooms: keys stored in each room, where rooms[i] is a subset of [0, 1, ..., N-1]
    :return: if we can enter every room
    """
    to_visit = set(range(1, len(rooms)))
    opening = {0}
    while to_visit and opening:
        to_visit -= opening
        to_open = set()
        for room_i in opening:
            to_open |= set(rooms[room_i])
        opening = to_open & to_visit

    return not to_visit


def can_visit_all_rooms_stack(rooms: List[List[int]]) -> bool:
    """
    :param rooms: keys stored in each room, where rooms[i] is a subset of [0, 1, ..., N-1]
    :return: if we can enter every room
    """
    visited = set()
    to_open = [0]
    while to_open:
        current_room = to_open.pop()
        visited.add(current_room)
        for next_room in rooms[current_room]:
            if next_room not in visited:
                to_open.append(next_room)
    return len(visited) == len(rooms)


test_cases = [([[1], [2], [3], []], True),
              ([[1, 3], [3, 0, 1], [2], [0]], False),
              ([[94], [], [], [], [26], [59], [], [19], [], [], [], [32, 42, 71], [], [25, 38], [74], [], [],
                [8, 23, 39, 48, 77], [31], [], [], [], [72, 78], [97], [34], [61], [], [4, 50], [87], [], [53], [], [],
                [], [24, 54, 83], [27], [1, 33], [22], [18, 41, 49], [69], [], [], [], [], [], [3, 86], [57], [13, 62],
                [20, 95], [], [], [], [2, 29, 40, 84, 99], [], [75], [14], [], [43, 64, 66], [51], [], [79], [98],
                [6, 28, 70, 82], [10], [], [], [], [68], [47, 52], [5, 73, 80], [], [17, 35, 46], [55], [12, 67],
                [11, 44, 76, 92], [63], [7, 45], [37], [], [60], [16, 21, 81], [65, 90], [93], [], [], [], [], [58],
                [96], [30], [15], [56, 88], [], [], [89], [85], [36], [9], [91], []], False),
              ([[95, 99, 46, 82, 22, 97], [12], [26, 78], [41], [69, 43], [17, 35], [19], [91, 20], [78, 92],
                [71, 8, 68], [4, 79, 54, 19, 46], [16], [24, 23, 63, 89], [11, 27, 81], [55, 8, 31, 45, 71, 91],
                [33, 6, 67], [56, 9, 88, 47], [51, 80], [40, 49, 80, 86, 70, 98], [38, 53, 35], [6, 22, 74],
                [44, 90, 23], [97, 29, 13, 62], [2, 26, 60, 61, 86, 1, 17], [59], [64], [81, 19, 7, 9, 41],
                [13, 40, 87], [18, 20], [14, 36, 89], [25, 28, 32, 57, 87], [48, 65, 81, 29], [43, 79], [75, 16],
                [29, 65, 73], [67], [57, 24, 26, 34], [66, 64, 97], [16, 93], [44, 63, 80, 12], [9, 21, 83, 90], [],
                [64, 39, 59], [57, 53, 59, 25], [37, 33], [85, 24, 52], [35, 28, 31, 99, 18, 55, 86], [23, 84],
                [92, 91, 96], [38, 62, 14], [10, 72], [12, 20, 62, 15, 36, 85, 65], [27, 88, 41, 58, 77], [14, 49, 15],
                [22, 73], [66, 6, 32], [11, 71, 67, 82], [8], [47, 68, 93, 40, 61], [25, 58], [76, 28],
                [17, 84, 98, 42, 51], [42, 75], [58, 92], [], [5, 37], [90], [30, 34, 21, 54, 79], [52, 96],
                [31, 87, 3, 56], [39, 54, 2], [83], [37, 69, 89, 95, 60, 96], [45, 56, 98, 53, 84], [], [5],
                [21, 45, 55], [3, 34, 36, 74], [5, 15, 10, 88], [38], [46, 77, 99], [50, 3], [60, 72, 2, 30, 66, 76],
                [7, 32, 77, 27, 44], [94], [61, 93], [73, 74, 4, 70, 95], [18, 82, 68, 94, 75], [1, 48],
                [78, 50, 4, 51], [39, 42], [30, 47, 52, 49, 50, 72], [48, 70, 1], [13, 33, 11], [], [], [10, 7, 85],
                [63], [43, 94], [76, 83, 69]], True), ]
for can_visit_all_rooms in [can_visit_all_rooms_stack, can_visit_all_rooms_set]:
    for test_input, expected_output in test_cases:
        assert can_visit_all_rooms(test_input) is expected_output
