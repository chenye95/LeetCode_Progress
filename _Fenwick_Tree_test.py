from _Fenwick_Tree import FenwickTree

num_array = [3, 2, -1, 6, 5, 4, -3, 3, 7, 2, 3]
cumulative_sum = [sum(num_array[:i]) for i in range(1, len(num_array) + 1)]
num_bit_array = [0, 3, 5, -1, 10, 5, 9, -3, 19, 7, 9, 3]

epsilon = 0.001

"""Set Up"""
test_tree = FenwickTree(init_frequencies=num_array)
assert num_bit_array == test_tree.bit_array

"""At Index I"""
for i in range(len(num_array)):
    assert test_tree.at_idx_i(i) == num_array[i], \
        "at_idx_i(%d): Expected %d, Got %d" % (i, num_array[i], test_tree.at_idx_i(i))

"""Range Sum"""
for i in range(1, len(num_array)):
    for j in range(i, len(num_array)):
        assert test_tree.range_sum(i, j) == cumulative_sum[j] - cumulative_sum[i-1], \
            "range_sum(%d, %d): Expected %d Got %d" % (i, j, cumulative_sum[j] - cumulative_sum[i-1],
                                                       test_tree.range_sum(i, j))
for i in range(1, len(num_array)):
    assert test_tree.range_sum(i) == cumulative_sum[-1] - cumulative_sum[i-1], \
        "range_sum(%d) to end: Expected %d Got %d" % (i, cumulative_sum[-1] - cumulative_sum[i-1],
                                                      test_tree.range_sum(i))
assert test_tree.range_sum(0) == cumulative_sum[-1]
for i in range(len(num_array)):
    assert test_tree.range_sum(end_idx=i) == cumulative_sum[i], \
        "range_sum(%d) from start: Expected %d Got %d" % (i, cumulative_sum[i], test_tree.range_sum(end_idx=i))

"""Scale"""
test_tree.scale(test_tree.range_sum())
for i in range(1, len(num_array)):
    assert abs(test_tree.range_sum(end_idx=i) - (cumulative_sum[i] / float(cumulative_sum[-1]))) < epsilon, \
        "Scale Function"

"""Cumulative Sum Test"""
num_array = [1, 0, 2, 1, 1, 4, 0, 3, 2, 5, 2, 2, 3, 1, 0, 2]
new_tree = FenwickTree(num_array)
cumulative_sum = [sum(num_array[:i]) for i in range(len(num_array))]
assert new_tree.bit_array == [0, 1, 1, 2, 4, 1, 5, 0, 12, 2, 7, 2, 11, 3, 4, 0, 29]

for cum_sum_target in cumulative_sum:
    i = new_tree.find_cumulative_sum(cum_sum_target)
    assert cumulative_sum[i] == cum_sum_target
assert new_tree.find_cumulative_sum(15) == -1
assert new_tree.find_cumulative_sum(1) == 2
# print(cumulative_sum)
