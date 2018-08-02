str = "1234567890abcdefghijklmnop1"
# is it ASCII or Unicode?

def is_unique(string):
    if len(str) > 256:
        return False
    
    lookup_table = {}
    for x in string:
        if x not in lookup_table:
            lookup_table[x] = True
        else:
            return False
    return True

print(is_unique(str))

def is_unique_two(string):
    for x in range(len(string)):
        for y in range(x+1, len(string)):
            if string[x] == string[y]:
                return False
    return True


print(is_unique_two(str))
