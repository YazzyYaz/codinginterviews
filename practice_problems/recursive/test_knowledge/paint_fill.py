def paint_fill(matrix, color, point):
    if not matrix:
        return [[]]
    row = point[0]
    column = point[1]
    starting_color = matrix[point[0]][point[1]]
    paint(matrix, color, starting_color, row, column)
    return matrix

def paint(matrix, target_color, start_color, row, column):
    if (row > len(matrix) - 1) or (column > len(matrix[0])- 1) or row < 0 or column < 0 or matrix[row][column] != start_color:
        return
    elif matrix[row][column] == start_color:
        matrix[row][column] = target_color
        paint(matrix, target_color, start_color, row + 1, column)
        paint(matrix, target_color, start_color, row - 1, column)
        paint(matrix, target_color, start_color, row, column + 1)
        paint(matrix, target_color, start_color, row, column + 1)


matrix = [["white", "white", "white", "white"],
        ["white", "white", "black", "black"],
        ["black", "black", "yellow", "yellow"],
        ["black", "black", "black", "black"]]
print(paint_fill(matrix, "green", (0,0)))
