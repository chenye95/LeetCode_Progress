"""
Given a binary tree, we install cameras on the nodes of the tree.

Each camera at a node can monitor its parent, itself, and its immediate children.

Calculate the minimum number of cameras needed to monitor all nodes of the tree.
"""
from typing import Tuple, Optional

from _Binary_Tree import TreeNode, ConstructTree


def min_camera_cover_dynamic_programming(root: TreeNode) -> int:
    """
    Top down approach: start from root

    :param root: root of a non empty binary tree with 1 <= # of nodes <= 1000
    :return: minimum number of cameras needed to monitor all nodes in the binary tree
    """
    max_count = 1000

    def cover_sub_tree(current_node: Optional[TreeNode]) -> Tuple[int, int, int]:
        """
        :param current_node: inspecting sub tree beneath current_node
        :return: minimum camera to cover (all nodes in sub tree except current_node, all nodes in sub tree but not
            placing a camera on current_node, all nodes in sub tree and placing a camera on current_node)
        """
        if current_node is None:
            return 0, 0, max_count

        left_node_not_covered, left_no_camera, left_camera = cover_sub_tree(current_node.left)
        right_node_not_covered, right_no_camera, right_camera = cover_sub_tree(current_node.right)

        not_cover_self = left_no_camera + right_no_camera
        cover_self_no_camera = min(right_camera + min(left_no_camera, left_camera),
                                   left_camera + min(right_no_camera, right_camera))
        cover_self_camera = 1 + \
                            min(left_node_not_covered, left_no_camera, left_camera) + \
                            min(right_node_not_covered, right_no_camera, right_camera)

        return not_cover_self, cover_self_no_camera, cover_self_camera

    return min(cover_sub_tree(root)[1:])


def min_camera_cover_greedy(root: TreeNode) -> int:
    """
    Bottom up approach: start from leaf nodes

    :param root: root of a non empty binary tree with 1 <= # of nodes <= 1000
    :return: minimum number of cameras needed to monitor all nodes in the binary tree
    """

    covered_nodes = {None}

    def cover_sub_tree(current_node: TreeNode, parent_node: TreeNode = None) -> int:
        """
        :param current_node: inspecting sub tree beneath current_node
        :param parent_node: parent node of current_node
        :return: min number of cameras needed to cover sub tree
        """
        camera_count = (cover_sub_tree(current_node.left, current_node) if current_node.left else 0) \
                       + (cover_sub_tree(current_node.right, current_node) if current_node.right else 0)
        """
        - if a node has children that is not covered by camera, place a camera
        - if a node has no parent and itself is not covered, place a camera
        - if a node has its children covered and has a parent, then it is strictly better to place the camera at this
         node's parent
        - in other words not placing cameras on leaf nodes
        """
        if parent_node is None and current_node not in covered_nodes or \
                current_node.left not in covered_nodes or current_node.right not in covered_nodes:
            camera_count += 1
            covered_nodes.update({current_node, parent_node})
            # also covered {current_node.left, current_node.right} but doesn't matter for back tracing

        return camera_count

    return cover_sub_tree(root, None)


