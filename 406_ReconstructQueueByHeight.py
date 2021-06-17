"""
You are given an array of people, people, which are the attributes of some people in a queue (not necessarily in order).
 Each people[i] = [hi, ki] represents the ith person of height hi with exactly ki other people in front who have a
 height greater than or equal to hi.

Reconstruct and return the queue that is represented by the input array people. The returned queue should be formatted
 as an array queue, where queue[j] = [hj, kj] is the attributes of the jth person in the queue (queue[0] is the person
 at the front of the queue).
"""
from typing import List, Tuple, Optional


def reconstruct_queue_asc_height(people: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    :param people: list of (h_i, k_i) height of person i and number of person taller or equal to h_i in front of him
    :return: reconstructed list of [(h_i, k_i)]
    """
    reconstructed_queue: List[Optional[Tuple[int, int]]] = [None] * len(people)
    # sort people list by ascending order of height h_i, then descending order of k_i
    people.sort(key=lambda person_i: (person_i[0], -person_i[1]))
    free_spot: List[int] = list(range(len(people)))

    for person_i in people:
        # since person_i in ascending order of height,
        # guaranteed every one before him is shorter or equal to him
        # since again in descending order of k_i
        # among persons with the same h_i, the first in the list will appear last in the search
        given_spot = free_spot[person_i[1]]
        reconstructed_queue[given_spot] = person_i
        free_spot.remove(given_spot)

    return reconstructed_queue


def reconstruct_queue_dsc_height(people: List[Tuple[int, int]]) -> List[Tuple[int, int]]:
    """
    :param people: list of (h_i, k_i) height of person i and number of person taller or equal to h_i in front of him
    :return: reconstructed list of [(h_i, k_i)]
    """
    # sort people list by descending order of height h_i, then ascending order of k_i
    people.sort(key=lambda person_i: (-person_i[0], person_i[1]))
    reconstructed_queue = []
    for person_i in people:
        # since person_i in descending order of height,
        # guaranteed every one before him is taller or equal to him
        # since again in ascending order of k_i
        # among persons with the same h_i, the first in the list will appear first in the search
        reconstructed_queue.insert(person_i[1], person_i)
    return reconstructed_queue


test_cases = [([(7, 0), (4, 4), (7, 1), (5, 0), (6, 1), (5, 2)], [(5, 0), (7, 0), (5, 2), (6, 1), (4, 4), (7, 1)]),
              ([(6, 0), (5, 0), (4, 0), (3, 2), (2, 2), (1, 4)], [(4, 0), (5, 0), (2, 2), (3, 2), (1, 4), (6, 0)]),
              ([(40, 11), (81, 12), (32, 60), (36, 39), (76, 19), (11, 37), (67, 13), (45, 39), (99, 0), (35, 20),
                (15, 3), (62, 13), (90, 2), (86, 0), (26, 13), (68, 32), (91, 4), (23, 24), (73, 14), (86, 13), (62, 6),
                (36, 13), (67, 9), (39, 57), (15, 45), (37, 26), (12, 88), (30, 18), (39, 60), (77, 2), (24, 38),
                (72, 7), (96, 1), (29, 47), (92, 1), (67, 28), (54, 44), (46, 35), (3, 85), (27, 9), (82, 14), (29, 17),
                (80, 11), (84, 10), (5, 59), (82, 6), (62, 25), (64, 29), (88, 8), (11, 20), (83, 0), (94, 4), (43, 42),
                (73, 9), (57, 32), (76, 24), (14, 67), (86, 2), (13, 47), (93, 1), (95, 2), (87, 8), (8, 78), (58, 16),
                (26, 75), (26, 15), (24, 56), (69, 9), (42, 22), (70, 17), (34, 48), (26, 39), (22, 28), (21, 8),
                (51, 44), (35, 4), (25, 48), (78, 18), (29, 30), (13, 63), (68, 8), (21, 38), (56, 20), (84, 14),
                (56, 27), (60, 40), (98, 0), (63, 7), (27, 46), (70, 13), (29, 23), (49, 6), (5, 64), (67, 11), (2, 31),
                (59, 8), (93, 0), (50, 39), (84, 6), (19, 39)],
               [(83, 0), (86, 0), (77, 2), (15, 3), (93, 0), (35, 4), (86, 2), (92, 1), (49, 6), (21, 8), (62, 6),
                (27, 9), (90, 2), (59, 8), (63, 7), (26, 13), (40, 11), (26, 15), (72, 7), (36, 13), (11, 20), (68, 8),
                (67, 9), (29, 17), (82, 6), (30, 18), (62, 13), (23, 24), (67, 11), (35, 20), (29, 23), (2, 31),
                (22, 28), (58, 16), (69, 9), (67, 13), (93, 1), (56, 20), (11, 37), (42, 22), (29, 30), (73, 9),
                (21, 38), (19, 39), (84, 6), (37, 26), (98, 0), (24, 38), (15, 45), (70, 13), (13, 47), (26, 39),
                (91, 4), (80, 11), (56, 27), (73, 14), (62, 25), (70, 17), (96, 1), (81, 12), (5, 59), (25, 48),
                (84, 10), (27, 46), (36, 39), (5, 64), (46, 35), (29, 47), (13, 63), (57, 32), (24, 56), (95, 2),
                (82, 14), (45, 39), (14, 67), (67, 28), (34, 48), (64, 29), (43, 42), (50, 39), (87, 8), (8, 78),
                (76, 19), (78, 18), (88, 8), (84, 14), (3, 85), (51, 44), (54, 44), (99, 0), (32, 60), (60, 40),
                (76, 24), (68, 32), (39, 57), (12, 88), (26, 75), (86, 13), (94, 4), (39, 60)]),
              ([(40, 11), (81, 12), (32, 60), (36, 39), (76, 19), (11, 37), (67, 13), (45, 39), (99, 0), (35, 20),
                (15, 3), (62, 13), (90, 2), (86, 0), (26, 13), (68, 32), (91, 4), (23, 24), (73, 14), (86, 13), (62, 6),
                (36, 13), (67, 9), (39, 57), (15, 45), (37, 26), (12, 88), (30, 18), (39, 60), (77, 2), (24, 38),
                (72, 7), (96, 1), (29, 47), (92, 1), (67, 28), (54, 44), (46, 35), (3, 85), (27, 9), (82, 14), (29, 17),
                (80, 11), (84, 10), (5, 59), (82, 6), (62, 25), (64, 29), (88, 8), (11, 20), (83, 0), (94, 4), (43, 42),
                (73, 9), (57, 32), (76, 24), (14, 67), (86, 2), (13, 47), (93, 1), (95, 2), (87, 8), (8, 78), (58, 16),
                (26, 75), (26, 15), (24, 56), (69, 9), (42, 22), (70, 17), (34, 48), (26, 39), (22, 28), (21, 8),
                (51, 44), (35, 4), (25, 48), (78, 18), (29, 30), (13, 63), (68, 8), (21, 38), (56, 20), (84, 14),
                (56, 27), (60, 40), (98, 0), (63, 7), (27, 46), (70, 13), (29, 23), (49, 6), (5, 64), (67, 11), (2, 31),
                (59, 8), (93, 0), (50, 39), (84, 6), (19, 39)],
               [(83, 0), (86, 0), (77, 2), (15, 3), (93, 0), (35, 4), (86, 2), (92, 1), (49, 6), (21, 8), (62, 6),
                (27, 9), (90, 2), (59, 8), (63, 7), (26, 13), (40, 11), (26, 15), (72, 7), (36, 13), (11, 20), (68, 8),
                (67, 9), (29, 17), (82, 6), (30, 18), (62, 13), (23, 24), (67, 11), (35, 20), (29, 23), (2, 31),
                (22, 28), (58, 16), (69, 9), (67, 13), (93, 1), (56, 20), (11, 37), (42, 22), (29, 30), (73, 9),
                (21, 38), (19, 39), (84, 6), (37, 26), (98, 0), (24, 38), (15, 45), (70, 13), (13, 47), (26, 39),
                (91, 4), (80, 11), (56, 27), (73, 14), (62, 25), (70, 17), (96, 1), (81, 12), (5, 59), (25, 48),
                (84, 10), (27, 46), (36, 39), (5, 64), (46, 35), (29, 47), (13, 63), (57, 32), (24, 56), (95, 2),
                (82, 14), (45, 39), (14, 67), (67, 28), (34, 48), (64, 29), (43, 42), (50, 39), (87, 8), (8, 78),
                (76, 19), (78, 18), (88, 8), (84, 14), (3, 85), (51, 44), (54, 44), (99, 0), (32, 60), (60, 40),
                (76, 24), (68, 32), (39, 57), (12, 88), (26, 75), (86, 13), (94, 4), (39, 60)]),
              ]
for reconstruct_queue in [reconstruct_queue_dsc_height, reconstruct_queue_asc_height, ]:
    for test_people, expected_queue in test_cases:
        assert reconstruct_queue(test_people) == expected_queue, reconstruct_queue.__name__
