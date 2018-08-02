def sum_list(alist):
    if alist == []:
        return 0
    return alist[0] + sum_list(alist[1:])

alist = [1, 2, 3, 4, 5]
print(sum_list(alist))
