"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

    arr.length >= 3
    There exists some i with 0 < i < arr.length - 1 such that:
        arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
        arr[i] > arr[i + 1] > ... > arr[arr.length - 1]


Examples:
    Input: arr = [2,1]
    Output: false

    Input: arr = [3,5,5]
    Output: false

    Input: arr = [0,3,2,1]
    Output: true
"""

## MY SOLUTION ##
def validMountainArray(arr):
    if len(arr) < 3:
        return False
    peak = 0
    first = -1
    for i in range(len(arr[:-1])):
        if arr[i] > arr[i+1]:
            if i == 0:
                return False
            if peak == 0:
                first = i
            peak += 1
        elif arr[i] == arr[i+1]:
            return False
    if first != -1 and peak == len(arr[first:])-1:
        return True
    return False

print(validMountainArray([0, 1, 2, 3, 4, 3, 2]))    # True
print(validMountainArray([0, 2, 3, 4, 5, 2, 1, 0])) # True
print(validMountainArray([0, 3, 5, 5]))             # False
print(validMountainArray([0, 1, 2, 3, 4, 5, 6, 7])) # False
