"""
Given a string s, remove duplicate letters so that every letter appears once and only once. You must make sure your
 result is the smallest in lexicographical order among all possible results.
"""


def remove_duplicate_letters(s: str) -> str:
    """
    :param s: 1 <= len(s) <= 10000, of lowercase English letters only
    :return: smallest in lexicographical order among substrings with every letter appears once and only once
    """
    last_seen = {c: i for i, c in enumerate(s)}
    return_list = ['!']
    for i, c in enumerate(s):
        if c not in return_list:
            while c < return_list[-1] and i < last_seen[return_list[-1]]:
                # return_list[-1] will appear again
                return_list.pop()
            return_list.append(c)
    return ''.join(return_list[1:])


test_cases = [("bcabc", "abc"),
              ("cbacdcbc", "acdb"),
              ("", ""),
              ("yiklorymxepctlnomfmymitulgfuudxturmemjxxlloevwyfriazwyckgbfogfrppnsomjfhoobirytzzksemgrcbcegbbhaurrrl" +
               "yxquuoivdcykcpnntgrktwtmgstjrvsvajfukhxwgvsvgzwoatnnzszksxstzkojmyuriyriyqkaqghoxilykyxepnsjeybgxxwyy" +
               "ornzxzttsylsoqlumzwlsdxvzgjfpwwoejsieeyoremvqfyekmxdsabogijmqxdruiydlkrvobwqmlmahmfpwbopbdxhinowqavda" +
               "snkeagpjvznzfmlllydgosztljnkrkpjhsqtjxjumzasfitacjqenwcskkkifgzatcevfwererjjabmmmdsnuacxzrgjyytbmxcca" +
               "gjbemkmemjpaqwpjdsunvmfuromfhmumhlzycbhptfjuodlgjxuxcggtotaxjlqbccghyplvtgrwwlhmriwnecdhjmbpzdaqgpyhi" +
               "nawvmxjyiptiroxtuwybcjjkqcirscdqbakpwdiabgirknpvlwmvspufpdqchvbqbspyznfuscidqcbtcvwsqgjjdfpnuhgpxkgik" +
               "vagtbhnssycxpefsqxbcgtubdmtcojbzpcjvfoslunoiixxdakfczg",
               "abcdefghijklmnoprqstvwuxyz"),
              ]
for test_s, expected_s in test_cases:
    assert remove_duplicate_letters(test_s) == expected_s
