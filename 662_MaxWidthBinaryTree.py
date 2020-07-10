"""
Given a binary tree, write a function to get the maximum width of the given tree. The width of a tree is the maximum
width among all levels. The binary tree has the same structure as a full binary tree, but some nodes are null.

The width of one level is defined as the length between the end-nodes (the leftmost and right most non-null nodes in
the level, where the null nodes between the end-nodes are also counted into the length calculation.
"""
from _Binary_Tree import TreeNode, ConstructTree


def width_of_binary_tree(root: TreeNode) -> int:
    """
    :param root:
    :return:
    """
    if not root:
        return 0
    if not root.left and not root.right:
        return 1

    stack = [(0, 0, root)]
    level_min, level_max = dict(), dict()
    max_width = 0
    while stack:
        current_level, current_id, current_node = stack.pop()
        if current_node.left:
            next_level, next_id = current_level + 1, 2 * current_id
            level_min[next_level] = min(level_min.get(next_level, 2 ** next_level), next_id)
            level_max[next_level] = max(level_max.get(next_level, 0), next_id)
            max_width = max(max_width, level_max[next_level] - level_min[next_level] + 1)
            stack.append((next_level, next_id, current_node.left))
        if current_node.right:
            next_level, next_id = current_level + 1, 2 * current_id + 1
            level_min[next_level] = min(level_min.get(next_level, 2 ** next_level), next_id)
            level_max[next_level] = max(level_max.get(next_level, 0), next_id)
            max_width = max(max_width, level_max[next_level] - level_min[next_level] + 1)
            stack.append((next_level, next_id, current_node.right))
    return max_width


test_cases = [([1, 3, 2, 5, 3, None, 9], 4),
              ([1, 3, None, 5, 3, None, None], 2),
              ([1, 3, 2, 5, None, None, None], 2),
              ([1, 3, 2, 5, None, None, 9, 6, None, None, 7, None, None, None, None], 8)]

for tree_list, expected_out in test_cases:
    test_tree = ConstructTree.build_tree_leetcode(tree_list)
    assert width_of_binary_tree(test_tree.root) == expected_out
