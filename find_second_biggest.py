def find_second_biggest(arr):
    sec_big = 0
    big = arr[0]
    for num in arr:
        if num > big:
            sec_big = big
            big = num
        elif num > sec_big:
            sec_big = num
    return sec_big

print(find_second_biggest([4, 5, 2, 3, 1, 7, 9, 5, 1, 110, 44, 0]))
