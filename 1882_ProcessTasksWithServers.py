"""
You are given two 0-indexed integer arrays servers and tasks of lengths n and m respectively. servers[i] is the weight
 of the i server, and tasks[j] is the time needed to process the j task in seconds.

You are running a simulation system that will shut down after all tasks are processed. Each server can only process one
 task at a time. You will be able to process the jth task starting from the jth second beginning with the 0th task at
 second 0. To process task j, you assign it to the server with the smallest weight that is free, and in case of a tie,
 choose the server with the smallest index. If a free server gets assigned task j at second t, it will be free again at
 the second t + tasks[j].

If there are no free servers, you must wait until one is free and execute the free tasks as soon as possible. If
 multiple tasks need to be assigned, assign them in order of increasing index.

You may assign multiple tasks at the same second if there are multiple free servers.

Build an array ans of length m, where ans[j] is the index of the server the jth task will be assigned to.

Return the array ans.
"""
import heapq
from typing import List, Tuple


def assign_tasks(servers: List[int], tasks: List[int]) -> List[int]:
    """
    :param servers: 1 <= len(servers) <= 2 * 10**5, 1 <= servers[i] <= 2 * 10**5；
        Assign smallest servers[i] among all available servers
    :param tasks: 1 <= len(tasks) <= 2 * 10**5, 1 <= tasks[i] <= 2 * 10**5; task t arrives at time t and takes tasks[t]
    :return: assignment for each task
    """
    available_servers = [(weight_i, i) for i, weight_i in enumerate(servers)]
    unavailable_servers: List[Tuple[int, int, int]] = []
    heapq.heapify(available_servers)

    assignments = [0] * len(tasks)
    current_time = 0

    for task_i, task_duration in enumerate(tasks):
        if available_servers:
            current_time = max(task_i, current_time)
        else:
            # weight for the first free machine
            current_time, server_weight, server_i = heapq.heappop(unavailable_servers)
            heapq.heappush(available_servers, (server_weight, server_i))

        while unavailable_servers and unavailable_servers[0][0] <= current_time:
            # re add all machines that have finished processing
            _, server_weight, server_i = heapq.heappop(unavailable_servers)
            heapq.heappush(available_servers, (server_weight, server_i))

        server_weight, server_i = heapq.heappop(available_servers)
        assignments[task_i] = server_i
        heapq.heappush(unavailable_servers, (current_time + task_duration, server_weight, server_i))

    return assignments


