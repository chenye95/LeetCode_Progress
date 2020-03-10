"""
Implement pow(x, n), which calculates x raised to the power n (x^n).
"""
def myPow(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    elif n < 0:
        return 1.0 / myPow(x, -n)
    elif n % 2 == 1:
        return x * myPow(x * x, n // 2)
    else:
        return myPow(x * x, n // 2)


assert myPow(x=2.0, n=10) == 1024.0
