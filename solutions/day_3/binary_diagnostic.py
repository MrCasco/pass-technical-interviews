import sys
sys.path.insert(1, 'C:\Python\check-if-want-to-pass-technical-interviews')

from txt_reader import text_reader


def binary_diagnostic(arr):
    res = [0 for digit in range(12)]
    for number in arr:
        for i in range(len(number)):
            digit = int(number[i])
            res[i] += digit
    epsilon = ''.join(['0' if x > len(arr)/2 else '1' for x in res])
    gamma = ''.join(['1' if x > len(arr)/2 else '0' for x in res])
    return int(epsilon, 2) * int(gamma, 2)

def helper(arr, type):
    prospects = arr[:]
    while len(prospects) > 1:
        for i in range(len(arr[0])):
            if len(prospects) == 1:
                break
            ones = []
            zeros = []
            majority = 0
            for number in prospects:
                digit = int(number[i])
                majority += digit
                if digit == 1:
                    ones.append(number)
                else:
                    zeros.append(number)
            if type == 'upper':
                if majority < len(prospects)/2:
                    prospects = zeros[:]
                elif majority >= len(prospects)/2 and len(prospects)/2 != 0:
                    prospects = ones[:]
            else:
                if majority < len(prospects)/2:
                    prospects = ones[:]
                else:
                    prospects = zeros[:]
    return int(prospects[0], 2)

def binary_diagnostic_follow_up(arr):
    return helper(arr, 'lower') * helper(arr, 'upper')

arr = text_reader('day_3/binary_diagnostic.txt')
print(binary_diagnostic_follow_up(arr))
