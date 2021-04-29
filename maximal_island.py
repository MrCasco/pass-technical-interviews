def maximal_square(binaryMatrix):
    if len(binaryMatrix) == 1 and len(binaryMatrix[0]) == 1:
        return binaryMatrix[0][0]
    numIsland = 0
    for i in range(len(binaryMatrix)):
        for j in range(len(binaryMatrix[i])):
            if binaryMatrix[i][j] == 1:
                numIsland = max(numIsland, explore(binaryMatrix, i, j))
    return numIsland

def explore(grid, i, j):
    if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[i]) or grid[i][j] == 0:
        return 0
    grid[i][j] = 0
    return 1+explore(grid, i+1, j)+explore(grid, i-1, j)+explore(grid, i, j+1)+explore(grid, i, j-1)

grid = [
    [1,0,1,0,0],
    [1,0,1,1,1],
    [1,1,1,1,0],
    [1,0,0,1,0]
]
print(maximal_square(grid))
