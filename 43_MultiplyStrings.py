"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also
 represented as a string.

Note: You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""


def multiply_short_string(num1: str, num2: str) -> str:
    """
    :param num1: string representation of a non-negative integer, 1 <= len(num1) <= 200
    :param num2: string representation of a non-negative integer, 1 <= len(num1) <= 200
    :return: num1 * num2
    """
    int_1, s_2 = (int(num1), num2[::-1]) if len(num1) < len(num2) else (int(num2), num1[::-1])
    if int_1 == 0:
        return "0"

    return_tmp = [0] * len(s_2)
    for i, c_i in enumerate(s_2):
        return_tmp[i] = int_1 * int(c_i)

    return_string = ""
    carry_over = 0
    for tmp_i in return_tmp:
        digit_i = carry_over + tmp_i
        return_string += str(digit_i % 10)
        carry_over = digit_i // 10

    return str(carry_over) + return_string[::-1] if carry_over else return_string[::-1]


def multiply_chr(num1: str, num2: str) -> str:
    """
    :param num1: string representation of a non-negative integer, 1 <= len(num1) <= 200
    :param num2: string representation of a non-negative integer, 1 <= len(num1) <= 200
    :return: num1 * num2
    """
    if num1 == '0' or num2 == '0':
        return "0"

    return_tmp = [0] * (len(num1) + len(num2) - 1)

    for i, c_i in enumerate(num1[::-1]):
        int_i = int(c_i)
        for j, c_j in enumerate(num2[::-1]):
            return_tmp[i + j] += int_i * int(c_j)

    return_string = ""
    carry_over = 0
    for tmp_i in return_tmp:
        digit_i = carry_over + tmp_i
        return_string += str(digit_i % 10)
        carry_over = digit_i // 10

    return str(carry_over) + return_string[::-1] if carry_over else return_string[::-1]


test_cases = [("2", "3", "6"),
              ("123", "456", "56088"),
              ("498828660196", "840477629533", "419254329864656431168468"),
              ("60974249908865105026646412538664653190280198809433017",
               "500238825698990292381312765074025160144624723742",
               "30501687172287445993560048081057096686019986405658336826483685740920318317486606305094807387278589614"),
              ("67671277416626746657687631784163120468201083678333022807",
               "75138261749170153751287529338436149297384291426911342094149902719958688209361264598799405315699784765" +
               "59542476",
               "50847021554312075367065022884158445009446324947347521916908708112113803297824405078597476590575760897" +
               "8384951778534457307060313852727533847814934704264749265993250132"), ]
for multiply in [multiply_chr, multiply_short_string, ]:
    for test_num1, test_num2, expected_output in test_cases:
        assert multiply(test_num1, test_num2) == expected_output, multiply.__name__
