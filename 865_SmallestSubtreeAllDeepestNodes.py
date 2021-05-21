"""
Given the root of a binary tree, the depth of each node is the shortest distance to the root.

Return the smallest subtree such that it contains all the deepest nodes in the original tree.

A node is called the deepest if it has the largest depth possible among any node in the entire tree.

The subtree of a node is tree consisting of that node, plus the set of all descendants of that node.

Note: This question is the same as 1123: https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
"""
from typing import Tuple, Optional

from _Binary_Tree import BinaryTree, TreeNode, ConstructTree


def sub_tree_with_all_deepest_nodes(root: TreeNode) -> TreeNode:
    """
    :param root: root of an non empty binary tree
    :return: root of the smallest sub tree with all deepest nodes
    """

    def solve_beneath(current_node: TreeNode) -> Tuple[int, Optional[TreeNode]]:
        """
        :param current_node: solve the problem within sub tree beneath current_node
        :return: deepest depth (with the sub tree), and root of the smallest sub tree (within the sub tree)
        """
        left_depth, left_node = solve_beneath(current_node.left) if current_node.left else (0, None)
        right_depth, right_node = solve_beneath(current_node.right) if current_node.right else (0, None)
        if left_depth > right_depth:
            # left child has deeper sub tree
            return 1 + left_depth, left_node
        elif left_depth < right_depth:
            # right child has deeper sub tree
            return 1 + right_depth, right_node
        else:
            # two sides have equally deep tree nodes
            return 1 + left_depth, current_node

    return solve_beneath(root)[1]


