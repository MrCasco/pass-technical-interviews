def findEncryptedWord(s):
  if len(s) == 1 or not s:
    return s
  mid = (len(s)-1)//2
  left = findEncryptedWord(s[:mid])
  if mid+1 >= len(s):
    right = ''
  else:
    right = findEncryptedWord(s[mid+1:])
  return s[mid]+left+right

s1 = "abc"
expected_1 = "bac"
output_1 = findEncryptedWord(s1)
assert expected_1 == output_1

s2 = "abcd"
expected_2 = "bacd"
output_2 = findEncryptedWord(s2)
assert expected_2 == output_2

s3 = "abcxcba"
expected_3 = "xbacbca"
output_3 = findEncryptedWord(s3)
assert expected_3 == output_3

s4 = "facebook"
expected_4 = "eafcobok"
output_4 = findEncryptedWord(s4)
assert expected_4 == output_4
