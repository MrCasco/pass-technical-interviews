def house_robber(nums):
    if len(nums) == 1:
        return nums[0]
    if not nums:
        return None
    dp = [nums[0], nums[1]]
    mx = max(dp)
    for i, house in enumerate(nums[2:], start=2):
        mx = max(mx, house+dp[i-2])
        dp.append(mx)
    return mx

print(house_robber([0, 3, 1, 6]))
print(house_robber([0, 1]))
