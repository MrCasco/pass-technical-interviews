def combinationSum(candidates, target):
    def dfs(complement, path, i):
        if complement == 0:
            res.append(path)
        for j in range(i, len(candidates)):
            if complement-candidates[j] >= 0:
                dfs(complement-candidates[j], path+[candidates[j]], j)
    res = []
    for i, num in enumerate(candidates):
        if target-num >= 0:
            dfs(target-num, [num], i)
    return res
