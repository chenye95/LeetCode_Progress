"""
Given a tree (i.e. a connected, undirected graph that has no cycles) consisting of n nodes numbered from 0 to n - 1 and
exactly n - 1 edges. The root of the tree is the node 0, and each node of the tree has a label which is a lower-case
character given in the string labels (i.e. The node with the number i has the label labels[i]).

The edges array is given on the form edges[i] = [ai, bi], which means there is an edge between nodes ai and bi in the
tree.

Return an array of size n where ans[i] is the number of nodes in the subtree of the ith node which have the same label
as node i.

A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.
"""
from collections import Counter, defaultdict
from typing import List


def count_sub_trees(n: int, edges: List[List[int]], labels: str) -> List[int]:
    """
    :param n: number of nodes in the tree, numbered 0, ..., n-1
    :param edges: list of edges in the tree
    :param labels: label for node in the tree
    :return: return_list[i] is the number of nodes in the subtree of the ith node which have the same label as node i
    """

    def depth_first_search_approach(current_node: int, parent_node: int) -> Counter:
        """
        :param current_node: root of the sub tree
        :param parent_node: parent node of current_node
        :return: Counter of label within sub tree of current_node
        """
        node_counter = Counter()
        for child_node in edge_list[current_node]:
            if child_node == parent_node:
                continue
            node_counter += depth_first_search_approach(child_node, current_node)
        node_counter[labels[current_node]] += 1
        return_list[current_node] = node_counter[labels[current_node]]
        return node_counter

    edge_list = defaultdict(list)
    for node_i, node_j in edges:
        edge_list[node_i].append(node_j)
        edge_list[node_j].append(node_i)
    return_list = [0] * n
    depth_first_search_approach(current_node=0, parent_node=-1)
    return return_list


assert [2, 1, 1, 1, 1, 1, 1] == count_sub_trees(n=7, edges=[[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]],
                                                labels="abaedcd")
assert [4, 2, 1, 1] == count_sub_trees(n=4, edges=[[0, 1], [1, 2], [0, 3]], labels="bbbb")
assert [3, 2, 1, 1, 1] == count_sub_trees(n=5, edges=[[0, 1], [0, 2], [1, 3], [0, 4]], labels="aabab")
assert [1, 2, 1, 1, 2, 1] == count_sub_trees(n=6, edges=[[0, 1], [0, 2], [1, 3], [3, 4], [4, 5]], labels="cbabaa")
assert [6, 5, 4, 1, 3, 2, 1] == count_sub_trees(n=7, edges=[[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6]],
                                                labels="aaabaaa")
assert [2, 2, 1, 1, 1, 3, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 1] == \
       count_sub_trees(25,
                       [[4, 0], [5, 4], [12, 5], [3, 12], [18, 3], [10, 18], [8, 5], [16, 8], [14, 16], [13, 16],
                        [9, 13],
                        [22, 9], [2, 5], [6, 2],
                        [1, 6], [11, 1], [15, 11], [20, 11], [7, 20], [19, 1], [17, 19], [23, 19], [24, 2], [21, 24]],
                       "hcheiavadwjctaortvpsflssg")
