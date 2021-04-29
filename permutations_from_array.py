def permute(nums):
    def dfs(path, visited):
        if len(path) == len(nums):
            res.append(path)
            return
        for num in nums:
            if num not in visited:
                visited.add(num)
                dfs(path+[num], visited)
                visited.remove(num)
    res = []
    dfs([], set())
    return res
