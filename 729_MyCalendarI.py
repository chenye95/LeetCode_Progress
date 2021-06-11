"""
Implement a MyCalendar class to store your events. A new event can be added if adding the event will not cause a double
 booking.

Your class will have the method, book(int start, int end). Formally, this represents a booking on the half open interval
 [start, end), the range of real numbers x such that start <= x < end.

A double booking happens when two events have some non-empty intersection (ie., there is some time that is common to
 both events.)

For each call to the method MyCalendar.book, return True if the event can be added to the calendar successfully without
 causing a double booking. Otherwise, return False and do not add the event to the calendar.

Your class will be called like this: MyCalendar cal = new MyCalendar(); MyCalendar.book(start, end)
"""


class CalendarEvent:
    def __init__(self, start: int, end: int):
        """
        :param start: 0 <= start < end 1e9, representing time interval [start, end)
        :param end: 0 <= start < end 1e9, representing time interval [start, end)
        """
        self.start, self.end = start, end
        self.left = self.right = None

    def add_event(self, new_event_start: int, new_event_end: int) -> bool:
        """
        :param new_event_start: attempting to add a new event with [new_event_start, new_event_end)
        :param new_event_end: attempting to add a new event with [new_event_start, new_event_end)
        :return: [new_event_start, new_event_end) has no conflict with existing events
        """
        if self.end <= new_event_start:
            if self.right is None:
                self.right = CalendarEvent(new_event_start, new_event_end)
                return True
            return self.right.add_event(new_event_start, new_event_end)
        elif new_event_end <= self.start:
            if self.left is None:
                self.left = CalendarEvent(new_event_start, new_event_end)
                return True
            return self.left.add_event(new_event_start, new_event_end)
        else:
            return False


class MyCalendar:
    def __init__(self):
        self.first_event = None

    def book(self, start: int, end: int) -> bool:
        """
        :param start: 0 <= start < end 1e9, representing time interval [start, end)
        :param end: 0 <= start < end 1e9, representing time interval [start, end)
        :return: whether new event not conflict with existing events and hence can be booked successfully
        """
        if self.first_event is None:
            self.first_event = CalendarEvent(start, end)
            return True
        return self.first_event.add_event(start, end)


