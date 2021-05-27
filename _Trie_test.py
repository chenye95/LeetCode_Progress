from typing import List, Optional

from _Trie import Trie


def run_simulation(instructions: List[str], parameters: List[List],
                   expected_output: List[Optional[bool]]) -> None:
    if parameters[0]:
        test_object = Trie(parameters[0][0])
    else:
        test_object = Trie()
    for i in range(1, len(instructions)):
        next_instruction, next_parameter, expected_value = instructions[i], parameters[i], expected_output[i]
        if next_instruction == "insert":
            test_object.insert(next_parameter[0])
        elif next_instruction == "search":
            assert test_object.search(next_parameter[0]) is expected_value
        else:
            assert test_object.starts_with(next_parameter[0]) is expected_value


test_cases = [(["Trie", "insert", "search", "search", "startsWith", "insert", "search"],
               [['$'], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]],
               [None, None, True, False, True, None, True]),
              (["Trie", "insert", "insert", "insert", "search", "search", "search", "search"],
               [[], ["bad"], ["dad"], ["mad"], ["pad"], ["bad"], [".ad"], ["b.."]],
               [None, None, None, None, False, True, True, True]),
              (["Trie", "insert", "insert", "search", "search", "search", "search", "search", "search", ],
               [[], ["a"], ["a"], ["a"], ["."], ["a"], ["aa"], [".a"], ["a."]],
               [None, None, None, True, True, True, False, False, False]),
              ]
for test_instructions, test_parameters, test_expected_values in test_cases:
    run_simulation(test_instructions, test_parameters, test_expected_values)
