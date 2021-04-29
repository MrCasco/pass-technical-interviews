def triangle_sum(triangle):
    queue = [(triangle[0][0], triangle[0][0], 0, 0)]
    mn = float('inf')
    while queue:
        node, suma, index, level = queue.pop(0)
        if level < len(triangle)-1:
            for k, num in enumerate(triangle[level+1][index:index+2], start=index):
                queue.append((num, num+suma, k, level+1))
        else:
            mn = min(mn, suma)
    return mn

triangle1 = [
    [2],
    [8, 6],
    [1, 5, 7]
]
triangle2 = [
    [2],
    [3, 4],
    [6, 5, 7],
    [4, 1, 8, 3]
]
triangle3 = [
    [10],
    [4,4],
    [6,6,5],
    [7,7,8,3],
    [8,9,7,2,1],
    [8,6,9,5,2,0]
]
triangle4 = [
    [9],
    [2, 1],
    [3, 4, 1],
    [6, 5, 7, 7],
    [2, 4, 5, 8, 8],
    [3, 4, 1, 2, 3, 3],
    [6, 5, 7, 2, 4, 1, 6],
    [2, 5, 8, 6, 2, 3, 4, 7],
    [3, 4, 8, 2, 1, 8, 9, 2, 1],
    [6, 5, 7, 8, 3, 7, 9, 9, 9, 9]
]

print(triangle_sum(triangle1))
print(triangle_sum(triangle2))
print(triangle_sum(triangle3))
print(triangle_sum(triangle4))
