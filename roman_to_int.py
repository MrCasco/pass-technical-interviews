def romanToInt(s: str) -> int:
    roman_nums = {
        'I':1,
        'IV':4,
        'V':5,
        'IX':9,
        'X':10,
        'XL':40,
        'L':50,
        'XC':90,
        'C':100,
        'CD':400,
        'D':500,
        'CM':900,
        'M':1000
    }
    ans = 0
    i = 0
    while i < len(s):
        if i+1 < len(s) and s[i:i+2] in roman_nums:
            ans += roman_nums[s[i:i+2]]
            i += 1
        else:
            ans += roman_nums[s[i]]
        i += 1
    return ans

print(romanToInt("III"))
print(romanToInt("IV"))
print(romanToInt("IX"))
print(romanToInt("LVIII"))
print(romanToInt("MCMXCIV"))
