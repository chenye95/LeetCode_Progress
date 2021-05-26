"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.

Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""
from _Binary_Tree import TreeNode, TREE_NODE_TYPE, ConstructTree


def is_cousins_double_list(root: TreeNode, x: TREE_NODE_TYPE, y: TREE_NODE_TYPE) -> bool:
    """
    :param root: a non empty binary tree with 2 ~ 100 tree nodes. Each node has an unique value between [1, 100]
    :param x: value of a tree node
    :param y: value of a tree node
    :return: whether x and y are on the same level but have different parent
    """
    if x == y:
        return False
    if root.val == x or root.val == y:
        return False

    current_level = []
    if root.left:
        current_level.append(root.left)
    if root.right:
        current_level.append(root.right)
    current_level_val = [(root.left.val if root.left else None), (root.right.val if root.right else None), ]

    while current_level:
        if len(current_level_val) > 1:
            if (x in current_level_val and y not in current_level_val) or \
                    (x not in current_level_val and y in current_level_val):
                # x and y are on different levels
                return False
            elif x in current_level_val and y in current_level_val:
                x_pos = current_level_val.index(x)
                y_pos = current_level_val.index(y)
                return abs(x_pos - y_pos) != 1 or (x_pos + y_pos) % 4 != 1

        next_level = []
        next_level_val = []
        for node in current_level:
            if node.left:
                next_level.append(node.left)
                next_level_val.append(node.left.val)
            else:
                next_level_val.append(None)

            if node.right:
                next_level.append(node.right)
                next_level_val.append(node.right.val)
            else:
                next_level_val.append(None)

        current_level = next_level
        current_level_val = next_level_val

    return False


def is_cousins_one_list(root: TreeNode, x: TREE_NODE_TYPE, y: TREE_NODE_TYPE) -> bool:
    """
    :param root: a non empty binary tree with 2 ~ 100 tree nodes. Each node has an unique value between [1, 100]
    :param x: value of a tree node
    :param y: value of a tree node
    :return: whether x and y are on the same level but have different parent
    """
    if x == y:
        return False
    if root.val == x or root.val == y:
        return False

    current_level = []
    if root.left:
        current_level.append(root.left)
    if root.right:
        current_level.append(root.right)

    x_found = y_found = False

    while current_level:
        next_level = []
        for current_node in current_level:
            found_in_current_node = 0
            for child_node in [current_node.left, current_node.right]:
                if child_node:
                    next_level.append(child_node)
                    if child_node.val == x:
                        found_in_current_node += 1
                        x_found = True
                    elif child_node.val == y:
                        found_in_current_node += 1
                        y_found = True

            if found_in_current_node == 2:
                # same parent
                return False

        if x_found or y_found:
            return x_found and y_found

        current_level = next_level

    return False


test_cases = [([1, 2, 3, 4], 4, 3, False),
              ([1, 2, 3, None, 4, None, 5], 5, 4, True),
              ([1, 2, 3, None, 4], 2, 3, False),
              ([1, 2, 10, 3, 4, 12, 15, 7, 6, 11, 5, 19, 16, 28, 31, None, 47, 14, 8, None, 17, 25, 13, None, None, 20,
                36, 32, None, None, None, None, None, None, 43, 23, 9, 22, None, None, 35, 39, 18, 41, None, 44, None,
                40, None, None, None, None, 29, 21, 37, 26, None, 46, None, 45, 42, 33, 24, None, None, None, 50, None,
                None, None, 48, None, 27, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, None, 49, 30, None, None, None, 34, 38], 33, 24, False),
              ([1, 18, 2, None, None, 3, 4, 17, 10, 5, 6, None, None, 21, 12, 8, 11, 31, 7, None, None, 37, 15, None, 9,
                29, 14, None, 35, 24, 20, 44, None, 19, 25, 22, 13, 41, 32, 39, 16, 36, None, None, None, 27, None,
                None, None, 23, None, None, 47, 30, 26, None, 49, None, 50, None, None, None, None, 45, 28, None, None,
                None, None, 43, None, None, None, 34, 38, None, 33, None, None, None, None, None, 46, 40, None, None,
                None, None, 48, None, 42], 28, 30, True), ]
for is_cousins in [is_cousins_one_list, is_cousins_double_list, ]:
    for test_tree_list, test_x, test_y, expected_output in test_cases:
        assert is_cousins(ConstructTree.build_tree_leetcode(test_tree_list).root, test_x, test_y) is expected_output, \
            is_cousins.__name__
