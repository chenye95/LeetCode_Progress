"""
You are given an integer hoursBefore, the number of hours you have to travel to your meeting. To arrive at your meeting,
 you have to travel through n roads. The road lengths are given as an integer array dist of length n, where dist[i]
 describes the length of the ith road in kilometers. In addition, you are given an integer speed, which is the speed
 (in km/h) you will travel at.

After you travel road i, you must rest and wait for the next integer hour before you can begin traveling on the next
 road. Note that you do not have to rest after traveling the last road because you are already at the meeting.
- For example, if traveling a road takes 1.4 hours, you must wait until the 2-hour mark before traveling the next road.
    If traveling a road takes exactly 2 hours, you do not need to wait.

However, you are allowed to skip some rests to be able to arrive on time, meaning you do not need to wait for the next
 integer hour. Note that this means you may finish traveling future roads at different hour marks.
- For example, suppose traveling the first road takes 1.4 hours and traveling the second road takes 0.6 hours. Skipping
    the rest after the first road will mean you finish traveling the second road right at the 2-hour mark, letting you
    start traveling the third road immediately.

Return the minimum number of skips required to arrive at the meeting on time, or -1 if it is impossible.
"""
from typing import List


def min_skips_two_list(distance: List[int], speed: int, hours_before: int) -> int:
    """
    :param distance: 1 <= len(distance) <= 1000, 1 <= distance[i] <= 1e5
    :param speed: 1 <= speed <= 1e6
    :param hours_before: 1 <= hours_before <= 1e7
    :return: minimum skips to arrive at the meeting on time
    """
    # Scale all times by speed to avoid float
    n = len(distance)
    # previous_road[max_skips] minimum time to reach road_i with at most max_skips, scale up by speed
    previous_road: List[int] = [speed * hours_before] * (n + 1)
    previous_road[0] = 0

    # road_i is 1 indexed
    for road_i, distance_i in enumerate(distance, 1):
        current_road: List[int] = [speed * hours_before] * (n + 1)
        current_road[0] = (previous_road[0] + distance_i + speed - 1) // speed * speed
        for skip_count in range(1, road_i + 1):
            current_road[skip_count] = min(previous_road[skip_count - 1] + distance_i,
                                           (previous_road[skip_count] + distance_i + speed - 1) // speed * speed)
        previous_road = current_road

    for skip_count, time_to_arrive in enumerate(previous_road):
        if time_to_arrive <= hours_before * speed:
            return skip_count

    return -1


def min_skips_one_list(distance: List[int], speed: int, hours_before: int) -> int:
    """
    :param distance: 1 <= len(distance) <= 1000, 1 <= distance[i] <= 1e5
    :param speed: 1 <= speed <= 1e6
    :param hours_before: 1 <= hours_before <= 1e7
    :return: minimum skips to arrive at the meeting on time
    """
    # Scale all times by speed to avoid float
    n = len(distance)
    # time_with_skips[max_skips] minimum time to reach road_i with at most max_skips, scale up by speed
    time_with_skips: List[int] = [speed * hours_before] * (n + 1)
    time_with_skips[0] = 0

    # road_i is 1 indexed
    for road_i, distance_i in enumerate(distance, 1):
        for skip_count in range(road_i, 0, -1):
            time_with_skips[skip_count] = min(time_with_skips[skip_count - 1] + distance_i,
                                              (time_with_skips[skip_count] + distance_i + speed - 1) // speed * speed)
        time_with_skips[0] = (time_with_skips[0] + distance_i + speed - 1) // speed * speed

    for skip_count, time_to_arrive in enumerate(time_with_skips):
        if time_to_arrive <= hours_before * speed:
            return skip_count

    return -1


test_cases = [([1, 3, 2], 4, 2, 1),
              ([7, 3, 5, 5], 2, 10, 2),
              ([7, 3, 5, 5], 1, 10, -1),
              ([57, 81, 39, 36, 76, 8, 46, 65, 10, 40, 60, 58, 5, 8, 48, 37, 10, 83, 12, 79, 77, 65, 50, 60, 75, 71, 95,
                6, 58, 74, 84, 25, 42, 78, 61, 65, 20, 8, 58, 14, 44, 92, 11, 65, 83, 23, 6, 32, 91, 57, 57, 68, 67, 79,
                21, 47, 48, 37, 50, 53, 100, 44, 87, 77, 7, 81, 83, 43, 9, 43, 13, 72, 87, 50, 37, 33, 93, 85, 78, 20,
                43, 11, 75, 85, 19, 45, 40, 84, 90, 85, 51, 17, 77, 91, 11, 40, 72, 49, 83, 43, 17, 86, 90, 95, 88, 68,
                12, 83, 86, 55, 66, 47, 3, 47, 40, 24, 28, 44, 99, 63, 25, 29, 18, 20, 10, 38, 13, 65, 99, 70, 95, 68,
                5, 85, 44, 99, 80, 17, 77, 49, 20, 21, 24, 89, 99, 80, 22, 93, 57, 6, 53, 47, 87, 93, 31, 57, 79, 37,
                97, 96, 58, 30, 69, 31, 40, 61, 25, 48, 87, 74, 57, 60, 99, 37, 100, 49, 65, 68, 54, 21, 26, 78, 18, 33,
                7, 83, 62, 48, 71, 14, 92, 67, 16, 37, 11, 98, 21, 35, 58, 66, 19, 56, 12, 29, 58, 45, 4, 54, 7, 51, 65,
                48, 31, 50, 11, 48, 29, 4, 41, 13, 92, 84, 43, 19, 18, 5, 37, 61, 90, 18, 98, 91, 61, 58, 79, 1, 11, 3,
                33, 28, 20, 71, 94, 78, 68, 55, 15, 100, 37, 31, 39, 16, 7, 31, 54, 82, 80, 59, 9, 15, 64, 77, 69, 3,
                81, 66, 74, 31, 92, 19, 38, 55, 1, 79, 46, 31, 74, 54, 24, 86, 86, 11, 68, 47, 9, 68, 70, 65, 65, 71, 3,
                50, 61, 6, 82, 50, 48, 33, 96, 3, 46, 9, 45, 31, 94, 85, 81, 14, 99, 75, 95, 97, 43, 18, 6, 46, 70, 44,
                83, 23, 100, 88, 60, 90, 62, 81, 24, 18, 9, 92, 100, 59, 5, 38, 26, 6, 26, 6, 41, 40], 53, 782, 0),
              ([259, 623, 825, 966, 313, 730, 991, 727, 659, 282, 434, 917, 386, 873, 358, 471, 259, 224, 478, 310, 694,
                534, 845, 639, 407, 599, 105, 8, 524, 679, 990, 864, 860, 384, 575, 663, 609, 624, 290, 306, 701, 111,
                494, 66, 345, 284, 656, 333, 883, 284, 268, 672, 729, 976, 914, 668, 306, 193, 154, 530, 784, 247, 922,
                59, 825, 878, 822, 830, 615, 414, 677, 328, 698, 144, 739, 27, 672, 510, 303, 266, 929, 429, 415, 398,
                755, 37, 598, 726, 586, 836, 195, 352, 744, 731, 228, 703, 548, 654, 804, 488, 929, 964, 688, 368, 520,
                308, 866, 175, 861, 674, 898, 572, 186, 301, 100, 483, 132, 759, 265, 743, 828, 573, 782, 935, 188, 970,
                697, 922, 344, 671, 92, 228, 364, 229, 763, 893, 315, 431, 808, 909, 340, 381, 267, 600, 302, 475, 872,
                121, 482, 55, 888, 650, 598, 595, 967, 636, 73, 484, 911, 200, 513, 123, 889, 698, 391, 543, 306, 424,
                56, 892, 875, 155, 141, 206, 351, 420, 584, 915, 929, 469, 147, 324, 884, 733, 185, 798, 83, 500, 341,
                647, 182, 321, 650, 60, 5, 463, 281, 215, 780, 793, 173, 591, 783, 163, 502, 805, 782, 799, 91, 133,
                630, 445, 649, 440, 414, 440, 989, 489, 393, 5, 39, 547, 205, 749, 383, 973, 15, 914, 330, 776, 854,
                544, 196, 19, 693, 5, 642, 752, 255, 232, 711, 899, 353, 320, 133, 106, 393, 516, 603, 314, 172, 67,
                844, 47, 306, 972, 298, 467, 746, 533, 611, 537, 346, 445, 910, 704, 138, 351, 924, 502, 368, 769, 193,
                169, 971, 929, 941, 832, 414, 20, 234, 230, 745, 135, 217, 752, 23, 604, 517, 174, 127, 376, 729, 667,
                812, 39, 385, 898, 656, 262, 790, 548, 639, 50, 609, 50, 678, 111, 670, 857, 21, 50, 707, 119, 427, 455,
                390, 127, 561, 259, 486, 719, 157, 211, 712, 703, 646, 10, 309, 431, 678, 104, 679, 533, 277, 638, 621,
                718, 141, 429, 851, 921, 108, 524, 737, 633, 121, 290, 117, 804, 109, 510, 204, 624, 205, 797, 270, 852,
                536, 997, 207, 367, 721, 420, 303, 165, 41, 562, 509, 933, 213, 705, 956, 493, 339, 241, 3, 14, 688, 92,
                929, 114, 856, 588, 686, 506, 153, 973, 93, 799, 524, 77, 741, 741, 104, 927, 263, 660, 237, 468, 304,
                271, 476, 52, 103, 833, 179, 896, 41, 873, 298, 369, 821, 694, 321, 437, 757, 119, 98, 872, 777, 912,
                47, 10, 873, 142, 680, 663, 175, 337, 367, 916, 449, 979, 637, 275, 900, 751, 96, 382, 835, 351, 188,
                117, 411, 410, 986, 468, 279, 856, 395, 707, 872, 490, 820, 432, 665, 908, 817, 171, 116, 136, 713, 744,
                61, 966, 865, 164, 107, 427, 934, 605, 495, 822, 583, 695, 449, 186, 626, 389, 798, 368, 627, 30, 884,
                701, 902, 859, 745, 997, 914, 134, 495, 943, 500, 116, 909, 422, 452, 48, 65, 268, 671, 322, 13, 722,
                890, 695, 538, 786, 762, 591, 742, 579, 230, 979, 686, 895, 347, 532, 536, 705, 718, 634, 98, 444, 678,
                745, 255, 494, 355, 680, 693, 657, 395, 153, 860, 847, 572, 914, 628, 56, 12, 659, 957, 161, 518, 870,
                481, 873, 508, 891, 170, 77, 770, 504, 329, 247, 339, 994, 285, 52, 520, 229, 564, 659, 388, 413, 837,
                241, 81, 471, 455, 821, 587, 459, 91, 878, 511, 458, 324, 122, 510, 764, 670, 19, 106, 414, 423, 37,
                571, 563, 1, 846, 94, 811, 619, 987, 634, 653, 312, 912, 521, 576, 212, 671, 688, 468, 974, 350, 373,
                846, 56, 837, 229, 865, 466, 340, 574, 786, 635, 615, 485, 734, 673, 373, 734, 464, 117, 100, 778, 675,
                228, 3, 350, 364, 850, 649, 988, 820, 299, 561, 535, 383, 719, 109, 47, 919, 169, 505, 144, 842, 735,
                761, 739, 420, 110, 261, 626, 201, 193, 124, 953, 873, 403, 221, 469, 845, 801, 196, 734, 347, 111, 776,
                425, 48, 949, 649, 858, 689, 603, 127, 791, 914, 462, 469, 675, 604, 980, 517, 138, 987, 511, 5, 544,
                754, 50, 567, 958, 444, 859, 600, 495, 947, 521, 800, 944, 933, 182, 709, 593, 178, 749, 835, 132, 107,
                397, 674, 615, 621, 904, 330, 517, 903, 394, 429, 624, 938, 710, 781, 255, 281, 408, 987, 352, 994, 302,
                464, 825, 137, 142, 423, 617, 717, 908, 767, 525, 307, 864, 719, 561, 882, 322, 729, 755, 958, 567, 648,
                223, 206, 215, 640, 732, 298, 704, 354, 944, 689, 136, 728, 666, 999, 982, 183, 516, 556, 711, 653, 331,
                728, 119, 780, 361, 576, 492, 597, 585, 966, 684, 728, 428, 691, 766, 916, 862, 547, 293, 899, 868, 433,
                828, 14, 536, 110, 26, 391, 149, 55, 687, 58, 205, 274, 769, 805, 165, 294, 700, 257, 150, 860, 64, 708,
                804, 303, 209, 772, 555, 34, 368, 834, 464, 105, 631, 889, 692, 758, 576, 886, 230, 761, 663, 575, 399,
                244, 524, 804, 816, 818, 713, 295, 710, 681, 49, 949, 391, 397, 427, 980, 808, 1000, 702, 321, 990, 566,
                56, 14, 762, 258, 208, 636, 890, 800, 882, 892, 454, 850, 231, 934, 649, 722, 727, 664, 377, 774, 603,
                560, 757, 618, 202, 795, 743, 988, 199, 302, 460, 182, 700, 77, 192, 986, 178, 753, 527, 123, 387, 42,
                439, 286, 570, 271, 134, 165, 599, 867, 262, 6, 339, 478, 727, 960, 159, 41, 158, 951, 331, 612, 53,
                793, 955, 641, 631, 864, 678, 309, 503, 809, 587, 564, 367, 75, 803, 725, 326, 539, 226, 980, 189, 534,
                70, 806, 518, 164, 426, 557, 550, 414, 95, 358, 227, 905, 219, 680, 340, 340, 370, 301, 224, 974, 771,
                634, 544, 487, 575, 844, 771, 665, 10, 118, 685, 355, 457, 247, 927, 658, 629, 941, 637, 250, 982, 41,
                699, 907, 329, 391, 938, 816, 968, 117, 396, 263], 556, 2148, 0), ]
for min_skips in [min_skips_one_list, min_skips_two_list, ]:
    for test_distance, test_speed, test_hours, expected_value in test_cases:
        assert min_skips(test_distance, test_speed, test_hours) == expected_value, min_skips.__name__