test_cases = [([(10, 20), (15, 25), (20, 30), ],
               [True, False, True]),
              ([(99, 100), (45, 57), (79, 94), (53, 72), (88, 99), (70, 82), (51, 69), (84, 97), (80, 98), (26, 44),
                (73, 87), (92, 100), (56, 74), (50, 67), (71, 85), (26, 41), (96, 100), (78, 91), (50, 61), (27, 41),
                (56, 66), (70, 80), (82, 92), (64, 80), (57, 76), (13, 27), (39, 57), (87, 100), (92, 100), (9, 22),
                (99, 100), (31, 47), (93, 100), (52, 65), (53, 67), (8, 19), (14, 26), (42, 52), (93, 100), (86, 100)],
               [True, True, True, False, False, False, False, False, False, True, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, True, False, False, False, False, True,
                False, False, False, False, False, False, False, False, False, False]),
              ([(69, 70), (3, 4), (39, 40), (35, 36), (3, 4), (55, 56), (61, 62), (97, 98), (79, 80), (76, 77),
                (46, 47), (78, 79), (47, 48), (38, 39), (83, 84), (90, 91), (90, 91), (49, 50), (49, 50), (77, 78),
                (23, 24), (89, 90), (8, 9), (3, 4), (2, 3), (48, 49), (96, 97), (4, 5), (54, 55), (30, 31), (97, 98),
                (65, 66), (93, 94), (49, 50), (24, 25), (17, 18), (53, 54), (45, 46), (53, 54), (32, 33), (37, 38),
                (5, 6), (50, 51), (48, 49), (14, 15), (91, 92), (79, 80), (73, 74), (28, 29), (31, 32), (98, 99),
                (37, 38), (19, 20), (49, 50), (54, 55), (37, 38), (98, 99), (12, 13), (24, 25), (46, 47), (74, 75),
                (87, 88), (64, 65), (61, 62), (68, 69), (28, 29), (43, 44), (89, 90), (64, 65), (72, 73), (69, 70),
                (88, 89), (68, 69), (28, 29), (20, 21), (64, 65), (17, 18), (40, 41), (88, 89), (22, 23), (8, 9),
                (33, 34), (13, 14), (19, 20), (53, 54), (99, 100), (24, 25), (82, 83), (77, 78), (90, 91), (72, 73),
                (33, 34), (73, 74), (0, 1), (25, 26), (69, 70), (73, 74), (12, 13), (33, 34), (47, 48), (26, 27),
                (77, 78), (95, 96), (28, 29), (77, 78), (28, 29), (87, 88), (16, 17), (42, 43), (51, 52), (44, 45),
                (63, 64), (24, 25), (18, 19), (0, 1), (45, 46), (65, 66), (21, 22), (37, 38), (77, 78), (97, 98),
                (24, 25), (83, 84), (20, 21), (29, 30), (66, 67), (29, 30), (37, 38), (63, 64), (15, 16), (85, 86),
                (61, 62), (0, 1), (23, 24), (96, 97), (91, 92), (90, 91), (80, 81), (18, 19), (69, 70), (3, 4),
                (59, 60), (21, 22), (75, 76), (54, 55), (65, 66), (34, 35), (19, 20), (79, 80), (6, 7), (24, 25),
                (29, 30), (35, 36), (9, 10), (0, 1), (73, 74), (65, 66), (78, 79), (32, 33), (58, 59), (25, 26), (3, 4),
                (78, 79), (92, 93), (37, 38), (91, 92), (5, 6), (79, 80), (94, 95), (78, 79), (38, 39), (16, 17),
                (81, 82), (34, 35), (16, 17), (33, 34), (42, 43), (34, 35), (89, 90), (88, 89), (33, 34), (68, 69),
                (92, 93), (73, 74), (64, 65), (91, 92), (44, 45), (13, 14), (97, 98), (64, 65), (31, 32), (91, 92),
                (1, 2), (57, 58), (21, 22), (38, 39), (70, 71), (84, 85), (50, 51), (58, 59)],
               [True, True, True, True, False, True, True, True, True, True, True, True, True, True, True, True, False,
                True, False, True, True, True, True, False, True, True, True, True, True, True, False, True, True,
                False, True, True, True, True, False, True, True, True, True, False, True, True, False, True, True,
                True, True, False, True, False, False, False, False, True, False, False, True, True, True, False, True,
                False, True, False, False, True, False, True, False, False, True, False, False, True, False, True,
                False, True, True, False, False, True, False, True, False, False, False, False, False, True, True,
                False, False, False, False, False, True, False, True, False, False, False, False, True, True, True,
                True, True, False, True, False, False, False, True, False, False, False, False, False, False, True,
                True, False, False, False, True, True, False, False, False, False, False, False, True, False, False,
                False, True, False, True, False, False, True, False, False, True, False, False, False, True, False,
                False, False, False, False, True, False, False, False, True, False, False, False, False, True, False,
                False, False, True, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, False, False, False, False, True, True, False, False, True, True, False, False]),
              ([(7379, 7397), (3573, 3585), (4248, 4267), (4597, 4609), (1815, 1828), (992, 1006), (877, 892),
                (8632, 8643), (6488, 6504), (5187, 5203), (3962, 3980), (8917, 8928), (3157, 3171), (6159, 6176),
                (2621, 2633), (620, 636), (2584, 2602), (9223, 9235), (7521, 7534), (9237, 9252), (6283, 6297),
                (7686, 7696), (6038, 6051), (2751, 2761), (7557, 7568), (7832, 7843), (567, 577), (6499, 6518),
                (7758, 7768), (838, 856), (5477, 5489), (4519, 4535), (9045, 9064), (6056, 6070), (2649, 2663),
                (1717, 1728), (9449, 9468), (5991, 6009), (2237, 2252), (1058, 1070), (8311, 8322), (415, 430),
                (6162, 6181), (7808, 7823), (8696, 8715), (8062, 8076), (5489, 5502), (5868, 5878), (162, 180),
                (843, 862), (2070, 2082), (5801, 5820), (5871, 5888), (323, 335), (1888, 1907), (1492, 1502),
                (2584, 2603), (8375, 8389), (2859, 2872), (3821, 3834), (1140, 1153), (1962, 1978), (8570, 8586),
                (2742, 2761), (2310, 2320), (9285, 9302), (5355, 5370), (9671, 9689), (1722, 1736), (6315, 6330),
                (6996, 7011), (303, 321), (2215, 2225), (5316, 5332), (8847, 8864), (6137, 6150), (4750, 4761),
                (4005, 4023), (3953, 3968), (7973, 7991), (4975, 4990), (8451, 8469), (8483, 8495), (4712, 4728),
                (7444, 7463), (1888, 1901), (7892, 7909), (9989, 10000), (2158, 2168), (4392, 4402), (6412, 6425),
                (2467, 2483), (9899, 9911), (6102, 6117), (2299, 2310), (9135, 9148), (2238, 2248), (8496, 8507),
                (1680, 1691), (1585, 1601), (8812, 8824), (3273, 3291), (1850, 1869), (4636, 4646), (9144, 9159),
                (1916, 1928), (6964, 6979), (3029, 3046), (7979, 7996), (8741, 8756), (1662, 1677), (5697, 5710),
                (2750, 2762), (3855, 3874), (703, 716), (8095, 8105), (316, 333), (2696, 2706), (17, 27), (4116, 4133),
                (3398, 3416), (2010, 2021), (5459, 5472), (2841, 2857), (6077, 6095), (7493, 7510), (7237, 7248),
                (3114, 3130), (6780, 6791), (7490, 7507), (474, 487), (5705, 5718), (1065, 1076), (977, 992),
                (7133, 7146), (6074, 6092), (3965, 3979), (2237, 2249), (8983, 8997), (7787, 7805), (2217, 2234),
                (5498, 5515), (8959, 8976), (2900, 2916), (9999, 10000), (5112, 5125), (418, 428), (6922, 6941),
                (2031, 2044), (7849, 7868), (1758, 1772), (4958, 4969), (9281, 9293), (7037, 7054), (3328, 3342),
                (7974, 7987), (8853, 8869), (9233, 9248), (7907, 7922), (2930, 2941), (6926, 6939), (3912, 3930),
                (621, 631), (6616, 6632), (3619, 3634), (4251, 4270), (1547, 1563), (2603, 2621), (1443, 1454),
                (5657, 5669), (3288, 3298), (7614, 7626), (5711, 5725), (8889, 8908), (7005, 7020), (368, 382),
                (7618, 7631), (6189, 6201), (1238, 1255), (6965, 6977), (2400, 2413), (2900, 2918), (2311, 2325),
                (5, 17), (2309, 2319), (3566, 3578), (4800, 4818), (9379, 9392), (9007, 9017), (1327, 1340),
                (9914, 9933), (8311, 8330), (66, 78), (4915, 4934), (3656, 3671), (182, 197), (5108, 5127),
                (1211, 1226), (6354, 6367), (589, 602), (7361, 7372), (4892, 4907), (7043, 7057), (5747, 5764),
                (3108, 3118), (9387, 9400), (5499, 5509), (5824, 5842), (2028, 2043), (272, 286), (3318, 3330),
                (7547, 7560), (1701, 1714), (6425, 6443), (3234, 3250), (1827, 1841), (205, 224), (5899, 5909),
                (5699, 5716), (7057, 7067), (1338, 1348), (7429, 7446), (8279, 8294), (5619, 5635), (6793, 6807),
                (5752, 5767), (2782, 2799), (4576, 4594), (6280, 6290), (5643, 5662), (5997, 6016), (1904, 1919),
                (4620, 4634), (5053, 5067), (7027, 7041), (3169, 3183), (6262, 6274), (1538, 1548), (1461, 1475),
                (3993, 4012), (1518, 1537), (586, 599), (1562, 1579), (2180, 2197), (7355, 7374), (526, 537),
                (4564, 4581), (5562, 5579), (2044, 2054), (6767, 6781), (6111, 6127), (1279, 1295), (1561, 1580),
                (479, 491), (841, 855), (5592, 5608), (6573, 6585), (517, 528), (9210, 9225), (781, 791), (9129, 9141),
                (7417, 7428), (6040, 6059), (2121, 2138), (9469, 9483), (8588, 8606), (9108, 9127), (7050, 7060),
                (5702, 5717), (5012, 5022), (2589, 2605), (553, 568), (8296, 8312), (5201, 5214), (6714, 6728),
                (6983, 6995), (3736, 3749), (2067, 2080), (5576, 5594), (3807, 3817), (5791, 5803), (5144, 5157),
                (3782, 3800), (2624, 2635), (4035, 4046), (2483, 2497), (7245, 7264), (964, 974), (2786, 2798),
                (1513, 1531), (5068, 5086), (9421, 9432), (5115, 5130), (7071, 7085), (3171, 3183), (8903, 8920),
                (2205, 2224), (4490, 4504), (1923, 1933), (48, 60), (3309, 3321), (4977, 4987), (5412, 5424),
                (2170, 2181), (3678, 3694), (2813, 2829), (4012, 4025), (3684, 3698), (348, 365), (5058, 5072),
                (5310, 5329), (4635, 4645), (8247, 8258), (1489, 1500), (8052, 8069), (6164, 6176), (204, 218),
                (5445, 5456), (6084, 6097), (4295, 4313), (8364, 8383), (20, 35), (7783, 7801), (4918, 4937),
                (8083, 8094), (5517, 5528), (1467, 1479), (6372, 6388), (606, 616), (543, 556), (3703, 3720),
                (1140, 1157), (3139, 3154), (3102, 3115), (4846, 4861), (6598, 6610), (7548, 7561), (7339, 7350),
                (6210, 6224), (3081, 3094), (9437, 9454), (9950, 9964), (9475, 9485), (2317, 2336), (3688, 3701),
                (2035, 2053), (7013, 7027), (9940, 9958), (5442, 5455), (4844, 4856), (8231, 8242), (8164, 8181),
                (899, 912), (3740, 3756), (8016, 8034), (3619, 3629), (9058, 9068), (4830, 4843), (8506, 8520),
                (8477, 8496), (6173, 6192), (5465, 5477), (7569, 7588), (8606, 8619), (392, 402), (3463, 3473),
                (8926, 8943), (3317, 3332), (6735, 6748), (9329, 9348), (4360, 4372), (2630, 2649), (1191, 1205),
                (6151, 6163), (7670, 7684), (9715, 9728), (1612, 1630), (9770, 9789), (2276, 2295), (2700, 2713),
                (4627, 4638), (3564, 3576), (2476, 2491), (475, 492), (6591, 6601), (5686, 5702), (9372, 9388),
                (9340, 9354), (9714, 9725), (751, 768), (7179, 7194), (7910, 7923), (9791, 9808), (51, 61),
                (6262, 6274), (5146, 5158), (7078, 7088), (2159, 2176), (8181, 8200), (3593, 3610), (2386, 2403),
                (9704, 9718), (6625, 6640), (3667, 3678), (5965, 5984), (6924, 6941), (4597, 4611), (9384, 9397),
                (4679, 4693), (9124, 9139), (8508, 8524), (6634, 6645), (2236, 2254), (5574, 5589), (9144, 9163),
                (9789, 9804), (1130, 1140), (3128, 3143), (3050, 3069), (3806, 3825), (5420, 5437), (5541, 5554),
                (4152, 4162), (1143, 1154), (784, 803), (3592, 3605), (1671, 1686), (1921, 1935), (5153, 5171),
                (2101, 2120), (6331, 6342), (2973, 2991), (4037, 4048), (1567, 1579), (5478, 5493), (4984, 4998),
                (8362, 8376), (9222, 9232), (845, 861), (6402, 6417), (7613, 7624), (4098, 4111), (1633, 1646),
                (1795, 1808), (998, 1009), (3139, 3155), (9198, 9209), (3079, 3095), (2859, 2874), (4755, 4772),
                (839, 855), (9552, 9566), (5114, 5125), (5442, 5459), (4569, 4587), (6735, 6754), (5678, 5689),
                (9955, 9973), (1946, 1956), (4983, 5001), (4418, 4434), (561, 576), (9568, 9583), (9302, 9314),
                (7891, 7909), (2862, 2873), (444, 455), (8753, 8767), (4206, 4223), (4448, 4458), (674, 686),
                (5188, 5203), (5415, 5433), (7489, 7503), (993, 1005), (9641, 9655), (9470, 9481), (6770, 6780),
                (5278, 5297), (2613, 2625), (6148, 6158), (3882, 3892), (313, 329), (359, 377), (9213, 9225),
                (8694, 8711), (7458, 7469), (9203, 9220), (2024, 2042), (8868, 8887), (2225, 2238), (7190, 7207),
                (117, 132), (6276, 6294), (5863, 5879), (1172, 1187), (9194, 9208), (8701, 8718), (4654, 4667),
                (9615, 9633), (1649, 1668), (7988, 8000), (7376, 7389), (7669, 7684), (9722, 9735), (4654, 4666),
                (9850, 9864), (8307, 8323), (2678, 2688), (1144, 1158), (2796, 2810), (9363, 9373), (9468, 9487),
                (9196, 9211), (2213, 2226), (1431, 1443), (7530, 7540), (3130, 3143), (9647, 9666), (1791, 1807),
                (4063, 4074), (7423, 7436), (7634, 7648), (7920, 7933), (6773, 6791), (8743, 8753), (128, 144),
                (7688, 7707), (2965, 2979), (6521, 6537), (3610, 3622), (3777, 3793), (88, 107), (903, 915),
                (7841, 7852), (4159, 4173), (5732, 5746), (7401, 7415), (1785, 1800), (6367, 6386), (8213, 8224),
                (2290, 2303), (8572, 8591), (626, 637), (7393, 7408), (7460, 7470), (1177, 1193), (7744, 7761),
                (675, 692), (4390, 4405), (6238, 6257), (1638, 1655), (3745, 3757), (3493, 3503), (1152, 1170),
                (8622, 8634), (3406, 3421), (4832, 4849), (2769, 2788), (1273, 1290), (30, 48), (8526, 8542),
                (3137, 3155), (9017, 9036), (2687, 2703), (5812, 5826), (2032, 2042), (7257, 7273), (9115, 9131),
                (2457, 2473), (9253, 9272), (2804, 2818), (6670, 6689), (3559, 3576), (6730, 6745), (8130, 8141),
                (548, 566), (285, 297), (1364, 1378), (3671, 3689), (3952, 3967), (7927, 7937), (422, 432),
                (5288, 5302), (1744, 1759), (3385, 3397), (4030, 4049), (8355, 8370), (770, 786), (5754, 5773),
                (632, 649), (3646, 3663), (2085, 2104), (9922, 9936), (9030, 9040), (4835, 4846), (4386, 4402),
                (494, 505), (234, 253), (9610, 9628), (4306, 4319), (2789, 2804), (2974, 2988), (5462, 5474),
                (686, 696), (7575, 7585), (4453, 4465), (4251, 4267), (7975, 7988), (9519, 9530), (1610, 1628),
                (3232, 3248), (1745, 1757), (2495, 2514), (6796, 6808), (5141, 5158), (7942, 7961), (4237, 4251),
                (2241, 2259), (2626, 2643), (7688, 7707), (2391, 2409), (7605, 7619), (1867, 1878), (9691, 9701),
                (5524, 5536), (9818, 9833), (7033, 7052), (4072, 4082), (1901, 1919), (3362, 3379), (9368, 9378),
                (7085, 7101), (8793, 8810), (7760, 7773), (2876, 2893), (3266, 3279), (1576, 1595), (7806, 7821),
                (4928, 4940), (1305, 1315), (8307, 8321), (8971, 8986), (9999, 10000), (6939, 6951), (6606, 6620),
                (3471, 3486), (3589, 3601), (9870, 9887), (4578, 4588), (9265, 9279), (9635, 9646), (4440, 4453),
                (5676, 5690), (3596, 3610), (2914, 2924), (2692, 2703), (5202, 5217), (8111, 8129), (288, 301),
                (3085, 3102), (7500, 7516), (6083, 6102), (7308, 7327), (2542, 2557), (956, 969), (9272, 9286),
                (1098, 1112), (3892, 3909), (9959, 9974), (9058, 9073), (2666, 2678), (3124, 3142), (3727, 3741),
                (1880, 1895), (2313, 2327), (4342, 4356), (3541, 3553), (1397, 1409), (8186, 8197), (9504, 9523),
                (7731, 7745), (6410, 6428), (5183, 5196), (445, 457), (4260, 4272), (9526, 9539), (8046, 8060),
                (8066, 8080), (6313, 6329), (6498, 6516), (6626, 6636), (2662, 2676), (3537, 3548), (2654, 2667),
                (9246, 9259), (7116, 7127), (1432, 1444), (3374, 3389), (7868, 7880), (4447, 4457), (5225, 5241),
                (6966, 6976), (2195, 2212), (582, 601), (8791, 8808), (1740, 1752), (7765, 7775), (4450, 4468),
                (3466, 3479), (1722, 1733), (6337, 6350), (8616, 8635), (4699, 4715), (5201, 5212), (4361, 4378),
                (2428, 2440), (1665, 1675), (4561, 4580), (9537, 9554), (1777, 1787), (1063, 1078), (7867, 7886),
                (1506, 1523), (482, 494), (1866, 1879), (7674, 7684), (515, 527), (5144, 5160), (6300, 6317),
                (5026, 5043), (2541, 2551), (7366, 7383), (3569, 3583), (1334, 1350), (5540, 5558), (4527, 4545),
                (9388, 9403), (1177, 1191), (6808, 6819), (3033, 3048), (1434, 1448), (4152, 4170), (8723, 8735),
                (4256, 4271), (3421, 3435), (2408, 2423), (390, 404), (3903, 3914), (8552, 8567), (8138, 8149),
                (7990, 8001), (6092, 6102), (1931, 1945), (9943, 9955), (8298, 8310), (5378, 5390), (9987, 10000),
                (9984, 10000), (228, 246), (9494, 9507), (4696, 4710), (4767, 4785), (8456, 8471), (1556, 1575),
                (5905, 5915), (4650, 4669), (2474, 2485), (3643, 3657), (8044, 8057), (5457, 5476), (5841, 5860),
                (9521, 9539), (7930, 7945), (7981, 8000), (551, 570), (3953, 3968), (5019, 5035), (9299, 9317),
                (4930, 4944), (8522, 8541), (7846, 7863), (954, 970), (9596, 9607), (9357, 9368), (3239, 3255),
                (4233, 4244), (4779, 4797), (5299, 5311), (9815, 9827), (9100, 9111), (9486, 9503), (2043, 2054),
                (6509, 6527), (128, 143), (4063, 4080), (3460, 3476), (2961, 2980), (7992, 8002), (5226, 5240),
                (7780, 7798), (3834, 3852), (3161, 3175), (5746, 5760), (138, 151), (7794, 7810), (7090, 7101),
                (7602, 7620), (8635, 8654), (4455, 4467), (5777, 5795), (6028, 6040), (1043, 1058), (6493, 6511),
                (9390, 9400), (1058, 1073), (1292, 1305), (4915, 4926), (95, 114), (6642, 6653), (332, 346),
                (2753, 2763), (768, 787), (6574, 6587), (7124, 7139), (6668, 6684), (8072, 8090), (7151, 7167),
                (3061, 3076), (46, 61), (8870, 8887), (827, 837), (9369, 9386), (8902, 8913), (2877, 2887),
                (3477, 3494), (3910, 3924), (3397, 3407), (3345, 3362), (9942, 9957), (9696, 9713), (9852, 9865),
                (1106, 1124), (7725, 7743), (2819, 2833), (7402, 7415), (886, 903), (5241, 5251), (7551, 7566),
                (2879, 2898), (6548, 6566), (291, 308), (1012, 1026), (547, 562), (7153, 7167), (2152, 2166),
                (5733, 5747), (2400, 2416), (3330, 3340), (2980, 2995), (5721, 5731), (1403, 1422), (950, 960),
                (4862, 4875), (7828, 7840), (4372, 4384), (8689, 8703), (3491, 3509), (3456, 3467), (5556, 5572),
                (7860, 7874), (2135, 2154), (7583, 7595), (3300, 3310), (2404, 2415), (6671, 6685), (7706, 7721),
                (216, 233), (5803, 5820), (5004, 5020), (4144, 4156), (4782, 4794), (2084, 2101), (8943, 8954),
                (4407, 4422), (5611, 5624), (7967, 7984), (8523, 8536), (2348, 2360), (3230, 3247), (8326, 8339),
                (1840, 1859), (6547, 6559), (8295, 8312), (3023, 3040), (886, 903), (2674, 2693), (6195, 6212),
                (3422, 3438), (1893, 1907), (9793, 9811), (8377, 8392), (4992, 5008), (4617, 4635), (433, 443),
                (595, 612), (2651, 2661), (2126, 2136), (2791, 2809), (9767, 9785), (8427, 8445), (3756, 3766),
                (6149, 6163), (2286, 2298), (44, 54), (7091, 7110), (7960, 7978), (5796, 5812), (6179, 6194),
                (6986, 7005), (4404, 4422), (8565, 8575), (2078, 2096), (832, 846), (7726, 7740), (28, 40),
                (1988, 2006), (5336, 5346), (6192, 6204), (2219, 2231), (655, 670), (6475, 6485), (8375, 8389),
                (8407, 8418), (760, 778), (9506, 9522), (3013, 3023), (9532, 9545), (8216, 8229), (6066, 6078),
                (5261, 5271), (204, 216), (3768, 3782), (989, 1002), (6891, 6906), (1029, 1041), (7056, 7069),
                (2641, 2651), (220, 232), (8663, 8677), (7003, 7017), (5369, 5380), (8030, 8040), (4164, 4179),
                (174, 186), (4419, 4435), (3913, 3923), (5804, 5815), (5275, 5288), (8756, 8772), (1195, 1207),
                (5532, 5549), (2889, 2900), (1500, 1510), (5688, 5702), (7985, 8000), (8640, 8651), (6708, 6718),
                (2902, 2912), (9178, 9192), (2796, 2809), (1214, 1230), (5326, 5336), (418, 430), (2595, 2606),
                (672, 682), (4171, 4183), (9435, 9454), (63, 74), (979, 994), (8457, 8473), (2595, 2610), (7793, 7805),
                (6568, 6582), (4779, 4794), (7314, 7330), (1501, 1516), (9569, 9581), (2891, 2901), (4857, 4869),
                (3184, 3199), (959, 975), (9075, 9085), (5589, 5603), (5673, 5689), (5174, 5187), (5085, 5095),
                (5641, 5652), (3057, 3070), (4859, 4875)],
               [True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True,
                True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True,
                True, True, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True,
                True, False, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True,
                False, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True, True,
                False, True, True, True, True, True, True, True, True, True, True, False, True, True, True, True, True,
                True, True, False, True, True, True, False, True, True, True, False, True, True, True, False, True,
                True, True, True, True, True, True, True, True, True, True, True, False, True, False, False, True, True,
                False, False, False, True, True, False, False, True, True, False, True, False, True, True, True, True,
                True, False, True, True, False, False, False, False, True, False, True, False, True, True, False, True,
                True, True, True, False, True, True, True, False, True, False, True, True, False, True, False, False,
                True, False, False, True, True, True, True, True, False, True, True, True, True, False, True, True,
                True, True, True, False, True, False, False, False, True, False, True, False, False, True, True, True,
                False, True, True, False, True, False, False, True, True, True, False, True, True, False, False, False,
                False, True, True, False, False, True, False, True, False, True, False, False, True, False, True, False,
                True, True, False, False, True, False, False, False, True, True, False, False, True, False, True, False,
                True, True, True, True, False, False, True, False, False, False, False, True, True, True, False, False,
                True, False, True, True, False, True, True, False, True, False, False, True, True, False, True, True,
                False, False, True, False, True, True, False, True, False, True, True, False, False, True, False, False,
                False, True, False, False, False, False, True, False, True, False, False, False, False, True, True,
                False, True, True, True, True, False, True, False, True, True, False, True, True, True, False, True,
                False, False, False, False, True, False, False, False, True, True, True, False, True, False, False,
                True, False, False, False, False, True, True, True, True, False, False, True, True, True, False, True,
                False, True, True, True, True, True, False, False, False, False, False, False, False, False, False,
                False, True, True, True, True, False, False, False, False, False, True, True, False, False, False,
                False, True, False, False, False, True, False, True, True, False, False, False, False, True, False,
                True, False, False, True, True, False, False, False, False, False, False, True, True, True, False, True,
                False, False, False, False, False, False, False, True, True, True, False, False, True, False, False,
                False, False, True, False, False, False, False, True, False, True, False, True, False, True, True,
                False, False, True, False, True, True, True, False, False, False, False, True, False, True, True, False,
                False, True, False, False, False, False, False, False, False, True, False, False, True, False, False,
                True, False, False, True, True, False, False, False, False, False, False, True, False, True, False,
                False, True, False, False, False, True, False, False, False, False, True, False, True, False, False,
                False, False, False, False, True, False, False, True, False, False, False, True, True, False, False,
                True, False, False, False, False, False, False, False, False, False, True, False, False, True, False,
                False, False, False, False, False, True, True, False, True, False, False, False, True, False, False,
                True, False, True, False, False, True, False, False, True, False, False, True, False, False, False,
                True, False, True, False, False, False, False, False, False, False, False, False, True, True, False,
                False, False, False, False, True, False, False, False, False, True, False, False, True, False, False,
                False, True, False, False, False, False, False, False, False, True, False, True, False, False, False,
                True, False, True, True, False, True, False, False, False, False, True, False, False, False, False,
                False, False, False, True, False, False, False, False, False, False, False, False, False, True, True,
                False, False, False, True, True, False, False, True, True, False, False, True, False, False, False,
                False, True, True, True, False, False, True, False, False, False, False, False, True, False, False,
                False, False, False, False, False, False, True, False, False, True, False, True, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, True, False, False, False,
                True, False, False, False, False, False, False, False, False, False, True, False, False, False, False,
                False, False, False, False, True, False, False, False, True, False, True, False, False, False, True,
                False, False, False, True, False, True, True, False, False, False, True, True, True, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, False, True, False, False, True, False, True, False, False, False, False, False, False,
                False, False, False, True, False, False, True, False, False, True, False, False, False, False, False,
                True, False, True, False, False, False, False, False, False, False, False, False, False, False, False,
                False, False, True, False, False, False, True, False, False, False, False, False, False, True, False,
                False, False, False, False, False, False, False, True, False, False, True, False, True, False, False,
                False, False, False, False, False, False, False, True, True, False, True, False, False, False, False,
                False, False, False, False, False, False, True, False, False, False, False, False, True, True, False,
                False, False, False, True, False, True, False, False, False, False, False, False, False, False, False,
                False, False, True, False, True, False, False, False, False, False, True, True, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, True, True, False, False,
                True, True, False, True, False, False, True, True, False, False, True, False, True, False, True, True,
                False, False, False, True, False, False, False, True, False, False, False, False, False, True, False,
                False, False, False, False, False, False, False, False, True, False, False, False, False, False, False,
                False, False, False, False, False, False, False, False, False, False, False, False, False, False, True,
                False, True, False, False, True, False, True, False, False]), ]
for test_parameters, expected_values in test_cases:
    test_object = MyCalendar()
    for (test_start, test_end), expected_output in zip(test_parameters, expected_values):
        assert test_object.book(test_start, test_end) is expected_output
