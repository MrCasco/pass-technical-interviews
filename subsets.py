def subsets(nums):
    def dfs(i, s):
        if len(s) == len(set(s)): res.append(s)
        for j in range(i+1, len(nums)):
            dfs(j, s+[nums[j]])
    res = [[]]
    for i, num in enumerate(nums):
        dfs(i, [num])
    return res
