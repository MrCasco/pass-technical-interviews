def longestIncreasingSubsequence(nums):
    if not nums:
        return 1
    arr = [1 for _ in range(len(nums))]
    x, y, mx = 0, 1, 1
    while x < len(nums)-1 and y < len(nums):
        if nums[y] > nums[x]:
            arr[y] = max(arr[x]+1, arr[y])
            mx = max(mx, arr[y])
        if y-1 == x:
            y += 1
            x = 0
        else:
            x += 1
    return mx

print(longestIncreasingSubsequence([1, 4, 5, 6, 2, 3, 5, 8, 1, 1, 10, -5, 20, 1, 2, 3, 4, 0, 5, 6, 7, 8]))
print(longestIncreasingSubsequence([1, 2, 3, 4, 5]))
