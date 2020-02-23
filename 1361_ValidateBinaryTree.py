"""
You have n binary tree nodes numbered from 0 to n - 1 where node i has two children leftChild[i] and rightChild[i],
return true if and only if all the given nodes form exactly one valid binary tree.

If node i has no left child then leftChild[i] will equal -1, similarly for the right child.
"""
from typing import List


def validateBinaryTreeNodes(n: int, leftChild: List[int], rightChild: List[int]) -> bool:
    if n <= 1:
        return True

    visited = [False] * n
    stack = [0]
    visited[0] = True

    while stack:
        to_visit = stack.pop()
        if leftChild[to_visit] != -1:
            if visited[leftChild[to_visit]]:
                return False
            visited[leftChild[to_visit]] = True
            stack.append(leftChild[to_visit])
        if rightChild[to_visit] != -1:
            if visited[rightChild[to_visit]]:
                return False
            visited[rightChild[to_visit]] = True
            stack.append(rightChild[to_visit])
    return all(visited)


assert validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,-1,-1,-1])
assert not validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1])
assert not validateBinaryTreeNodes(n = 2, leftChild = [1,0], rightChild = [-1,-1])
assert not validateBinaryTreeNodes(n = 6, leftChild = [1,-1,-1,4,-1,-1], rightChild = [2,-1,-1,5,-1,-1])
assert not validateBinaryTreeNodes(n = 4, leftChild = [1,-1,3,-1], rightChild = [2,3,-1,-1])