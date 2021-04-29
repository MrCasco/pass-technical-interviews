def longestCommonPrefix(strs):
    if not strs: return ''
    if len(strs) == 1: return strs[0]
    lowest = min(strs, key=len)
    for i in range(len(lowest)):
        for word in strs[1:]:
            if word.startswith(lowest[:i+1]) == False:
                return lowest[:i]
    return lowest

def longestCommonPrefix(lst):
    if not lst: return ''
    prefix = min(lst, key=len)

    while prefix:
        for word in lst:
            if word[:len(prefix)] != prefix:
                prefix = prefix[:-1]
                break
        else:
            return prefix
    return ""

print(longestCommonPrefix(["flower","flow","flight"]))
