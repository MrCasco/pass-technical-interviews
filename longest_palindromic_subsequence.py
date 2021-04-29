def longestPalindrome(word):
    
    if not word: return ''
    if word == word[::-1]: return word

    start, end = 0, 0
    for i in range(len(word)):
        len1 = expandFromMiddle(word, i, i)
        len2 = expandFromMiddle(word, i, i+1)
        ln = max(len1, len2)
        if ln > end-start:
            start = i-((ln-1)//2)
            end = i+(ln//2)
    return word[start:end+1]


def expandFromMiddle(word, left, right):
    if not word or left > right: return 0
    while left >= 0 and right < len(word) and word[left] == word[right]:
        left -= 1
        right += 1
    return right-left-1

print(longestPalindrome("aacabdkacaa"))
