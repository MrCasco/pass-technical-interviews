from collections import Counter

def numberOfWays(arr, k):
    dic = Counter(arr)
    pairs = 0
    for num in arr:
        if k-num in dic:
            dic[num] -= 1
            if dic[num] == 0:
                if k-num != num:
                    pairs += dic[k-num]
                del dic[num]
            else:
                pairs += dic[k-num]
    return pairs

print(numberOfWays([1, 5, 3, 3, 3], 6))
print(numberOfWays([1, 2, 3, 4, 3], 6))
