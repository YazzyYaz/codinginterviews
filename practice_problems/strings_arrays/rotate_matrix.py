import pprint

def rotate_matrix(matrix):
    n = len(matrix)
    new_matrix = [None] * n 
    for i in range(n):
        new_matrix[i] = [None] * n 
    
    for row in range(n):
        for column in range(n):
            new_matrix[n - column - 1][row] = matrix[row][column]

    return new_matrix


matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
pprint.pprint(matrix)
pprint.pprint(rotate_matrix(matrix))
