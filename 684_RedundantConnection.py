"""
In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added
 edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented
 as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the
 graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers,
 return the answer that occurs last in the input.
"""
from typing import List, Tuple, Dict

from _Union_Find import UnionFindArray


def find_redundant_connections_dfs(edges: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    Tree with 3 <= n <= 1000 nodes, with an additional graph that caused a cycle (i.e. the graph is connected)

    :param edges: list of (ai, bi) representing an edge between ai and bi,
        1 <= ai < bi < len(edges),
        ai != bi,
        no repeated edges
    :return: an edge of the cycle that showed last in the edges list
    """

    def dfs_is_connected(start_node: int, end_node: int) -> bool:
        """
        :param start_node: a node in graph
        :param end_node: a node in graph
        :return: there exists a path from start_node to to_node
        """
        if start_node == end_node:
            return True
        seen_nodes.add(start_node)
        return any(dfs_is_connected(neighbor_node, end_node)
                   for neighbor_node in graph[start_node] if neighbor_node not in seen_nodes)

    graph: Dict[int, List[int]] = {}
    for u, v in edges:
        seen_nodes = set()
        if u in graph and v in graph and dfs_is_connected(u, v):
            return u, v
        if u in graph:
            graph[u].append(v)
        else:
            graph[u] = [v]
        if v in graph:
            graph[v].append(u)
        else:
            graph[v] = [u]


def find_redundant_connections_union_find(edges: List[Tuple[int, int]]) -> Tuple[int, int]:
    """
    Tree with 3 <= n <= 1000 nodes, with an additional graph that caused a cycle (i.e. the graph is connected)

    :param edges: list of (ai, bi) representing an edge between ai and bi,
        1 <= ai < bi < len(edges),
        ai != bi,
        no repeated edges
    :return: an edge of the cycle that showed last in the edges list
    """
    nodes_list = UnionFindArray(len(edges) + 1, use_recursion=True)
    for edge in edges:
        if nodes_list.is_connected(*edge):
            return edge
        nodes_list.unify(*edge)


test_cases = [([(1, 2), (1, 3), (2, 3)], (2, 3)),
              ([(1, 2), (2, 3), (3, 4), (1, 4), (1, 5)], (1, 4)),
              ([(85, 163), (37, 148), (22, 167), (60, 114), (66, 179), (53, 118), (15, 133), (52, 70), (19, 198),
                (147, 184), (20, 125), (76, 153), (94, 132), (98, 127), (144, 180), (2, 109), (144, 161), (89, 197),
                (62, 174), (81, 149), (76, 168), (36, 197), (11, 122), (140, 145), (87, 134), (131, 154), (86, 134),
                (3, 80), (37, 135), (36, 163), (88, 144), (24, 109), (18, 113), (57, 115), (13, 194), (9, 104),
                (20, 104), (36, 78), (71, 78), (59, 174), (59, 111), (107, 192), (74, 112), (85, 190), (108, 197),
                (21, 157), (15, 91), (74, 130), (38, 62), (127, 145), (99, 171), (115, 168), (41, 175), (75, 168),
                (67, 179), (21, 68), (125, 180), (63, 124), (114, 188), (17, 69), (155, 175), (61, 196), (43, 165),
                (10, 189), (129, 139), (152, 174), (71, 186), (86, 146), (4, 131), (7, 193), (152, 178), (77, 160),
                (26, 149), (92, 179), (141, 155), (121, 164), (14, 135), (28, 70), (15, 182), (85, 177), (33, 123),
                (10, 30), (25, 150), (19, 105), (76, 101), (45, 58), (146, 173), (79, 96), (183, 190), (40, 124),
                (128, 151), (142, 153), (46, 175), (50, 156), (19, 64), (64, 174), (54, 73), (67, 114), (27, 30),
                (12, 110), (80, 195), (48, 184), (42, 124), (99, 102), (156, 166), (150, 199), (29, 90), (106, 166),
                (59, 139), (44, 67), (141, 167), (81, 123), (99, 115), (19, 100), (95, 116), (21, 97), (1, 46),
                (55, 73), (118, 195), (148, 151), (29, 192), (47, 98), (156, 194), (32, 133), (90, 189), (18, 101),
                (39, 108), (35, 58), (94, 164), (24, 129), (84, 115), (113, 147), (19, 120), (15, 187), (125, 127),
                (23, 118), (158, 193), (6, 93), (89, 130), (51, 190), (83, 117), (46, 181), (143, 191), (11, 165),
                (100, 143), (9, 122), (60, 193), (49, 83), (68, 96), (5, 37), (8, 105), (124, 126), (48, 82), (46, 116),
                (94, 137), (147, 159), (7, 169), (56, 74), (5, 155), (103, 185), (154, 160), (56, 185), (77, 151),
                (79, 132), (10, 17), (53, 65), (172, 177), (31, 136), (10, 54), (7, 165), (113, 173), (47, 119),
                (31, 72), (93, 144), (153, 176), (31, 123), (12, 27), (94, 199), (35, 68), (102, 200), (162, 176),
                (94, 170), (138, 153), (15, 102), (144, 178), (106, 151), (3, 45), (70, 149), (23, 49), (81, 196),
                (28, 34), (21, 61), (17, 150), (40, 154), (48, 51), (78, 192), (16, 74), (116, 158), (12, 16),
                (13, 34)], (12, 16)),
              ([(47, 193), (409, 848), (40, 220), (107, 207), (232, 944), (225, 507), (715, 914), (1, 883), (595, 619),
                (911, 918), (111, 650), (226, 991), (87, 761), (303, 805), (46, 963), (10, 113), (542, 634), (37, 176),
                (229, 943), (378, 944), (184, 974), (354, 439), (721, 762), (559, 566), (456, 798), (139, 433),
                (777, 860), (59, 102), (438, 934), (363, 900), (305, 403), (703, 888), (132, 415), (230, 766),
                (83, 783), (896, 917), (35, 152), (535, 836), (178, 506), (349, 787), (337, 776), (268, 796),
                (277, 824), (299, 902), (258, 598), (240, 861), (410, 858), (396, 699), (7, 116), (153, 618),
                (212, 352), (75, 573), (158, 377), (556, 607), (185, 678), (236, 649), (487, 872), (101, 641),
                (306, 889), (208, 471), (318, 947), (345, 796), (9, 343), (63, 111), (525, 857), (592, 792), (739, 849),
                (387, 560), (162, 874), (238, 831), (464, 820), (336, 692), (127, 719), (359, 580), (115, 434),
                (565, 924), (649, 840), (573, 985), (53, 527), (113, 302), (616, 689), (200, 910), (39, 741), (82, 343),
                (67, 265), (409, 517), (250, 734), (311, 898), (263, 584), (688, 971), (305, 994), (648, 839),
                (45, 526), (213, 615), (43, 85), (476, 564), (424, 965), (488, 860), (249, 967), (261, 583), (267, 420),
                (106, 462), (1, 533), (158, 862), (205, 468), (438, 587), (526, 891), (522, 586), (181, 357), (73, 881),
                (253, 383), (73, 903), (14, 263), (410, 492), (508, 830), (413, 845), (267, 705), (134, 247),
                (506, 978), (348, 534), (159, 403), (937, 964), (282, 761), (171, 320), (146, 384), (182, 971),
                (77, 262), (50, 693), (319, 857), (101, 887), (542, 887), (152, 329), (11, 213), (374, 599), (154, 738),
                (65, 180), (654, 998), (144, 415), (403, 624), (357, 867), (460, 652), (35, 454), (71, 954), (650, 659),
                (61, 183), (221, 403), (108, 292), (341, 345), (328, 608), (335, 574), (341, 365), (31, 965),
                (392, 747), (189, 989), (518, 963), (759, 925), (570, 576), (352, 818), (163, 859), (408, 703),
                (22, 590), (118, 639), (19, 369), (55, 633), (1, 637), (541, 676), (27, 142), (396, 603), (660, 913),
                (117, 436), (832, 884), (195, 542), (381, 696), (455, 766), (36, 370), (657, 953), (146, 630),
                (868, 938), (139, 297), (216, 446), (808, 890), (32, 696), (163, 400), (331, 753), (809, 1000),
                (419, 591), (398, 463), (130, 683), (521, 839), (344, 551), (364, 850), (702, 789), (446, 736),
                (170, 831), (46, 147), (738, 831), (68, 91), (494, 991), (64, 110), (278, 435), (276, 998), (717, 749),
                (311, 591), (38, 885), (341, 784), (803, 965), (370, 391), (353, 870), (450, 465), (43, 949), (52, 802),
                (93, 605), (68, 910), (343, 945), (215, 489), (167, 596), (36, 957), (431, 631), (474, 807), (98, 748),
                (334, 946), (123, 202), (403, 627), (503, 879), (509, 951), (78, 981), (133, 807), (260, 554),
                (575, 702), (453, 960), (463, 645), (183, 876), (464, 794), (101, 481), (333, 760), (519, 832),
                (680, 737), (26, 921), (109, 770), (23, 835), (186, 716), (940, 991), (574, 767), (677, 895),
                (957, 990), (85, 725), (1, 260), (19, 557), (696, 854), (241, 684), (23, 322), (275, 775), (686, 865),
                (632, 716), (86, 90), (602, 777), (222, 587), (119, 716), (253, 773), (33, 504), (120, 260), (127, 928),
                (394, 829), (829, 913), (625, 654), (276, 816), (103, 379), (188, 475), (214, 580), (362, 878),
                (24, 922), (462, 791), (745, 900), (390, 953), (239, 779), (912, 941), (65, 703), (431, 944),
                (601, 796), (105, 537), (412, 959), (158, 402), (648, 727), (91, 909), (85, 685), (596, 853),
                (120, 653), (253, 713), (836, 988), (679, 775), (113, 417), (275, 432), (2, 823), (407, 683),
                (126, 437), (73, 695), (401, 791), (306, 550), (163, 605), (298, 808), (210, 901), (663, 811),
                (346, 593), (278, 744), (459, 744), (117, 271), (74, 573), (444, 536), (621, 952), (171, 543),
                (779, 855), (124, 721), (156, 975), (60, 465), (355, 426), (406, 710), (247, 845), (571, 742),
                (678, 841), (247, 972), (18, 234), (257, 935), (668, 753), (528, 811), (30, 780), (607, 704), (38, 56),
                (136, 958), (432, 589), (695, 792), (160, 920), (735, 989), (330, 824), (161, 233), (440, 448),
                (625, 650), (765, 976), (349, 646), (767, 815), (224, 791), (278, 343), (585, 893), (457, 773),
                (321, 735), (396, 979), (39, 227), (363, 744), (248, 557), (170, 967), (184, 869), (96, 511),
                (130, 776), (274, 712), (181, 194), (675, 868), (508, 799), (120, 801), (75, 536), (145, 368),
                (453, 879), (372, 727), (69, 247), (146, 483), (878, 929), (242, 896), (225, 350), (730, 843),
                (758, 871), (315, 971), (621, 983), (609, 956), (207, 555), (150, 525), (47, 473), (309, 327),
                (417, 701), (332, 411), (90, 711), (534, 700), (167, 366), (772, 916), (70, 612), (391, 793),
                (177, 477), (687, 856), (587, 715), (52, 737), (451, 678), (76, 432), (430, 519), (349, 751),
                (261, 594), (411, 423), (239, 899), (310, 637), (406, 890), (480, 585), (152, 339), (241, 793),
                (560, 723), (43, 328), (387, 640), (84, 764), (479, 866), (283, 704), (743, 966), (285, 544),
                (130, 905), (38, 718), (607, 749), (764, 877), (633, 861), (273, 532), (109, 172), (412, 417),
                (486, 544), (310, 950), (21, 834), (415, 505), (37, 700), (41, 458), (108, 284), (184, 626), (104, 779),
                (139, 667), (392, 825), (42, 274), (37, 257), (105, 572), (179, 439), (600, 661), (280, 572),
                (558, 822), (59, 257), (279, 795), (182, 324), (762, 783), (81, 208), (374, 398), (651, 769),
                (486, 662), (438, 827), (499, 992), (266, 841), (44, 441), (56, 872), (192, 957), (169, 930),
                (510, 617), (183, 964), (172, 846), (106, 509), (259, 309), (243, 440), (90, 577), (241, 691),
                (209, 984), (66, 786), (365, 855), (195, 666), (427, 501), (138, 421), (680, 851), (367, 652),
                (389, 464), (100, 632), (131, 551), (72, 158), (167, 720), (23, 501), (729, 831), (433, 878),
                (422, 708), (67, 792), (281, 710), (405, 438), (57, 171), (157, 736), (80, 161), (273, 611), (226, 856),
                (431, 545), (55, 905), (173, 426), (168, 703), (212, 806), (89, 437), (122, 253), (613, 942), (20, 667),
                (85, 342), (326, 651), (437, 678), (323, 472), (722, 826), (938, 986), (425, 564), (2, 614), (270, 316),
                (511, 994), (340, 342), (227, 386), (136, 586), (361, 482), (342, 908), (374, 778), (443, 814),
                (682, 886), (147, 382), (164, 936), (425, 453), (752, 814), (621, 767), (452, 941), (391, 820),
                (98, 658), (160, 954), (785, 959), (470, 889), (347, 504), (467, 730), (43, 606), (507, 944), (30, 698),
                (201, 760), (270, 279), (616, 708), (177, 493), (627, 790), (396, 623), (380, 429), (360, 956),
                (34, 639), (532, 571), (144, 636), (346, 857), (442, 527), (130, 287), (92, 649), (606, 764),
                (228, 438), (726, 955), (885, 894), (28, 984), (701, 814), (670, 948), (422, 816), (467, 627),
                (112, 666), (482, 572), (480, 803), (617, 918), (20, 997), (99, 895), (374, 538), (244, 689), (60, 472),
                (186, 873), (135, 640), (220, 691), (575, 638), (213, 864), (485, 738), (165, 922), (129, 797),
                (201, 237), (17, 557), (307, 553), (357, 446), (6, 861), (382, 665), (469, 947), (225, 288), (809, 933),
                (358, 845), (347, 500), (196, 229), (464, 529), (513, 523), (103, 828), (12, 249), (252, 836),
                (523, 977), (197, 705), (349, 581), (853, 909), (66, 495), (897, 975), (133, 869), (343, 664),
                (211, 390), (826, 937), (402, 817), (501, 514), (149, 704), (520, 849), (379, 798), (898, 955),
                (56, 155), (380, 743), (688, 870), (238, 707), (149, 496), (118, 129), (419, 932), (517, 995),
                (564, 892), (432, 582), (147, 215), (148, 552), (539, 737), (652, 699), (252, 926), (668, 745),
                (177, 880), (198, 780), (498, 551), (120, 326), (29, 153), (141, 810), (191, 606), (137, 395),
                (622, 946), (186, 907), (384, 727), (490, 783), (308, 726), (613, 794), (393, 918), (156, 465),
                (108, 291), (340, 674), (569, 828), (222, 255), (351, 826), (261, 394), (17, 672), (48, 988),
                (865, 924), (296, 790), (438, 561), (277, 915), (141, 212), (254, 620), (454, 952), (234, 987),
                (424, 610), (380, 541), (49, 798), (235, 843), (93, 428), (441, 512), (137, 166), (702, 879),
                (515, 619), (57, 768), (474, 842), (150, 968), (125, 211), (620, 676), (64, 286), (312, 922),
                (596, 883), (388, 546), (51, 187), (190, 289), (472, 543), (3, 356), (304, 911), (395, 430), (445, 496),
                (842, 956), (347, 478), (506, 819), (84, 847), (771, 836), (571, 726), (461, 826), (462, 549),
                (139, 830), (810, 866), (15, 18), (346, 623), (187, 996), (314, 576), (63, 143), (45, 833), (50, 133),
                (222, 993), (720, 983), (863, 922), (482, 939), (772, 897), (416, 891), (212, 656), (151, 185),
                (929, 932), (305, 333), (458, 680), (344, 482), (164, 704), (152, 338), (203, 229), (418, 759),
                (520, 717), (220, 473), (770, 896), (250, 692), (897, 969), (286, 578), (77, 647), (142, 263),
                (221, 927), (347, 856), (436, 1000), (308, 872), (440, 503), (69, 325), (260, 562), (309, 922),
                (230, 300), (579, 636), (337, 638), (128, 929), (356, 502), (77, 651), (428, 486), (94, 257),
                (590, 901), (732, 816), (635, 639), (227, 993), (488, 622), (99, 523), (919, 954), (25, 318),
                (674, 730), (163, 958), (23, 223), (787, 968), (5, 400), (671, 686), (597, 622), (171, 788), (690, 765),
                (545, 706), (156, 996), (15, 318), (218, 881), (438, 531), (811, 996), (13, 633), (290, 468),
                (303, 355), (626, 724), (697, 961), (780, 960), (224, 850), (184, 559), (40, 643), (517, 703),
                (404, 439), (259, 744), (188, 436), (63, 258), (670, 690), (563, 875), (673, 869), (11, 692),
                (358, 813), (62, 272), (273, 290), (447, 746), (513, 915), (23, 570), (45, 238), (66, 672), (231, 798),
                (97, 603), (122, 204), (427, 599), (204, 527), (267, 852), (901, 973), (148, 160), (758, 880),
                (655, 694), (844, 1000), (149, 313), (66, 559), (224, 653), (4, 110), (130, 644), (114, 384),
                (288, 917), (479, 787), (123, 771), (757, 759), (295, 753), (614, 821), (547, 928), (272, 694),
                (44, 991), (218, 583), (100, 906), (306, 956), (246, 463), (555, 970), (761, 895), (40, 426),
                (403, 612), (578, 781), (888, 988), (921, 989), (429, 666), (156, 886), (642, 861), (552, 930),
                (548, 779), (416, 460), (144, 848), (336, 750), (58, 518), (206, 772), (332, 546), (558, 709),
                (82, 269), (116, 224), (376, 608), (205, 684), (934, 943), (321, 580), (302, 999), (993, 997),
                (293, 403), (432, 740), (276, 499), (190, 476), (188, 515), (427, 516), (728, 824), (272, 585),
                (78, 322), (250, 807), (436, 904), (908, 982), (397, 432), (34, 577), (179, 277), (123, 274),
                (524, 578), (28, 80), (145, 477), (324, 468), (495, 733), (594, 774), (256, 997), (343, 679),
                (268, 745), (399, 476), (561, 989), (607, 721), (486, 553), (681, 927), (409, 785), (92, 464),
                (299, 569), (174, 947), (389, 665), (568, 671), (373, 524), (491, 868), (16, 385), (728, 755),
                (381, 520), (534, 826), (3, 217), (147, 882), (250, 385), (345, 714), (59, 924), (32, 52), (301, 307),
                (581, 777), (357, 414), (444, 748), (423, 858), (126, 294), (432, 495), (628, 830), (354, 782),
                (418, 765), (509, 822), (520, 961), (953, 973), (393, 846), (199, 343), (186, 669), (774, 809),
                (297, 884), (567, 913), (32, 645), (140, 937), (946, 976), (841, 861), (274, 838), (298, 318),
                (191, 233), (151, 572), (175, 839), (417, 962), (138, 227), (251, 898), (407, 616), (490, 763),
                (162, 875), (153, 207), (591, 920), (756, 798), (471, 645), (739, 837), (8, 614), (257, 466),
                (375, 987), (135, 694), (183, 828), (162, 675), (439, 825), (54, 931), (49, 600), (121, 632),
                (242, 629), (461, 923), (291, 490), (63, 442), (662, 902), (79, 766), (177, 448), (317, 346),
                (706, 992), (75, 484), (118, 245), (127, 592), (178, 927), (271, 839), (489, 804), (114, 926),
                (666, 747), (111, 449), (21, 264), (21, 980), (153, 548), (373, 800), (166, 941), (614, 989),
                (147, 497), (540, 841), (181, 823), (27, 317), (186, 990), (22, 384), (698, 958), (279, 343),
                (217, 752), (523, 671), (754, 811), (263, 767), (534, 563), (88, 704), (597, 617), (588, 936),
                (805, 817), (219, 806), (366, 731), (492, 999), (31, 391), (414, 447), (371, 538), (127, 804),
                (358, 730), (262, 506), (54, 898), (530, 668), (375, 496), (95, 553), (93, 980), (634, 658), (14, 604),
                (359, 800), (928, 991), (577, 981), (146, 267), (115, 577), (812, 939), (47, 336), (3, 528), (899, 975),
                (140, 300), (129, 585), (18, 209)], (899, 975)), ]
for find_redundant_connections in [find_redundant_connections_union_find, find_redundant_connections_dfs, ]:
    for test_edges, expected_value in test_cases:
        assert find_redundant_connections(test_edges) == expected_value, find_redundant_connections.__name__
