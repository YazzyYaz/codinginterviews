from collections import Counter

def one_away(string1, string2):
    len1 = len(string1)
    len2 = len(string2)
    
    if len1 == len2:
        return check_edit(string1, string2)
    elif len1 + 1 == len2:
        return check_insert(string1, string2)
    elif len1 - 1 == len2:
        return check_insert(string2, string1)

def check_edit(string1, string2):
    found_edit = False
    for index in range(len(string1)):
        if string1[index] != string2[index]:
            if found_edit:
                return False
            found_edit = True
    return True

string2 = "adn"
string1 = "an"

def check_insert(string1, string2):
    index1 = 0
    index2 = 0
    while index1 < len(string1) and index2 < len(string2):
        if string1[index1] != string2[index2]:
            if index1 != index2:
                return False
            index2 += 1
        else:
            index1 += 1
            index2 += 1
    return True

print(one_away(string1, string2))






