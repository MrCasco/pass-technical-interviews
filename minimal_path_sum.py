"""
Suppose we have a m x n matrix filled with non-negative integers, find a path from
top left corner to bottom right corner. which minimizes the sum of all numbers along its path.

    Note: Movements can only be either down or right at
    any point in time.

Example:
Input:

  [
    [1,3,1],
    [1,5,1],
    [4,2,1]
  ]

Output:

7

Explanation:

Because the path 1 → 3 → 1 → 1 → 1 minimizes the sum.
"""

def minPathSum(grid):
    for row in range(1, len(grid)):
        grid[row][0] += grid[row-1][0]
        
    for col in range(1, len(grid[0])):
        grid[0][col] += grid[0][col-1]

    for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
            grid[row][col] += min(grid[row-1][col], grid[row][col-1])
    return grid[-1][-1]

def minimal_path_sum(maze):
    if not maze or not maze[0]:
        return None
    INF = float('inf')
    grid = [[INF for _ in range(len(maze))] for _ in range(len(maze[0]))]
    grid[0][0] = maze[0][0]
    cols = len(maze[0])
    rows = len(maze)
    for col in range(cols):
        for row in range(rows):
            if col == 0 and row == 0:
                continue
            cur = maze[row][col]
            grid[row][col] = min(grid[row-1][col], grid[row][col-1])+cur
    return grid[-1][-1]


maze1 = [
    [1, 3, 1],
    [1, 5, 1],
    [4, 2, 1]
]

maze2 = [
    [1, 3, 6],
    [3, 2, 6],
    [4, 2, 1]
]

maze3 = [
    [1, 0, 0, 0, 3, 0],
    [0, 0, 2, 0, 1, 0],
    [0, 2, 0, 3, 0, 0],
    [0, 0, 0, 0, 3, 0],
    [0, 0, 0, 4, 0, 0],
    [1, 1, 5, 0, 0, 1]
]

maze4 = [
    [1, 0, 0, 0, 3, 0],
    [0, 0, 2, 0, 0, 0],
    [0, 2, 0, 3, 0, 0],
    [0, 0, 0, 0, 3, 0],
    [0, 0, 0, 4, 0, 0],
    [1, 1, 5, 0, 0, 0]
]

print('Minimum path sum for maze1 is:', minimal_path_sum(maze1))
print('Minimum path sum for maze2 is:', minimal_path_sum(maze2))
print('Minimum path sum for maze3 is:', minimal_path_sum(maze3))
print('Minimum path sum for maze4 is:', minimal_path_sum(maze4))
