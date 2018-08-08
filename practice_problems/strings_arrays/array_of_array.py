def product_left_recursive(alist, result=None):
    if alist == []:
        return result 
    g = result[-1] * alist[0]
    result.append(g)
    return product_left_recursive(alist[1:], result)

def product_left(alist):
    new_list = [1]
    for index in range(1, len(alist)):
        value = new_list[-1] * alist[index-1]
        new_list.append(value)
    return new_list

def product_right(alist):
    new_list = [1]
    for index in range(len(alist)-2, -1, -1):
        value = new_list[-1] * alist[index-1]
        new_list.append(value)
    return new_list

def product_of_array_of_array(alist):
    left_list = product_left(alist)
    right_list = product_right(alist)
    new_list = []
    for index, item in enumerate(alist):
        value = left_list[index] * right_list[index]
        new_list.append(value)
    return new_list

def product_recursive(alist):
    if alist == []:
        return 1
    return alist[0] * product_recursive(alist[1:])

def paa(alist):
    new_list = []
    for index, item in enumerate(alist):
        current_list = alist[:index] + alist[index+1:]
        value = product_recursive(current_list)
        new_list.append(value)
    return new_list

alist = [1, 2, 3, 4, 5, 6]
rlist = alist[::-1]
print(alist)
print(product_left(alist))
print(product_left_recursive(alist[1:], [1]))
print(product_left_recursive(rlist[1:], [1]))
print(product_right(alist))
#print(product_right_recursive(alist, [1]))
#print(product_of_array_of_array(alist))
#print(paa(alist))
