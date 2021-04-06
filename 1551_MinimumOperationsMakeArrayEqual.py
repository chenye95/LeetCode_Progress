"""
You have an array arr of length n where arr[i] = (2 * i) + 1 for all valid values of i (i.e. 0 <= i < n).

In one operation, you can select two indices x and y where 0 <= x, y < n and subtract 1 from arr[x] and add 1 to arr[y]
 (i.e. perform arr[x] -=1 and arr[y] += 1). The goal is to make all the elements of the array equal. It is guaranteed
  that all the elements of the array can be made equal using some operations.

Given an integer n, the length of the array. Return the minimum number of operations needed to make all the elements
 of arr equal.
"""


def min_operations_split_cases(n: int) -> int:
    """
    :param n: array of length n where arr[i] = 2 * i + 1 for 0 <= i < n
    :return: number of operations to make all elements in the array equal
    """
    # operations to make all elements equal to median of array
    # operate on pairs of elements around median
    c = n // 2
    return (c + 1) * c if n % 2 else c * c


def min_operations_all(n: int) -> int:
    """
    :param n: array of length n where arr[i] = 2 * i + 1 for 0 <= i < n
    :return: number of operations to make all elements in the array equal
    """
    # operations to make all elements equal to median of array
    # operate on pairs of elements around median
    c = n // 2
    return (n - c) * c


test_cases = [(1, 0), (2, 1), (3, 2), (4, 4), (5, 6), (6, 9), (7, 12), (8, 16), (9, 20),
              (50, 625), ]
for min_operations in [min_operations_split_cases, ]:
    for test_n, expected_output in test_cases:
        assert min_operations(test_n) == expected_output, min_operations.__name__
