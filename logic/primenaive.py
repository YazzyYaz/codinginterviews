def is_prime_naive(x):
    if x < 2:
        return False
    for i in range(2, x - 1):
        if x % i == 0:
            return False
    return True
