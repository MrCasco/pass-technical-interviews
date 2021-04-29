def decodeString(s):
    if not '[' in s:
        return s
    #try:
    k = int(s[0])
    return k * decodeString(s[1:].strip('[').strip(']'))
    #except:
    #    return k * decodeString(s.strip('[').strip(']'))

print(decodeString('4[ab]'))
