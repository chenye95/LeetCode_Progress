"""
You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of
node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no
such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.
"""
from typing import List


class TreeAncestor:
    PRE_COMPUTE_MAX_STEP: int = 15
    NONE_EXISTENCE: int = -1

    def __init__(self, n: int, parent: List[int]):
        """
        Binary Lifting: pre-compute 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8th ... level ancestor of node i
        :param n: n nodes numbered 0 to n-1
        :param parent: parent[i] is the parent of node i
        """
        current_step_ancestor, current_step = dict(enumerate(parent)), 0
        jump_map = [current_step_ancestor]
        has_next_level = True
        while current_step < self.PRE_COMPUTE_MAX_STEP and has_next_level:
            has_next_level = False
            next_step_ancestor = {}
            for i in current_step_ancestor:
                if current_step_ancestor.get(current_step_ancestor[i], self.NONE_EXISTENCE) != self.NONE_EXISTENCE:
                    # Exists grandparent node
                    next_step_ancestor[i] = current_step_ancestor[current_step_ancestor[i]]
                    has_next_level = True
            current_step_ancestor = next_step_ancestor
            jump_map.append(current_step_ancestor)
            current_step += 1
        self.PRE_COMPUTE_MAX_STEP = current_step
        self.jump_map = jump_map

    def getKthAncestor(self, node: int, k: int) -> int:
        """
        break down k into binaries of 1,0 and use jump_map for look up
            e.g. 5th (1001) ancestor = 1st ancestor of 4th ancestor of node
        :return: k-th ancestor of node if exists or else -1
        """
        step = self.PRE_COMPUTE_MAX_STEP
        while k > 0 and node >= 0:
            # find the leading 1 in binary representation of node
            if k >= 1 << step:
                node = self.jump_map[step].get(node, self.NONE_EXISTENCE)
                k -= 1 << step
            else:
                step -= 1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
test_obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
assert test_obj.getKthAncestor(3, 1) == 1
assert test_obj.getKthAncestor(5, 2) == 0
assert test_obj.getKthAncestor(6, 3) == -1

test_obj = TreeAncestor(5, [-1, 0, 0, 0, 3])
assert test_obj.getKthAncestor(1, 5) == -1
assert test_obj.getKthAncestor(3, 2) == -1
assert test_obj.getKthAncestor(0, 1) == -1
assert test_obj.getKthAncestor(3, 1) == 0
assert test_obj.getKthAncestor(3, 5) == -1
