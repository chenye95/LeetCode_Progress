"""
Design your implementation of the linked list. You can choose to use a singly or doubly linked list.

A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next
 is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the
 linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:
- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the index_th node in the linked list. If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the
    new node will be the first node of the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the index_th node in the linked list. If index
    equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater
    than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the index_th node in the linked list, if the index is valid.
"""
from typing import List, Optional

from _Linked_Complex import DoubleLinkedList


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[int]]) -> None:
    test_object = DoubleLinkedList()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "addAtHead":
            test_object.add_at_head(next_parameter[0])
        elif next_instruction == "addAtTail":
            test_object.add_at_tail(next_parameter[0])
        elif next_instruction == "addAtIndex":
            test_object.add_at_index(next_parameter[0], next_parameter[1])
        elif next_instruction == "get":
            assert test_object.get_at_index(next_parameter[0]) == expected_value
        else:
            test_object.delete_at_index(next_parameter[0])


test_cases = [(["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"],
               [[], [1], [3], [1, 2], [1], [1], [1]],
               [None, None, None, None, 2, None, 3]),
              (["MyLinkedList", "addAtHead", "addAtTail", "addAtTail", "addAtTail", "addAtTail", "addAtTail",
                "addAtTail", "deleteAtIndex", "addAtHead", "addAtHead", "get", "addAtTail", "addAtHead", "get",
                "addAtTail", "addAtIndex", "addAtTail", "addAtHead", "addAtHead", "addAtHead", "get", "addAtIndex",
                "addAtHead", "get", "addAtHead", "deleteAtIndex", "addAtHead", "addAtTail", "addAtTail", "addAtIndex",
                "addAtTail", "addAtHead", "get", "addAtTail", "deleteAtIndex", "addAtIndex", "deleteAtIndex",
                "addAtHead", "addAtTail", "addAtHead", "addAtHead", "addAtTail", "addAtTail", "get", "get", "addAtHead",
                "addAtTail", "addAtTail", "addAtTail", "addAtIndex", "get", "addAtHead", "addAtIndex", "addAtHead",
                "addAtTail", "addAtTail", "addAtIndex", "deleteAtIndex", "addAtIndex", "addAtHead", "addAtHead",
                "deleteAtIndex", "addAtTail", "deleteAtIndex", "addAtIndex", "addAtTail", "addAtHead", "get",
                "addAtIndex", "addAtTail", "addAtHead", "addAtHead", "addAtHead", "addAtHead", "addAtHead", "addAtHead",
                "deleteAtIndex", "get", "get", "addAtHead", "get", "addAtTail", "addAtTail", "addAtIndex", "addAtIndex",
                "addAtHead", "addAtTail", "addAtTail", "get", "addAtIndex", "addAtHead", "deleteAtIndex", "addAtTail",
                "get", "addAtHead", "get", "addAtHead", "deleteAtIndex", "get", "addAtTail", "addAtTail"],
               [[], [38], [66], [61], [76], [26], [37], [8], [5], [4], [45], [4], [85], [37], [5], [93], [10, 23], [21],
                [52], [15], [47], [12], [6, 24], [64], [4], [31], [6], [40], [17], [15], [19, 2], [11], [86], [17],
                [55], [15], [14, 95], [22], [66], [95], [8], [47], [23], [39], [30], [27], [0], [99], [45], [4],
                [9, 11], [6], [81], [18, 32], [20], [13], [42], [37, 91], [36], [10, 37], [96], [57], [20], [89], [18],
                [41, 5], [23], [75], [7], [25, 51], [48], [46], [29], [85], [82], [6], [38], [14], [1], [12], [42],
                [42], [83], [13], [14, 20], [17, 34], [36], [58], [2], [38], [33, 59], [37], [15], [64], [56], [0],
                [40], [92], [63], [35], [62], [32]],
               [None, None, None, None, None, None, None, None, None, None, None, 61, None, None, 61, None, None, None,
                None, None, None, 85, None, None, 37, None, None, None, None, None, None, None, None, 23, None, None,
                None, None, None, None, None, None, None, None, DoubleLinkedList.INDEX_OUT_OF_BOUND, 95, None, None,
                None, None, None, 31, None, None, None, None, None, None, None, None, None, None, None, None, None,
                None, None, None, 8, None, None, None, None, None, None, None, None, None, 6, 47, None, 23, None, None,
                None, None, None, None, None, 93, None, None, None, None, 48, None, 93, None, None, 59, None, None]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
