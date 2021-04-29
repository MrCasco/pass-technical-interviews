def square_root(num):
    arr = [x*x for x in range(num)]
    left, right = 0, len(arr)-1
    middle = (left+right)//2
    cur = arr[middle]
    while left != right:
        if cur == num:
            return middle
        elif cur > num:
            right = middle - 1
        elif cur < num:
            left = middle + 1
        middle = (left+right)//2
        cur = arr[middle]
    return middle

print(square_root(8))
print(square_root(16))
print(square_root(4))
print(square_root(9))
