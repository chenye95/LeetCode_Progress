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
              ([[1, 3], [3, 0, 1], [2], [0]], False), ]
for can_visit_all_rooms in [can_visit_all_rooms_stack, can_visit_all_rooms_set]:
    for test_input, expected_output in test_cases:
        assert can_visit_all_rooms(test_input) is expected_output
