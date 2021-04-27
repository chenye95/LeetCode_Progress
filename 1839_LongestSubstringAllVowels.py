"""
A string is considered beautiful if it satisfies the following conditions:
- Each of the 5 English vowels ('a', 'e', 'i', 'o', 'u') must appear at least once in it.
- The letters must be sorted in alphabetical order (i.e. all 'a's before 'e's, all 'e's before 'i's, etc.).

For example, strings "aeiou" and "aaaaaaeiiiioou" are considered beautiful, but "uaeio", "aeoiu", and "aaaeeeooo" are
 not beautiful.

Given a string word consisting of English vowels, return the length of the longest beautiful substring of word. If no
 such substring exists, return 0.

A substring is a contiguous sequence of characters in a string.
"""


def longest_beautiful_substring(word: str) -> int:
    """
    :param word: 1 <= len(word) <= 5 * 10^5, consisting of lower letter english vowels 'a', 'e', 'i', 'o', and 'u'.
    :return: length of longest beautiful substring in word
    """
    max_len = 0
    search_string = ' aeiou '

    continuation_int, next_int = 0, 1
    continuation_chr, next_chr = '', 'a'
    current_sub_str_len = 0

    for c in word:
        if c == continuation_chr:
            current_sub_str_len += 1
        elif c == next_chr:
            current_sub_str_len += 1
            continuation_int += 1
            next_int += 1
            continuation_chr = search_string[continuation_int]
            next_chr = search_string[next_int]
        elif continuation_int > 0:
            if continuation_chr == 'u':
                max_len = max(max_len, current_sub_str_len)
            if c == 'a':
                continuation_int, next_int = 1, 2
                continuation_chr, next_chr = 'a', 'e'
                current_sub_str_len = 1
            else:
                continuation_int, next_int = 0, 1
                continuation_chr, next_chr = '', 'a'
                current_sub_str_len = 0

    if continuation_chr == 'u':
        max_len = max(max_len, current_sub_str_len)
    return max_len


