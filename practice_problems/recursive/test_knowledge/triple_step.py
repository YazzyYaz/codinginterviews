def count_step(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_step(n - 1) + count_step(n - 2) + count_step(n - 3)


n = 10
print(count_step(n))
