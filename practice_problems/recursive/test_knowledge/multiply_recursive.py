def multiply_recursive(n1, n2):
    if n2 == 0:
        return 0
    return n1 + multiply_recursive(n1, n2-1)

n1 = 2
n2 = 5 
print(multiply_recursive(n1, n2))
