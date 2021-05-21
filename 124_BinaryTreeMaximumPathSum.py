"""
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the
parent-child connections. The path must contain at least one node and does not need to go through the root.
"""
from _Binary_Tree import TreeNode, ConstructTree


def max_path_sum(root: TreeNode) -> int:
    """
    :param root: root of an non-empty binary tree
    :return: maximum path sum in the tree
    """

    def max_path_end_at_node(node: TreeNode) -> int:
        """
        :return: max value of the path ends at node. return 0 if the max path is negative
        """
        nonlocal global_max
        if not node:
            return 0
        left_max = max_path_end_at_node(node.left)
        right_max = max_path_end_at_node(node.right)
        global_max = max(global_max, left_max + node.val + right_max)
        return max(node.val + max(left_max, right_max), 0)

    global_max = -2 ** 31 + 1
    max_path_end_at_node(root)
    return global_max


test_cases = [([1, 2, 3], 6),
              ([-10, 9, 20, None, None, 15, 7], 42),
              ([-191, 563, 664, -875, 988, 198, -505, -420, 795, 957, None, 536, -995, -681, 821, 381, -852, -506, -786,
                964, 392, -675, -654, -717, 479, -402, -223, -666, None, 249, None, None, None, 714, 164, None, None,
                None, None, -580, None, None, 652, -153, 144, 142, -776, 906, -665, 194, None, None, None, None, None,
                382, None, 25, 118, None, 433, -754, 53, 701, None, -496, 837, None, None, 994, -440, None, -98, -456,
                852, -237, -159, None, 92, 628, -681, None, None, 547, None, None, 600, None, None, None, None, None,
                None, None, None, None, None, 237, -127, 795, None, None, None, 316, 53, -191, 628, 3, 357, 474, None,
                None, None, None, None, None, None, None, None, -746, -650, None, 805, -201, 750, None, None, None,
                None, -925, -237, None, -147, 629, -769, None, None, None, -846, None, -776, None, None, None, None,
                None, None, None, None, None, None, -906, 552, None, None, None, None, 675, -832, 594, None, -61, None,
                None, None, -291, -783, None, None, -660, None, 789, None, None, -786, -853, None, -534, -321, -564,
                -398, 358, -874, None, None, None, None, None, None, None, None, None, None, None, None, None, -598,
                None, None, None, None, None, 593], 7317),
              ([0], 0),
              ([-3], -3),
              ([-10, 9, 20, None, None, 15, 7], 42), ]
for test_tree_list, expected_value in test_cases:
    assert max_path_sum(ConstructTree.build_tree_leetcode(test_tree_list).root) == expected_value