test_cases = [([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], [2, 7, 4]),
              ([1], [1]),
              ([0, 1, 3, None, 2], [2]),
              ([0, 1, None, None, 2, None, 3, None, 4], [4]),
              ([0, 1, 29, 2, 3, 41, 43, 11, 4, None, 5, None, None, None, None, 27, 15, 18, 7, 19, 6, None, 36, None,
                33, None, None, 8, 10, None, 22, None, 17, None, None, None, None, 16, 9, 20, 12, 23, 28, None, 39, 34,
                None, 14, None, 46, 42, 26, 13, 31, None, 30, 48, None, None, None, None, None, 37, None, 47, None,
                None, 45, None, 21, 44, None, None, None, 35, None, 49, None, None, None, None, None, None, 24, 32,
                None, None, None, None, None, None, 25, None, None, None, None, 38, None, 40], [40]),
              ([0, 216, 1, 411, 251, 2, 9, None, None, 264, None, 14, 3, 18, 35, 476, None, 21, 362, 6, 4, 84, 39, 54,
                48, None, None, 32, 27, None, None, 7, 19, 11, 5, None, 112, 56, 49, 77, 180, 74, None, 37, None, 59,
                100, 20, 8, 266, 26, 16, 24, 15, 12, 138, 260, None, 170, 51, 302, None, 85, None, 233, 101, 454, 122,
                61, 81, 345, 245, 154, 31, 66, 13, 10, None, 395, None, 36, 33, 17, 44, 38, 91, 30, 34, 40, 333, 227,
                446, 343, 218, None, 92, 70, None, None, None, 99, 497, None, 468, 102, None, None, 327, 147, 117, 62,
                104, 87, None, 372, 257, None, None, 294, 96, 57, 75, 413, 25, 63, 42, 90, None, None, 52, 64, 45, 68,
                22, 23, 76, 116, None, 60, None, 151, 238, 228, 78, 131, None, 134, None, 451, None, 382, None, None,
                469, None, 348, None, 201, 111, 492, 298, 267, 172, None, None, None, None, 182, None, None, None, 250,
                186, 305, 220, 80, 86, 175, None, 385, 97, 416, 429, None, None, None, 383, None, 160, None, 120, 225,
                262, None, None, 124, 28, 118, 110, 71, None, 103, 98, 82, 162, 241, 73, 121, None, None, 265, 46, 69,
                41, 55, None, None, 129, 288, 126, 105, None, 152, 428, 408, None, None, 83, 143, 244, 312, None, 214,
                None, None, None, 488, None, None, 452, None, 208, 311, 287, 141, None, None, 314, None, 270, None, 291,
                253, None, None, 309, 338, None, 423, None, None, 277, 299, 135, 156, 114, 443, None, 356, 387, None,
                200, 153, None, 461, None, 433, None, None, 290, None, 276, 352, 306, 240, None, None, 188, 169, 29, 53,
                165, 178, None, 132, 194, 232, 316, 205, 158, 296, 211, 93, None, 179, None, None, None, 419, 146, None,
                272, 279, 89, 50, 88, 246, 168, 119, 72, 58, 231, 140, 450, 417, 230, 176, 315, 149, 207, None, None,
                None, None, 409, 95, 148, 167, 489, None, 328, 368, 359, None, None, None, None, None, 467, 217, None,
                None, 355, None, 330, None, None, None, None, None, 426, 394, None, 334, None, None, None, None, None,
                None, None, 278, 357, None, None, 185, None, None, None, 133, None, None, None, None, None, None, None,
                331, None, 174, 366, None, None, None, 439, 459, None, None, None, None, None, 407, 367, None, 318, 301,
                None, None, 171, 43, 47, 199, 144, 379, 249, None, None, 166, 444, None, None, None, 310, None, None,
                None, None, 203, 226, None, None, None, 256, 195, None, None, None, None, None, 213, 285, None, 404,
                None, 472, 145, 177, 123, None, 127, 106, 397, None, 424, 346, None, 173, 109, 79, 65, 137, 393, None,
                None, 283, None, None, None, None, 386, None, 204, 193, None, 353, 187, None, 415, 300, None, None, 161,
                None, 189, 181, 190, None, None, None, 449, None, None, 398, None, None, None, None, None, 274, None,
                None, None, None, None, 442, None, None, None, None, 284, None, 402, None, 215, None, None, 336, None,
                None, 470, 317, None, None, None, None, None, None, None, None, None, None, 323, None, None, 341, None,
                None, 67, 155, 197, 198, None, 297, None, 435, None, None, 354, 255, None, 375, 480, None, None, None,
                360, 252, 374, None, 406, 482, None, None, 286, None, None, None, None, None, None, None, None, 191,
                271, None, 282, None, 235, 498, 273, 107, 457, None, None, None, None, 400, 361, 380, 125, 222, 128,
                108, 94, 329, 434, 295, None, 437, None, None, None, None, None, 219, None, 462, None, 445, 236, 319,
                None, None, 339, None, 163, 326, 209, None, 392, 258, 196, None, None, None, None, 412, 471, 499, None,
                448, 324, None, None, None, 391, 242, None, 475, None, None, None, None, None, None, 390, None, 261,
                130, 237, 184, 313, None, 281, 487, None, None, None, None, None, 425, None, None, None, None, None,
                None, 414, 466, None, 453, None, None, None, None, None, None, 292, 478, 192, None, 293, 303, None, 370,
                248, None, None, None, 430, None, 139, 304, 465, 477, None, None, None, 364, None, None, None, 229, 320,
                None, 183, None, 212, 113, 496, None, None, 340, None, None, 381, None, None, None, 221, None, None,
                None, None, None, 335, 388, None, None, None, 363, None, 440, None, None, 325, 247, None, None, None,
                None, 289, None, None, 432, None, None, None, None, None, None, None, 484, None, None, 321, 269, None,
                None, None, None, None, 373, 485, 403, 344, 243, 254, 202, None, 473, 347, 455, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, None, None, 308, None, None, None, None,
                None, None, None, None, None, 142, None, None, 369, None, None, None, None, 436, None, 376, 420, None,
                None, None, None, None, None, 115, 263, None, None, None, 399, None, None, 371, 234, 351, None, 474,
                None, 441, None, None, None, 483, 418, None, None, 358, 427, None, None, None, None, 349, None, 365,
                None, 389, None, None, None, None, None, 384, 438, None, 410, None, None, 378, 350, None, 479, None,
                None, None, 464, None, 332, 405, None, None, None, None, None, None, None, None, 447, 136, 164, 280,
                None, 401, None, 456, None, None, 422, None, None, None, None, None, None, None, None, 486, None, None,
                None, None, 493, None, None, None, None, None, None, 458, None, None, None, None, None, None, None,
                None, 490, None, None, None, 494, None, None, None, None, None, None, 150, 157, 206, 396, None, 337,
                None, None, None, 495, None, 481, None, None, None, None, None, None, None, None, None, None, 159, 210,
                307, 377, 259, None, None, 421, None, None, None, None, None, None, 268, None, 431, 223, None, 342,
                None, 491, None, None, None, None, None, None, None, 460, 275, 224, None, None, None, None, None, None,
                None, None, 322, 239, 463], [463]), ]
for test_tree_list, expected_list in test_cases:
    get_root = sub_tree_with_all_deepest_nodes(ConstructTree.build_tree_leetcode(test_tree_list).root)
    get_tree = BinaryTree(get_root).leetcode_traversal()
    assert get_tree[:len(expected_list)] == expected_list
    assert get_tree[len(expected_list):] == [None] * (len(get_tree) - len(expected_list))
