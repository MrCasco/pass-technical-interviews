"""
A string S of lowercase English letters is given. We want to partition this string into as many
parts as possible so that each letter appears in at most one part, and return a list of integers
representing the size of these parts.



Example 1:

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
"""

## NAIVE SOLUTION ##
from collections import Counter
def partitionString(S: str):
    counts = Counter(S)
    right = 0
    cur_sub = Counter()
    res = []
    while right < len(S):
        cur_sub.update(S[right])
        if len(counts - cur_sub) == len(counts)-len(cur_sub):
            res.append(len(S[:right+1]))
            if right+1 < len(S):
                S = S[right+1:]
                cur_sub = Counter()
                right = 0
            else:
                break
        else:
            right += 1
    return res

## BEST SOLUTION ##
from collections import Counter, defaultdict
def partitionString(S: str):
    summ = Counter(S)
    left, right = 0, 0
    cur_sub = defaultdict(lambda: 0)
    res = []
    count = 0
    counts = 0
    while right < len(S):
        if S[right] not in cur_sub:
            counts += summ[S[right]]
        cur_sub[S[right]] += 1
        count += 1
        if count == counts:
            res.append(S[left:right+1])
            left, right = right+1, right+1
            if right < len(S):
                cur_sub = defaultdict(lambda: 0)
                count = 0
                counts = 0
        else:
            right += 1
    return res

print(partitionString('baddacx'))
print(partitionString('bbeadcxede'))
print(partitionString('abcdefghhc'))
