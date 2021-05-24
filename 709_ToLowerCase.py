"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""


def to_lower_case_list(input_str: str) -> str:
    """
    :param input_str: a string of all kinds of character
    :return: return the same string in lowercase wherever there is an uppercase english letter
    """
    steps = ord('a') - ord('A')
    return ''.join([chr(ord(c) + steps) if 'A' <= c <= 'Z' else c for c in input_str])


def to_lower_case_str(input_str: str) -> str:
    """
    :param input_str: a string of all kinds of character
    :return: return the same string in lowercase wherever there is an uppercase english letter
    """
    steps = ord('a') - ord('A')
    return_str = ""
    for c in input_str:
        if 'A' <= c <= 'Z':
            return_str += chr(ord(c) + steps)
        else:
            return_str += c

    return return_str


test_cases = [("here", "here"),
              ("Hello", "hello"),
              ("LOVELY", "lovely"),
              ("loWERcAse", "lowercase"),
              ("Mymommaalwayssaid,\"Lifewaslikeaboxofchocolates.Youneverknowwhatyou'regonnaget.",
               "mymommaalwayssaid,\"lifewaslikeaboxofchocolates.youneverknowwhatyou'regonnaget."), ]
for to_lower_case in [to_lower_case_list, to_lower_case_str, ]:
    for test_input, expected_output in test_cases:
        assert test_input.lower() == expected_output
        assert to_lower_case(test_input) == expected_output
