"""
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
Example 1:

Input: m = 3, n = 2

Output: 3

Explanation:

From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:

    Right -> Right -> Down

    Right -> Down -> Right

    Down -> Right -> Right

Example 2:

Input: m = 5, n = 3

Output: 15
"""

def unique_paths(m, n):
    if not m or not n:
        return 0
    grid = [[0 for __ in range(n)] for _ in range(m)]
    grid[0][0] = 1
    for col in range(n):
        for row in range(m):
            if col == 0 and row == 0:
                continue
            if col == 0:
                grid[row][col] += grid[row-1][col]
            elif row == 0:
                grid[row][col] += grid[row][col-1]
            else:
                grid[row][col] += grid[row-1][col]
                grid[row][col] += grid[row][col-1]
    return grid[-1][-1]

def unique_paths(m, n):
    grid = [[0 for __ in range(n)] for _ in range(m)]
    for i in range(m):
        grid[i][0] = 1

    for i in range(n):
        grid[0][i] = 1

    for col in range(1, n):
        for row in range(1, m):
            grid[row][col] = grid[row-1][col]+grid[row][col-1]
    return grid[-1][-1]

print(unique_paths(3, 3))
print(unique_paths(10, 5))
print(unique_paths(7, 3))
print(unique_paths(1, 1))
print(unique_paths(3, 2))
