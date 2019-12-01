from collections import Counter


def getHint(secret: str, guess: str) -> str:
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

assert getHint(secret = "1123", guess = "0111") == "1A1B"
assert getHint(secret = "1807", guess = "7810") == "1A3B"
