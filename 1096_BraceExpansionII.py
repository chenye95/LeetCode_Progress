"""
Under a grammar given below, strings can represent a set of lowercase words.  Let's use R(expr) to denote the set of 
words the expression represents.

Formally, the 3 rules for our grammar:
(1) For every lowercase letter x, we have R(x) = {x}
(2) For expressions e_1, e_2, ... , e_k with k >= 2, we have R({e_1,e_2,...}) = R(e_1) ∪ R(e_2) ∪ ...
(3) For expressions e_1 and e_2, we have R(e_1 + e_2) = {a + b for (a, b) in R(e_1) × R(e_2)}, where + denotes
concatenation, and × denotes the cartesian product.

Given an expression representing a set of words under the given grammar, return the sorted list of words that the
expression represents.
"""
from typing import List


def braceExpansionII(expression: str) -> List[str]:
    stack, current_brace, current_comma = [], [], []
    for c in expression:
        if c.isalpha():
            current_comma = [preceding + c for preceding in current_comma or ["", ]]
        elif c == "{":
            stack.append(current_brace)
            stack.append(current_comma)
            current_brace, current_comma = [], []
        elif c == "}":
            precede_brace = stack.pop()
            current_comma = [prev + cur for cur in current_brace + current_comma for prev in precede_brace or ["", ]]
            current_brace = stack.pop()
        elif c == ",":
            current_brace.extend(current_comma)
            current_comma = []
    return sorted(set(current_brace + current_comma))


test_cases = [("{a,b}{c,{d,e}}", ["ac", "ad", "ae", "bc", "bd", "be", ]),
              ("{{a,z},a{b,c},{ab,z}}", ["a", "ab", "ac", "z", ]),
              ("{ab,cd}{e,f}", ["abe", "abf", "cde", "cdf", ]),
              ("{a,b}c{d,e}f", ["acdf", "acef", "bcdf", "bcef", ]),
              ("abcd", ["abcd", ]),
              ("{{a,{x,ia,o},w},er,a{x,ia,o}w}", ["a", "aiaw", "aow", "axw", "er", "ia", "o", "w", "x", ]),
              ]

for test_input, test_output in test_cases:
    assert braceExpansionII(test_input) == test_output, test_input
