"""
A sentence S is given, composed of words separated by spaces. Each word consists of lowercase and uppercase letters only

We would like to convert the sentence to "Goat Latin" (a made-up language similar to Pig Latin.)

The rules of Goat Latin are as follows:

- If a word begins with a vowel (a, e, i, o, or u), append "ma" to the end of the word. For example, the word 'apple'
becomes 'applema'.

- If a word begins with a consonant (i.e. not a vowel), remove the first letter and append it to the end, then add "ma".
For example, the word "goat" becomes "oatgma".

- Add one letter 'a' to the end of each word per its word index in the sentence, starting with 1. For example, the first
 word gets "a" added to the end, the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin.
"""


def to_goat_latin(s: str) -> str:
    words = s.split()
    goat_latin_words = [''] * len(words)
    for i, word_i in enumerate(words):
        if word_i[0].lower() in ('a', 'e', 'i', 'o', 'u'):
            goat_latin_words[i] = word_i + 'ma' + 'a' * (i + 1)
        else:
            goat_latin_words[i] = word_i[1:] + word_i[0] + 'ma' + 'a' * (i + 1)
    return ' '.join(goat_latin_words)


test_cases = [
    ("I speak Goat Latin", "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"),
    ("The quick brown fox jumped over the lazy dog",
     "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa")
]
for test_input, test_output in test_cases:
    assert to_goat_latin(test_input) == test_output
