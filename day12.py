# Leetle Day 12 - Count Islands
# 12.01.2025

def solve(grid):
    if not grid or not grid[0]:
        return 0
    rows = len(grid)
    cols = len(grid[0])
    visited = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(False)
        visited.append(row)
    island_count = 0
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and not visited[row][col]:
                flood_fill(grid, row, col, visited)
                island_count += 1
    return island_count

def flood_fill(grid, row, col, visited):
    rows = len(grid)
    cols = len(grid[0])
    if row < 0 or row >= rows:
        return
    if col < 0 or col >= cols:
        return
    if grid[row][col] == 0:
        return
    if visited[row][col]:
        return
    visited[row][col] = True
    flood_fill(grid, row - 1, col, visited)
    flood_fill(grid, row + 1, col, visited)
    flood_fill(grid, row, col - 1, visited)
    flood_fill(grid, row, col + 1, visited)