from _Union_Find import UnionFind, UnionFindArray

print("Testing Union Find")
try:
    failed_creation_empty = UnionFind([])
except ValueError as e:
    print("Expected Value Error Message:", e)

elements = ['E', 'F', 'I', 'D', 'C', 'A', 'J', 'L', 'G', 'K', 'B', 'H']
try:
    failed_creation = UnionFind(elements + ['A'])
except ValueError as e:
    print("Expected Value Error Message:", e)

test_union_find = UnionFind(elements, False)
assert not test_union_find.union_find_array.use_recursion
try:
    test_union_find.is_connected('Z', 'A')
except ValueError as e:
    print("Expected Value Error Message:", e)

assert test_union_find.size() == len(elements)
assert test_union_find.components_count() == len(elements)
join_list = [('C', 'K', False, 2), ('F', 'E', False, 2), ('A', 'J', False, 2),
             ('A', 'B', False, 3), ('C', 'D', False, 3), ('D', 'I', False, 4),
             ('L', 'F', False, 3), ('C', 'A', False, 7), ('A', 'B', True, 7),
             ('H', 'G', False, 2), ('H', 'F', False, 5), ('H', 'B', False, len(elements))]
expected_component_count = len(elements)
for e1, e2, previously_connected, expected_component_size in join_list:
    assert (test_union_find.find(e1, True) == test_union_find.find(e2)) is previously_connected
    assert test_union_find.is_connected(e1, e2) is previously_connected
    test_union_find.unify(e1, e2)
    assert test_union_find.is_connected(e1, e2) is True
    assert test_union_find.component_size(e1) == expected_component_size
    assert test_union_find.component_size(e2) == expected_component_size
    if not previously_connected:
        expected_component_count -= 1
    assert test_union_find.components_count() == expected_component_count
assert test_union_find.components_count() == 1

assert test_union_find.find('Z') == test_union_find.ELEMENT_NOT_FOUND
try:
    test_union_find.unify('A', 'Z')
except ValueError as e:
    print("Expected Value Error Message:", e)

print("Testing Union Find Array")
mapping = {e: i for i, e in enumerate(elements)}
try:
    failed_creation_empty_array = UnionFindArray(0)
except ValueError as e:
    print("Expected Value Error Message:", e)

test_union_find_array = UnionFindArray(len(elements))
assert not test_union_find_array.use_recursion
try:
    test_union_find_array.is_connected(-1, mapping['A'])
except ValueError as e:
    print("Expected Value Error Message:", e)

assert test_union_find_array.size() == len(elements)
assert test_union_find_array.components_count() == len(elements)
expected_component_count = len(elements)
for e1, e2, previously_connected, expected_component_size in join_list:
    assert test_union_find_array.is_connected(mapping[e1], mapping[e2]) is previously_connected
    test_union_find_array.unify(mapping[e1], mapping[e2])
    assert test_union_find_array.is_connected(mapping[e1], mapping[e2]) is True
    assert test_union_find_array.component_size(mapping[e1]) == expected_component_size
    assert test_union_find_array.component_size(mapping[e2]) == expected_component_size
    if not previously_connected:
        expected_component_count -= 1
    assert test_union_find_array.components_count() == expected_component_count
assert test_union_find_array.components_count() == 1

assert test_union_find_array.find(-1) == test_union_find.ELEMENT_NOT_FOUND
assert test_union_find_array.find(len(elements)) == test_union_find.ELEMENT_NOT_FOUND
try:
    test_union_find_array.unify(mapping['A'], -1)
except ValueError as e:
    print("Expected Value Error Message:", e)

try:
    test_union_find_array.unify(mapping['A'], len(elements))
except ValueError as e:
    print("Expected Value Error Message:", e)
