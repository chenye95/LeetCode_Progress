from _BST import BST
from _Binary_Tree import TreeNode
from _Linked_List import LinkedList
from copy import deepcopy

values = list(range(1, 19, 2))
values.append(12)
values.reverse()
new_bst = BST(values)
assert new_bst.balance_factor() == 0
assert values == new_bst.traversal()
assert new_bst.is_balanced()

new_bst.insert(6)
values.append(6)
values.sort()
assert values == new_bst.traversal()

new_bst.insert(8)
new_bst.insert(10)
new_bst.insert(16)
new_bst.insert(16.5)
new_bst.insert(19)
assert new_bst.is_valid()
assert not new_bst.is_balanced()
values.extend([8, 10, 16, 16.5, 19])

values.sort()
assert values == new_bst.traversal()


for i in range(len(values)):
    deletion_tree = deepcopy(new_bst)
    assert deletion_tree.delete_node(values[i])
    assert deletion_tree.is_valid()
    # print('Deleted: %d, Remaining: %s' % (values[i], str(deletion_tree.traversal())))
    assert deletion_tree.traversal() == values[:i] + values[i+1:]

assert not new_bst.delete_node(20)
assert not new_bst.delete_node(7.5)
assert not new_bst.is_balanced()

new_bst.hard_re_balance()
assert new_bst.is_balanced()
assert values == new_bst.traversal()
assert -1 <= new_bst.balance_factor() <= 1
assert new_bst.look_up(6)
assert not new_bst.look_up(14)

for i in range(len(values)):
    deletion_tree = deepcopy(new_bst)
    assert deletion_tree.delete_node(values[i])
    assert deletion_tree.is_valid()
    # print('Deleted: %d, Remaining: %s' % (values[i], str(deletion_tree.traversal())))
    assert deletion_tree.traversal() == values[:i] + values[i+1:]

expected_values = [6, 7, 8, 9, 10, 11, 12, 13]
assert new_bst.traverse_range(6, 13) == expected_values
assert new_bst.traverse_range(6, 14) == expected_values
assert new_bst.traverse_range(5.5, 13) == expected_values


sorted_list = list(range(1, 11))
head = LinkedList.create_linked_list(sorted_list)
new_bst = BST(head)
assert new_bst.traversal() == sorted_list
assert new_bst.is_balanced()

new_bst = BST([-1])
new_bst.root.right = TreeNode(1)
new_bst.root.right.left = TreeNode(-1)
assert new_bst.is_valid()

new_bst = BST([1])
new_bst.root.left = TreeNode(-1)
new_bst.root.left.right = TreeNode(1)
assert not new_bst.is_valid()

new_bst = BST([1, 3, 4])
new_bst.root.left.right = TreeNode(2)
for i in range(1, 5):
    assert new_bst.kthSmallest(i) == i, "Expecting %d got %d" % (i, new_bst.kthSmallest(i))
assert new_bst.kthSmallest(5) is None


