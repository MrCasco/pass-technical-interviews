from collections import Counter

def numberOfWays(arr, k):
    dic = Counter(arr)
    pairs = 0
    for num in arr:
        import ipdb; ipdb.set_trace()
        while k-num in dic:
            dic[num] -= 1
            if dic[num] == 0 and k-num == num:
                del dic[num]
            elif dic[num] == 0:
                pairs += 1
                del dic[num]
            else:
                pairs += 1
    return pairs

print(numberOfWays([1, 5, 3, 3, 3], 6))
