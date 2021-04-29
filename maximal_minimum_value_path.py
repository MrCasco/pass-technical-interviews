def maximal_minimum_path(matrix):
    grid = [[0 for _ in matrix[0]] for _ in matrix]
    grid[0][0] = matrix[0][0]
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            # import ipdb; ipdb.set_trace()
            if row == col == 0:
                continue
            elif row == 0:
                grid[row][col] = min(matrix[row][col], matrix[row][col-1])
            elif col == 0:
                grid[row][col] = min(matrix[row][col], matrix[row-1][col])
            else:
                one = min(matrix[row][col], matrix[row-1][col])
                if matrix[row][col] < matrix[row][col-1] and matrix[row][col] < matrix[row-1][col]:
                    two = min(matrix[row-1][col], matrix[row][col-1])
                else:
                    if type(grid[row][col-1]) is int:
                        two = grid[row][col-1]
                    else:
                        two = sorted([x for x in grid[row][col-1]])[:2]
                if type(two) is int:
                    two = [two]
                grid[row][col] = sorted([one]+two)
            if row == col == len(matrix)-1:
                if matrix[-1][-1] < grid[row-1][col][0] and matrix[-1][-1] < grid[row][col-1][0]:
                    return matrix[-1][-1]
                else:
                    one = min(matrix[row][col], grid[row-1][col][-1])
                    two = min(matrix[row][col], grid[row][col-1][-1])
                grid[row][col] = max(one, two)
    return grid[-1][-1]

matrix = [
    [7,5,3],
    [2,0,9],
    [4,5,9]
]

matrix = [
    [4,5,9],
    [2,2,9],
    [7,5,3]
]

print(maximal_minimum_path(matrix))
