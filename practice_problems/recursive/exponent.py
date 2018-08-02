def exponent(x, n):
    if n == 0:
        return x
    else:
        return x * exponent(x, n - 1)

x = exponent(2,16)
print(x)
