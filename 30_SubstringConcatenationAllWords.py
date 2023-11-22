"""
You are given a string s and an array of strings words of the same length. Return all starting indices of substring(s)
 in s that is a concatenation of each word in words exactly once, in any order, and without any intervening characters.

You can return the answer in any order.
"""
from collections import Counter, defaultdict, deque
from typing import List


def find_substring_sequential_scan(s: str, words: List[str]) -> List[int]:
    """
    :param s: string to find words in
    :param words: list of words of exact same length
    :return: a list of all starting indices of substrings of length len(word[0]) * len(words) such that each is a
        concatenation of words exactly once, in any order, without any intervening characters
    """
    if not s or not words:
        return []

    word_counter = Counter(words)
    word_len = len(words[0])
    num_word = len(words)
    expected_substring_len = word_len * num_word

    first_letters = {word[0] for word in words}

    return_list = []
    for substring_start in range(len(s) - expected_substring_len + 1):
        if s[substring_start] in first_letters:
            to_be_found = dict(word_counter)
            word_used = 0
            for word_start in range(substring_start, substring_start + expected_substring_len, word_len):
                if s[word_start] not in first_letters:
                    break
                possible_word = s[word_start: word_start + word_len]
                if to_be_found.get(possible_word, 0) > 0:
                    to_be_found[possible_word] -= 1
                    word_used += 1
                else:
                    break

            if word_used == num_word:
                return_list.append(substring_start)

    return return_list


def find_substring_group_scan(s: str, words: List[str]) -> List[int]:
    """
    :param s: string to find words in
    :param words: list of words of exact same length
    :return: a list of all starting indices of substrings of length len(word[0]) * len(words) such that each is a
        concatenation of words exactly once, in any order, without any intervening characters
    """
    if not s or not words:
        return []

    word_counter = Counter(words)
    word_len = len(words[0])
    num_word = len(words)
    expected_substring_len = word_len * num_word
    s_len = len(s)

    return_list = []

    for substring_start_mod in range(word_len):
        scanning_start = scanning_end = substring_start_mod
        word_appearance: dict[str, deque[int]] = defaultdict(deque)
        while scanning_start + expected_substring_len <= s_len:
            # extend out one word
            possible_word = s[scanning_end: scanning_end + word_len]
            scanning_end += word_len

            if possible_word in word_counter:
                word_end_list = word_appearance[possible_word]
                word_end_list.append(scanning_end)
                while word_end_list[0] < scanning_start:
                    # drop all appearances outside of window scanning_start: scanning_start + expected_substring_len
                    word_end_list.popleft()
                while len(word_end_list) > word_counter[possible_word]:
                    # drop additional repetitions of possible_word
                    scanning_start = word_end_list.popleft()

                if scanning_start + expected_substring_len == scanning_end:
                    # since <= word_counter[word] are enforced for all word
                    # this means concatenation of all words according to word_counter
                    return_list.append(scanning_start)
            else:
                # reset scan point to after substring_end
                scanning_start = scanning_end

    return return_list


test_cases = [("barfoothefoobarman", ["foo", "bar"], [0, 9]),
              ("wordgoodgoodgoodbestword", ["word", "good", "best", "word"], []),
              ("barfoofoobarthefoobarman", ["bar", "foo", "the"], [6, 9, 12]),
              ("lingmindraboofooowingdingbarrwingmonkeypoundcake", ["fooo", "barr", "wing", "ding", "wing"], [13]),
              ("cacaabaacccdaadcaabdcddbababbbddcbdcddcbbaacadaadbdcacdaadbbbbad", ["bbd", "dcb", "dcd"], [28]),
              ("pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjgfordrpapjuunmqnxxdrqrfgkr" +
               "sjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwpizlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfio" +
               "kkdprznnnjycttprkxpuykhmpchiksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocd" +
               "hekumttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgbspeotkgvddcwgxidaiq" +
               "cvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvubnhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabej" +
               "ifmxombiamxvauuitoltyymsarqcuuoezcbqpdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvix" +
               "nsqsxacfwndzvrwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhzjokkbctweq" +
               "tigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnhukcbtmxzshoyyufjhzadhrelweszbfgwp" +
               "kzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxyaztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzj" +
               "nilwpoermxrtlfroqoclexxisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzva" +
               "ibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfonmseszhczapxdlauexehha" +
               "ireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqixtzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgc" +
               "dgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdrczxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquh" +
               "lazkjfluxrzopqdstulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnmjzq" +
               "rrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjsfiaharkcqxefghgceeixkdg" +
               "kuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpescpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnaf" +
               "vuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkrzwrpabqrrhnlerxjojemcxel",
               ["dhvf", "sind", "ffsl", "yekr", "zwzq", "kpeo", "cila", "tfty", "modg", "ztjg", "ybty", "heqg", "cpwo",
                "gdcj", "lnle", "sefg", "vimw", "bxcb"], [935]), ]
for find_substring in [find_substring_group_scan, find_substring_sequential_scan, ]:
    for test_s, test_words, expected_list in test_cases:
        assert sorted(find_substring(test_s, test_words)) == expected_list, find_substring.__name__
