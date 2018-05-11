def BinarySearch(alist, item):
    first = 0
    last = len(alist) - 1
    found = False
    while first < last and not found:
        midpoint = (first + last) / 2
        if alist[midpoint] == item:
            found = True
        else:
            if alist[midpoint] > item:
                last = midpoint - 1
            else:
                first = midpoint + 1
    return found
