"""
You have two integer arrays, a and b, and an integer target value v.
Determine whether there is a pair of numbers, where one number is taken from a and the other from b,
that can be added together to get a sum of v.
Return true if such a pair exists, otherwise return false.
"""
## NAIVE SOLUTION ##
def sumOfTwo(a, b, v):
    for num1 in a:
        for num2 in b:
            if num1+num2 == v:
                return True
    return False

## OPTIMIZED SOLUTION USING A DICTIONARY ##
def sumOfTwo(a, b, v):
    b = set(b)
    for num in a:
        if v-num in b:
            return True
    return False

print(sumOfTwo([1, 2, 3], [4, 4, 4], 3))
