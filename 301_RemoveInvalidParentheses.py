"""
Given a string s that contains parentheses and letters, remove the minimum number of invalid parentheses to make the
 input string valid.

Return all the possible results. You may return the answer in any order.
"""
from typing import List


def remove_invalid_parentheses(s: str) -> List[str]:
    """
    :param s: consists of '(', ')' and lowercase English letters. At most 20 parentheses in s
    :return: list valid parentheses after removing minimum number of invalid '(' or ')'
    """

    def recurse(index: int, left_parentheses_count: int, right_parentheses_count: int,
                left_to_remove: int, right_to_remove: int, expression: str) -> None:
        """
        :param index: evaluating where to take or drop s[index]
        :param left_parentheses_count: count of '(' so far in expressions
        :param right_parentheses_count: count of ')' so far in expressions
        :param left_to_remove: number of '(‘ need to be removed from s[index:]
        :param right_to_remove:  number of ')‘ need to be removed from s[index:]
        :param expression: current state of the expression, valid so far with some extra '('
        """
        while index < len(s) and s[index] not in ('(', ')'):
            expression += s[index]
            index += 1

        if index == len(s):
            if left_to_remove == 0 and right_to_remove == 0:
                valid_string_set.add(expression)
            return

        # Prune case - drop s[index]
        if s[index] == '(' and left_to_remove > 0:
            recurse(index + 1, left_parentheses_count, right_parentheses_count,
                    left_to_remove - 1, right_to_remove, expression)
        elif s[index] == ')' and right_to_remove > 0:
            recurse(index + 1, left_parentheses_count, right_parentheses_count,
                    left_to_remove, right_to_remove - 1, expression)

        # Save case - take s[index]
        expression += s[index]
        if s[index] == '(':
            recurse(index + 1, left_parentheses_count + 1, right_parentheses_count,
                    left_to_remove, right_to_remove, expression)
        elif s[index] == ')' and left_parentheses_count > right_parentheses_count:
            recurse(index + 1, left_parentheses_count, right_parentheses_count + 1,
                    left_to_remove, right_to_remove, expression)

    # First calculates how many parentheses will the final result have
    left_removal = right_removal = 0

    for c in s:
        if c == '(':
            left_removal += 1
        elif c == ')':
            if left_removal:
                # have a matching ( to make a valid pair
                left_removal -= 1
            else:
                # do not have a matching to (, need to remove the current )
                right_removal += 1

    # Second, find all valid removal options
    valid_string_set = set()
    recurse(index=0, left_parentheses_count=0, right_parentheses_count=0,
            left_to_remove=left_removal, right_to_remove=right_removal, expression="")
    return list(valid_string_set)


test_cases = [("()())()", {"(())()", "()()()"}),
              ("(a)())()", {"(a())()", "(a)()()"}),
              (")(", {""}),
              ("o(()()()m()((()t",
               {"o()()()m()()t", "o(())()m()()t", "o(()())m()()t", "o(()()()m)()t", "o(()()()m())t"}),
              ("((m)(())(((", {"(m)(())", "((m)())"}),
              ("()((())h()(()()()))((", {"()((())h()(()()()))"}), ]
for test_s, expected_set in test_cases:
    assert set(remove_invalid_parentheses(test_s)) == expected_set
