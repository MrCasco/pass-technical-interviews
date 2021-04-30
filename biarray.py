# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import Counter

def solution(A):
    seen = set()
    l, r = 0, 0
    A.append(-1)
    mx = float('-inf')
    print(A)
    while r < len(A):
        if A[r] not in seen:
            seen.add(A[r])
        if len(seen) > 2:
            mx = max(mx, len(A[l:r]))
            while A[l] in seen:
                seen.remove(A[l])
                l += 1
        r += 1
    return mx if mx != float('-inf') else len(A)


solution([1,2,3,2])
