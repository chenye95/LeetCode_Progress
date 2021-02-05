"""
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi
function).

The algorithm for myAtoi(string s) is as follows:
- Read in and ignore any leading whitespace.
- Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is
    either. This determines if the final result is negative or positive respectively. Assume the result is positive if
    neither is present.
- Read in next the characters until the next non-digit charcter or the end of the input is reached. The rest of the
    string is ignored.
- Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0.
    Change the sign as necessary (from step 2).
- If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in
    the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should
    be clamped to 231 - 1.
- Return the integer as the final result.
"""


def my_atoi(s: str) -> int:
    i, sign = 0, 1
    return_result = 0

    int_max, int_min = (1 << 31) - 1, -(1 << 31)

    if len(s) == 0:
        return 0

    # Discard white spaces in the beginning
    while i < len(s) and s[i] == ' ':
        i += 1

    # Check if optional sign if it exists
    if i < len(s) and (s[i] == '+' or s[i] == '-'):
        sign = -1 if (s[i] == '-') else 1
        i += 1

    # Build result:
    while i < len(s) and '0' <= s[i] <= '9':
        if return_result > int_max // 10 or (return_result == int_max // 10 and ord(s[i]) - ord('0') > int_max % 10):
            return int_max if sign == 1 else int_min
        return_result = return_result * 10 + ord(s[i]) - ord('0')
        i += 1

    return return_result * sign


assert my_atoi(s="42") == 42
assert my_atoi(s="   -42") == -42
assert my_atoi(s="4193 with words") == 4193
assert my_atoi(s="words and 987") == 0
assert my_atoi(s="-91283472332") == -2147483648
assert my_atoi(s="21474836460") == (1 << 31) - 1
