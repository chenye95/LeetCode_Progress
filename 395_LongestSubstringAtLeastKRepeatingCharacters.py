"""
Given a string s and an integer k, return the length of the longest substring of s such that the frequency of each
 character in this substring is greater than or equal to k.
"""


def longest_substring_search(s: str, k: int) -> int:
    """
    :param s: 1 <= len(s) <= 10_000, of lower case English letters only
    :param k: 1 <= k <= 100_000
    :return: longest substring of s where each character appears at least k times
    """
    a_ord = ord('a')

    def longest_substring_in_between(start: int, end: int) -> int:
        """
        :return: length of longest substring within s[start: end] that satisfies the condition
        """
        if end - start < k:
            return 0

        substring_count = [0] * 26
        seen_count = [0] * 26
        for c_i in s[start: end]:
            substring_count[ord(c_i) - a_ord] += 1

        mid_point = start
        while mid_point < end:
            c_mid_point = ord(s[mid_point]) - a_ord
            if substring_count[c_mid_point] + seen_count[c_mid_point] >= k:
                substring_count[c_mid_point] -= 1
                seen_count[c_mid_point] += 1
                mid_point += 1
            else:
                break

        if mid_point < end:
            # s[mid_point] appears less than k times
            # break into s[start: mid_point] and s[mid_next: end] to search
            # mid_next is the first character after s[mid_point] that appears at least k times
            mid_next = mid_point + 1
            while mid_next < end - k + 1 and substring_count[ord(s[mid_next]) - a_ord] < k:
                substring_count[ord(s[mid_next]) - a_ord] -= 1
                mid_next += 1

            return max(longest_substring_in_between(start, mid_point),
                       longest_substring_in_between(mid_next, end))

        # all characters in s[start: end] appear at least k times
        return end - start

    return longest_substring_in_between(0, len(s))


def longest_substring_sliding_window(s: str, k: int) -> int:
    """
    :param s: 1 <= len(s) <= 10_000, of lower case English letters only
    :param k: 1 <= k <= 100_000
    :return: longest substring of s where each character appears at least k times
    """
    a_ord = ord('a')

    def unique_characters_in_s() -> int:
        """
        :return: number of unique characters in s
        """
        found_in_s = [False] * 26
        unique_count = 0
        for c_i in s:
            if not found_in_s[ord(c_i) - a_ord]:
                found_in_s[ord(c_i) - a_ord] = True
                unique_count += 1
        return unique_count

    max_unique_chr = unique_characters_in_s()
    max_substring = 0

    for unique_chr_in_substring in range(1, max_unique_chr + 1):
        # searching for substring with unique_chr_in_substring unique characters
        substring_count = [0] * 26
        window_start = window_end = 0
        unique_count = count_at_least_k = 0

        while window_end < len(s):
            if unique_count <= unique_chr_in_substring:
                # Expand sliding window
                ord_c = ord(s[window_end]) - a_ord
                if substring_count[ord_c] == 0:
                    unique_count += 1
                substring_count[ord_c] += 1
                if substring_count[ord_c] == k:
                    count_at_least_k += 1
                window_end += 1
            else:
                # Shrink sliding window
                ord_c = ord(s[window_start]) - a_ord
                if substring_count[ord_c] == k:
                    count_at_least_k -= 1
                substring_count[ord_c] -= 1
                if substring_count[ord_c] == 0:
                    unique_count -= 1
                window_start += 1

            if unique_count == unique_chr_in_substring and unique_count == count_at_least_k and \
                    window_end - window_start > max_substring:
                max_substring = window_end - window_start

    return max_substring


test_cases = [("aaabb", 3, 3),
              ("aaabbb", 3, 6),
              ("ababbc", 2, 5),
              ("zzzzzzzzzzaaaaaaaaabbbbbbbbhbhbhbhbhbhbhicbcbcibcbccccccccccbbbbbbbbaaaaaaaaafffaahhhhhiaahiiiiiiiiif" +
               "eeeeeeeeee", 10, 21),
              ("hadccccccddddcccccddddddccccccccdddddddeeffgglhkj", 7, 37),
              ("bababababababababababababababababaabababababaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbbbbbbbbbbb" +
               "bbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbb" +
               "bbbbbbbbbbbbbbcbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa" +
               "aa", 30, 216), ]
for longest_substring in [longest_substring_search, longest_substring_sliding_window, ]:
    for test_s, test_k, expected_output in test_cases:
        assert longest_substring(test_s, test_k) == expected_output, longest_substring.__name__
