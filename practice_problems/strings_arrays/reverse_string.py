def reverse_string(string):
    string_list = [x for x in string]
    reversed_string_list = reversed(string_list)
    reversed_string = "".join(reversed_string_list)
    return reversed_string

string = "hello"
print(reverse_string(string))
