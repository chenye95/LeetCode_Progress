"""
You are given an integer array cards where cards[i] represents the value of the ith card. A pair of cards are matching
 if the cards have the same value.

Return the minimum number of consecutive cards you have to pick up to have a pair of matching cards among the picked
 cards. If it is impossible to have matching cards, return -1.
"""
from typing import List


def minimum_pick_up(cards: List[int]) -> int:
    return_val = len(cards) + 1
    last_seen = {}

    for i, card_i in enumerate(cards):
        if card_i in last_seen:
            return_val = min(return_val, i - last_seen[card_i] + 1)
        last_seen[card_i] = i

    return -1 if return_val > len(cards) else return_val


test_cases = [
    ([3, 4, 2, 3, 4, 7], 4),
    ([1, 0, 5, 3], -1),
    ([67, 19, 45, 41, 21, 47, 75, 83, 0, 64, 56, 98, 6, 73, 25, 78, 76, 79, 26, 23, 17, 58, 55, 35, 28, 3, 61, 60, 80,
      46, 24, 1, 2, 40, 84, 13, 31, 14, 59, 7, 57, 12, 49, 94, 68, 10, 15, 16, 33, 38, 54, 34, 29, 43, 90, 20], -1),
    ([746, 464, 175, 787, 105, 164, 370, 110, 642, 413, 353, 410, 200, 141, 915, 170, 928, 326, 123, 528, 8, 11, 474,
      168, 992, 43, 901, 133, 579, 152, 135, 893, 950, 102, 863, 119, 835, 795, 783, 728, 35, 916, 770, 698, 832, 324,
      391, 338, 102, 770, 183, 739, 804, 468, 591, 174, 929, 992, 406, 349, 472, 260, 586, 938, 677, 331, 629, 769, 148,
      566, 501, 628, 845, 197, 48, 369, 754, 542, 608, 632, 639, 815, 758, 206, 400, 105, 298, 993, 187, 133, 950, 430,
      92, 225, 609, 507, 753, 873, 732, 353, 894, 63, 867, 814, 736, 109, 440, 288, 846, 152, 164, 42, 96, 134, 170,
      649, 832, 385, 265, 178, 447, 678, 415, 32, 428, 524, 118, 775, 593, 221, 247, 887, 119, 159, 391, 661, 220, 175,
      693, 184, 534, 281, 569, 306, 383, 330, 355, 408, 30, 200, 391, 136, 721, 925], 8),
]
for test_cards, expected_value in test_cases:
    assert minimum_pick_up(test_cards) == expected_value
