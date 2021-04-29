def longest_palindromic_substring(word):
    if not word:
        return ''
    palindrome = lambda x: x == x[::-1]
    if palindrome(word):
        return word
    def dfs(cur_word, longest, memo):
        palindrome = lambda x: x == x[::-1]
        if cur_word == '' or len(longest) >= len(cur_word):
            return longest
        if cur_word in memo:
            return memo[cur_word]
        if palindrome(cur_word):
            if len(cur_word) > len(longest):
                longest = cur_word
        for next_word in [cur_word[:-1], cur_word[1:]]:
            ans = dfs(next_word, longest, memo)
            if len(longest) < len(ans):
                longest = ans
        memo[cur_word] = longest
        return longest
    return dfs(word, '', {})


print(longest_palindromic_substring("babaddtattarrattatddetartrateedredividerb"))
print(longest_palindromic_substring("abbcccbbbcaaccbababcbcabca"))
print(longest_palindromic_substring('babad'))
print(longest_palindromic_substring('baaba'))
print(longest_palindromic_substring('cbbd'))
