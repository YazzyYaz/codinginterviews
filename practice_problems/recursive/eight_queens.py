GRID_SIZE = 8
grid = [["." for x in range(GRID_SIZE)] for x in range(GRID_SIZE)]
print(grid)

def eight_queens(grid, row, column):
    if (row > len(grid) - 1) or (column > len(grid[0]) - 1) or row < 0 or column < 0 or grid[row][column] != ".": 
        return
    else:
        eight_queens(grid, row - 1, column)
        eight_queens(grid, row + 1, column)
        eight_queens(grid, row, column - 1)
        eight_queens(grid, row, column + 1)
        eight_queens(grid, row - 1, column - 1)
        eight_queens(grid, row + 1, column - 1)
        eight_queens(grid, row - 1, column + 1)
        eight_queens(grid, row + 1, column + 1)
        grid[row][column] = "Q"

row=0
column=0
grid[row][column] = "Q"
eight_queens(grid, row, column+1)
print(grid)
