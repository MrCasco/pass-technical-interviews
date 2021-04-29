"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]


Example 2:

Input: n = 1
Output: ["()"]

"""

def generateParenthesis(n: int):
    def dfs(opening, closing, path):
        if opening+closing == n*2:
            res.append(path[:])
            return
        if opening > closing:
            if opening < n:
                dfs(opening+1, closing, path+'(')
            dfs(opening, closing+1, path+')')
        elif opening == closing:
            dfs(opening+1, closing, path+'(')
    res = []
    dfs(0, 0, '')
    return res

print(generateParenthesis(1))
print(generateParenthesis(2))
print(generateParenthesis(3))
print(generateParenthesis(4))
print(generateParenthesis(5))
print(generateParenthesis(6))
print(generateParenthesis(7))
print(generateParenthesis(8))
