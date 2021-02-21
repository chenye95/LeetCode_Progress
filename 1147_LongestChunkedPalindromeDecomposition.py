"""
Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

- Each a_i is a non-empty string;
- Their concatenation a_1 + a_2 + ... + a_k is equal to text;
- For all 1 <= i <= k,  a_i = a_{k-i+1}.
"""


def longest_decomposition(text: str) -> int:
    if not text:
        return 0
    elif len(text) <= 1:
        return len(text)
    for i in range(1, len(text) // 2 + 1):
        if text[:i] == text[-i:]:
            return 2 + longest_decomposition(text[i:len(text) - i])
    return 1


test_cases = [("ghiabcdefhelloadamhelloabcdefghi", 7),
              ("merchant", 1),
              ("antaprezatepzapreanta", 11),
              ]
for test_input, expected_output in test_cases:
    assert longest_decomposition(test_input) == expected_output
