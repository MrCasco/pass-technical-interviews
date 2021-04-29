from collections import Counter, defaultdict
def get_shortest_unique_substring(arr, str):
  left, right = 0, 0
  shortest = str+'_'
  cur = defaultdict(int)
  arr = set(arr)
  while left <= right <= len(str):
    while len(cur) == len(arr):
      shortest = min(shortest, str[left:right], key=len)
      if str[left] in arr:
          if cur[str[left]]-1 == 0:
              cur.pop(str[left])
          else:
              cur[str[left]] -= 1
      left += 1
    else:
      if right < len(str) and str[right] in arr:
        cur[str[right]] += 1
      right += 1
  return '' if shortest == str+'_' else shortest

print(get_shortest_unique_substring(['A'], 'A'))
