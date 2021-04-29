def user_input():
    return int(input('Ingresa un número en el rango de 1 a 1,000,000'))

num = user_input()

def binary_search(num):
    low_bound = 0
    upper_bound = 1000000
    middle = 500000
    while num != middle:
        if num < middle:
            upper_bound = middle
            middle = upper_bound // 2
        elif num > middle:
            temp = low_bound
            low_bound = middle
            if (upper_bound-middle)//2 == 0:
                middle += 1
            else:
                middle += (upper_bound-middle)//2
    return middle

print(binary_search(num))
#
#
# num = user_input()
# print(binary_search(num))


# def iterative_factorial(num):
#     result = 1
#     for i in range(2, num+1):
#         result *= i
#     return result
#
# def recursive_factorial(num):
#     if num <= 1:
#         return 1
#     return num * recursive_factorial(num-1)
#
# print(iterative_factorial(num))
# print(recursive_factorial(num))
#
# import math
#
# def convert_to_binary(num):
#     binary = []
#     for i in range(int(math.log(num, 2))+1):
#         binary.append(num%2)
#         num //= 2
#     return binary[::-1]
#
# print(convert_to_binary(num))
