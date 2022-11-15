"""
Given a string s, return true if the s can be palindrome after deleting at most one character from it.
"""


def valid_palindrome(s: str) -> bool:
    if not s or s == s[::-1]:
        return True
    point_l, point_r = 0, len(s) - 1
    while point_l < point_r:
        if s[point_l] == s[point_r]:
            point_l += 1
            point_r -= 1
        else:
            return s[point_l + 1: point_r + 1] == s[point_l + 1: point_r + 1][::-1] \
                   or s[point_l: point_r] == s[point_l: point_r][::-1]
    return True


test_cases = [
    ("aba", True),
    ("abca", True),
    ("abc", False),
    ("deeee", True),
    ("cbbcc", True),
    ("vkjtmxzlpurgthxqxvokfcvdjgpvryculxhmyqbwyiogzcrwghbbssessgpbwdyfjjtobigtnmmrvkfixfjoknpsixljlhhruwllvsvekeiwqqk"
     "ezjwffxqspfzikxftycyorrjyhnojdabogmdttzgxpyliwcadpfaqprfvwhsrkngqoxisvjjeivmypzzevoyznekbiowuoiuadgwtkcujkvsgei"
     "whwrnzdywuuvcoluuywljnacgoyezzeyogcanjlwyuulocvuuwydznrwhwiegsvkjucktwgdauiouwoibkenzyovezzpymviejjvsixoqgnkrsh"
     "wvfrpqafpdacwilypxgzttdmgobadjonhyjrroycytfxkizfpsqxffwjzekqqwiekevsvllwurhhljylxispnojfxifkvrmmntgibotjjfydwbp"
     "gssessbbhgwrczgoiywbqymhxlucyrvpgjdvcfkovxqxhtgruplzxmtjkv", False),
    ("vmpmofafcwfoycbtjjdeklsbvhqwpdfqalnjwzhliyuovedxvgygayobytuvlieicrlllrniwtvgzaxbezvwiarbqphtmtqrzcktfkdphgmbxvq"
     "ufcbmbhtaekloljgmsxjemzpyxfwbyiqcomczxwgdrtyicjcizbjvhrurlvzkvshdizquvnigxvofuygkqirszejsmhotmpwjuvjluttckswmms"
     "fkgwrqiijwikxucpjxkmqvpjnjjxxjjnjpvqmkxjpcuxkiwjiiqrwgkfsmmwskcttuljvujwpmtohmsjezsriqkgyufovxginvuqzidhsvkzvlr"
     "urhvjbzicjciytrdgwxzcmocqiybwfxypzmejxsmgjlolkeathbmbcfuqvxbmghpdkftkczrqtmthpqbraiwvzebxazgvtwinrlllrcieilvuty"
     "boyagygvxdevouyilhzwjnlaqfdpwqhvbslkedjjtbcyofwcfafompmv", True),
]
for test_s, expected_value in test_cases:
    assert valid_palindrome(test_s) is expected_value
