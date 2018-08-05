def reverse_string(astr):
    if len(astr) == 1:
        return astr
    return astr[-1] + reverse_string(astr[:-1])

string = "ABCDE"
print(reverse_string(string))
