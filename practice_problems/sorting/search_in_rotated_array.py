def search_in_rotated_array(alist, k, leftix=0, rightix=None):
    if not rightix:
        rightix = len(alist)
    midpoint = (leftix + rightix) / 2
    aleft, amiddle = alist[leftix], alist[midpoint]
    if k == amiddle:
        return midpoint
    if k == aleft:
        return leftix 
    if aleft > amiddle:
        if amiddle < k and k < aleft:
            return search_in_rotated_array(alist, k, midpoint+1, rightix)
        else:
            return search_in_rotated_array(alist, k, leftix+1, midpoint)
    elif aleft < k and k < amiddle:
        return search_in_rotated_array(alist, k, leftix+1, midpoint)
    else:
        return search_in_rotated_array(alist, k, midpoint+1, rightix)

array = [55, 60, 65, 70, 75, 80, 85, 90, 95, 15, 20, 25, 30, 35, 40, 45]
print(search_in_rotated_array(array, 40))
