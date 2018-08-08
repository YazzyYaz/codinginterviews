def sorted_merge(alist, blist):
    bix = len(blist) - 1
    aix = len(alist) - len(blist) - 1
    while bix >= 0 and aix >= 0:
        if blist[bix] >= alist[aix]:
            alist[aix + bix + 1] = blist[bix]
            bix -= 1
        else:
            alist[aix + bix + 1] = alist[aix]
            aix -= 1
    while bix >= 0:
        alist[bix] = blist[bix]
        bix -= 1
    return alist


alist = [1, 2, 4, 6, 7, 10, 20, 44, None, None, None, None]
blist = [3, 5, 15, 22]
print(sorted_merge(alist, blist))
