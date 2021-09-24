from collections import Counter


def checkInclusion(s1: str, s2: str) -> bool:
    set1 = Counter(s1)
    original_set = Counter(s1)
    cur = '' 
    l, r = 0, 0
    while r < len(s2):
        if len(cur) == len(s1):
            return True
        if s2[r] in set1:
            cur += s2[r]
            if set1[s2[r]] - 1  <= 0:
                del set1[s2[r]]
            else:
                set1[s2[r]] -= 1
        elif s2[r] not in original_set:
            l = r+1
            set1 = original_set.copy()
            cur = ''
        else:
            l += 1
            r = l-1
            set1 = original_set.copy()
            cur = ''
        r += 1
    return len(cur) == len(s1)
