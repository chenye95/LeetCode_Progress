"""
You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of
node i. The root of the tree is node 0.

Implement the function getKthAncestor(int node, int k) to return the k-th ancestor of the given node. If there is no
such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.
"""
from typing import List


class TreeAncestor:
    PRE_COMPUTE_MAX_JUMP: int = 50_000
    NONE_EXISTENCE: int = -1

    def __init__(self, n: int, parent: List[int]):
        """
        Binary Lifting: pre-compute 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8th ... level ancestor of node i
        :param n: n nodes numbered 0 to n-1
        :param parent: parent[i] is the parent of node i
        """
        # current_jump_ancestor is 2^current_jump-th ancestor
        # initialize to current_jump = 0 and current_jump_ancestor is 1st ancestor
        current_jump = 0
        current_jump_ancestors = {i: parent_i for i, parent_i in enumerate(parent)}
        jump_map = [current_jump_ancestors]
        has_next_jump = True

        while current_jump < self.PRE_COMPUTE_MAX_JUMP and has_next_jump:
            has_next_jump = False
            # next_jump_ancestor is 2^(current_jump+1)-th ancestor
            next_jump_ancestor = {}
            for i in current_jump_ancestors:
                if current_jump_ancestors.get(current_jump_ancestors[i], self.NONE_EXISTENCE) != self.NONE_EXISTENCE:
                    # Exists next jump node
                    next_jump_ancestor[i] = current_jump_ancestors[current_jump_ancestors[i]]
                    has_next_jump = True
            current_jump_ancestors = next_jump_ancestor
            jump_map.append(current_jump_ancestors)
            current_jump += 1

        self.PRE_COMPUTE_MAX_JUMP = current_jump
        self.jump_map = jump_map

    def getKthAncestor(self, node: int, k: int) -> int:
        """
        break down k into binaries of 1,0 and use jump_map for look up
            e.g. 5th (1001) ancestor = 1st ancestor of 4th ancestor of node
        :param: node such that 0 <= node < n, 1 <= n <= 5*10^4
        :param: 1 <= k <= 5*10^4
        :return: k-th ancestor of node if exists or else -1
        """
        jump = self.PRE_COMPUTE_MAX_JUMP
        while k > 0 and node >= 0:
            # find the leading 1 in binary representation of node
            if k >= 1 << jump:
                node = self.jump_map[jump].get(node, self.NONE_EXISTENCE)
                if node == self.NONE_EXISTENCE:
                    return self.NONE_EXISTENCE
                k -= 1 << jump
            else:
                jump -= 1
        return node


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.getKthAncestor(node,k)
test_obj = TreeAncestor(7, [-1, 0, 0, 1, 1, 2, 2])
assert test_obj.getKthAncestor(3, 1) == 1
assert test_obj.getKthAncestor(5, 2) == 0
assert test_obj.getKthAncestor(6, 3) == test_obj.NONE_EXISTENCE

test_obj = TreeAncestor(5, [-1, 0, 0, 0, 3])
assert test_obj.getKthAncestor(1, 5) == test_obj.NONE_EXISTENCE
assert test_obj.getKthAncestor(3, 2) == test_obj.NONE_EXISTENCE
assert test_obj.getKthAncestor(0, 1) == test_obj.NONE_EXISTENCE
assert test_obj.getKthAncestor(3, 1) == 0
assert test_obj.getKthAncestor(3, 5) == test_obj.NONE_EXISTENCE
