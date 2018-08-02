from collections import defaultdict


def letter_mover_finder(array):
    hash_table = defaultdict(list)
    for word in array:
        hash_table[word].append(word.lower() + word.lower())
        hash_table[word].append(False)
    
    final_array = []
    for key, value in hash_table.items():
        for index, word in enumerate(array):
            if word.lower() in value[0] and word != key:
                if not value[1]:
                    final_array.append([key, word])
                    value[1] = True
                    hash_table[word][1] = True

    for key, value in hash_table.items():
        if not value[1]:
            final_array.append(key)


array = ['Tokyo', 'London', 'Rome', 'Donlon', 'Kyoto', 'Paris']
print(letter_mover_finder(array))
