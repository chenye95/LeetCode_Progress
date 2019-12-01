"""
A password is considered strong if below conditions are all met:
- It has at least 6 characters and at most 20 characters.
- It must contain at least one lowercase letter, at least one uppercase letter, and at least one digit.
- It must NOT contain three repeating characters in a row ("...aaa..." is weak, but "...aa...a..." is strong, assuming
    other conditions are met).

Write a function strongPasswordChecker(s), that takes a string s as input, and return the MINIMUM change required to
make s a strong password. If s is already strong, return 0.
Insertion, deletion or replace of any one character are all considered as one change.
"""

def strongPasswordChecker(s: str) -> int:
    missing_types = 3
    if any('A' <= c <= 'Z' for c in s): missing_types -= 1
    if any('a' <= c <= 'z' for c in s): missing_types -= 1
    if any('0' <= c <= '9' for c in s): missing_types -= 1

    replace_op = type_1_change = type_2_change = 0
    # Type 1: replication length is 3l + can replace one change_op with one deletion
    # Type 2: replication length is 3l+2, can replace one change_op with two deletions
    # All change_op can be replaced by 3 deletion
    i = 2
    while i < len(s):
        if s[i] == s[i-1] == s[i-2]:
            length = 2
            while i < len(s) and s[i] == s[i-1]:
                length += 1
                i += 1

            replace_op += length // 3
            if length % 3 == 0:
                type_1_change += 1
            elif length % 3 == 1:
                type_2_change += 1

        else:
            i += 1

    if len(s) < 6:
        return max(missing_types, 6 - len(s))  # Note you can insert inside s
        """ Special Case:
        (1) ***: change_op = 1, missing_types = 2, add_op = 3: insert 3 inside s
        (2) ****: change_op = 1, missing_types = 2, add_op = 2: insert 2 inside s
        (3) *****: change_op = 1, missing_types = 2, add_op = 1: insert 1 and change 1
        """
    elif len(s) <= 20:
        return max(missing_types, replace_op)
    else:  # len(s) > 20  need to delete
        delete_op = len(s) - 20

        # Type 1: replication length is 3l, can replace one change with 1 deletion
        replace_op -= min(delete_op, type_1_change)
        # Type 2: replication length is 3l+2, can replace one change with 2 deletions
        replace_op -= min(max(delete_op - type_1_change, 0), type_2_change * 2) // 2
        # All change_op can be replaced by 3 deletions
        replace_op -= max(delete_op - type_1_change - 2 * type_2_change, 0) // 3

        # missing_types >= 0
        return delete_op + max(missing_types, replace_op)


assert(strongPasswordChecker("") == 6)
assert(strongPasswordChecker("aaa111") == 2)
assert(strongPasswordChecker("1111111111") == 3)
assert(strongPasswordChecker("ABABABABABABABABABAB1") == 2)