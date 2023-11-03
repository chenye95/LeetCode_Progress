"""
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a
 positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the
 beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the
 most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game
"""
from functools import cache
from sys import setrecursionlimit
from typing import List


def stone_game(piles: List[int]) -> bool:
    """
    :param piles: len(piles) is an even number between 2 and 500, 1 <= piles[i] <= 500, and sum(piles) is odd
    :return: whether Alex will win the game, when both play strategically
    """
    n = len(piles)

    @cache
    def play_sub_game(i: int, j: int) -> int:
        """
        :return: difference of Alex's score over Lee's score when playing piles[i: j + 1]
        """
        if i > j:
            return 0
        is_player_1 = (n - (j - i)) % 2
        if is_player_1:
            return max(play_sub_game(i + 1, j) + piles[i], play_sub_game(i, j - 1) + piles[j])
        else:
            return min(play_sub_game(i + 1, j) - piles[i], play_sub_game(i, j - 1) - piles[j])

    return play_sub_game(0, n - 1) > 0


setrecursionlimit(1200)
test_cases = [([5, 3, 4, 5], True),
              ([59, 48, 36, 70, 59, 93, 60, 98, 15, 32, 31, 13, 27, 14, 8, 17, 4, 76, 24, 47, 39, 81, 26, 6, 70, 73, 8,
                36, 71, 19, 66, 61, 86, 63, 97, 32, 15, 36, 68, 69, 32, 53, 83, 35, 100, 41, 44, 8, 28, 76, 39, 90, 37,
                35, 11, 99, 48, 49, 64, 74, 6, 54, 12, 99, 34, 47, 78, 36, 51, 26, 43, 83, 10, 68, 32, 48, 72, 54, 64,
                64, 44, 62, 77, 60, 100, 84, 15, 24, 95, 6, 6, 8, 24, 21, 84, 61, 75, 26, 63, 54], True),
              ]
""" 
              requires change to maximum recursion depth
             ([364, 26, 430, 378, 394, 280, 389, 452, 269, 102, 307, 224, 299, 383, 294, 203, 118, 265, 343, 283, 265,
               100, 385, 120, 361, 439, 417, 298, 315, 125, 463, 112, 326, 129, 213, 463, 286, 109, 405, 35, 143, 423,
               179, 239, 319, 404, 141, 194, 126, 490, 470, 492, 61, 435, 372, 189, 266, 27, 34, 33, 36, 361, 42, 493,
               56, 359, 46, 453, 9, 426, 44, 485, 81, 394, 250, 465, 481, 346, 240, 10, 342, 419, 137, 63, 453, 370,
               35, 232, 205, 51, 292, 266, 229, 172, 489, 322, 309, 350, 307, 209, 135, 264, 124, 279, 328, 282, 112,
               49, 264, 46, 200, 169, 16, 105, 154, 449, 140, 175, 500, 479, 157, 197, 272, 84, 201, 260, 327, 181,
               412, 495, 328, 465, 146, 109, 188, 58, 366, 444, 238, 427, 282, 230, 432, 278, 249, 89, 80, 91, 427,
               420, 155, 36, 22, 327, 22, 147, 306, 315, 344, 439, 302, 5, 436, 83, 109, 312, 493, 110, 189, 354, 15,
               254, 497, 58, 403, 202, 115, 193, 71, 214, 247, 462, 284, 458, 33, 293, 421, 204, 263, 89, 13, 446, 252,
               208, 91, 67, 190, 461, 23, 296, 128, 349, 468, 320, 278, 420, 413, 153, 406, 232, 23, 100, 215, 20, 282,
               162, 399, 163, 23, 414, 67, 395, 350, 435, 348, 239, 189, 314, 232, 276, 397, 337, 212, 110, 186, 192,
               174, 430, 339, 161, 175, 403, 249, 59, 421, 235, 318, 370, 472, 478, 445, 399, 432, 207, 483, 407, 281,
               52, 485, 280, 488, 150, 143, 408, 104, 428, 121, 87, 308, 217, 412, 315, 260, 126, 118, 225, 398, 245,
               429, 118, 438, 414, 486, 295, 361, 98, 299, 235, 47, 371, 491, 380, 373, 411, 120, 329, 166, 211, 331,
               251, 426, 88, 484, 345, 468, 159, 234, 178, 168, 423, 413, 295, 187, 273, 398, 334, 217, 292, 118, 86,
               93, 246, 61, 186, 279, 328, 300, 483, 25, 203, 28, 493, 39, 321, 479, 78, 432, 160, 139, 34, 398, 247,
               288, 273, 120, 157, 37, 155, 339, 27, 360, 405, 57, 147, 232, 42, 147, 88, 322, 32, 337, 292, 383, 93,
               16, 43, 315, 306, 454, 204, 263, 344, 465, 132, 489, 291, 488, 384, 35, 258, 273, 483, 263, 392, 70,
               181, 244, 189, 22, 452, 423, 312, 251, 38, 351, 120, 280, 254, 310, 248, 301, 328, 87, 90, 226, 302, 35,
               329, 118, 201, 117, 170, 140, 397, 81, 379, 306, 320, 342, 143, 146, 34, 138, 257, 472, 348, 185, 6,
               185, 367, 168, 130, 402, 94, 152, 336, 288, 194, 385, 364, 368, 207, 383, 402, 65, 117, 482, 30, 491,
               244, 90, 422, 251, 203, 497, 488, 30, 10, 455, 374, 31, 237, 45, 293, 39, 235, 288, 395, 29, 464, 281,
               351, 43, 257, 21, 138, 12, 260, 215, 323, 18, 440, 351, 30, 438, 179, 11, 43, 4, 55, 244, 470, 114, 325,
               17, 223, 356, 456, 498, 238], True),
"""
for test_nums, expected_value in test_cases:
    assert stone_game(test_nums) is expected_value
