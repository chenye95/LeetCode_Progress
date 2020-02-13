"""
Under a grammar given below, strings can represent a set of lowercase words.  Let's use R(expr) to denote the set of 
words the expression represents.
"""
from typing import List
from copy import deepcopy

def braceExpansionII(expression: str) -> List[str]:
    if not expression:
        return []

    stack = []
    current_expressions = set()
    last_operator = current_str = None
    for c in expression:
        if 'a' <= c <= 'z':
            current_str = c if current_str is None else current_str + c
        else:
            if current_str:
                if last_operator == ',' or not current_expressions:
                    current_expressions.add(current_str)
                else:
                    current_expressions = set([curr + current_str for curr in current_expressions])
                current_str = None
            if c == ',' or c == '{':
                stack.append((c, deepcopy(current_expressions)))
                current_expressions = set()
                last_operator = c
            else:  # c == '}'
                while stack[-1][0] == ',':
                    last_operator, previous_expressions = stack.pop()
                    if previous_expressions is not None:
                        current_expressions = current_expressions.union(previous_expressions)
                last_operator, previous_expressions = stack.pop()
                if previous_expressions:
                    current_expressions = set([prev + curr for prev in previous_expressions
                                                           for curr in current_expressions])
                last_operator = c

    if 'a' <= expression[-1] <= 'z':
        if current_expressions:
            current_expressions = set([curr + current_str for curr in current_expressions])
        else:
            current_expressions = set([current_str])
    return sorted(list(current_expressions))

test_cases = [#("{a,b}{c,{d,e}}", ["ac","ad","ae","bc","bd","be"]),
              #("{{a,z},a{b,c},{ab,z}}", ["a","ab","ac","z"]),
              #("{ab,cd}{e,f}", ["abe", "abf", "cde", "cdf"]),
              #("{a,b}c{d,e}f", ["acdf","acef","bcdf","bcef"]),
              #("abcd", "abcd"),
              ("{{a,{x,ia,o},w},er,a{x,ia,o}w}", ["a","aiaw","aow","axw","er","ia","o","w","x"])]

for test_input, test_output in test_cases:
    assert braceExpansionII(test_input) == test_output