"""
Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.

You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must
 also not convert the inputs to integers directly.
"""


def add_strings(num1: str, num2: str) -> str:
    """
    :param num1: string representation of a non negative integer 0 <= len(num1) <= 10000
    :param num2: string representation of a non negative integer 0 <= len(num2) <= 10000
    :return: num1 + num2
    """
    if num1 == '0':
        return num2
    if num2 == '0':
        return num1

    return_string = ""
    s1, s2 = (num1[::-1], num2[::-1]) if len(num1) < len(num2) else (num2[::-1], num1[::-1])

    i = 0
    carry_over = 0
    while i < len(s1):
        tmp = int(s1[i]) + int(s2[i]) + carry_over
        return_string += str(tmp % 10)
        carry_over = tmp // 10
        i += 1

    while i < len(s2) and carry_over:
        tmp = int(s2[i]) + carry_over
        return_string += str(tmp % 10)
        carry_over = tmp // 10
        i += 1

    if i < len(s2):
        return_string += s2[i:]
    elif carry_over:
        return_string += str(carry_over)

    return return_string[::-1]


test_cases = [("11", "123", "134"), ("456", "77", "533"), ("0", "0", "0"), ("1", "9", "10"),
              ("67671277416626746657687631784163120468201083678333022807",
               "75138261749170153751287529338436149297384291426911342094149902719958688209361264598799405315699784765" +
               "59542476",
               "75138261749170153751287529338436149297384291426911342770862676886226154786237582440430609997710621548" +
               "92565283"),
              ("401716832807512840963", "167141802233061013023557397451289113296441069",
               "167141802233061013023557799168121920809282032"), ]
for test_num1, test_num2, expected_output in test_cases:
    assert add_strings(test_num1, test_num2) == expected_output
