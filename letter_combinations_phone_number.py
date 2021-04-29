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


def letter_combinations_of_phone_number(digits):
    def dfs(path, res):
        import ipdb; ipdb.set_trace()
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

print(letter_combinations_of_phone_number('56'))
