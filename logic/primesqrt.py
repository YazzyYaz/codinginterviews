from math import sqrt


def is_prime_sqrt(n):
    if n < 2:
        return False
    x = sqrt(n)
    for i in range(2, x):
        if x % i == 0:
            return False
    return True
