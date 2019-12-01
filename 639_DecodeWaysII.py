"""
639. Decode Ways II
A message containing letters from A-Z is being encoded to numbers using the following mapping way:
    A -> 1
    B -> 2
    ...
    Z -> 26
Beyond that, now the encoded string can also contain the character '*', which can be treated as one of the numbers from
1 to 9.
Given the encoded message containing digits and the character '*', return the total number of ways to decode it.
Also, since the answer may be very large, you should return the output mod 10^9 + 7.

"""

def numDecodings(s: str) -> int:
    M = 10**9 + 7
    ways = [0] * (len(s) + 1)
    ways[0] = 1
    for i in range(len(s)):
        point_i = i + 1
        if s[i] == '*':
            ways[point_i] = 9 * ways[point_i-1]
            if i > 0 and (s[i-1] == '1' or s[i-1] == '*'):  # 11-19 as * can be 1-9
                ways[point_i] = (ways[point_i] + 9 * ways[point_i-2]) % M
            if i > 0 and (s[i-1] == '2' or s[i-1] == '*'):  # 21-26
                ways[point_i] = (ways[point_i] + 6 * ways[point_i-2]) % M
        else:
            ways[point_i] = ways[point_i-1] if s[i] != '0' else 0
            if i > 0 and s[i-1] == '1':  #1x
                ways[point_i] = (ways[point_i] + ways[point_i-2]) % M
            elif i > 0 and s[i-1] == '2' and s[i] <= '6':  #2x for 1 <= x <= 6
                ways[point_i] = (ways[point_i] + ways[point_i-2]) % M
            elif i > 0 and s[i-1] == '*':
                ways[point_i] = (ways[point_i] + 2 * ways[point_i-2]) % M if s[i] <= '6' \
                    else (ways[point_i] + ways[point_i-2]) % M
    return ways[-1]





assert(numDecodings("*") == 9)
assert(numDecodings("2*9") == 16)
assert(numDecodings("1*") == 18)


