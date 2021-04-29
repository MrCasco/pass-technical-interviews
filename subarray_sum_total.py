"""
FOLLOW UP FROM subarray_sum:

Find the total number of subarrays that sums up to target.
"""

def subarray_sum_total(arr, target):
    left, right = 0, len(arr)
    dp = [arr[0], arr[0]]+[0]*(right-1)
    ways = 0
    for i in range(1, len(arr)):
        dp[i] = dp[i-1]+arr[i]
    while left < len(arr):
        if dp[right-1]-dp[left-1] == target:
            ways += 1
        if right == left:
            left += 1
            right = len(arr)
            continue
        right -= 1
    return ways

print(subarray_sum_total([10, 5, -5, -20, 10], -10))
print(subarray_sum_total([1, 1, 1], 2))
