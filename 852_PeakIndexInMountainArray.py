"""
Let's call an array A a mountain if the following properties hold:

A.length >= 3
There exists some 0 < i < A.length - 1 such that A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1]
Given an array that is definitely a mountain, return any i such that
A[0] < A[1] < ... A[i-1] < A[i] > A[i+1] > ... > A[A.length - 1].
"""
from typing import List

def peakIndexInMountainArray(A: List[int]) -> int:
    i = 0
    while i < len(A) - 1 and A[i] < A[i+1]:
        i += 1
    return i

assert peakIndexInMountainArray([0,2,1,0]) == 1
assert peakIndexInMountainArray([0,1,0]) == 1