def permutations(l):
    def dfs(path, used, res):
        if len(path) == len(l):
            res.add(''.join(path[:])) # note [:] make a deep copy since otherwise we'd be append the same list over and over
            return
        for i, letter in enumerate(l):
            # skip used letters
            if used[i]:
                continue
            # add letter to permutation, mark letter as used
            path.append(letter)
            used[i] = True
            dfs(path, used, res)
            # remove letter from permutation, mark letter as unused
            path.pop()
            used[i] = False
    res = set()
    dfs([], [False]*len(l), res)
    return res

print(permutations('abc'))
