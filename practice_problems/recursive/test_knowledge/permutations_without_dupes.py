def permutations(string):
    # Base Case
    if len(string) == 1:
        return [string]
    perm_list = []
    # Iterate Over Characters of String
    for char in string:
        # Build Sublist of All Other Chars Except Current Char
        sublist = [x for x in string if x != char]
        # Recursive Call to get Permutations of Sublist
        z = permutations(sublist)
        for p in z:
            # Append Char not in sublist to each sublist 
            perm_list.append([char] + p)
    return perm_list


astr = "abcd"
print(permutations(astr))
