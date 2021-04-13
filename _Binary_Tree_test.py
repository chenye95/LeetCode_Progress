from _Binary_Tree import *

# TreeNode and BinaryTree
root = TreeNode(1)
root.left = TreeNode(4)
root.right = TreeNode(2)
root.right.left = TreeNode(3)
tree = BinaryTree(root)
assert [1, 4, 2, 3] == tree.preorder_traversal()
assert [4, 1, 3, 2] == tree.inorder_traversal()

root = TreeNode('A')
tree = BinaryTree(root)
assert ['A'] == tree.preorder_traversal()
assert ['A'] == tree.inorder_traversal()
assert ['A'] == tree.postorder_traversal()

tree.root.left = TreeNode('B')
assert ['A', 'B'] == tree.preorder_traversal()
assert ['B', 'A'] == tree.inorder_traversal()
assert ['B', 'A'] == tree.postorder_traversal()

tree.root.right = TreeNode('C')
assert ['A', 'B', 'C'] == tree.preorder_traversal()
assert ['B', 'A', 'C'] == tree.inorder_traversal()
assert ['B', 'C', 'A'] == tree.postorder_traversal()

tree.root.left = None
assert ['A', 'C'] == tree.preorder_traversal()
assert ['A', 'C'] == tree.inorder_traversal()
assert ['C', 'A'] == tree.postorder_traversal()

assert tree is not None
assert tree != 3
assert tree != TreeNode('A')
assert tree != BinaryTree(TreeNode('A'))
other_root = TreeNode('A')
other_root.left = TreeNode('C')
other_tree = BinaryTree(other_root)
assert tree != other_tree
other_root.left = None
other_root.right = TreeNode('B')
assert tree != other_tree
other_root.right.val = 'C'
assert tree == other_tree

reference_head = TreeNode('F')
reference_head.left = TreeNode('B')
reference_head.left.left = TreeNode('A')
reference_head.left.right = TreeNode('D')
reference_head.left.right.left = TreeNode('C')
reference_head.left.right.right = TreeNode('E')
reference_head.right = TreeNode('G')
reference_head.right.right = TreeNode('I')
reference_head.right.right.left = TreeNode('H')

reference_tree = BinaryTree(reference_head)
assert reference_tree.height() == 4, "height"
print_array = reference_tree.print_tree(filler=' ')
expected_output = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', 'F', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                   [' ', ' ', ' ', 'B', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'G', ' ', ' ', ' '],
                   [' ', 'A', ' ', ' ', ' ', 'D', ' ', ' ', ' ', ' ', ' ', ' ', ' ', 'I', ' '],
                   [' ', ' ', ' ', ' ', 'C', ' ', 'E', ' ', ' ', ' ', ' ', ' ', 'H', ' ', ' ']]
for layer in range(len(print_array)):
    assert print_array[layer] == expected_output[layer], layer

preorder = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
inorder = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']
postorder = ['A', 'C', 'E', 'D', 'B', 'H', 'I', 'G', 'F']
layeroder = ['F', 'B', 'G', 'A', 'D', 'I', 'C', 'E', 'H']
layerorder_by_layer = [['F'], ['B', 'G'], ['A', 'D', 'I'], ['C', 'E', 'H']]
leetcodeorder = ['F', 'B', 'G', 'A', 'D', None, 'I', None, None, 'C', 'E', 'H', None, None, None, None, None, None, None]

assert preorder == reference_tree.preorder_traversal()
assert inorder == reference_tree.inorder_traversal()
assert postorder == reference_tree.postorder_traversal()
assert leetcodeorder == reference_tree.leetcode_traversal(), reference_tree.leetcode_traversal()
assert layerorder_by_layer == reference_tree.layer_traversal_by_layer()

assert reference_tree.right_side_view() == ['F', 'G', 'I', 'H']
assert reference_tree.left_side_view() == ['F', 'B', 'A', 'C']

# ConstructTree
built_tree = ConstructTree.build_tree_pre_in(preorder=preorder, inorder=inorder)
assert built_tree == reference_tree
assert preorder == built_tree.preorder_traversal()
assert inorder == built_tree.inorder_traversal()
assert layeroder == built_tree.layer_traversal()
assert layerorder_by_layer == built_tree.layer_traversal_by_layer()

built_tree = ConstructTree.build_tree_in_post(inorder=inorder, postorder=postorder)
assert built_tree == reference_tree
assert preorder == built_tree.preorder_traversal()
assert inorder == built_tree.inorder_traversal()
assert layeroder == built_tree.layer_traversal()
assert layerorder_by_layer == built_tree.layer_traversal_by_layer()

built_tree = ConstructTree.build_tree_leetcode(['F', 'B', 'G', 'A', 'D', None, 'I', None, None, 'C', 'E', 'H'])
assert built_tree == reference_tree
assert preorder == built_tree.preorder_traversal()
assert inorder == built_tree.inorder_traversal()
assert layeroder == built_tree.layer_traversal()
assert layerorder_by_layer == built_tree.layer_traversal_by_layer()

built_tree = ConstructTree.build_tree_leetcode(reference_tree.leetcode_traversal())
assert built_tree == reference_tree

built_tree = ConstructTree.build_tree_leetcode([-1, 0, 1])
assert built_tree.leetcode_traversal() == [-1, 0, 1, None, None, None, None]

built_tree = BinaryTree(TreeNode(0))
print(built_tree.print_tree())

test_tree_1 = ConstructTree.build_tree_leetcode([2, None, 4])
test_tree_2 = ConstructTree.build_tree_leetcode([2, 3, 4])
assert test_tree_1 != test_tree_2

test_tree_1 = ConstructTree.build_tree_leetcode([2, 3, None])
test_tree_2 = ConstructTree.build_tree_leetcode([2, 3, 4])
assert test_tree_1 != test_tree_2

assert BinaryTree(None) == BinaryTree(None)
assert test_tree_1 != BinaryTree(None)
assert BinaryTree(None) != test_tree_2

# Test Binary Tree Trim Boundary
test_cases = [([1, 0, 2], 1, 2, [1, None, 2]),
              ([3, 0, 4, None, 2, None, None, 1], 1, 3, [3, 2, None, 1]),
              ([1], 1, 2, [1]),
              ([1, None, 2], 1, 3, [1, None, 2]),
              ([1, None, 2], 2, 4, [2]), ]
for tree_input, low_input, high_input, expected_output in test_cases:
    test_tree = ConstructTree.build_tree_leetcode(tree_input)
    test_tree.trim_boundary(low_input, high_input)
    len_leetcode = len(test_tree.leetcode_traversal())
    assert test_tree.leetcode_traversal()[:len(expected_output)] == expected_output
    assert test_tree.leetcode_traversal()[len(expected_output):] == [None] * (len_leetcode - len(expected_output))

# Test Binary Tree Max Width
test_cases = [([1, 3, 2, 5, 3, None, 9], 4),
              ([1, 3, None, 5, 3], 2),
              ([1, 3, 2, 5], 2),
              ([1, 3, 2, 5, None, None, 9, 6, None, None, 7], 8)]
for tree_list, expected_out in test_cases:
    test_tree = ConstructTree.build_tree_leetcode(tree_list)
    assert test_tree.max_width() == expected_out
