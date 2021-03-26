"""
We are given two arrays A and B of words.  Each word is a string of lowercase letters.

Now, say that word b is a subset of word a if every letter in b occurs in a, including multiplicity.  For example,
"wrr" is a subset of "warrior", but is not a subset of "world".

Now say a word a from A is universal if for every b in B, b is a subset of a.

Return a list of all universal words in A.  You can return the words in any order
"""
from collections import Counter
from typing import List


def word_subset_counter(a: List[str], b: List[str]) -> List[str]:
    b_requirement = Counter()
    for word_b in b:
        b_requirement |= Counter(word_b)
    list_b = [b_requirement[b_c] for b_c in b_requirement]

    return_list = []
    for word_a in a:
        counter_a = Counter(word_a)
        list_a = [counter_a[b_c] for b_c in b_requirement]
        if all(x >= y for x, y in zip(list_a, list_b)):
            return_list.append(word_a)

    return return_list


def word_subset_list(a: List[str], b: List[str]) -> List[str]:
    def count_word(word: str) -> List[int]:
        word_count = [0] * 26
        for letter in word:
            word_count[ord(letter) - ord('a')] += 1
        return word_count

    b_requirement = [0] * 26
    for word_b in b:
        for i, b_word_i in enumerate(count_word(word_b)):
            b_requirement[i] = max(b_requirement[i], b_word_i)

    return_list = []
    for word_a in a:
        if all(x >= y for x, y in zip(count_word(word_a), b_requirement)):
            return_list.append(word_a)

    return return_list


