from string import ascii_uppercase


def excel_column_count(column):
    alphabet_list = list(ascii_uppercase)
    alphabet_lookup = {item:index+1 for index, item in enumerate(alphabet_list)}
    column_number = []
    column_list = list(reversed([x for x in column]))
        
    for index, char in enumerate(column_list):
        number = (26 ** index) * alphabet_lookup[char]
        column_number.append(number)
        
    return sum(column_number)

print(excel_column_count("AZ"))
