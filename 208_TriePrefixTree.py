"""
A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a
 dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:
- Trie() Initializes the trie object.
- void insert(String word) Inserts the string word into the trie.
- boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false
    otherwise.
- boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix,
    and false otherwise.
"""
from typing import List, Optional

from _Trie import Trie


# Place holder to run test cases
def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[bool]]) -> None:
    test_object = Trie('')
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "insert":
            test_object.insert(next_parameter[0])
        elif next_instruction == "search":
            assert test_object.search(next_parameter[0]) is expected_value
        else:
            assert test_object.starts_with(next_parameter[0]) is expected_value


test_cases = [(["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
               [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
               [None, None, True, False, True, None, True]),
              ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
