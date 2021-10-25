def arithmetic_power(a, b):
    if b == 0:
        return 1
    return a*arithmetic_power(a, b//a) * (a if b%2 != 0 else 1)

print(arithmetic_power(2, 4))
print(arithmetic_power(2, 5))
print(arithmetic_power(2, 8))
print(arithmetic_power(2, 9))
