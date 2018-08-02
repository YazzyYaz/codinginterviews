def flatten_list(array, result=None):
    if result is None:
        result = []
  
    for element in array:
        print(element)
        if isinstance(element, list):
            flatten_list(element, result)
        else:
            result.append(element)
    return result

print(flatten_list([1, 2, 3, 4, 5, [1, 2], [4, 5]]))
