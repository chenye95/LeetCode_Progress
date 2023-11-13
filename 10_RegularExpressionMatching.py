"""
Given an input string s and a pattern p, implement regular expression matching with support for '.' and '*' where:
 - '.' Matches any single character.
 - '*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).
"""


def is_match_dp(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    # match_so_far[i][j]: if is_match_dp(s[:i], p[:i])
    match_so_far = [[False] * (n + 1) for _ in range(m + 1)]
    match_so_far[0][0] = True

    # in the future, last_position = any(match_so_far[i - 1][j])
    last_position = True
    for i in range(m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                match_so_far[i][j] = (match_so_far[i][j - 2] or
                                      (i > 0 and match_so_far[i - 1][j]) and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
            else:
                match_so_far[i][j] = i > 0 and match_so_far[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
        current_position = any(match_so_far[i])
        if not last_position and not current_position:
            return False
        last_position = current_position

    return match_so_far[-1][-1]


test_cases = [
    ("aa", "a", False),
    ("aa", "a*", True),
    ("ab", ".*", True),
    ("mississippi", "mis*is*p*.", False),
    ("bbabacccbcbbcaaab", "a*b*a*a*c*aa*c*bc*", False),
]
for is_match_method in [is_match_dp, ]:
    for test_s, test_p, expected_value in test_cases:
        assert is_match_method(test_s, test_p) is expected_value, is_match_method.__name__
