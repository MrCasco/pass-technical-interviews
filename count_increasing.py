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

def count_increasing_triplets(arr):
    prev = sum([int(x) for x in arr[:3]])
    count = 0
    for i in range(1, len(arr)-2):
        cur = sum([int(x) for x in arr[i:i+3]])
        if cur > prev:
            count += 1
        prev = cur
    return count

arr = text_reader('count_triplet_increasing.txt')

# print(count_increasing(arr))
print(count_increasing_triplets(arr))
