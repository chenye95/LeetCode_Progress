"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children left_child[i] and right_child[i],
return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
"""
from typing import List


def validate_binary_tree_nodes(n: int, left_child: List[int], right_child: List[int]) -> bool:
    """
    :param n: number of nodes in the proposed binary tree
    :param left_child: left_child[i] is the left child of node i, equals to -1 if none
    :param right_child: right_child[i] is the right child of node i, equals to -1 if none
    :return: whether the proposed tree is a valid binary tree
    """
    if n <= 1:
        return True

    visited = [False] * n
    stack = [0]
    visited[0] = True

    while stack:
        to_visit = stack.pop()
        if left_child[to_visit] != -1:
            if visited[left_child[to_visit]]:
                return False
            visited[left_child[to_visit]] = True
            stack.append(left_child[to_visit])
        if right_child[to_visit] != -1:
            if visited[right_child[to_visit]]:
                return False
            visited[right_child[to_visit]] = True
            stack.append(right_child[to_visit])
    return all(visited)


test_cases = [(4, [1, -1, 3, -1], [2, -1, -1, -1], True),
              (4, [1, -1, 3, -1], [2, 3, -1, -1], False),
              (2, [1, 0], [-1, -1], False),
              (6, [1, -1, -1, 4, -1, -1], [2, -1, -1, 5, -1, -1], False),
              (4, [1, -1, 3, -1], [2, 3, -1, -1], False), ]
for test_n, test_left, test_right, expected_output in test_cases:
    assert validate_binary_tree_nodes(n=test_n, left_child=test_left, right_child=test_right) is expected_output
