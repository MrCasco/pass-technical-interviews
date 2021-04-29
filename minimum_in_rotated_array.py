## MY SOLUTION ##
def find_min_rotated(arr):
    left, right = 0, len(arr)-1
    middle = (left+right)//2
    while left != right:
        # import ipdb; ipdb.set_trace()
        cur = arr[middle]
        if middle+1 < len(arr)-1:
            if cur > arr[middle+1]:
                return middle+1
            elif cur < arr[middle+1]:
                left = middle+1
        else:
            if arr[-1] < arr[0]:
                return middle
            else:
                return 0
        middle = (left+right)//2
    return 0


## BEST SOLUTION ##
def find_min_rotated(arr):
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        # if <= last element, then belongs to lower half
        if arr[mid] <= arr[-1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1

    return boundary_index

print(find_min_rotated([3, 4, 5, 1, 2]))
print(find_min_rotated([1, 2, 3, 4, 5]))
print(find_min_rotated([1, 2, 3, 4, 0]))
