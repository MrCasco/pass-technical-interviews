def exist(board, word):
    def dfs(x, y, i, visited):
        if i == len(word)-1:
            if board[y][x] == word[-1]:
                return True
            return False
        if (x, y) in visited or x < 0 or x >= len(board[0]) or y < 0 or y >= len(board):
            return False
        visited.add((x, y))
        for nx, ny in [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]:
            if i+1 < len(word) and (nx < 0 or nx >= len(board[0]) or ny < 0 or ny >= len(board) or (nx, ny) in visited or board[ny][nx] != word[i+1]):
                continue
            if dfs(nx, ny, i+1, visited.copy()):
                return True
    for col in range(len(board[0])):
        for row in range(len(board)):
            if board[row][col] == word[0]:
                if dfs(col, row, 0, set()):
                    return True
    return False

print(exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))
print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'SEE'))
