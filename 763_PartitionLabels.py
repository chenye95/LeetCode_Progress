"""
A string S of lowercase English letters is given. We want to partition this string into as many parts as possible so
that each letter appears in at most one part, and return a list of integers representing the size of these parts.
"""
from typing import List


def partition_labels(s: str) -> List[int]:
    """
    Greedy Algorithm

    :param s: partition s into as many parts as possible so that each letter appears in at most one part
    :return: a list of integers representing the size of these parts
    """
    # index of last appearance for each character
    last_appears = {c: i for i, c in enumerate(s)}

    # Greedily look for boundaries of current partition
    current_end = current_start = 0
    partition_len = []
    for i, c in enumerate(s):
        # Scan for new characters that will extend out current_end
        current_end = max(current_end, last_appears[c])
        if i == current_end:
            partition_len.append(i - current_start + 1)
            current_start = i + 1
    return partition_len


test_cases = [("ntswuqqbidunnixxpoxxuuupotaatwdainsotwvpxpsdvdbwvbtdiptwtxnnbtqbdvnbowqitudutpsxsbbsvtipibqpvpnivott" +
               "sxvoqqaqdxiviidivndvdtbvadnxboiqivpusuxaaqnqaobutdbpiosuitdnopoboivopaapadvqwwnnwvxndpxbapixaspwxxxvp" +
               "poptqxitsvaaawxwaxtbxuixsoxoqdtopqqivaitnpvutzchkygjjgjkcfzjzrkmyerhgkglcyffezmehjcllmlrjghhfkfylkgyh" +
               "yjfmljkzglkklykrjgrmzjyeyzrrkymccefggczrjflykclfhrjjckjlmglrmgfzlkkhffkjrkyfhegyykrzgjzcgjhkzzmzyejyc" +
               "frkkekmhzjgggrmchkeclljlyhjkchmhjlehhejjyccyegzrcrerfzczfelzrlfylzleefgefgmzzlggmejjjygehmrczmkrc",
               [246, 254]),
              ("jybmxfgseq", [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]),
              ("eeeeeeeeeeeeeeeeeeelllllllllllllllllllllllllllllllllllluuuuuuuuuuuuuuuuuuuuuuuuuuuuuddddddddddddddddd" +
               "ddddddddddddddzzzzzzzzzzzzzzzzzzzzbbbbbbbbbbbbbbbbbbbbgggggggggggggggggggggggggggjjjjjjjjjjjjjjjjjjjj" +
               "ppppppppppppppppppppppppxrxrrrxrxrrxrxrxrrxrrfffffffffffffffffffffffffffffkkkkkkkkkkkkkkkkkkkkwwwwwww" +
               "wwwwwwwwwwwwwwwwwwwwwwwwwccccccccccccccccccccccccccccmmmmmmmmmmmmmmmmmmmmmvhhhhvhvvvvhvvvhhvvvvhvhnnn" +
               "nnnnnnnnnnnnnniiiiiiiiiiiiiiiiiiiiiioqqqtqtqtqoooottooqoottqtqqtosassyyyyysaaayyaysayaasayysssaa",
               [19, 36, 29, 31, 20, 20, 27, 20, 24, 21, 29, 20, 32, 28, 21, 24, 17, 22, 29, 31]),
              ("ababcbacadefegdehijhklij", [9, 7, 8]), ]
for test_s, expected_output in test_cases:
    assert partition_labels(test_s) == expected_output
