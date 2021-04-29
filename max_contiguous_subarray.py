## SOLUTION 1 WHICH INCLUDES NEGATIVE NUMBER HANDLING ##
def max_sequenceBest(arr):
    max,curr=0,0
    for x in arr:
        curr+=x
        if curr<0:curr=0
        if curr>max:max=curr
    return max

## MY SOLUTION WITHOUT NEGATIVE NUMS HANDLING ##
def max_sequence(arr):
    if not arr:
        return 0
    prev = arr[0]
    mx = arr[0]
    for num in arr[1:]:
        prev = max(prev, prev+num)
        mx = max(mx, prev)
    return mx

## SOLUTION TWO WHICH ONLY WORKS FOR POSITIVE NUMBERS ##
def max_contiguous(lst):
    prev = lst[0]
    gmx = prev
    for num in lst[1:]:
        prev = max(prev+num, num)
        gmx = max(prev, gmx)
    return gmx

print('Best solution code:', max_sequenceBest([-2, 1, -3, 4, -1, 2, 1]))
print('My solution code:', max_contiguous([-2, 1, -3, 4, -1, 2, 1]))
print('Back to back SWE code:', max_sequence([-2, 1, -3, 4, -1, 2, 1]))
## SOLUTION ##
## https://backtobackswe.com/platform/content/max-contiguous-subarray-sum/solutions ##
