def island_count(grid):
    if not grid:
        return 0
    count = 0
    for row in range(len(grid)):
        for column in range(len(grid[0])):
            if grid[row][column] == "1":
                dfs(grid, row, column)
                count += 1
    return count

def dfs(grid, row, column):
    if row < 0 or column < 0 or row >= len(grid) or column >= len(grid[0]) or grid[row][column] != "1":
        return
    grid[row][column] = "V"
    dfs(grid, row - 1, column)
    dfs(grid, row + 1, column)
    dfs(grid, row, column + 1)
    dfs(grid, row, column - 1)

grid = [["1", "0", "1", "1"],
        ["1", "0", "1", "1"],
        ["1", "0", "1", "1"],
        ["1", "0", "1", "1"]]

print(island_count(grid))
