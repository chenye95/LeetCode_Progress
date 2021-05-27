"""
Design a data structure that supports the following two operations:
- void addWord(word)
- bool search(word)

search(word) can search a literal word or a regular expression string containing only letters a-z or '.'
A . means it can represent any one letter.
"""
from typing import List, Optional

from _Trie import Trie


# Place holder to run test cases
def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[bool]]) -> None:
    test_object = Trie('.')
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "addWord":
            test_object.insert(next_parameter[0])
        else:
            assert test_object.search(next_parameter[0]) is expected_value


test_cases = [(["WordDictionary", "addWord", "addWord", "addWord", "search", "search", "search", "search"],
               [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
               [None, None, None, None, False, True, True, True]),
              (["WordDictionary", "addWord", "addWord", "search", "search", "search", "search", "search", "search", ],
               [[], ["a"], ["a"], ["a"], ["."], ["a"], ["aa"], [".a"], ["a."]],
               [None, None, None, True, True, True, False, False, False]), ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
