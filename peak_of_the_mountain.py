"""
A mountain array is defined as an array that has at least 3 elements
let's call the element with the largest value the "peak", with index k.
The array elements monotonically increase from the first element to A[k],
and then monotonically decreases from A[k + 1] to the last element of the array.
Thus creating a "mountain" of numbers.

Find the index of the peak element. Assume there is no duplicate.

Input: 0 1 2 3 2 1 0

Output: 3

Explanation: the largest element is 3 and its index is 3.
"""


## MY SOLUTION ##
def peak_of_mountain_array(arr):
    left, right = 0, len(arr)-1
    mid = (left+right)//2
    while left <= right:
        if arr[mid] > arr[mid+1]:
            if arr[mid] > arr[mid-1]:
                return mid
            right = mid+1
        elif arr[mid] < arr[mid+1]:
            left = mid
        mid = (left+right)//2
    return mid

## BEST SOLUTION ##
def peak_of_mountain_array(arr):
    left, right = 0, len(arr) - 1
    boundary_index = -1

    while left <= right:
        mid = (left + right) // 2
        if mid == len(arr) - 1 or arr[mid] >= arr[mid + 1]:
            boundary_index = mid
            right = mid - 1
        else:
            left = mid + 1
    return boundary_index

assert peak_of_mountain_array([-1, 0, 1, 2, 3, 2, 1, 0]) == 4, 'Error'
assert peak_of_mountain_array([0, 10, 3, 2, 1, 2, 1]) == 1, 'Error'
