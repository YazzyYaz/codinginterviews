def recursive_palindrome(astr):
    if len(astr) == 1:
        return True
    return astr[0] == astr[-1] and recursive_palindrome(astr[1:-1])

astr = "kayak"
astr2 = "radar"
astr3 = "fdssss"
print(recursive_palindrome(astr))
print(recursive_palindrome(astr2))
print(recursive_palindrome(astr3))
