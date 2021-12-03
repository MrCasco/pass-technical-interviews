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

arr = text_reader('day_3/binary_diagnostic.txt')
print(binary_diagnostic(arr))
