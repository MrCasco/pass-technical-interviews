"""
Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l)
there are such that A[i] + B[j] + C[k] + D[l] is zero.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
"""


from collections import defaultdict

def fourSumCount(A, B, C, D):
    res = 0
    sums  = defaultdict(lambda: 0)
    for k in range(len(C)):
        for l in range(len(D)):
            sums[C[k]+D[l]] += 1

    for i in range(len(A)):
        for j in range(len(B)):
            if -(A[i]+B[j]) in sums:
                res += sums[-(A[i]+B[j])]
    return res

print(fourSumCount([-1,-1],[-1,1],[-1,1],[1,-1]))
print(fourSumCount([0,1,-1],[-1,1,0],[0,0,1],[-1,1,1]))
print(fourSumCount([1,2],[-2,-1],[-1,2],[0,2]))
