"""
You are given a very large integer n, represented as a string, and an integer digit x. The digits in n and the digit x
 are in the inclusive range [1, 9], and n may represent a negative number.

You want to maximize n's numerical value by inserting x anywhere in the decimal representation of n. You cannot insert x
 to the left of the negative sign.
- For example, if n = 73 and x = 6, it would be best to insert it between 7 and 3, making n = 763.
- If n = -55 and x = 2, it would be best to insert it before the first 5, making n = -255.

Return a string representing the maximum value of n after the insertion.
"""


def max_value(n: str, x: int) -> str:
    """
    :param n: n represents a valid number: 1 <= len(n) <= 10**5, with '1' <= n[i] <= '9' and n[0] can be '-'
    :param x: 1 <= x <= 9
    :return: max value of string after inserting x into n
    """
    x = str(x)
    if n[0] == '-':
        i = 1
        while i < len(n) and n[i] <= x:
            i += 1
    else:
        i = 0
        while i < len(n) and n[i] >= x:
            i += 1
    return n[:i] + x + n[i:]


test_cases = [("-132", 3, "-1323"),
              ("-13", 2, "-123"),
              ("-39", 2, "-239"),
              ("-2", 3, "-23"),
              ("99", 9, '999'),
              ("98", 9, '998'),
              ("3", 9, "93"),
              ("61243714257379169578189224174597565854956217769712535413891459155311711332696691485529233233384138955" +
               "95486664258262356854846837473696538775345748614393198324247733563984173557715769136885364313232315888" +
               "2323131175542535363673585", 2,
               "62124371425737916957818922417459756585495621776971253541389145915531171133269669148552923323338413895" +
               "59548666425826235685484683747369653877534574861439319832424773356398417355771576913688536431323231588" +
               "82323131175542535363673585"),
              ]
for test_n, test_x, expected_value in test_cases:
    assert max_value(test_n, test_x) == expected_value
