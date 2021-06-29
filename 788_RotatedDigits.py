"""
x is a good number if after rotating each digit individually by 180 degrees, we get a valid number that is different
 from x. Each digit must be rotated - we cannot choose to leave it alone.

A number is valid if each digit remains a digit after rotation. 0, 1, and 8 rotate to themselves; 2 and 5 rotate to each
 other (on this case they are rotated in a different direction, in other words 2 or 5 gets mirrored); 6 and 9 rotate to
 each other, and the rest of the numbers do not rotate to any other number and become invalid.

Now given a positive number n, how many numbers x from 1 to n are good?
"""

s1 = {1, 8, 0}
s2 = {1, 8, 0, 6, 9, 2, 5}


def rotated_digits_check(n: int) -> int:
    """
    :param n: 1 <= n <= 10000
    :return: number of 0 <= i <= n such that if digits of i rotated 180 degrees result in a new valid number
    """

    def is_good(x: int) -> bool:
        s = set(map(int, str(x)))
        return s.issubset(s2) and not s.issubset(s1)

    return sum(is_good(i) for i in range(n + 1))


def rotated_digits_construct(n: int) -> int:
    """
    :param n: 1 <= n <= 10000
    :return: number of 0 <= i <= n such that if digits of i rotated 180 degrees result in a new valid number
    """
    count = 0
    n_digit = len(str(n))
    # max digits in each position to ensure less or equal to n
    # confirmed_digits = set()
    confirmed_subset_s1 = True
    # from the most significant to least significant, set the digits
    for i, max_digit_i in enumerate(map(int, str(n))):
        for digit_i in range(max_digit_i):
            if digit_i in s2:
                count += 7 ** (n_digit - i - 1)
            if confirmed_subset_s1 and digit_i in s1:
                count -= 3 ** (n_digit - i - 1)
        if max_digit_i not in s2:
            return count
        # confirmed_digits.add(max_digit_i)
        confirmed_subset_s1 = confirmed_subset_s1 and max_digit_i in s1
    return count if confirmed_subset_s1 else count + 1


test_cases = [(10, 4),
              (50, 16),
              (857, 247),
              (10000, 2320), ]
test_cases.extend(
    [(0, 0), (100, 40), (200, 81), (300, 129), (400, 129), (500, 130), (600, 179), (700, 227), (800, 227), (900, 268),
     (1000, 316), (1100, 356), (1200, 397), (1300, 445), (1400, 445), (1500, 446), (1600, 495), (1700, 543),
     (1800, 543), (1900, 584), (2000, 633), (2100, 682), (2200, 731), (2300, 779), (2400, 779), (2500, 780),
     (2600, 829), (2700, 877), (2800, 878), (2900, 927), (3000, 975), (3100, 975), (3200, 975), (3300, 975),
     (3400, 975), (3500, 975), (3600, 975), (3700, 975), (3800, 975), (3900, 975), (4000, 975), (4100, 975),
     (4200, 975), (4300, 975), (4400, 975), (4500, 975), (4600, 975), (4700, 975), (4800, 975), (4900, 975),
     (5000, 976), (5100, 1025), (5200, 1074), (5300, 1122), (5400, 1122), (5500, 1123), (5600, 1172), (5700, 1220),
     (5800, 1221), (5900, 1270), (6000, 1319), (6100, 1368), (6200, 1417), (6300, 1465), (6400, 1465), (6500, 1466),
     (6600, 1515), (6700, 1563), (6800, 1564), (6900, 1613), (7000, 1661), (7100, 1661), (7200, 1661), (7300, 1661),
     (7400, 1661), (7500, 1661), (7600, 1661), (7700, 1661), (7800, 1661), (7900, 1661), (8000, 1661), (8100, 1701),
     (8200, 1742), (8300, 1790), (8400, 1790), (8500, 1791), (8600, 1840), (8700, 1888), (8800, 1888), (8900, 1929),
     (9000, 1978), (9100, 2027), (9200, 2076), (9300, 2124), (9400, 2124), (9500, 2125), (9600, 2174), (9700, 2222),
     (9800, 2223), (9900, 2272), (10000, 2320), ])
for rotated_digits in [rotated_digits_check, rotated_digits_construct, ]:
    for test_n, expected_value in test_cases:
        assert rotated_digits(test_n) == expected_value, rotated_digits.__name__
