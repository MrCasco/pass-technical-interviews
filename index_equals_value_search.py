def index_equals_value_search(arr):
  l, r = 0, len(arr)-1
  low = float('inf')
  while r > l:
    mid = (r+l)//2
    if arr[mid] == mid:
      low = min(low, mid)
    if mid <= arr[mid]:
      r = mid
    else:
      l = mid+1
  if l == arr[l]:
    return l
  if low == float('inf'):
    return -1
  return low
