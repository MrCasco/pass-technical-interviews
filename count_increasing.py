from txt_reader import text_reader

def count_increasing(arr):
    prev = int(arr[0])
    count = 0
    for num in arr[1:]:
        num = int(num)
        if num > prev:
            count += 1
        prev = num
    return count

print(count_increasing(text_reader('count_increasing.txt')))