test_cases = [("aeiaaioaaaaeiiiiouuuooaauuaeiu", 13),
              ("aaeiaaioaaaaeiiiiouuuooaauuaeiu", 13),
              ("eaeiaaioaaaaeiiiiouuuooaauuaeiu", 13),
              ("iaeiaaioaaaaeiiiiouuuooaauuaeiu", 13),
              ("oaeiaaioaaaaeiiiiouuuooaauuaeiu", 13),
              ("uaeiaaioaaaaeiiiiouuuooaauuaeiu", 13),
              ("aeeeiiiioooauuuaeiou", 5),
              ("a", 0),
              ("eieuuoeeueauueeoiiueaeuioeiiieioaouoeeoiiauiueiiuieueeeoaeaeoooiuauiaaueieoeeeeioauaouueiioeiaaaaooea" +
               "aaeoouoaoioauoaeuiioaiuuiaaaiieiuiuoiaeuuiooeiiuoaauoioeaeieaeeeiouieuaaaaaeoaeiaeeeaoaeooueieaaaeieo" +
               "oouueaueeiaiuoioiioieuoeeoeaaeeaauoaiaoaauaauioaueiaiooeoiiaiauaooiiauaiaoaoeaioeiaeeuueioauoueuaaiio" +
               "uoeoeoiaeeooaauieoeaiueioiaieouiaeauaeiaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" +
               "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" +
               "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" +
               "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" +
               "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" +
               "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" +
               "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" +
               "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee" +
               "eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeiiiiiiiiiiiiiiii" +
               "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
               "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
               "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
               "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii" +
               "iiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiooooooooooooooooooooooooooooooooooooooooooooooooooooooooo" +
               "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo" +
               "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo" +
               "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo" +
               "ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooouuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu" +
               "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu" +
               "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu" +
               "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu" +
               "uuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuiuaeouiioieoui" +
               "eeiuaeeuoiooioiiaoueioeuaeeoaauoaaeeaaoiuueoeaeoaaeueoueeiiiuiouieaiuoieeoooueiiiaeeuaaieeaaoiuuoeuoa" +
               "uouiieuaeeiueaeeeaaoieaeuiuoeuoaaiueieiouiiiaoueuuiuooeioaeooaeueouiaeuaaiueuoeeiouioiiueiueaaiuoaieu" +
               "iaoeuoeaeaiuaaoeeuouiiioeeoueuuauoieiaoaeeaeioouoaiieueoauaoeeoeouaiaoaueioiuaooouiueuieuauieeoeaiouo" +
               "aoeeeueuoeuieooaaaaaiuoououiuuueoioieueuueaueaeuaieueeaieioieuuuueoooueueoiaoiuuiooiauaaiiiiuoaaueeai" +
               "iaeaauaooooeaaeuiaaouooauaaaaiieiaeeeeeiauiiuaueieuieaoeeiauiuaueouaeoaaoiuaoiaiouaiaeoiaooieeioiieie" +
               "ioeeioeuioeiooouiiioaiaeeaaieouoaooaiaiueeuieoiuaeuieeiuaoaueiouoieauieiuoooieuiaooeaeaoiueaeeuieaioi" +
               "uoaeieuaaeouuoiieioeoiaeuiiiuiuaaaoeaaaoiuauaiiuaaaaiieeueeoieuiueuaueiiaioaoaoueiieueoauuueeeeuuueoi" +
               "uuaiaaeuauuiaeuuaeiaiiioiooeaeiaeoeaeouuaouueeiieaoaeoaueuaoouoioeiaiuiouaueuaiaoeouoeoooioiuioaeeoea" +
               "aoioeiioiuoaiiuioiiioeuiiaaaieaoaaeoaeieuiiiuieiieaaioaueoiiiuueeiouuueoiiaeuuaeaaiauaeeieoaioiiuueua" +
               "oieieiuiaioeaeuiiaioaieeeaoaieoooiuiaeuuuieeaeeeeuoeueioeiiaaieaiaiiieiouueaouoooueeoiauooeieeoeuouei" +
               "oauieoeuooiiaiueeouiiuuiaiuuouoaaiuiiiouuuaiiiuiiuouiioaoauiaoeiioaooeuoaauaiiieiuueuueioeaioaaieuuoi" +
               "oeaeeeuauouuiaauuiauuuaiiiooaiaeaeeuioaueeaoiaioiieooueaieoeieoiaouuuuioaieauioeuoauauaaeaoueeiaaoooa" +
               "uoioueaieeaaiuuiieieaaaeoiueeoeoeoaaoioaueeoeoiooeiioiaoeieieaeiaaaoeeuoiueaueoeoaueeiioauuuoaiaeaooa" +
               "iaaauuieaioeaaoeioouaiauiaaoieiiieeioeeuaiauuaeeooiuuuaeeieaeieoaaiioaoooeaaeaooouaaoeaoiiuaiauooaiuo" +
               "eauoeiaeaaeueeiaiooaeaoioeuuauaioaiiioioeuuueiuaeoeaiiuaioiueooioeiueaaeueeiauoiaoeooiuaeuoaououiiiau" +
               "uaaeeuaiuueaaoioueouaooaaiieeeiueieeouoieiuoueeueauauoueaooaoiuouuiauaeoiouaoeaauaaaoaaueoaeaoeuaiiia" +
               "ueeiiaaoeuaouiaaiauoeeueueiaooeiooaeuooiieioaaeiueuieuoueiaeiiiaaueaaaoauiauaooaeoeouaaoeeoieuioeuooe" +
               "aeeoioeeoouieiouuooeaioooouoaoeeouueioaeuoeoiioeouoeuiuuaaouaiuaioaiiuiiuuieaoiiieaaeeioeeiuuouioiuoa" +
               "iuuuouoeauuoauoeiuuoiiuauoaeuieaiaaoaoiieoeeiaoaueuuoiaauioueeiueeaouioiiauoeuaooiueaaeuuiiiooioeiuio" +
               "aeuuaouieeiuooaeeaeiiiaiieoaeeoaoioieiuiaeiaiiiouoeoeaeuiuaoeuiiouoaeioiouioiaouiaoooioooieiieaeeaiaa" +
               "iuoaaaaeoauioiouaaaoeiiueaooeieieueaoiuiaiueaaauiuiuooeaaaaeoiooeueiaaueeaeaoouoioouoeouaoaooauieeuuo" +
               "eooaauuoaueoaaauiiueoaauiiaaiaoaiuoeeooiiauaueeuoiuooaiueeeauaoeeaiieeoeaaaoueaeiouaouioauoouaeoiauaa" +
               "uouuuaoeuaaeueeeouoaouueaooiueeauuiiioeaeeieoaoeaooauaiiiueoaiauoueeiooueeiooiaouauiaoooioaaaaoeiaieo" +
               "eaeaeeoaoaeeaeeuuuuioouaioeouuiuouuoeoaeeaaaeeaoooiaeieiuiuauouuieuiauooioiuoeeoieooeeouoiaaoueoaaiai" +
               "uauaauouiauiuoiioiiiauiuooiaooeeiuoeaoaeouuauueiueiuoioeiiaiioueeuiiiueoaieuueaoaiioeeuuauuuiuaueooea" +
               "aeeioieuieuuieaeoeoaaoeaoaoueiiaueuouiuuaauiiiuuoaaouaeioioooieoaioeouiiuoeaiaiiueoauaaiaeaaeouaeoiou" +
               "ieuaiaeuieuuioueiueueuaooiiouaioeuooeuaaoooieuauuaueiieoeiouaoaeuiaoaooeoeiaoieeaiiuaeaeauoaieeoeoeoa" +
               "uiauiaooouioaoiueuiueaueaaaoaouoeauueaieeuaiueiuauiueaoieoaioouiaaeuiiiueuaiuaiaeiaouooeioaoeaoiaieae" +
               "iuouaieeieoaiaaoioaeau", 2169), ]
for test_s, expected_output in test_cases:
    assert longest_beautiful_substring(test_s) == expected_output
