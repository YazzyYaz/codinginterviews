def magic_index(alist, start, end):
    if end < start:
        return None 
    midpoint = (start + end) / 2
    if alist[midpoint] == midpoint:
        return midpoint 
    if alist[midpoint] > midpoint:
        return magic_index(alist, 0, midpoint-1)
    else:
        return magic_index(alist, midpoint + 1, end)

alist = [-1, 0, 2, 10, 12, 20, 21]
print(magic_index(alist, 0, len(alist)-1))
