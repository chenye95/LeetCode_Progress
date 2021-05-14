"""
Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.
"""


def min_remove_to_make_valid(s: str) -> str:
    """
    :param s: string of '(', ')' and lowercase English letters
    :return: remove minimum number of parentheses so that the resulting string is valid, return any valid strings
    """
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


test_cases = [("lee(t(c)o)de)", {"lee(t(c)o)de", "lee(t(co)de)", "lee(t(c)ode)"}),
              ("a)b(c)d", {"ab(c)d"}),
              ("))((", {""}),
              ("(a(b(c)d)", {"a(b(c)d)", "a(bc)d", "(abc)d"}),
              ("))()qc)(())))))a)()s)()((xh()()t(()))(((()((((r()())))((((())(((((()())()(())((())())((r(()())(())))",
               {"()qc(())a()s()(xh()()t(()))()(((r()())))(())(()())()(())((())())((r(()())(())))", }), ]
for test_s, expected_output in test_cases:
    assert min_remove_to_make_valid(test_s) in expected_output, test_s
