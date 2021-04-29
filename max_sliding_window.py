## NAIVE SOLUTION ##
def max_sliding_window(arr, k):
    sums = []
    for i in range(len(arr)-(k-1)):
        sums.append(max(arr[i:i+k]))
    return sums

## BEST SOLUTION ##
from heapq import heappop, heappush, heapify

def max_sliding_window(arr, k):
    heap = []
    [heappush(heap, (-x, i)) for x, i in zip(arr[:k], range(k))]
    res = [-heap[0][0]]
    for i in range(k, len(arr)):
        heappush(heap, (-arr[i], i))
        while heap and i-k >= heap[0][1]:
            heappop(heap)
        res.append(-heap[0][0])
    return res

print(max_sliding_window([1, 3, -1, -3, 2, 3, 6, 7], 3))
print(max_sliding_window([-1, 3, 5, 2, 3, 8, 0, 0, -10], 3))
