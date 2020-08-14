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
    :param secret:
    :param guess: of equal length as secret
    :return: %dA%dB
    """
    assert len(secret) == len(guess)
    a = sum(i == j for i, j in zip(secret, guess))
    s, g = Counter(secret), Counter(guess)
    b = sum((s & g).values()) - a
    return '%dA%dB' % (a, b)


assert get_hint(secret="1123", guess="0111") == "1A1B"
assert get_hint(secret="1807", guess="7810") == "1A3B"
