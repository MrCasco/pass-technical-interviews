## BRUTE FORCE ALGORITHM ##
def subarray_sum(arr, target):
    seen = {}
    left, right = 0, len(arr)
    while left < len(arr)-1:
        if sum(arr[left:right]) == target:
            return [left, right]
        if right == left:
            left += 1
            right = len(arr)-1
        right -= 1
    return []

## BEST SOLUTION ##
def subarray_sum(arr, target):
    left, right = 0, len(arr)
    dp = [arr[0], arr[0]]+[0]*(right-1)

    for i in range(1, len(arr)):
        dp[i] = dp[i-1]+arr[i]

    while left < len(arr):
        if dp[right-1]-dp[left-1] == target:
            return [left, right]
        if right == left:
            left += 1
            right = len(arr)-1
            continue
        right -= 1

## BEST SOLUTION 2 ##
def subarray_sum(arr, target):
    # prefix_sum 0 happens when we have an empty array
    prefix_sums = {0: 0}
    cur_sum = 0
    for i in range(len(arr)):
        cur_sum += arr[i]
        complement = cur_sum - target
        if complement in prefix_sums:
            return [prefix_sums[complement], i + 1]
        prefix_sums[cur_sum] = i + 1

print(subarray_sum([1, 3, -3, 8, 5, 7], 5))
print(subarray_sum([1, 1, 1], 3))
print(subarray_sum([3, 1, 2, 5, 1], 3))
print(subarray_sum([1, -20, -3, 30, 5, 7], 7))
print(subarray_sum([1, 8, 6, 3, 1, 8, 3, 8, 0, 0, 0, 3, 1, 1, 1, 5, 3, 32], 32))
