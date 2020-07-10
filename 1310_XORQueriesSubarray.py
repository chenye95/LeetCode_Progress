"""
Given the array arr of positive integers and the array queries where queries[i] = [Li, Ri], for each query i compute the
 XOR of elements from Li to Ri (that is, arr[Li] xor arr[Li+1] xor ... xor arr[Ri] ). Return an array containing the
 result for the given queries.
"""
from typing import List


def xorQueries(arr: List[int], queries: List[List[int]]) -> List[int]:
    """
    :param arr: array of positive integers
    :param queries: list of queries of form [Li, Ri]
    :return: return arr[Li] xor arr[Li+1] xor .... xor arr[Ri]
    """
    pre_compute = [0] * (len(arr) + 1)
    for i in range(len(arr)):
        pre_compute[i + 1] = pre_compute[i] ^ arr[i]
    return [pre_compute[Ri + 1] ^ pre_compute[Li] for Li, Ri in queries]


assert xorQueries(arr=[1, 3, 4, 8], queries=[[0, 1], [1, 2], [0, 3], [3, 3]]) == [2, 7, 14, 8]
assert xorQueries(arr=[4, 8, 2, 10], queries=[[2, 3], [1, 3], [0, 0], [0, 3]]) == [8, 0, 4, 4]
