"""
Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a
 value greater than X.

Return the number of good nodes in the binary tree.
"""
from _Binary_Tree import TreeNode, TREE_NODE_TYPE, ConstructTree


def good_nodes_count(root: TreeNode) -> int:
    """
    :param root: root a binary tree with 1 <= no of nodes <= 100000
    :return: number of good nodes, i.e. x where x is greater than or equal to all nodes from root to x
    """

    def count_in_sub_tree(current_node: TreeNode, max_value_in_path: TREE_NODE_TYPE) -> int:
        """
        :param current_node: can not be None
        :param max_value_in_path: max value in the path from root to current_node
        :return: no. of good nodes in sub tree beneath current_node
        """
        self_is_good_node = max_value_in_path <= current_node.val
        max_value_in_path = max(max_value_in_path, current_node.val)
        return self_is_good_node + \
               (count_in_sub_tree(current_node.left, max_value_in_path) if current_node.left else 0) + \
               (count_in_sub_tree(current_node.right, max_value_in_path) if current_node.right else 0)

    return 1 + \
           (count_in_sub_tree(root.left, root.val) if root.left else 0) + \
           (count_in_sub_tree(root.right, root.val) if root.right else 0)


test_cases = [([3, 1, 4, 3, None, 1, 5], 4),
              ([3, 3, None, 4, 2], 3),
              ([1], 1),
              ([474, -33, 862, 10, 855, -760, 823, -451, 641, 175, -542, 696, 92, -273, 919, 938, 334, -377, -726, None,
                -365, 280, 454, -595, -284, -151, -626, -525, 507, -173, None, 750, 820, 493, -654, 276, None, -181,
                894, -657, -701, None, None, 281, 700, None, None, 937, -828, None, None, None, None, -460, 56, 956,
                -574, 835, 150, -802, 341, 42, -675, -630, -467, 687, -441, None, None, 884, 324, 493, 301, None, None,
                None, None, -810, -617, 955, 827, -495, 834, -20, 441, None, 358, 525, -860, 555, 778, None, None, 920,
                -589, 207, -374, None, 878, None, 401, 785, -738, -551, 13, 458, 545, -309, None, None, 987, -57, None,
                -319, 644, 636, -904, -319, 36, -342, -44, None, None, -738, 421, -268, -957, None, None, -557, 178,
                600, 386, -892, -565, -814, None, None, 571, -778, -150, 972, -875, 732, -185, 68, 654, 220, -717, None,
                None, 68, -369, -886, -135, -212, 792, -950, 913, None, 863, -595, 644, 989, 866, None, -132, -835, 231,
                538, -151, 250, -475, None, -992, None, None, -468, 669, -195, 517, None, -602, 48, 352, -39, 782, 308,
                -821, 906, -699, None, -300, 1, 725, None, 114, None, None, None, None, None, 795, 851, None, 190, -751,
                None, 769, 995, 231, None, None, None, None, None, None, 669, -378, -50, -483, None, None, None, 458,
                -720, 539, 284, -661, 455, 78, 681, 607, 355, None, None, None, None, None, 896, -413, -151, 257, -129,
                None, None, None, None, 139, -405, -237, None, None, None, 358, 782, 296, -50, 303, None, -366, 291,
                -457, None, None, 967, None, -666, 533, -422, None, 514, -748, 252, -795, None, -73, 264, 875, None, 86,
                -24, 144, -12, 273, -930, 617, 994, 723, None, -333, None, None, None, 246, 690, -724, 171, -992, -298,
                596, 361, -989, -477, None, 320, -133, 644, None, -713, -825, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, -808, -100, -226, None, None, 415, None, None,
                None, None, 308, 274, -515, None, -543, 654, 195, None, -737, -197, None, 34, None, -312, None, 596,
                None, None, None, 48, -28, -837, None, None, None, -166, 189, None, None, None, 198, None, -704, None,
                -600, -822, -348, 538, -566, 853, None, None, 8, -544, None, 526, None, None, None, None, -295, 867,
                None, -347, -917, 689, None, None, 745, -108, -187, 211, 328, -198, None, None, -432, None, -712, None,
                None, 421, None, -358, -997, None, 866, None, 715, None, 558, 150, -872, -551, -155, 348, 896, -788,
                -133, -738, None, -158, None, None, None, None, None, 614, -484, 608, 137, -429, None, 786, 757, -31,
                None, 172, 365, None, None, -763, 427, -160, None, -547, None, -721, None, None, None, None, 222, -659,
                None, 36, -848, None, None, -102, None, None, None, None, None, None, -230, -891, -193, -731, -496, 172,
                None, 110, -255, -753, 730, -661, -152, -690, None, None, -3, None, 457, None, None, None, None, -694,
                -597, None, -866, None, None, None, None, -364, -515, None, 426, 87, None, None, None, None, None, None,
                None, None, None, None, None, None, -692, None, 150, 387, -911, 68, None, None, -157, 217, -206, -481,
                -627, None, None, None, 337, -316, -483, -260, -127, -829, -253, None, None, 721, -820, None, None,
                None, None, None, None, None, None, None, 739, 972, None, None, -368, -453, -584, None, None, -966,
                -643, 660, -332, None, None, 476, None, -748, None, None, -325, -749, 595, None, None, None, 562, -230,
                -40, 388, -399, None, -115, 929, None, None, -688, None, None, None, None, None, None, None, 244, -88,
                -162, 2, -688, None, None, None, None, None, None, None, None, -273, None, None, None, None, 857, -724,
                None, None, None, None, None, -783, -297, None, -417, None, None, None, -767, None, -368, -478, -394,
                None, None, -453, None, None, -138, -557, None, None, None, None, None, None, None, None, None, None,
                816, 370, None, 870, None, -847, None, None, 356, 756, 849, 325, 206, None, -274, None, None, None,
                None, -561, -986, -368, None, -891, None, None, -812, None, 316, None, -608, -391, 860, 237, 540, None,
                None, None, -217, 435, None, None, None, None, None, None, None, None, None, None, 856, -120, 243, None,
                None, 774, None, None, -975, None, 994, 673, None, None, -218, 704, None, None, -240, None, None, None,
                None, None, 621, 81, -392, None, None, 898, -351, None, -437, 734, -280, 210, None, None, None, None,
                None, None, -429, None, -511, 495, -29, -622, 437, 123, None, None, -648, None, None, None, -265, None,
                None, None, None, 413, None, None, None, None, None, None, 184, -600, None, None, -62, None, None, None,
                None, 950, 212, 421, None, 897, None, None, None, None, -212, None, None, None, 33, None, -473, 9, -32,
                -175, -396, -64, None, None, 50, None, None, None, None, 691, 491, -372, None, None, None, None, None,
                922, None, None, None, None, None, None, None, None, None, -818, -685, -855, None, -231, 821, -514,
                None, None, None, None, -657, None, None, None, None, None, None, None, None, None, 268, -564, None,
                -951, None, None, None, 627, None, None, None, None, None, None, None, 965, None, None, None, None, 1,
                None, -631, None, None, None, None, None, -679, 106, None, -311, None, None, None, None, None, None,
                None, None, 735, 397, -813, None, None, None, 757, None, None, None, None, -612, None, None, -756, None,
                None, None, None, 149, None, None, 306, None, 515, None, -905, 106, None, None, None, -610, -414, -575,
                None, None, 764, 554, None, 749, -905, None, None, None, -885, None, None, -681, None, None, None, -148,
                None, -807, None, 713, None, None, 147, None, None, None, None, None, 128, None, None, 201, None, None,
                None, None, None, 75, None, None, None, None, 377, 176, -489, None, None, None, None, None, None, None,
                708, 288, 595, None, None, None, 78, -34, None, None, 942, -903, None, None, None, None, -493, None,
                None, None, None, None, None, None, None, None, None, None, 286, -132, None, -37, None, None, None,
                None, None, None, None, None, None, None, None, -129, 894, None, -828, None, None, 455, 909, None, None,
                -664, -72, None, None, None, None, None, None, None, None, 823, None, -952, None, None, -283, None,
                -967, None, 774, 149, None, None, None, None, None, 863, 461, 751, None, None, None, None, None, None,
                None, None, None, None, None, -165, -900], 41),
              ]
for test_tree_list, expected_count in test_cases:
    assert good_nodes_count(ConstructTree.build_tree_leetcode(test_tree_list).root) == expected_count
