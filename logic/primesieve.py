def is_prime_sieve(limit):
    a = [True] * limit
    a[0] = a[1] = False
    for (index, isprime) in enumerate(a):
        if isprime:
            yield index
            for n in range(index*index, limit, index):
                a[n] = False
