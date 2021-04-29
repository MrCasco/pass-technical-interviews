"""
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

       0  1  2  3  4  5  6  7   8  9
arr = [1, 4, 5, 2, 3, 7, 8, 6, 10, 9], k = 2
1 -> 0, 1, 2 == [1, 4, 5, 2, 3, 7, 8, 6, 10, 9]
4 -> 0, 1, 2, 3 == [1, 2, 5, 4, 3, 7, 8, 6, 10, 9]
                       |k + 1  |
k == 2
5 -> 0, 1, 2, 3, 4 == [1, 2, 5, 4, 3, 7, 8, 6, 10, 9]

from heapq import heappop, heappush, heapify
def sort_k_messed_array(arr, k):
  for i, num in enumerate(arr[:-1]):
    cur_min = arr[i]           # 4
    swap_index = i             # 1
    if i+k < len(arr):
      for j in range(i+1, i+k+1):  # from 2 to 4
        if cur_min > arr[j]:  # false / 4>2
          cur_min = arr[j]    #
          swap_index = j      # 3
    else:
      for j in range(i+1, len(arr)):  # from 2 to 4
        if cur_min > arr[j]:  # false / 4>2
          cur_min = arr[j]    #
          swap_index = j
    arr[i], arr[swap_index] = arr[swap_index], arr[i]
  return arr

"""



from heapq import heappop, heappush, heapify
def sort_k_messed_array(arr, k):
  heap = arr[:k+1]
  heapify(heap)
  for i in range(len(arr)):
    arr[i] = heappop(heap)
    if i+k+1 < len(arr):
      heappush(heap, arr[i+k+1])
  return arr
