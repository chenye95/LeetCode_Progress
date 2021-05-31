"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""


def is_palindrome(s: str) -> bool:
    """
    :return: whether the alphanumeric characters of s make a valid palindrome
    """
    alpha_numeric_s = ''.join(c for c in s if c.isalpha() or c.isdigit()).lower()
    return alpha_numeric_s == alpha_numeric_s[::-1]


test_cases = [("0P", False),
              ("A man, a plan, a canal: Panama", True),
              ("race a car", False),
              ("Ud L?dPze8Z6?INK:2:V9jwp.;.;?nO?!9XqKiesU:7Y ;,82c:6w!YMn,\",? ,`!;E:b!lF!8,5kAtx;`qoH,aK?8K:gGT2Q!C8" +
               "26:ODM;qJs'sJq;MDO:628C!Q2TGg:K8?Ka,Hoq`;xtAk5,8!Fl!b:E;!`, ?,\",nMY!w6:c28,; Y7:UseiKqX9!'On';.;.pwj" +
               "9V:2:KNI?6Z8ezPd?L dU", True),
              ("QZrD2 7UL91z,i`O2ef:6e'2\"yP !:,U.:pX90PU3CXo'i!;3 `j 0?\"'hK8 ? BAjM2\"DBw?7!4R3?U2E8F2y!?3 R2!fw 6e" +
               "!:0  ErCi98KM`,8`8648,mi3P0`,!5 E.?00J3A 52\"x8,tHy!'2!DLBbK'j!tt1C' 7`JPulW\"\"uRTbr\"',\",U`ZOW5'\"" +
               "LMDQDMJ\"'5WOZ`U,\",'\"rbTRu\"\"WluPJ`7 'C1tt!j'KbBJD!2'!yHt,8x\"25 A3J00?.E 5!,`0P3im,8468`8,`MK89iC" +
               "rE  0:!e6 wf!2R 3?!y2F8E2U?3R4!7?wBD\"2MjAB ? 8Kh'\"?0 j` 3;!i'oXC3UP09Xp:.U,:! Py\"2'e6:fe2O`i,z19LU" +
               "7 2DrZQ", False), ]
for test_s, expected_output in test_cases:
    assert is_palindrome(s=test_s) is expected_output
