def string_permutation(string1, string2):
    lookup_table = {}
    lookup_table2 = {}
    for x in string1:
        if x not in lookup_table:
            lookup_table[x] = 1
        else:
            lookup_table[x] += 1

    for y in string2:
        if y not in lookup_table2:
            lookup_table2[y] = 1
        else:
            lookup_table2[y] += 1
    return lookup_table2 == lookup_table

string1 = "1234560"
string2 = "6543210"
print(string_permutation(string1, string2))

def string_permutation2(string1, string2):
    sorted_string1 = "".join(sorted(string1))
    sorted_string2 = "".join(sorted(string2))
    return sorted_string1 == sorted_string2

print(string_permutation2(string1, string2))
