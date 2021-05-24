"""
You are given a tree with n nodes numbered from 0 to n-1 in the form of a parent array where parent[i] is the parent of
node i. The root of the tree is node 0.

Implement the function get_kth_ancestor(int node, int k) to return the k-th ancestor of the given node. If there is no
such ancestor, return -1.

The k-th ancestor of a tree node is the k-th node in the path from that node to the root.
"""
from typing import List, Tuple


class TreeAncestor:
    PRE_COMPUTE_MAX_JUMP: int = 50_000
    NONE_EXISTENCE: int = -1

    def __init__(self, n: int, parent: List[int]):
        """
        Binary Lifting: pre-compute 2^0 = 1, 2^1 = 2, 2^2 = 4, 2^3 = 8th ... level ancestor of node child_node

        :param n: n nodes numbered 0 to n-1
        :param parent: parent[child_node] is the parent of node child_node
        """
        # current_jump_ancestor is 2^current_jump_count-th ancestor
        # initialize to current_jump_count = 0 and current_jump_ancestor is 1st ancestor
        current_jump_count = 0
        current_jump_ancestors = {i: parent_i for i, parent_i in enumerate(parent)}
        jump_map = [current_jump_ancestors]

        while current_jump_count < self.PRE_COMPUTE_MAX_JUMP and current_jump_ancestors:
            # next_jump_ancestors is 2^(current_jump_count+1)-th ancestor
            next_jump_ancestors = {}
            for child_node in current_jump_ancestors:
                if current_jump_ancestors[child_node] in current_jump_ancestors:
                    # Exists next jump node
                    next_jump_ancestors[child_node] = current_jump_ancestors[current_jump_ancestors[child_node]]
            current_jump_ancestors = next_jump_ancestors
            jump_map.append(current_jump_ancestors)
            current_jump_count += 1

        self.PRE_COMPUTE_MAX_JUMP = current_jump_count
        self.jump_map = jump_map

    def get_kth_ancestor(self, node: int, k: int) -> int:
        """
        break down k into binaries of 1,0 and use jump_map for look up
            e.g. 5th (1001) ancestor = 1st ancestor of 4th ancestor of node

        :param: node such that 0 <= node < n, 1 <= n <= 5*10^4
        :param: 1 <= k <= 5*10^4
        :return: k-th ancestor of node if exists or else -1
        """
        jump = self.PRE_COMPUTE_MAX_JUMP
        while k > 0 and node >= 0:
            # find the leading 1 in binary representation of k
            if k >= 1 << jump:
                node = self.jump_map[jump].get(node, self.NONE_EXISTENCE)
                if node == self.NONE_EXISTENCE:
                    return self.NONE_EXISTENCE
                k -= 1 << jump
            else:
                jump -= 1
        return node


def run_test_case(n: int, parent_list: List[int], parameters: List[Tuple[int, int]], expected_output: List[int]):
    assert len(parameters) == len(expected_output)
    test_obj = TreeAncestor(n, parent_list)
    for node_id_k, expected_node in zip(parameters, expected_output):
        test_node, test_k = node_id_k
        assert test_obj.get_kth_ancestor(test_node, test_k) == (expected_node if expected_node != -1
                                                                else test_obj.NONE_EXISTENCE)


# Your TreeAncestor object will be instantiated and called as such:
# obj = TreeAncestor(n, parent)
# param_1 = obj.get_kth_ancestor(node,k)
test_cases = [(7, [-1, 0, 0, 1, 1, 2, 2], [(3, 1), (5, 2), (6, 3)], [1, 0, -1]),
              (5, [-1, 0, 0, 0, 3], [(1, 5), (3, 2), (0, 1), (3, 1), (3, 5)], [-1, -1, -1, 0, -1]),
              (50000, [-1] + list(range(49999)), [(43495, 41615), ], [43495 - 41615, ])]
for test_n, test_parent_list, test_parameters, expected_list in test_cases:
    run_test_case(test_n, test_parent_list, test_parameters, expected_list)
