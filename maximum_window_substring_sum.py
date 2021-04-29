def maximum_window_substring_sum(arr, k):
    l, r = 1, k
    dp = [0]
    mx = float('-inf')
    for i in range(1, len(arr)+1):
        dp.append(dp[i-1]+arr[i-1])

    while r < len(arr):
        mx = max(mx, dp[r]-dp[l-1])
        l += 1
        r += 1
    return mx

print(maximum_window_substring_sum([10, 30, -50, 80, 50, -100], 2))
