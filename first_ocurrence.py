"""
Given a sorted array of integers and a target integer, find the first occurrence of the
target and return its index. Return -1 if the target is not in the array.

Input:

arr = [1, 3, 3, 3, 3, 6, 10, 10, 10, 100]
target = 3

Output:

1
"""

def find_first_occurrence(lst, target):
    if len(lst) == 1:
        if target in lst:
            return 0
        else:
            return -1
    left, right = 0, len(lst)-1
    middle = (left+right)//2
    while right != left and middle > -1:
        res = lst[middle]
        if res > target:
            right = middle-1
        elif res < target:
            left = middle+1
        elif res == target:
            if lst[middle-1] != target or middle-1 == -1:
                return middle
            right = middle
        middle = (left+right)//2
    return -1

print(find_first_occurrence([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 1))
print(find_first_occurrence([1, 2, 2, 3, 3, 4, 4, 5, 5], 3))
print(find_first_occurrence([1, 3, 3, 3, 3, 6, 10, 10, 10, 100], 3))
print(find_first_occurrence([4, 6, 7, 7, 7, 20], 3))
