def SelectionSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        position_of_max = 0
        for position in range(1, passnum + 1):
            if alist[position] > alist[position_of_max]:
                position_of_max = position
        alist[passnum], alist[position_of_max] = alist[position_of_max], alist[passnum]
    return alist