test_cases = [([3, 3, 2], [1, 2, 3, 2, 1, 2], [2, 2, 0, 2, 1, 2]),
              ([5, 1, 4, 3, 2], [2, 1, 2, 4, 5, 2, 1], [1, 4, 1, 4, 1, 3, 2]),
              ([338, 890, 301, 532, 284, 930, 426, 616, 919, 267, 571, 140, 716, 859, 980, 469, 628, 490, 195, 664, 925,
                652, 503, 301, 917, 563, 82, 947, 910, 451, 366, 190, 253, 516, 503, 721, 889, 964, 506, 914, 986, 718,
                520, 328, 341, 765, 922, 139, 911, 578, 86, 435, 824, 321, 942, 215, 147, 985, 619, 865],
               [773, 537, 46, 317, 233, 34, 712, 625, 336, 221, 145, 227, 194, 693, 981, 861, 317, 308, 400, 2, 391, 12,
                626, 265, 710, 792, 620, 416, 267, 611, 875, 361, 494, 128, 133, 157, 638, 632, 2, 158, 428, 284, 847,
                431, 94, 782, 888, 44, 117, 489, 222, 932, 494, 948, 405, 44, 185, 587, 738, 164, 356, 783, 276, 547,
                605, 609, 930, 847, 39, 579, 768, 59, 976, 790, 612, 196, 865, 149, 975, 28, 653, 417, 539, 131, 220,
                325, 252, 160, 761, 226, 629, 317, 185, 42, 713, 142, 130, 695, 944, 40, 700, 122, 992, 33, 30, 136,
                773, 124, 203, 384, 910, 214, 536, 767, 859, 478, 96, 172, 398, 146, 713, 80, 235, 176, 876, 983, 363,
                646, 166, 928, 232, 699, 504, 612, 918, 406, 42, 931, 647, 795, 139, 933, 746, 51, 63, 359, 303, 752,
                799, 836, 50, 854, 161, 87, 346, 507, 468, 651, 32, 717, 279, 139, 851, 178, 934, 233, 876, 797, 701,
                505, 878, 731, 468, 884, 87, 921, 782, 788, 803, 994, 67, 905, 309, 2, 85, 200, 368, 672, 995, 128, 734,
                157, 157, 814, 327, 31, 556, 394, 47, 53, 755, 721, 159, 843],
               [26, 50, 47, 11, 56, 31, 18, 55, 32, 9, 4, 2, 23, 53, 43, 0, 44, 30, 6, 51, 29, 51, 15, 17, 22, 34, 38,
                33, 42, 3, 25, 10, 49, 51, 7, 58, 16, 21, 19, 31, 19, 12, 41, 35, 45, 52, 13, 59, 47, 36, 1, 28, 48, 39,
                24, 8, 46, 20, 5, 54, 27, 37, 14, 57, 40, 59, 8, 45, 4, 51, 47, 7, 58, 4, 31, 23, 54, 7, 9, 56, 2, 46,
                56, 1, 17, 42, 11, 30, 12, 44, 14, 32, 7, 10, 23, 1, 29, 27, 6, 10, 33, 24, 19, 10, 35, 30, 35, 10, 17,
                49, 50, 36, 29, 1, 48, 44, 7, 11, 24, 57, 42, 30, 10, 55, 3, 20, 38, 15, 7, 46, 32, 21, 40, 16, 59, 30,
                53, 17, 18, 22, 51, 11, 53, 36, 57, 26, 5, 36, 56, 55, 31, 34, 57, 7, 52, 37, 31, 10, 0, 51, 41, 2, 32,
                25, 0, 7, 49, 47, 13, 14, 24, 57, 28, 4, 45, 43, 39, 38, 8, 2, 44, 45, 29, 25, 25, 12, 54, 5, 44, 30,
                27, 23, 26, 7, 33, 58, 41, 25, 52, 40, 58, 9, 52, 40]),
              ([433, 139, 314, 951, 660, 142, 250, 856, 27, 854, 804, 677, 152, 546, 820, 727, 58, 318, 134, 149, 150,
                140, 162, 617, 119, 289, 713, 721, 128, 256, 999, 383, 155, 648, 998, 46, 396, 118, 212, 436, 869, 623,
                182, 453, 917, 493, 189, 355, 311, 846, 268, 205, 400, 264, 934, 648, 574, 778, 769, 595, 892, 955, 425,
                403, 191, 665, 68, 232, 63, 400, 331, 586, 997, 102, 333, 317, 81, 487, 530, 420, 220, 123, 430, 629,
                504, 290, 944, 656, 528, 639, 276, 102, 631, 40, 778, 258, 549, 115, 126, 641, 978, 761, 166, 717, 696,
                767, 286, 395, 833, 736, 365, 861, 720, 956, 270, 144, 765, 17, 570, 689, 732, 338, 35, 660, 774, 320,
                254, 792, 136, 51, 13, 507, 239, 382, 684, 295, 552, 29, 758, 144, 107, 237, 780, 945, 537, 715, 388,
                93, 802, 561, 645, 192, 740, 109, 800, 760, 812, 142, 155, 554, 746, 209, 82, 557, 563, 341, 668, 558,
                924, 265, 22, 839, 226, 88, 493, 95, 968, 482, 172, 135, 420, 689, 704, 416, 5, 13, 99, 442, 246, 219,
                200, 419, 728, 929, 709, 583, 983, 596, 764, 585, 588, 294, 653, 501, 206, 896, 178, 301, 701, 551, 524,
                222, 837, 530, 310, 507, 297, 72, 581, 686, 506, 563, 370, 74, 388, 585, 201, 812, 691, 486, 896, 295,
                776, 29, 806, 187, 200, 567, 12, 179, 463, 751, 987, 275, 690, 194, 799, 378, 292, 618, 777, 342, 272,
                499, 805, 39, 362, 410, 713, 122, 472, 161, 419, 523, 302, 474, 273, 363, 605, 834, 817, 931, 469, 455,
                365, 400, 703, 705, 201, 524, 691, 240, 374, 196, 828, 876, 652, 464, 210, 679, 398, 401, 568, 68, 896,
                337, 979],
               [129, 60, 825, 996, 986, 969, 671, 442, 222, 502, 462, 716, 382, 832, 68, 377, 370, 301, 330, 245, 831,
                778, 296, 371, 244, 168, 488, 970, 464, 514, 589, 182, 572, 334, 383, 691, 240, 940, 434, 119, 286, 511,
                335, 344, 600, 743, 345, 803, 750, 608, 380, 754, 51, 188, 149, 251, 2, 709, 758, 693, 505, 637, 252,
                461, 637, 454, 821, 650, 195, 208, 536, 913, 789, 918, 942, 873, 934, 688, 659, 953, 939, 519, 387, 484,
                258, 337, 890, 431, 788, 804, 227, 652, 307, 622, 848, 922, 765, 739, 1000, 998, 599, 433, 609, 573,
                898, 737, 971, 502, 259, 376, 514, 672, 347, 570, 913, 216, 65, 780, 128, 324, 329, 816, 11, 609, 396,
                268, 939, 233, 100, 484, 362, 980, 368, 217, 427, 161, 953, 784, 907, 315, 508, 197, 959, 154, 164, 464,
                476, 797, 499, 321, 551, 785, 455, 19, 943, 327, 556, 783, 929, 345, 492, 96, 440, 683, 167, 667, 118,
                601, 427, 584, 799],
               [184, 238, 130, 185, 117, 170, 8, 137, 233, 122, 255, 93, 35, 129, 16, 68, 66, 293, 217, 223, 76, 162,
                173, 147, 175, 186, 73, 91, 140, 153, 97, 37, 24, 259, 81, 98, 28, 18, 179, 128, 1, 21, 5, 157, 115,
                139, 19, 20, 12, 32, 158, 261, 22, 102, 178, 206, 239, 42, 239, 235, 46, 238, 64, 151, 245, 283, 190,
                236, 226, 278, 51, 204, 161, 288, 38, 189, 80, 211, 172, 67, 141, 132, 16, 281, 188, 6, 126, 29, 95, 53,
                169, 50, 114, 252, 266, 243, 90, 106, 25, 85, 248, 201, 135, 22, 231, 216, 207, 264, 214, 48, 2, 75, 17,
                125, 70, 74, 295, 121, 165, 251, 47, 256, 267, 110, 274, 222, 282, 247, 133, 184, 31, 146, 224, 267,
                107, 36, 290, 52, 69, 275, 291, 63, 257, 183, 191, 262, 79, 180, 62, 82, 0, 39, 187, 43, 273, 240, 287,
                272, 128, 260, 265, 177, 229, 77, 45, 174, 253, 203, 84, 220, 131]),
              ]
for test_servers, test_tasks, expected_assignments in test_cases:
    assert assign_tasks(test_servers, test_tasks) == expected_assignments