test_cases = [(["amazon", "apple", "facebook", "google", "leetcode"], ["e", "o"], {"facebook", "google", "leetcode"}),
              (["amazon", "apple", "facebook", "google", "leetcode"], ["l", "e"], {"apple", "google", "leetcode"}),
              (["amazon", "apple", "facebook", "google", "leetcode"], ["e", "oo"], {"facebook", "google"}),
              (["amazon", "apple", "facebook", "google", "leetcode"], ["lo", "eo"], {"google", "leetcode"}),
              (["amazon", "apple", "facebook", "google", "leetcode"], ["ec", "oc", "ceo"], {"facebook", "leetcode"}),
              (["faaapumkvq", "amdkqpfijv", "qpafqvfkpm", "mqfckamqvp", "fwapsmokvq", "bkfzqamvzp", "qckmpfsfva",
                "zbmnfykeyw", "pjvmqekfpa", "pqekvfmlac", "nkvamfpsqc", "vafqppqmkh", "qhpfmkbvas", "mvapkbnqaf",
                "vpiqmfzjak", "hunjgeaolc", "avkdqlpmft", "avskfpmmlq", "aecglrhxsg", "aapmqkfvlf", "mfpakqavap",
                "kavfwqepdm", "mytxzbmqma", "ozvmspkfaq", "zafjmpkqpv", "pjmqavfkjf", "scvakpcfmq", "vpjmfawqke",
                "nfzkpmvaaq", "afqmekopva", "vpmvpafkqy", "xfupkvmqad", "aggvkpmbfq", "cmpqvxatfk", "qkmfpvnamq",
                "utlusqhbfy", "oppjejmmcy", "wndhvprmoz", "kxpsawmvqf", "pxsvamnkqf", "vfmqlkplah", "avppfkqudm",
                "ksyvfpaqgm", "fmkhfpdqva", "pqlrvxamfk", "dfqvimjkap", "qpvmfwakxb", "rrkfcvqapm", "vhqrakfvmp",
                "msqhkfapvw", "qpfmktpmav", "okzckhugsd", "fpxkqdmagv", "aqpykvofqm", "avaqzpfkwm", "kvfpamvqzx",
                "pqfkmvacgm", "qvmgftkupa", "kelxxnfiei", "fkpakvqmau", "qkxxamvpfa", "kqqmcmfpav", "mqafvubkvp",
                "fcikmvxapq", "kpnfarmvqs", "vpmakfnpiq", "avkfwmspqk", "pmnfkwvqak", "avlfkqpvkm", "pymkvfqjpa",
                "qmfkaxpfrv", "qkkvffapwm", "fcwenlxtla", "qhpkvfmyaj", "fajhfkpqvm", "smvkpsaqzf", "fpthakqmxv",
                "tmqfawkjvp", "vkyaytqpmf", "apmtsqvwfk", "nujagbkcqj", "qwpfkamvpf", "mlvqkmpfal", "dduzzxmskv",
                "kjkggnwvar", "kqsvpamwxf", "apqfwekmmv", "mvbfpikeqa", "qviknmaifp", "sokvapfqbm", "mvpqaxfqfk",
                "klfvlqmppa", "azqkixfpvm", "gtframkvqp", "wkspfmavkq", "mpafjcvykq", "rmpxfqkiav", "gyaifdnbli",
                "wwnzulopnh", "vpafvcmkaq"],
               ["v", "vm", "vma", "vkq", "av", "vapmq", "fmqk", "qam", "k", "kqmvf", "aqpfkv", "kmqpfa", "fva", "mqfa",
                "vamkfq", "pa", "qpk", "qfka", "qa", "f", "pmq", "qmk", "mk", "fpamkv", "vk", "vpkm", "mva", "v",
                "kvaf", "aqvkmf", "qm", "v", "vapmf", "fvk", "mp", "avkmqf", "maf", "kfvqm", "k", "kaq", "a", "vk",
                "mafp", "k", "kpa", "pfqvm", "aq", "fa", "pqfkav", "p", "kvfpm", "q", "kfmqp", "a", "pvk", "q",
                "pfkvqa", "vkfamq", "vkfmpq", "afk", "p", "kvpam", "vkpaq", "vkqfap", "qk", "q", "qk", "vkamp", "ma",
                "v", "qvapmk", "vmqafk", "afqpv", "kavfmq", "f", "pvma", "paqvmk", "v", "amqkv", "mkpfv", "pkmv",
                "mkqvpf", "q", "vm", "v", "mfav", "fm", "f", "pmfvq", "qk", "fpqmk", "pamfv", "fv", "pv", "apfmvq",
                "qv", "v", "kvm", "pvmaq", "fvp"],
               {'faaapumkvq', 'amdkqpfijv', 'qpafqvfkpm', 'mqfckamqvp', 'fwapsmokvq', 'bkfzqamvzp', 'qckmpfsfva',
                'pjvmqekfpa', 'pqekvfmlac', 'nkvamfpsqc', 'vafqppqmkh', 'qhpfmkbvas', 'mvapkbnqaf', 'vpiqmfzjak',
                'avkdqlpmft', 'avskfpmmlq', 'aapmqkfvlf', 'mfpakqavap', 'kavfwqepdm', 'ozvmspkfaq', 'zafjmpkqpv',
                'pjmqavfkjf', 'scvakpcfmq', 'vpjmfawqke', 'nfzkpmvaaq', 'afqmekopva', 'vpmvpafkqy', 'xfupkvmqad',
                'aggvkpmbfq', 'cmpqvxatfk', 'qkmfpvnamq', 'kxpsawmvqf', 'pxsvamnkqf', 'vfmqlkplah', 'avppfkqudm',
                'ksyvfpaqgm', 'fmkhfpdqva', 'pqlrvxamfk', 'dfqvimjkap', 'qpvmfwakxb', 'rrkfcvqapm', 'vhqrakfvmp',
                'msqhkfapvw', 'qpfmktpmav', 'fpxkqdmagv', 'aqpykvofqm', 'avaqzpfkwm', 'kvfpamvqzx', 'pqfkmvacgm',
                'qvmgftkupa', 'fkpakvqmau', 'qkxxamvpfa', 'kqqmcmfpav', 'mqafvubkvp', 'fcikmvxapq', 'kpnfarmvqs',
                'vpmakfnpiq', 'avkfwmspqk', 'pmnfkwvqak', 'avlfkqpvkm', 'pymkvfqjpa', 'qmfkaxpfrv', 'qkkvffapwm',
                'qhpkvfmyaj', 'fajhfkpqvm', 'smvkpsaqzf', 'fpthakqmxv', 'tmqfawkjvp', 'vkyaytqpmf', 'apmtsqvwfk',
                'qwpfkamvpf', 'mlvqkmpfal', 'kqsvpamwxf', 'apqfwekmmv', 'mvbfpikeqa', 'qviknmaifp', 'sokvapfqbm',
                'mvpqaxfqfk', 'klfvlqmppa', 'azqkixfpvm', 'gtframkvqp', 'wkspfmavkq', 'mpafjcvykq', 'rmpxfqkiav',
                'vpafvcmkaq'}),
              ]
for word_subset in [word_subset_counter, word_subset_list]:
    for test_a, test_b, expected_output in test_cases:
        assert set(word_subset(test_a, test_b)) == expected_output
