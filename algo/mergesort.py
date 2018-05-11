def MergeSort(alist):
    if len(alist) > 1:
        midpoint = len(alist) // 2
        lefthalf = alist[:midpoint]
        righthalf = alist[midpoint:]
        MergeSort(lefthalf)
        MergeSort(righthalf)
        i, j, k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1
