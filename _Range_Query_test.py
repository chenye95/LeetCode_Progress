from copy import deepcopy
from operator import add
from random import randint

from _Range_Query import ActiveRangeQuery, LazyQueryRange

# Sum Range Query Tree
starting_arr = [18, 17, 13, 19, 15, 11, 20, 12, 33, 25]
expected_sum_range_tree = [183,
                           82, 101,
                           48, 34, 43, 58,
                           35, 13, 19, 15, 31, 12, 33, 25,
                           18, 17, 0, 0, 0, 0, 0, 0, 11, 20, 0, 0, 0, 0, 0, 0]
expected_max_range_tree = [33,
                           19, 33,
                           18, 19, 20, 33,
                           18, 13, 19, 15, 20, 12, 33, 25,
                           18, 17, 0, 0, 0, 0, 0, 0, 11, 20, 0, 0, 0, 0, 0, 0]

randint_a, randint_b = -15, 50

print("Testing Active Range Query Sum Increment")
arr = deepcopy(starting_arr)
tester = ActiveRangeQuery(arr, merge_function=add, update_function=add)
assert tester.range_query_tree == expected_sum_range_tree
for i in range(len(arr)):
    for j in range(i, len(arr)):
        assert tester.query_segment_tree(i, j) == sum(arr[i:j + 1])

arr_update_fn, arr_eval_fn = add, sum
for at_i in range(len(arr)):
    inc_i = randint(randint_a, randint_b)
    arr[at_i] = arr_update_fn(arr[at_i], inc_i)
    assert tester.update_segment_tree(at_index=at_i, value=inc_i)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            expected_value = arr_eval_fn(arr[i:j + 1])
            got_value = tester.query_segment_tree(i, j)
            assert expected_value == got_value, '%d with Increment %d, Expected %d Got %d' % (at_i, inc_i,
                                                                                              expected_value, got_value)

print("Testing Active Range Query Sum Replacement")
arr = deepcopy(starting_arr)
tester = ActiveRangeQuery(arr, merge_function=add, update_function=lambda old_value, to_new_value: to_new_value)
assert tester.range_query_tree == expected_sum_range_tree
for i in range(len(arr)):
    for j in range(i, len(arr)):
        assert tester.query_segment_tree(i, j) == sum(arr[i:j + 1])

arr_update_fn, arr_eval_fn = lambda old_value, to_new_value: to_new_value, sum
for at_i in range(len(arr)):
    new_value = randint(randint_a, randint_b)
    arr[at_i] = arr_update_fn(arr[at_i], new_value)
    assert tester.update_segment_tree(at_index=at_i, value=new_value)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            expected_value = arr_eval_fn(arr[i:j + 1])
            got_value = tester.query_segment_tree(i, j)
            assert expected_value == got_value, '%d with New Value %d, Expected %d Got %d' % (at_i, new_value,
                                                                                              expected_value, got_value)

print("Testing Active Range Query Max Replacement")
arr = deepcopy(starting_arr)
tester = ActiveRangeQuery(arr, merge_function=max, update_function=lambda old_value, to_new_value: to_new_value)
assert tester.range_query_tree == expected_max_range_tree
for i in range(len(arr)):
    for j in range(i, len(arr)):
        assert tester.query_segment_tree(i, j) == max(arr[i:j + 1])

arr_update_fn, arr_eval_fn = lambda old_value, to_new_value: to_new_value, max
for at_i in range(len(arr)):
    new_value = randint(randint_a, randint_b)
    arr[at_i] = arr_update_fn(arr[at_i], new_value)
    assert tester.update_segment_tree(at_index=at_i, value=new_value)
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            expected_value = arr_eval_fn(arr[i:j + 1])
            got_value = tester.query_segment_tree(i, j)
            assert expected_value == got_value, '%d with New Value %d, Expected %d Got %d' % (at_i, new_value,
                                                                                              expected_value, got_value)

print("Testing Lazy Range Query Sum Increment")
arr = deepcopy(starting_arr)
tester = LazyQueryRange(arr, merge_function=add,
                        range_update_function=lambda old_value, lo, hi, inc: old_value + (hi - lo + 1) * inc)
assert tester.range_query_tree == expected_sum_range_tree
for i in range(len(arr)):
    for j in range(i, len(arr)):
        assert tester.query_segment_tree(i, j) == sum(arr[i:j + 1])

arr_update_fn, arr_eval_fn = add, sum
for start in range(len(arr)):
    for end in range(start, len(arr)):
        inc_i = randint(randint_a, randint_b)
        for i in range(start, end + 1):
            arr[i] = arr_update_fn(arr[i], inc_i)
        tester.range_update(start, end, inc_i)
        got = tester.query_segment_tree(start, end)
        expected = arr_eval_fn(arr[start:end + 1])
        assert got == expected, '%d-%d with inc %d, Expected %d Got %d' % (start, end, inc_i, expected, got)

print("Testing Lazy Range Query Sum Replacement")
arr = deepcopy(starting_arr)
tester = LazyQueryRange(arr, merge_function=add,
                        range_update_function=lambda old_value, lo, hi, to_new_value: (hi - lo + 1) * to_new_value)
assert tester.range_query_tree == expected_sum_range_tree
for i in range(len(arr)):
    for j in range(i, len(arr)):
        assert tester.query_segment_tree(i, j) == sum(arr[i:j + 1])

arr_update_fn, arr_eval_fn = lambda old_value, to_new_value: to_new_value, sum
for start in range(len(arr)):
    for end in range(start, len(arr)):
        new_value = randint(randint_a, randint_b)
        for i in range(start, end + 1):
            arr[i] = arr_update_fn(arr[i], new_value)
        tester.range_update(start, end, new_value)
        got = tester.query_segment_tree(start, end)
        expected = arr_eval_fn(arr[start:end + 1])
        assert got == expected, '%d-%d with New Value %d, Expected %d Got %d' % (start, end, new_value, expected, got)

print("Testing Lazy Range Query Max Replacement")
arr = deepcopy(starting_arr)
tester = LazyQueryRange(arr, merge_function=max,
                        range_update_function=lambda old_value, lo, hi, to_new_value: to_new_value)
assert tester.range_query_tree == expected_max_range_tree
for i in range(len(arr)):
    for j in range(i, len(arr)):
        assert tester.query_segment_tree(i, j) == max(arr[i:j + 1])

arr_update_fn, arr_eval_fn = lambda old_value, to_new_value: to_new_value, max
for start in range(len(arr)):
    for end in range(start, len(arr)):
        new_value = randint(randint_a, randint_b)
        for i in range(start, end + 1):
            arr[i] = arr_update_fn(arr[i], new_value)
        tester.range_update(start, end, new_value)
        got = tester.query_segment_tree(start, end)
        expected = arr_eval_fn(arr[start:end + 1])
        assert got == expected, '%d-%d with New Value %d, Expected %d Got %d' % (start, end, new_value, expected, got)
