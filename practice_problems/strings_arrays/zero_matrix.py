import pprint

def zero_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    row_vector = [False] * m
    column_vector = [False] * n

    for row in range(m):
        for column in range(n):
            if matrix[row][column] == 0:
                row_vector[row] = True
                column_vector[column] = True

    for index, item in enumerate(row_vector):
        if item:
            matrix[index] = [0] * n
    
    for index, item in enumerate(column_vector):
        if item:
            counter = 0
            while counter < m:
                matrix[counter][index] = 0
                counter += 1

    return matrix


matrix = [
    [1, 1, 0, 1],
    [1, 1, 1, 1],
    [1, 1, 1, 1],
    [0, 1, 1, 1]
]
        
pprint.pprint(matrix)
pprint.pprint(zero_matrix(matrix))
