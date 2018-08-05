def number_of_paths(n):
    row = 0
    column = 0
    count = traverse(n, row, column, {})
    return count

def traverse(n, row, column, adict=None):
    if row > n or column > n or row < column:
        return 0
    elif row == n - 1 or column == n - 1:
        adict[(row, column)] = 1
    elif (row, column) in adict:
        return adict[(row, column)]
    else:
        count = traverse(n, row + 1, column, adict) + traverse(n, row, column + 1, adict)
        if (row, column) not in adict:
            adict[(row, column)] = count
    return adict[(row, column)]


print(number_of_paths(5))
