"""
Given a string s, a k duplicate removal consists of choosing k adjacent and equal letters from s and removing them
 causing the left and the right side of the deleted substring to concatenate together.

We repeatedly make k duplicate removals on s until we no longer can.

Return the final string after all such duplicate removals have been made.

It is guaranteed that the answer is unique.
"""


def remove_duplicates_pointer(s: str, k: int):
    """
    :param s: string of lowercase letters
    :param k: need k consecutive characters to count as duplicates
    :return: processed s with all duplicates removed
    """
    processed_until = 0
    list_s = list(s)
    count_s = [0] * len(s)
    for c in s:
        list_s[processed_until] = c
        count_s[processed_until] = count_s[processed_until - 1] + 1 \
            if processed_until and list_s[processed_until - 1] == list_s[processed_until] else 1
        if count_s[processed_until] == k:
            processed_until -= k
        processed_until += 1

    return ''.join(list_s[:processed_until])


def remove_duplicates_stack(s: str, k: int):
    """
    :param s: string of lowercase letters
    :param k: need k consecutive characters to count as duplicates
    :return: processed s with all duplicates removed
    """
    chr_stack = [['#', 0]]
    for c in s:
        if chr_stack[-1][0] == c:
            chr_stack[-1][1] += 1
            if chr_stack[-1][1] == k:
                chr_stack.pop()
        else:
            chr_stack.append([c, 1])
    return ''.join(c * r for c, r in chr_stack)


test_cases = [("abbaca", 2, "ca"), ('aab', 2, 'b'), ('aa', 2, ''),
              ("egibhabdjdjbgeciacchifhhjccdhefecjfcebjbciajbiffgfjeieieiagfihfe", 2,
               "egibhabdjdjbgeciahifjdhefecjfcebjbciajbigfjeieieiagfihfe"),
              ("abcd", 2, "abcd"), ("deeedbbcccbdaa", 3, "aa"), ("pbbcggttciiippooaais", 2, "ps"),
              ("viittttttiiiillllkkkkkkllllllkkkkkkllkkkkkkcnoooossssssooasu", 6, "vcnasu"), ]
for remove_duplicates in [remove_duplicates_pointer, remove_duplicates_stack, ]:
    for test_s, test_k, expected_output in test_cases:
        assert remove_duplicates(test_s, test_k) == expected_output, remove_duplicates.__name__
