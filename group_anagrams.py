def groupAnagrams(strs):
    if not strs:
        return [['']]
    seen = {}
    for word in strs:
        binary_word = translate_to_binary(word)
        if binary_word in seen:
            seen[binary_word] += [word]
        else:
            seen[binary_word] = [word]
    return list(seen.values())

def translate_to_binary(word):
    binary = ['0' for _ in 'abcdefghijklmnopqrstuvwxyz']
    for letter in word:
        num = ord(letter)-97
        if int(binary[num]) >= 1:
            binary[num] = str(int(binary[num])+1)
        else:
            binary[num] = '1'
    return ' '.join(binary)

print(groupAnagrams(["bdddddddddd","bbbbbbbbbbc"]))
print(groupAnagrams(["ddddddddddg","dgggggggggg"]))
print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
