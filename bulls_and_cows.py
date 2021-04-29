from collections import defaultdict
def getHint(secret: str, guess: str) -> str:
    cows = 0
    secret, guess, bulls = remove_in_place(secret, guess)
    t = defaultdict(int)
    for char in secret:
        t[char] += 1
    for char in guess:
        if char in t:
            if t[char]-1 == 0:
                t.pop(char)
            else:
                t[char] -= 1
            cows += 1
    return str(bulls)+'A'+str(cows)+'B'

def remove_in_place(secret, guess):
    secret, guess = list(secret), list(guess)
    bulls, i = 0, 0
    while i < len(secret):
        if secret[i] == guess[i]:
            bulls += 1
            secret.pop(i)
            guess.pop(i)
        else:
            i += 1
    return ''.join(secret), ''.join(guess), bulls

print(getHint("1122", "1222"))
