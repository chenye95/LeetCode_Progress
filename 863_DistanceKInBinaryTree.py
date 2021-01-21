"""
We are given a binary tree (with root node root), a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from the target node.  The answer can be returned in any
 order.
"""
from _Binary_Tree import TreeNode, ConstructTree, TREE_NODE_TYPE
from typing import List
from collections import deque


def distance_k_list_1(root: TreeNode, target: TreeNode, k: int) -> List[TREE_NODE_TYPE]:
    # Percolate Distance
    # all depth are 1 indexed, i.e. root has a depth of  1

    return_list = []

    def depth_t_from_node(node: TreeNode, t_step_below: int) -> None:
        """
        Add all nodes depth (t_step_below + 1) in the subtree rooted from node
        """
        if not node or t_step_below < 0:
            return
        elif t_step_below == 0:
            return_list.append(node.val)
        else:
            depth_t_from_node(node.left, t_step_below - 1)
            depth_t_from_node(node.right, t_step_below - 1)

    def find_target_in_subtree(current_node: TreeNode):
        """
        :return: -1 if target is not in the subtree rooted at current_node
                else return depth of target within the subtree
        """
        if not current_node:
            return -1
        elif current_node is target:
            # nodes of depth k in the subtree rooted from target suffice the condition
            depth_t_from_node(target, k)
            return 1
        else:
            l, r = find_target_in_subtree(current_node.left), find_target_in_subtree(current_node.right)
            if l != -1:
                # target found in left sub tree
                if l == k:
                    return_list.append(current_node.val)
                # all nodes k - l - 1 below current_node.right suffice the condition
                depth_t_from_node(current_node.right, k - l - 1)
                return l + 1
            elif r != -1:
                # target found in right sub tree
                if r == k:
                    return_list.append(current_node.val)
                # all nodes k - r - 1 below current_node.left suffice the condition
                depth_t_from_node(current_node.left, k - r - 1)
                return r + 1
            else:
                return -1

    find_target_in_subtree(root)
    return return_list


def distance_k_list_2(root: TreeNode, target: TreeNode, k: int) -> List[TREE_NODE_TYPE]:
    def mark_parent(current_node: TreeNode, parent_node: TreeNode = None) -> None:
        current_node.parent = parent_node
        if current_node.left:
            mark_parent(current_node.left, current_node)
        if current_node.right:
            mark_parent(current_node.right, current_node)

    assert root is not None and target is not None
    mark_parent(root)

    exploration_queue = deque([(target, 0)])
    seen = {target}
    while exploration_queue:
        if exploration_queue[0][1] == k:
            return [node.val for node, _ in exploration_queue]
        current_node, depth = exploration_queue.popleft()
        for neighbor in (current_node.left, current_node.right, current_node.parent):
            if neighbor and neighbor not in seen:
                seen.add(neighbor)
                exploration_queue.append((neighbor, depth + 1))

    return []


test_tree = ConstructTree.build_tree_leetcode([0, 1, None, 3, 2])
target_node = test_tree.root.left.right
assert [1] == distance_k_list_1(test_tree.root, target_node, 1)
assert [1] == distance_k_list_2(test_tree.root, target_node, 1)

test_tree = ConstructTree.build_tree_leetcode([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
target_node = test_tree.root.left
assert [7, 4, 1] == distance_k_list_1(test_tree.root, target_node, 2)
assert [7, 4, 1] == distance_k_list_2(test_tree.root, target_node, 2)
