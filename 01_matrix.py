def updateMatrix(mat):
    queue = []
    in_bound = lambda r, c: 0 <= r < len(mat) and 0 <= c < len(mat[0])
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if mat[i][j] == 0:
                queue.append((i,j))
            else:
                mat[i][j] = '#'
    for r, c in queue:
        for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
            if in_bound(nr, nc) and mat[nr][nc] == '#':
                mat[nr][nc] = mat[r][c] + 1
                queue.append((nr, nc))
    return mat

print(updateMatrix([[1,1,1],[1,1,1],[1,1,0]]))
print(updateMatrix([[1,1,1,1,1,1],[1,1,1,1,0,1],[1,0,1,1,1,1],[0,1,1,0,0,0]]))
