#n = 3
#return [(), (0), (1), (2), (0,1), (0, 2), (1, 2), (0, 1, 2)]

#n = 4
#return [(), (0), (1), (2), (3), (0,1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3), (0, 1, 2), (0, 1, 3), (1, 2, 3), (0, 1, 2, 3)]

#n = 2
#return [(), (0), (1), (0, 1)]

def subset(n):
    alist = [[]]
    for i in range(n):
        alist += [x+[i] for x in alist]
    return alist

def subset_recursive(n, alist=None):
    if n >= 0:
        alist += [[n] + x for x in alist]
        subset_recursive(n-1, alist)
        return alist
n = 3
alist = [[]]
print(subset_recursive(3, alist))
