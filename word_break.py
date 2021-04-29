"""
Given a string and a list of words, determine if the string can be constructed from
concatenating words from the list of words. A word can be used multiple times.

Input:
s = "algomonster"
words = ["algo", "monster"]
Output: true

Input:
s = "aab"
words = ["a", "c"]
Output: false
"""

def word_break(phrase, words):
    def dfs(cur):
        if cur == '':
            return True
        if cur in phrase:
            for move in words:
                if cur.startswith(move):
                    return dfs(cur.replace(move, '', 1))
        return False
    return dfs(phrase)

print(word_break('algomonster', ['algo', 'monster']))
print(word_break('abctreabc', ['abc', 'treabc', 'zzzzz']))
print(word_break('abctreabc', ['abc', 'tre', 'abc']))
print(word_break('lemamazzz', ['l', 'e', 'm', 'a', 'zz']))
# print(word_break('abctreabc', ['abc', 'treabc']))
# print(word_break('abctreabc', ['abc', 'treabc']))
