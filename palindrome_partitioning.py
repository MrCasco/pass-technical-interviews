def partition(word: str):
    def dfs(i, path):
        if i == len(word):
            res.append(path)
            return
        palindrome = lambda x: x == x[::-1]
        for j in range(i+1, len(word)+1):
            new_word = word[i:j]
            if palindrome(new_word):
                dfs(j, path+[new_word])
    res = []
    dfs(0, [])
    return res

# def partition(s):
#     ans = []
#     n = len(s)
#     def is_palindrome(word):
#         return word == word[::-1]
#     def dfs(start, cur_path):
#         if start == n:
#             ans.append(cur_path[:])
#             return
#         for i in range(start + 1, n + 1):
#             prefix = s[start: i]
#             if is_palindrome(prefix):
#                 dfs(i, cur_path + [prefix])
#     dfs(0, [])
#     return ans

print(partition('cdd'))
print(partition('aab'))
print(partition('aba'))
print(partition('abba'))
