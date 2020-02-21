"""
Return the largest possible k such that there exists a_1, a_2, ..., a_k such that:

- Each a_i is a non-empty string;
- Their concatenation a_1 + a_2 + ... + a_k is equal to text;
- For all 1 <= i <= k,  a_i = a_{k+1 - i}.
"""
def longestDecomposition(text: str) -> int:
    if not text:
        return 0
    for l in range(1, len(text) // 2 + 1):
        if text[:l] == text[-l:]:
            return 2 + longestDecomposition(text[l:len(text)-l])


test_cases = [("ghiabcdefhelloadamhelloabcdefghi", 7),
              ("merchant", 1),
              ("antaprezatepzapreanta", 11),
              ]