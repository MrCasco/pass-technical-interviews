roman_nums = {
    1:'I',
    4:'IV',
    5:'V',
    9:'IX',
    10:'X',
    40:'XL',
    50:'L',
    90:'XC',
    100:'C',
    400:'CD',
    500:'D',
    900:'CM',
    1000:'M'
}

## MY SOLUTION ##
def int_to_roman(num):
    num = str(num)
    n = len(num)-1
    roman = ''
    for digit in num:
        import ipdb; ipdb.set_trace()
        if digit == '0':
            n -= 1
            continue
        digit = int(digit)
        if digit*(10**n) in roman_nums:
            roman += roman_nums[digit*(10**n)]
        else:
            cur = digit*(10**n)
            while cur not in roman_nums:
                cur -= 10**n
            complement = (digit*(10**n))-cur
            if (digit*(10**n))%(digit*(10**n)/cur) == 0 and complement != 1:
                roman += roman_nums[cur]*(digit*(10**n)//cur)
            else:
                roman += roman_nums[cur]+(roman_nums[10**n]*(complement//10**n))
        n -= 1
    return roman

## BEST SOLUTION ##
def int_to_roman(num: int) -> str:
    result = ''
    tdh = 0
    for i in list(roman_nums.keys())[::-1]:
        if i > num:
            continue
        tdh = num//i
        num = num%i
        result += roman_nums[i]*tdh
    return result

print(int_to_roman(101))
print(int_to_roman(60))
print(int_to_roman(27))
print(int_to_roman(30))
print(int_to_roman(10))
print(int_to_roman(20))
print(int_to_roman(6))
