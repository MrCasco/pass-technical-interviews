def sentence_reverse(arr):
    temp = []
    word = '' if arr[0] != ' ' else ' '
    for ch in arr:
        if ch == ' ':
            temp.append(word.strip())
            word = ''
        word += ch
    if word != '':
        temp.append(word.strip())
    res = []
    for word in temp[::-1]:
        for ch in word:
            res.append(ch)
        res.append(' ')
    return res[:-1]

print(sentence_reverse([x for x in 'perfect makes practice']))
print(sentence_reverse([x for x in 'a   b']))
print(sentence_reverse([x for x in ' a   b ']))
