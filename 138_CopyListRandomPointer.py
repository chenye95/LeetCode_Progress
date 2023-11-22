"""
A linked list of length n is given such that each node contains an additional random pointer, which could point to any
node in the list, or null.

Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has
its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should
point to new nodes in the copied list such that the pointers in the original list and copied list represent the same
list state. None of the pointers in the new list should point to nodes in the original list.
"""


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val: int = int(x)
        self.next: Node = next
        self.random: Node = random


def copy_random_list(head: Node) -> Node:
    """
    :param head: node contains an additional random pointer, which could point to any node in the list, or None.
    :return: head node of the copy list
    """
    if not head:
        return head

    prev_copy = Node(head.val)
    node_map: dict[Node, Node] = {head: prev_copy}
    if head.random:
        if head.random != head:
            node_map[head.random] = Node(head.random.val)
            prev_copy.random = node_map[head.random]
        else:
            prev_copy.random = prev_copy

    current_original = head
    while current_original.next:
        current_original = current_original.next
        if current_original not in node_map:
            node_map[current_original] = Node(current_original.val)
        current_node = node_map[current_original]
        prev_copy.next = current_node

        if current_original.random:
            if current_original.random not in node_map:
                node_map[current_original.random] = Node(current_original.random.val)
            current_node.random = node_map[current_original.random]

        prev_copy = current_node

    return node_map[head]


test_cases = [[[-1, 0]],
              [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]],
              [[1, 1], [2, 1]],
              [[3, None], [3, 0], [3, None]],
              [], ]
for test_input in test_cases:
    if not test_input:
        test_head = None
    else:
        node_list = [Node(test_input[0][0])]
        for val, _ in test_input[1:]:
            node_list[-1].next = Node(val)
            node_list.append(node_list[-1].next)
        for i, (_, random_point) in enumerate(test_input):
            if random_point is not None:
                node_list[i].random = node_list[random_point]
        test_head = node_list[0]
    output_head = copy_random_list(head=test_head)
    output_node_map = {}
    output_current = output_head
    i = 0
    while output_current:
        output_node_map[output_current] = i
        i += 1
        output_current = output_current.next
    output_current = output_head
    output_list = []
    while output_current:
        if output_current.random is None:
            output_list.append([output_current.val, None])
        else:
            output_list.append([output_current.val, output_node_map[output_current.random]])
        output_current = output_current.next
    assert output_list == test_input, test_input