test_cases = [([0], 1),
              ([0, None, 0], 1),
              ([0, 0, None, 0, 0], 1),
              ([0, 0, None, 0, None, 0, None, None, 0], 2),
              ([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None,
                None, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0,
                None, 0, 0, None, 0, None, 0, 0, 0, 0, 0, None, None, None, None, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0,
                0, None, None, None, None, 0, None, None, 0, None, None, None, None, 0, 0, 0, 0, 0, None, 0, 0, None,
                None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, 0, 0, None, None, 0, 0, None,
                0, None, 0, None, 0, 0, 0, None, 0, 0, None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0,
                None, 0, 0, 0, 0, 0, None, 0, 0, 0, None, None, 0, 0, 0, 0, 0, 0, None, 0, 0, None, None, 0, None, 0, 0,
                None, 0, 0, None, 0, 0, 0, 0, 0, None, 0, None, 0, None, None, None, 0, 0, 0, 0, 0, 0, None, None, None,
                0, 0, 0, 0, 0, None, None, None, 0, None, None, 0, None, None, None, None, 0, None, 0, None, 0, 0, 0,
                None, None, 0, None, None, None, 0, 0, 0, None, None, 0, 0, 0, 0, None, None, 0, 0, None, 0, 0, 0, None,
                0, 0, None, 0, None, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, None, None, None, 0, 0, 0, 0, 0,
                None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, 0, None, None, None, None, 0, 0, None, None, 0,
                None, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, None, None, None, None, None, None, None, 0, 0, 0, 0,
                None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, None, 0, None, None, 0, None, None, None, None, None, None, 0, 0,
                None, None, 0, None, None, None, None, None, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0,
                0, 0, 0, None, None, None, 0, 0, None, 0, 0, None, 0, None, None, 0, 0, None, None, None, 0, 0, None,
                None, None, None, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0,
                0, None, None, None, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, 0, None, 0, None, None, None, 0, 0, 0,
                None, 0, None, None, None, 0, None, 0, 0, None, None, None, 0, None, None, 0, None, None, 0, 0, 0, None,
                0, None, None, None, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, None, 0, None, None, 0, None,
                None, 0, 0, None, None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None,
                0, 0, 0, 0, 0, 0, 0, None, None, 0, None, None, 0, None, 0, None, 0, None, 0, 0, 0, 0, 0, None, None,
                None, None, None, None, 0, 0, None, 0, 0, None, 0, 0, 0, 0, None, None, None, None, None, 0, None, None,
                0, None, 0, None, None, None, 0, None, None, None, None, 0, 0, 0, 0, None, None, 0, None, None, None, 0,
                0, 0, None, 0, 0, 0, 0, 0, 0, None, 0, None, None, 0, 0, None, None, None, None, 0, None, None, None,
                None, None, None, None, None, 0, None, None, None, None, 0, None, 0, None, 0, None, 0, 0, None, 0, None,
                None, 0, None, 0, None, 0, None, None, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, 0, None,
                None, None, None, None, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, None, 0, 0, 0, 0, 0, None, 0, None, 0, 0, 0, 0, 0, 0, None, 0, 0, 0, None, None, None, None,
                None, None, None, None, 0, None, 0, None, 0, None, None, None, 0, None, None, None, 0, 0, None, None,
                None, 0, 0, 0, 0, 0, 0, None, None, None, None, None, 0, 0, None, 0, 0, None, None, None, None, None,
                None, 0, None, 0, None, None, None, 0, 0, 0, None, 0, 0, None, 0, 0, None, None, None, None, None, None,
                0, 0, 0, 0, 0, None, None, 0, None, None, 0, 0, 0, 0, 0, 0, 0, None, None, None, 0, 0, None, None, None,
                None, None, None, None, None, None, None, 0, None, None, None, None, 0, None, None, None, None, None,
                None, None, 0, None, None, 0, None, 0, 0, None, None, 0, None, None, None, 0, None, None, None, None,
                None, None, None, None, None, None, None, None, 0, None, None, None, None, 0, 0, None, 0, 0, 0, None,
                None, None, None, 0, 0, None, None, None, None, 0, 0, 0, 0, None, None, 0, 0, None, 0, 0, 0, 0, 0, 0, 0,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, None, 0, 0, None, None, None, None, None, None,
                None, None, None, None, None, None, None, 0, 0, 0, 0, None, None, 0, None, None, None, None, None, 0,
                None, None, None, None, None, None, 0, 0, None, 0, None, 0, 0, 0, 0, None, None, None, None, None, None,
                0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, None, None, 0, 0, None, None, None, None, 0, 0, None, None, 0,
                None, 0, None, 0, None, None, 0, None, None, None, None, 0, None, 0, None, None, None, None, 0, 0, None,
                0, 0, 0, None, 0, 0, 0, None, 0, None, None, None, None, 0, None, None, None, None, None, None, None,
                None, 0, 0, 0, 0, None, 0, None, 0, None, 0, None, 0, 0, 0, 0, 0, None, 0, 0, 0, None, None, None, None,
                0, 0, 0, 0, None, 0, 0, None, None, 0, None, None, 0, None, 0, 0, None, 0, 0, 0, None, 0, 0, None, None,
                None, 0, 0, None, None, None, None, None, 0, 0, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None,
                0, None, None, None, 0, 0, None, None, None, 0, 0, None, 0, None, None, 0, None, None, 0, 0, None, None,
                None, 0, 0, None, None, 0, None, 0, None, 0, 0, None, None, None, 0, 0, None, None, None, None, 0, 0,
                None, 0, None, None, None, None, 0, 0, 0, 0, 0, 0, None, None, None, 0, 0, None, 0, None, None, None,
                None, 0, None, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, None, 0, None, None, None, None, None, None,
                None, None, None, 0, 0, 0, None, 0, None, None, 0, 0, None, 0, 0, 0, None, 0, None, None, None, 0, None,
                0, None, None, 0, None, 0, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, 0, None, None, None, None, None, 0,
                0, None, None, None, None, 0, 0, 0, 0, 0, None, 0, 0, 0, None, None, None, None, None, 0, None, None, 0,
                0, 0, 0, 0, None, None, 0, 0, 0, 0, None, None, None, 0, 0, None, None, 0, None, None, 0, 0, 0, None, 0,
                None, 0, None, 0, None, None, 0, 0, None, None, None, None, None, None, None, None, None, None, None,
                None, 0, None, None, 0, 0, None, None, None, None, None, 0, None, 0, 0, 0, 0, None, 0, 0, 0, None, None,
                0, None, None, 0, None, None, 0, None, None, None, None, None, None, 0, 0, 0, 0, 0, 0, 0, None, None,
                None, None, None, None, 0, 0, None, 0, None, 0, None, None, None, None, None, 0, None, None, None, None,
                None, 0, 0, 0, 0, None, None, None, None, None, None, None, None, 0, 0, 0, 0, 0, None, 0, 0, None, 0, 0,
                0, 0, 0, 0, 0, None, 0, 0, 0, None, None, 0, None, None, None, None, None, None, None, None, 0, None,
                None, None, 0, None, 0, None, 0, 0, None, None, 0, 0, None, 0, 0, 0, None, 0, 0, 0, None, 0, None, None,
                None, None, 0, None, 0, None, 0, None, None, None, None, None, None, 0, 0, 0, None, None, 0, None, None,
                None, 0, 0, None, None, None, None, 0, None, 0, None, None, None, 0, None, 0, 0, 0, 0, 0, 0, None, 0, 0,
                None, None, None, 0, None, 0, None, None, 0, None, None, None, None, None, None, None, None, None, None,
                0, None, 0, 0, None, None, None, None, 0, None, 0, None, None, None, None, 0, 0, None, None, 0, None,
                None, 0, 0, 0, 0, None, 0, None, None, 0, None, None, None, 0, None, 0, 0, 0, None, 0, 0, 0, 0, 0, None,
                None, None, None, None, 0, None, 0, None, 0, None, None, 0, None, None, None, None, None, None, None,
                None, None, 0, None, 0, 0, 0, None, None, None, None, 0, None, None, None, 0, None, None, None, None, 0,
                None, None, None, None, None, None, None, None, 0, None, 0, None, None, None, 0, None, None, None, None,
                None, 0, None, 0, 0, 0, 0, None, None, None, 0, 0, 0, None, 0, 0, 0, None, 0, None, None, None, None,
                None, None, None, None, None, None, None, None, 0, 0, 0, None, None, None, None, None, None, None, 0, 0,
                0, 0, 0, 0, None, None, None, 0, 0, None, None, None, 0, 0, None, 0, 0, 0, 0, None, None, None, 0, None,
                None, None, None, None, None, None, None, None, 0, None, None, None, None, None, None, None, 0, 0, 0, 0,
                0, None, 0, 0, None, None, None, 0, 0, 0, 0, 0, None, None, None, None, None, 0, 0, 0, None, 0, None,
                None, None, None, 0, 0, 0, None, None, None, 0, None, None, 0, 0, None, None, 0, 0, None, None, None,
                None, None, None, None, 0, None, 0, None, None, None, None, 0, 0, None, None, 0, 0, 0, 0, 0, None, None,
                0, None, None, 0, 0, 0, 0, 0, 0, None, None, None, 0, None, None, None, 0, 0, None, None, None, None,
                None, None, None, None, None, None, 0, 0, None, 0, None, None, 0, None, 0, None, None, None, None, None,
                None, None, 0, None, None, None, None, None, None, None, 0, None, 0, None, None, 0, None, None, 0, 0,
                None, None, None, 0, None, None, 0, 0, None, None, 0, 0, 0, 0, 0, 0, 0, 0, None, None, 0, 0, None, None,
                None, None, None, None, None, None, 0, 0, 0, None, None, None, None, 0, None, 0, None, 0, None, None,
                None, None, 0, 0, None, None, None, None, None, 0, 0, 0, None, 0, None, None, None, 0, None, None, 0, 0,
                None, None, None, None, 0, None, None, None, None, None, 0, 0, None, None, None, None, None, None, 0, 0,
                None, None, None, 0, None, None, None, None, None, None, None, None, None, None, 0, None, None, None,
                None, None, 0, 0, None, None, None, None, None, None, 0, 0, None, None, None, None, None, None, None,
                None, None, None, None, None, None, None, None, None, None, 0], 360), ]
for min_camera_cover in [min_camera_cover_dynamic_programming, min_camera_cover_greedy, ]:
    for test_tree_list, expected_count in test_cases:
        assert min_camera_cover(ConstructTree.build_tree_leetcode(test_tree_list).root) == expected_count
