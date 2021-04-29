## MY SOLUTION ##
def is_palindrome(st):
    st = [letter.lower() for letter in st if letter.isalnum()]
    left, right = 0, len(st)-1
    while right > left:
        if st[left] != st[right]:
            return False
        left += 1
        right -= 1
    return True

## BEST SOLUTION ##
def is_palindrome(s: str) -> bool:
    l, r = 0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum(): # Note 1, 2
            l += 1
        while l < r and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower(): # ignore case
            return False
        l += 1
        r -= 1
    return True

print(is_palindrome('Do geese see God'))
print(is_palindrome('Do 1geese see God'))
print(is_palindrome('Was it a car or a cat I saw?'))
print(is_palindrome('A brown fox jumping over'))
