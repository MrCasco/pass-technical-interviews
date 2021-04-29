## BEST SOLUTION ##
def combinationSum2(candidates, target):
    def backtrack(comb, remain, curr, counter, results):
        if remain == 0:
            # make a deep copy of the current combination
            #   rather than keeping the reference.
            results.append(comb[:])
            return
        elif remain < 0:
            return
        for next_curr in range(curr, len(counter)):
            candidate, freq = counter[next_curr]
            if freq <= 0:
                continue
            # add a new element to the current combination
            comb.append(candidate)
            counter[next_curr] = (candidate, freq-1)
            # continue the exploration with the updated combination
            backtrack(comb, remain - candidate, next_curr, counter, results)
            # backtrack the changes, so that we can try another candidate
            counter[next_curr] = (candidate, freq)
            comb.pop()
    results = []  # container to hold the final combinations
    counter = Counter(candidates)
    # convert the counter table to a list of (num, count) tuples
    counter = [(c, counter[c]) for c in counter]
    backtrack(comb = [], remain = target, curr = 0,
              counter = counter, results = results)
    return results

## MY SOLUTION ##
def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
    if sum(candidates) < target: return []
    def dfs(path, sum, start):
        if sum == target:
            path = tuple(path)
            res.add(path)
            return
        for i in range(start, len(candidates)):
            if sum+candidates[i] <= target:
                dfs(path+[candidates[i]], sum+candidates[i], i+1)
    res = set()
    candidates.sort()
    dfs([], 0, 0)
    return res
