def remove_duplicates(arr):
    right, left = 1, 0
    while right < len(arr):
        if arr[left] == arr[right]:
            arr.pop(right)
        else:
            left += 1
            right += 1
    return arr

print(remove_duplicates([0, 0, 1, 1, 1, 2, 2]))
print(remove_duplicates([0, 0, 1, 1, 2, 2]))
print(remove_duplicates([0, 1, 1, 2, 2]))
print(remove_duplicates([0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2]))
