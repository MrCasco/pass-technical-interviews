
def rotationalCipher(input, n):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    dic = {letter:i for i, letter in zip(range(26), alphabet)}
    new_word = ''
    for letter in input:
        new_letter = letter
        if letter.isalpha():
            if letter.isupper():
                letter = letter.lower()
            new_index = (dic[letter]+n) % 26
            new_letter = alphabet[new_index] if not new_letter.isupper() else alphabet[new_index].upper()
        elif letter.isnumeric():
            new_letter = str(int(letter)+n) if int(letter)+n < 10 else str((int(letter)+n) % 10)
        new_word += new_letter
    return new_word

assert (rotationalCipher('abcdZXYzxy-999.@', 200) == 'stuvRPQrpq-999.@')
assert (rotationalCipher('All-convoYs-9-be:Alert1.', 4) == 'Epp-gsrzsCw-3-fi:Epivx5.')
print('All tests were asserted correctly!')
