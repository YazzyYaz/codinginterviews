def count_coins(n):
    if n == 0:
        return 1
    elif n < 0:
        return 0
    else:
        return count_coins(n-25) + count_coins(n-10) + count_coins(n-5)

n = 30 
print(count_coins(n))
