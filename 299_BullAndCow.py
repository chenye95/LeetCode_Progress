"""
You are playing the following Bulls and Cows game with your friend: You write down a number and ask your friend to guess
what the number is. Each time your friend makes a guess, you provide a hint that indicates how many digits in said guess
match your secret number exactly in both digit and position (called "bulls") and how many digits match the secret number
but locate in the wrong position (called "cows"). Your friend will use successive guesses and hints to eventually derive
the secret number.

Write a function to return a hint according to the secret number and friend's guess, use A to indicate the bulls and B
to indicate the cows.

Please note that both secret number and friend's guess may contain duplicate digits.
"""
from collections import Counter


def get_hint(secret: str, guess: str) -> str:
    """
     a hint that indicates how many digits in said guess match your secret number exactly in both digit and position
     (called "bulls") and how many digits match the secret number but locate in the wrong position (called "cows").

     use A to indicate the bulls and B to indicate the cows.

    :param secret: reference string to calculate guess's bulls and cows against
    :param guess: of equal length as secret
    :return: %dA%dB, where A is bull and B is cow
    """
    assert len(secret) == len(guess)
    a = sum(i == j for i, j in zip(secret, guess))
    s, g = Counter(secret), Counter(guess)
    b = sum((s & g).values()) - a
    return '%dA%dB' % (a, b)


test_cases = [("1123", "0111", "1A1B"),
              ("1807", "7810", "1A3B"), ]
for test_secret, test_guess, expected_output in test_cases:
    assert get_hint(secret=test_secret, guess=test_guess) == expected_output
