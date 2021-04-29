import math

sample_list = [[0,0,1,1,1], [0,1,1,1,1], [0,0,0,1,1], [1,1,1,1,1]]

def minimum_index_to_one(lst):
    mn = binary_search(lst[0])
    for ones in lst[1:]:
        mn = min(binary_search(ones[:mn]), mn)
    return mn

def binary_search(lst):
    middle = (len(lst))//2
    res = 0
    if lst[-1] == 0:
        return math.inf
    while middle != 0:
        res = lst[middle]
        if res != 1:
            middle = (middle//2)+middle
        else:
            if lst[middle-1] == 0 or middle == 0:
                return middle
            middle //= 2
    return middle

print(minimum_index_to_one(sample_list))
