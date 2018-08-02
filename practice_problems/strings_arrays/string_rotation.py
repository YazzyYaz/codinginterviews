def is_rotation(s1, s2):
    if len(s1) != len(s2):
        return False
    return is_substring(s1+s1, s2)

def is_substring(s1, s2):

    for x in range(len(s1) - len(s2) - 1):
        is_substring_flag = True
        for y in range(len(s2)):
            if s1[x+y] != s2[y]:
                is_substring_flag = False
                break
        if is_substring_flag:
            return True
    return False

s1 = "waterbottle"
s2 = "erbottlewat"
print(is_rotation(s1, s2))
