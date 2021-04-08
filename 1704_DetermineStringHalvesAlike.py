"""
You are given a string s of even length. Split this string into two halves of equal lengths, and let a be the first half
 and b be the second half.

Two strings are alike if they have the same number of vowels ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'). Notice
 that s contains uppercase and lowercase letters.

Return true if a and b are alike. Otherwise, return false.
"""


def halves_alike(s: str) -> bool:
    """
    :param s: string of even length of uppercase and lowercase letters
    :return: whether the first half has the same amount of vowels as the second half
    """
    vowels_list = "aeiouAEIOU"

    mid_len = len(s) // 2
    first_half_over_second = 0
    for c_1, c_2 in zip(s[:mid_len], s[mid_len:]):
        if c_1 in vowels_list:
            first_half_over_second += 1
        if c_2 in vowels_list:
            first_half_over_second -= 1

    return first_half_over_second == 0


test_cases = [("book", True), ("textbook", False), ("MerryChristmas", False),
              ("UoaUuIEIeaIOuoUUiAaEUIAUAAuEiUIUiUOeUUouIiiaoeiuioiOIosUoEUoIueAoAOUAiiOAUaIOeaoOUuueoOaoXMjkZDIvJlIQ" +
               "zQQUHHeIUZaUgNcflAvNPCTqbrIofxevHndldyTrwBDhLgQssEGmehKiDJLmRZxLzlaoYWQNyqDmU", False), ]
for test_s, expected_output in test_cases:
    assert halves_alike(s=test_s) is expected_output
