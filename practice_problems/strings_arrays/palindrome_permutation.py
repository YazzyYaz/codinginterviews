from collections import Counter

def palindrome_permutation(string):
    string = string.replace(" ", "")
    counter = Counter()
    for letter in string:
        counter[letter] += 1
    
    odd = 0
    for total in counter.values():
        odd += total % 2
        if odd > 1:
            return False
    return True

string = "tact coal"
print(palindrome_permutation(string))
