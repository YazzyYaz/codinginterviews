def string_compression(string):
    if len(string) == 0:
        return None
    string_list = []
    count = 1
    current_letter = string[0]
    for letter in string[1:]:
        print(letter)
        if current_letter == letter:
            count += 1
        else:
            string_list.append(current_letter + str(count))
            count = 1
            current_letter = letter
    string_list.append(current_letter + str(count))
    final_string = "".join(string_list)
    return final_string

string = "aabcccccaaa"
print(string_compression(string))
