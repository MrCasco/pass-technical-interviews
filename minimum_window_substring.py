"""
Given two strings s and t, return the minimum window in s which will contain all the characters in t.
If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example 1:

Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Example 2:

Input: s = "a", t = "a"
Output: "a"
"""
## NAIVE SOLUTION ##
from collections import Counter
def minimum_window_substring(string, subs):
    if len(subs) > len(string):
        return ''
    left, right = 0, 1
    counts = Counter(subs)
    minimum_window = '_'*len(string)
    while right <= len(string):
        while counts - Counter(string[left:right]) == Counter():
            if len(string[left:right]) <= len(minimum_window):
                minimum_window = string[left:right]
            left += 1
        right += 1
    if minimum_window == '_'*len(string):
        return ''
    return minimum_window

## BEST SOLUTION ##
from collections import defaultdict, Counter
def minWindow(string, subs):
    if len(subs) > len(string):
        return ''
    left, right = 0, 1
    cur_sub = defaultdict(lambda: 0)
    cur_sub[string[left]] += 1
    subs = Counter(subs)
    counts = 1 if string[left] in subs and subs[string[left]] == 1 else 0
    minimum_window = '_'*len(string)
    while right <= len(string):
        while counts == len(subs):
            if len(string[left:right]) <= len(minimum_window):
                minimum_window = string[left:right]
            cur_sub[string[left]] -= 1
            if cur_sub[string[left]] == 0:
                cur_sub.pop(string[left])
            if string[left] in subs and cur_sub[string[left]] < subs[string[left]]:
                counts -= 1
            left += 1
        if right < len(string):
            if string[right] in subs and cur_sub[string[right]]+1 == subs[string[right]]:
                counts += 1
            cur_sub[string[right]] += 1
        right += 1
    if minimum_window == '_'*len(string):
        return ''
    return minimum_window

print(minWindow('acbbaca', 'aba'))
print(minWindow('bbaa', 'baa'))
print(minWindow('a', 'aa'))
print(minWindow('adobecodebanc', 'abc'))
print(minWindow('azjskfzts', 'sz'))
print(minWindow('abcde', 'ace'))
