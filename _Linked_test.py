from random import randint

from _Linked_Complex import DoubleLinkedList, ComplexLinkedList
from _Linked_List import LinkedList, PrintableLinkedList, ListNode

test_node = ListNode(0)
assert test_node.last_node().val == 0

node_list = [1, 2, 3, 4, 5]
linked_list = LinkedList.create_linked_list(node_list)
assert node_list == linked_list.head.list_from_node()
assert linked_list.head.last_node().val == 5

printable_list = PrintableLinkedList.create_linked_list(node_list)
separator = ', '
expected_output = separator.join([str(val) for val in node_list])
assert str(printable_list) == expected_output

list1 = list(range(1, 7))
list2 = list(range(7, 11))
list3 = list(range(11, 13))
list_head_1 = ComplexLinkedList.create_linked_list(list1).head
list_head_2 = ComplexLinkedList.create_linked_list(list2).head
list_head_3 = ComplexLinkedList.create_linked_list(list3).head
list_head_1.next.next.child = list_head_2
list_head_2.next.child = list_head_3

end1 = list_head_1.last_node()
end2 = list_head_2.last_node()
end3 = list_head_3.last_node()

assert end1.val == 6
assert end2.val == 10
assert end3.val == 12
assert end1.first_node() == list_head_1
assert end2.first_node() == list_head_2
assert end3.first_node() == list_head_3
assert list_head_1.list_from_node() == end1.list_before_node() and list_head_1.list_from_node() == list1
assert list_head_2.list_from_node() == end2.list_before_node() and list_head_2.list_from_node() == list2
assert list_head_3.list_from_node() == end3.list_before_node() and list_head_3.list_from_node() == list3

expected_flatten = [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]
complex_list = ComplexLinkedList(head=list_head_1)
complex_list.flatten_structure()
current_node = complex_list.head
prev_node = None
flattened_list = []
while current_node:
    assert current_node.child is None
    assert current_node.prev == prev_node
    flattened_list.append(current_node.val)
    prev_node = current_node
    current_node = current_node.next
assert flattened_list == [1, 2, 3, 7, 8, 11, 12, 9, 10, 4, 5, 6]

double_linked_list = DoubleLinkedList.create_linked_list(list(range(10)))
assert len(double_linked_list) == 10
for i in range(10):
    assert double_linked_list.get_at_index(i) == i, i
assert double_linked_list.get_at_index(-1) == double_linked_list.INDEX_OUT_OF_BOUND
assert double_linked_list.get_at_index(11) == double_linked_list.INDEX_OUT_OF_BOUND
assert double_linked_list.tail.val == 9
double_linked_list.add_at_tail(10)
assert len(double_linked_list) == 11
for i in range(11):
    assert double_linked_list.get_at_index(i) == i, i
assert double_linked_list.get_at_index(-1) == double_linked_list.INDEX_OUT_OF_BOUND
assert double_linked_list.get_at_index(12) == double_linked_list.INDEX_OUT_OF_BOUND
assert double_linked_list.head.list_from_node() == list(range(11))
assert double_linked_list.head.prev is None
double_linked_list.add_at_head(-1)
assert len(double_linked_list) == 12
assert double_linked_list.get_at_index(0) == -1
assert double_linked_list.head.list_from_node() == list(range(-1, 11))
assert double_linked_list.head.prev is None

expected_output = list(range(10))
double_linked_list = DoubleLinkedList.create_linked_list(expected_output)
for _ in range(1000):
    index, val = randint(0, len(expected_output)), randint(0, 100)
    expected_output.insert(index, val)
    double_linked_list.add_at_index(index, val)
    assert double_linked_list.head.list_from_node() == expected_output

for _ in range(1000):
    index = randint(0, len(expected_output) - 1)
    del expected_output[index]
    double_linked_list.delete_at_index(index)
    assert double_linked_list.head.list_from_node() == expected_output, index

test_list = DoubleLinkedList()
test_list.add_at_head(1)
assert len(test_list) == 1
assert test_list.get_at_index(0) == 1
assert test_list.get_at_index(1) == test_list.INDEX_OUT_OF_BOUND

test_list = DoubleLinkedList()
test_list.add_at_tail(1)
assert len(test_list) == 1
assert test_list.get_at_index(0) == 1
assert test_list.get_at_index(1) == test_list.INDEX_OUT_OF_BOUND
