def robot_grid(grid):
    if not grid:
        return None
    row = len(grid) - 1 
    column = len(grid[0]) - 1 
    path = []
    if traverse(row, column, grid, path):
        return path 
    return None

def traverse(row, column, grid, path=None):
    if row < 0 or column < 0 or not grid[row][column]:
        return False
    at_origin = (row == 0) and (column == 0)
    if at_origin or traverse(row - 1, column, grid, path) or traverse(row, column - 1, grid, path):
        path.append((row, column))
        return True
    return False

grid = [[1, 0, 1, 1, 1, 0, 1],
        [1, 1, 1, 0, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1],
        [0, 1, 0, 0, 0, 1, 1]]

print(robot_grid(grid))
