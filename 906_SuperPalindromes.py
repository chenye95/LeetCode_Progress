"""
Let's say a positive integer is a super-palindrome if it is a palindrome, and it is also the square of a palindrome.

Given two positive integers left and right represented as strings, return the number of super-palindromes integers in
 the inclusive range [left, right].
"""


def super_palindrome_in_range_count(left: str, right: str):
    """
    :param left: string representation of an integer 1 <= l <= 10**18, l <= right
    :param right: string representation of an integer 1 <= l <= 10**18, l <= right
    :return: number of super palindrome, which is palindrome and is also the square of a palindrome,
        in range [left, right]
    """

    def is_palindrome(x: int) -> bool:
        """
        :param x: a non-negative integer x >= 0
        :return: whether x is a palindrome
        """
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //= 10

        return x == reversed_half or x == reversed_half // 10

    left_bound, right_bound = int(left), int(right)

    # palindrome image of a five digit number is 10 digits
    # square of a 10 digits integer is 20 digits > 10**18
    # search_upper_bound = 10 ** (18 // 4 + 1)
    search_upper_bound = 100000
    super_palindrome_count = 0

    # create the palindrome

    # Even length "12344321"
    for k in range(search_upper_bound):
        s = str(k)
        base_palindrome = s + s[::-1]
        base_squared = int(base_palindrome) ** 2
        if base_squared > right_bound:
            break
        if base_squared >= left_bound and is_palindrome(base_squared):
            super_palindrome_count += 1

    # Odd length "1234321"
    for k in range(search_upper_bound):
        s = str(k)
        base_palindrome = s + s[-2::-1]
        base_squared = int(base_palindrome) ** 2
        if base_squared > right_bound:
            break
        if base_squared >= left_bound and is_palindrome(base_squared):
            super_palindrome_count += 1

    return super_palindrome_count


def super_palindrome_in_range_pre_compute(left: str, right: str):
    """
    :param left: string representation of an integer 1 <= l <= 10**18, l <= right
    :param right: string representation of an integer 1 <= l <= 10**18, l <= right
    :return: number of super palindrome, which is palindrome and is also the square of a palindrome,
        in range [left, right]
    """
    satisfied_list = [1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001,
                      102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001,
                      10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001,
                      1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121,
                      1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001,
                      102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321,
                      123456787654321, 400000080000004, 10000000200000001, 10002000300020001, 10004000600040001,
                      10020210401202001, 10022212521222001, 10024214841242001, 10201020402010201, 10203040504030201,
                      10205060806050201, 10221432623412201, 10223454745432201, 12100002420000121, 12102202520220121,
                      12104402820440121, 12122232623222121, 12124434743442121, 12321024642012321, 12323244744232321,
                      12343456865434321, 12345678987654321, 40000000800000004, 40004000900040004]

    super_palindrome_count = 0
    left_bound, right_bound = int(left), int(right)
    for num_i in satisfied_list:
        if left_bound <= num_i <= right_bound:
            super_palindrome_count += 1
        elif num_i > right_bound:
            break

    return super_palindrome_count


test_cases = [("1", "213", 4),
              ('4', '1000', 4),
              ('1', '2', 1),
              ("40000000000000000", "50000000000000000", 2)]
for super_palindrome_in_range in [super_palindrome_in_range_pre_compute, super_palindrome_in_range_count, ]:
    for test_l, test_r, expected_count in test_cases:
        assert super_palindrome_in_range(test_l, test_r) == expected_count, super_palindrome_in_range.__name__
