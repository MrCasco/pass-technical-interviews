def checkInclusion(s1, s2):
    print(perms(s1))
    # for perm in perms(s1):
    #     if perm in s2:
    #         return True
    # return False

def perms(s):
    def dfs(cur, seen):
        if len(cur) == len(s):
            res.add(cur)
            return
        for j in range(len(s)):
            if j not in seen:
                seen.add(j)
                dfs(cur+s[j], seen.copy())
                seen.remove(j)
    res = set()
    for index in range(len(s)):
        dfs(s[index], set([index]))
    return res

checkInclusion("adc","dcda")
