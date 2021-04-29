def permutation(lst):
    if len(lst) == 0:
        return []
    if len(lst) == 1:
        return [lst]
    results = []
    for i, elem in enumerate(lst):
        fix = lst[i]
        new = elem[:i] + elem[i+1:]
        for remaining in permutation(new):
            r = [fix] + remaining
            if r not in remaining:
                results.append(r)
    return results
