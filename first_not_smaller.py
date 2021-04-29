def first_not_smaller(arr, target) -> int:
    left, right = 0, len(arr)-1
    middle = (left+right)//2
    cur = arr[middle]
    while left != right:
        if cur > target:
            if arr[middle-1] < target:
                return middle
            right = middle - 1
        elif cur < target:
            left = middle + 1
        middle = (left+right)//2
        cur = arr[middle]
    return middle

# first_not_smaller([1, 3, 3, 5, 8, 8, 10,], 2)
print(first_not_smaller([1, 2, 3, 4, 5, 6, 7, 8, 9, 10,], 10))
