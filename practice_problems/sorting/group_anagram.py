def group_anagram(alist):
    sorted_pairs = [(s, sorted(s)) for s in alist]
    sorted_pairs.sort(key=lambda s:s[1])
    return [s[0] for s in sorted_pairs]

strings = ["cat", "bat", "rat", "arts", "tab", "tar", "car", "star"]
print(group_anagram(strings))
