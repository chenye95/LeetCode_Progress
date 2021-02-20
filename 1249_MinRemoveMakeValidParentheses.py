"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.
"""


def min_remove_to_make_valid(s: str) -> str:
    s_list = list(s)
    open_parentheses = []
    for i, s_i in enumerate(s):
        if s_i == '(':
            open_parentheses.append(i)
        elif s_i == ')':
            if open_parentheses:
                open_parentheses.pop()
            else:
                s_list[i] = ''
    while open_parentheses:
        s_list[open_parentheses.pop()] = ''

    return ''.join(s_list)


assert min_remove_to_make_valid("lee(t(c)o)de)") == "lee(t(c)o)de"
assert min_remove_to_make_valid("a)b(c)d") == "ab(c)d"
assert min_remove_to_make_valid("))((") == ""
assert min_remove_to_make_valid("(a(b(c)d)") == "a(b(c)d)"
