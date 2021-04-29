# def binary_search(num):
#     low_bound = 0
#     upper_bound = 1000000
#     middle = 500000
#     while num != middle:
#         if num < middle:
#             upper_bound = middle
#             middle = upper_bound // 2
#         elif num > middle:
#             temp = low_bound
#             low_bound = middle
#             if (upper_bound-middle)//2 == 0:
#                 middle += 1
#             else:
#                 middle += (upper_bound-middle)//2
#     return middle


"""
Given a target, find in lg(n) time complexity this target and return its index
"""
def binary_search(arr, target):
    left, right = 1, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

print(binary_search([x for x in range(1, 101)], 2))
