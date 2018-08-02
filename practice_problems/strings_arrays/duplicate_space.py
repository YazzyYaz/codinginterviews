def duplicate_space(alist):
    if not alist:
        return False
    for index, element in enumerate(alist):
        for other_element in alist[index+1:]:
            if element == other_element:
                return True
    return False

alist = [0, 2, 3, 4, 5, 1, 6]
print(duplicate_space(alist))
