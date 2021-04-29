KEYBOARD = {
    '2': 'abc',
    '3': 'def',
    '4': 'ghi',
    '5': 'jkl',
    '6': 'mno',
    '7': 'pqrs',
    '8': 'tuv',
    '9': 'wxyz',
}

## MY SOLUTION ##
def letter_combinations_of_phone_number(num):
    def dfs(cur_path, i, res):
        if len(cur_path) == len(num):
            res.append(''.join(cur_path))
            return
        for letter in KEYBOARD[num[i]]:
            dfs(cur_path+[letter], i+1, res)
    res = []
    visited = {}
    dfs([], 0, res)
    return sorted(res)

def letterCombinations(digits: str):
    if digits == '': return []
    def dfs(i, s):
        if i > len(digits)-1:
            res.append(s)
            return
        for letter in KEYBOARD[digits[i]]:
            dfs(i+1, s+letter)
    res = []
    dfs(0, '')
    return res


## ALGO MONSTER'S SOLUTION ##
def letter_combinations_of_phone_number(digits):
    def dfs(path, res):
        if len(path) == len(digits):
            res.append(''.join(path))
            return

        next_number = digits[len(path)]
        for letter in KEYBOARD[next_number]:
            path.append(letter)
            dfs(path, res)
            path.pop()

    res = []
    dfs([], res)
    return res

print(letter_combinations_of_phone_number('342'))
